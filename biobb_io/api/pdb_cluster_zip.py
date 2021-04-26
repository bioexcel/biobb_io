#!/usr/bin/env python

"""PdbClusterZip Module"""
import os
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *

class PdbClusterZip():
    """
    | biobb_io PdbClusterZip
    | This class is a wrapper for downloading a PDB cluster from the Protein Data Bank.
    | Wrapper for the `Protein Data Bank in Europe <https://www.ebi.ac.uk/pdbe/>`_, the `Protein Data Bank <https://www.rcsb.org/>`_ and the `MMB PDB mirror <http://mmb.irbbarcelona.org/api/>`_ for downloading a PDB cluster.

    Args:
        output_pdb_zip_path (str): Path to the ZIP file containing the output PDB files. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_pdb_cluster.zip>`_. Accepted formats: zip (edam:format_3987).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB code.
            * **filter** (*str*) - (["ATOM", "MODEL", "ENDMDL"]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the official PDB specification (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
            * **cluster** (*int*) - (90) Sequence Similarity Cutoff. Values: 50 (structures having less than 50% sequence identity to each other), 70 (structures having less than 70% sequence identity to each other), 90 (structures having less than 90% sequence identity to each other), 95 (structures having less than 95% sequence identity to each other).
            * **api_id** (*str*) - ("pdbe") Identifier of the PDB REST API from which the PDB structure will be downloaded. Values: pdbe (`PDB in Europe REST API <https://www.ebi.ac.uk/pdbe/pdbe-rest-api>`_), pdb (`RCSB PDB REST API <https://data.rcsb.org/>`_), mmb (`MMB PDB mirror API <http://mmb.irbbarcelona.org/api/>`_).
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.pdb_cluster_zip import pdb_cluster_zip
            prop = { 
                'pdb_code': '2VGB', 
                'filter': ['ATOM', 'MODEL', 'ENDMDL'], 
                'cluster': 90, 
                'api_id': 'pdbe' 
            }
            pdb_cluster_zip(output_pdb_zip_path='/path/to/newStructures.zip', 
                            properties=prop)

    Info:
        * wrapped_software:
            * name: Protein Data Bank
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_pdb_zip_path, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # IN OUT files
        self.output_pdb_zip_path = output_pdb_zip_path

        # Properties specific for BB
        self.api_id = properties.get('api_id', 'pdbe')
        self.pdb_code = properties.get('pdb_code', None)
        self.filter = properties.get('filter', ['ATOM', 'MODEL', 'ENDMDL'])
        self.cluster = properties.get('cluster', 90)
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
        self.output_pdb_zip_path = check_output_path(self.output_pdb_zip_path, "output_pdb_zip_path", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`PdbClusterZip <api.pdb_cluster_zip.PdbClusterZip>` api.pdb_cluster_zip.PdbClusterZip object."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        check_mandatory_property(self.pdb_code, 'pdb_code', out_log, self.__class__.__name__)

        self.pdb_code = self.pdb_code.strip().lower()

        file_list = []
        #Downloading PDB_files
        pdb_code_list = get_cluster_pdb_codes(pdb_code=self.pdb_code, cluster=self.cluster, out_log=out_log, global_log=self.global_log)
        unique_dir = fu.create_unique_dir()
        for pdb_code in pdb_code_list:
            pdb_file = os.path.join(unique_dir, pdb_code+".pdb")
            pdb_string = download_pdb(pdb_code=pdb_code, api_id=self.api_id, out_log=out_log, global_log=self.global_log)
            write_pdb(pdb_string, pdb_file, self.filter, out_log, self.global_log)
            file_list.append(os.path.abspath(pdb_file))

        #Zipping files
        fu.log("Zipping the pdb files to: %s" % self.output_pdb_zip_path)
        fu.zip_list(self.output_pdb_zip_path, file_list, out_log=out_log)

        if self.remove_tmp:
            # remove temporary folder
            fu.rm(unique_dir)
            fu.log('Removed temporary folder: %s' % unique_dir, out_log)

        return 0

def pdb_cluster_zip(output_pdb_zip_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`PdbClusterZip <api.pdb_cluster_zip.PdbClusterZip>` class and
    execute the :meth:`launch() <api.pdb_cluster_zip.PdbClusterZip.launch>` method."""

    return PdbClusterZip(output_pdb_zip_path=output_pdb_zip_path,
                        properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Wrapper for the Protein Data Bank in Europe (https://www.ebi.ac.uk/pdbe/), the Protein Data Bank (https://www.rcsb.org/) and the MMB PDB mirror (http://mmb.irbbarcelona.org/api/) for downloading a PDB cluster.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o','--output_pdb_zip_path', required=True, help="Path to the ZIP or PDB file containing the output PDB files. Accepted formats: pdb, zip.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    #Specific call of each building block
    pdb_cluster_zip(output_pdb_zip_path=args.output_pdb_zip_path, 
                properties=properties)

if __name__ == '__main__':
    main()
