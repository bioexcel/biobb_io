#!/usr/bin/env python

"""MmbPdbVariants Module"""
import re
import logging
import argparse
import requests
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_io.mmb_api.common import get_uniprot
from biobb_io.mmb_api.common import get_variants
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class MmbPdbVariants():
    """Wrapper class for the MMB group UNIPROT REST API.
    This class is a wrapper for the UNIPROT (http://www.uniprot.org/)
    mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/)

    Args:
        output_mutations_list_txt (str): Path to the TXT file containing an ASCII comma separated values of the mutations.
        properties (dic):
            | - **pdb_code** (*str*): ("2vgb") RSCB PDB four letter code. ie: "2ki5".
            | - **url** (*str*): ("http://mmb.irbbarcelona.org/api") URL of the MMB REST API.
    """
    def __init__(self, output_mutations_list_txt, properties=None, **kwargs):
        properties = properties or {}

        # IN OUT files
        self.output_mutations_list_txt = output_mutations_list_txt

        # Properties specific for BB
        self.pdb_code = properties.get('pdb_code', '2vgb').strip().lower()
        self.url = properties.get('url', "http://mmb.irbbarcelona.org/api")

        # Common in all BB
        self.global_log = properties.get('global_log', None)
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

    def launch(self):
        """Writes the variants of the selected `pdb_code` to `output_mutations_list_txt`"""
        out_log, _ = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        uniprot_id = get_uniprot(self.pdb_code, self.url, out_log, self.global_log)
        url_mapPDBRes = (self.url+"/uniprot/"+uniprot_id+"/mapPDBRes?pdbId="+self.pdb_code)
        pattern = re.compile((r"p.(?P<wt>[a-zA-Z]{3})(?P<resnum>\d+)(?P<mt>[a-zA-Z]{3})"))

        fu.log('Fetching variants for uniprot_id: %s and pdb_code: %s' % (uniprot_id, self.pdb_code), out_log, self.global_log)
        unfiltered_dic = requests.get(url_mapPDBRes).json()
        if not unfiltered_dic:
            fu.log("No mutation found", out_log, self.global_log)
            return None

        mapdic = requests.get(url_mapPDBRes).json()
        mutations = []
        uniprot_var_list = get_variants(uniprot_id, self.url, out_log, self.global_log)
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

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the PDB Variants (http://www.rcsb.org/pdb/home/home.do) mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/)")
    parser.add_argument('--config', required=False)
    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    #Specific args of each building block
    parser.add_argument('--output_mutations_list_txt', required=True)
    ####

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    MmbPdbVariants(output_mutations_list_txt=args.output_mutations_list_txt, properties=properties).launch()
    ####

if __name__ == '__main__':
    main()
