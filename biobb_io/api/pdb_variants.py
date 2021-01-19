#!/usr/bin/env python

"""PdbVariants Module"""
import re
import argparse
import requests
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *

class PdbVariants():
    """
    | biobb_io PdbVariants
    | This class creates a text file containing a list of all the variants mapped to a PDB code from the corresponding UNIPROT entries.
    | Wrapper for the `UNIPROT <http://www.uniprot.org/>`_ mirror of the `MMB group REST API <http://mmb.irbbarcelona.org/api/>`_ for creating a list of all the variants mapped to a PDB code from the corresponding UNIPROT entries.

    Args:
        output_mutations_list_txt (str): Path to the TXT file containing an ASCII comma separated values of the mutations. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_pdb_variants.txt>`_. Accepted formats: txt (edam:format_2330).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB four letter code.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
            This is a use example of how to use the PdbVariants module from Python

            from biobb_io.api.pdb_variants import pdb_variants
            prop = { 
                'pdb_code': '2VGB' 
            }
            pdb_variants(output_mutations_list_txt='/path/to/newMutationsList.txt', 
                        properties=prop)

    Info:
        * wrapped_software:
            * name: UNIPROT
            * license: Creative Commons
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_mutations_list_txt, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # IN OUT files
        self.output_mutations_list_txt = output_mutations_list_txt

        # Properties specific for BB
        self.pdb_code = properties.get('pdb_code', None)
        self.properties = properties

        # Common in all BB
        self.global_log = properties.get('global_log', None)
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.output_mutations_list_txt = check_output_path(self.output_mutations_list_txt, "output_mutations_list_txt", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`PdbVariants <api.pdb_variants.PdbVariants>` api.pdb_variants.PdbVariants object."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        check_mandatory_property(self.pdb_code, 'pdb_code', out_log, self.__class__.__name__)

        self.pdb_code = self.pdb_code.strip().lower()

        url = 'http://mmb.irbbarcelona.org/api'
        uniprot_id = get_uniprot(self.pdb_code, url, out_log, self.global_log)
        url_mapPDBRes = (url+"/uniprot/"+uniprot_id+"/mapPDBRes?pdbId="+self.pdb_code)
        pattern = re.compile((r"p.(?P<wt>[a-zA-Z]{3})(?P<resnum>\d+)(?P<mt>[a-zA-Z]{3})"))

        fu.log('Fetching variants for uniprot_id: %s and pdb_code: %s' % (uniprot_id, self.pdb_code), out_log, self.global_log)
        unfiltered_dic = requests.get(url_mapPDBRes, verify=False).json()
        if not unfiltered_dic:
            fu.log("No mutation found", out_log, self.global_log)
            return None

        mapdic = requests.get(url_mapPDBRes, verify=False).json()
        mutations = []
        uniprot_var_list = get_variants(uniprot_id, url, out_log, self.global_log)
        for var in uniprot_var_list:
            uni_mut = pattern.match(var).groupdict()
            for k in mapdic.keys():
                for fragment in mapdic[k]:
                    if int(fragment['unp_start']) <= int(uni_mut['resnum']) <= int(fragment['unp_end']):
                        resnum = int(uni_mut['resnum']) + int(fragment['pdb_start']) - int(fragment['unp_start'])
                        mutations.append(k[-1]+'.'+uni_mut['wt']+str(resnum)+uni_mut['mt'])

        fu.log('Found %d mutations mapped to PDB: %s' % (len(mutations), self.pdb_code), out_log, self.global_log)
        fu.log('Writting mutations to: %s' % self.output_mutations_list_txt, out_log, self.global_log)

        with open(self.output_mutations_list_txt, 'w') as mut_file:
            mutations.sort()
            mut_file.write(",".join(mutations))

        return 0

def pdb_variants(output_mutations_list_txt: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`PdbVariants <api.pdb_variants.PdbVariants>` class and
    execute the :meth:`launch() <api.pdb_variants.PdbVariants.launch>` method."""

    return PdbVariants(output_mutations_list_txt=output_mutations_list_txt,
                        properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Wrapper for the UNIPROT (http://www.uniprot.org/) mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/) for creating a list of all the variants mapped to a PDB code from the corresponding UNIPROT entries.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_mutations_list_txt', required=True, help="Path to the TXT file containing an ASCII comma separated values of the mutations. Accepted formats: txt.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    #Specific call of each building block
    pdb_variants(output_mutations_list_txt=args.output_mutations_list_txt, 
                properties=properties)

if __name__ == '__main__':
    main()
