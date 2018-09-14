#!/usr/bin/env python

import argparse
import os
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
import logging
from biobb_io.mmb_api.common import download_pdb
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class MmbPdb(object):
    """Wrapper class for the MMB group PDB REST API.
    This class is a wrapper for the PDB (http://www.rcsb.org/pdb/home/home.do)
    mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/)

    Args:
        output_pdb_path (str): Path to the output PDB file.
        properties (dic):
            | - **pdb_code** (*str*) - RSCB PDB code. ie: "2VGB"
            | - **filter** (*str*) - ("filter=/1&group=ATOM") Filter for the :meth:`biobb_io.mmb_api.MmbPdb.get_pdb_zip` method following the J(s)Mol format.
            | - **url** (*str*) - ("http://mmb.irbbarcelona.org/api/pdb/") URL of the MMB PDB REST API.

    """
    def __init__(self, output_pdb_path, properties, **kwargs):
        self.output_pdb_path = output_pdb_path
        self.url = properties.get('url',"http://mmb.irbbarcelona.org/api/pdb/")
        self.pdb_code = properties.get('pdb_code').strip().lower()
        self.filt = properties.get('filter', 'filter=/1&group=ATOM')
        self.global_log= properties.get('global_log', None)
        self.prefix = properties.get('prefix',None)
        self.step = properties.get('step',None)
        self.path = properties.get('path','')

    def launch(self):
        """
        Writes the PDB file content of the first pdb_code
        to output_pdb_path.
        """
        out_log, _ = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step)

        #Downloading PDB_files
        pdb_string = download_pdb(self.pdb_code, self.url, self.filt, out_log, self.global_log)

        out_log.info("\nWritting: "+self.pdb_code+"\nto: "+os.path.abspath(self.output_pdb_path))
        if self.global_log:
            self.global_log.info(fu.get_logs_prefix()+"Writting: "+self.pdb_code+"\nto: "+os.path.abspath(self.output_pdb_path))

        with open(self.output_pdb_path, 'w') as f:
            f.write(pdb_string)

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the PDB (http://www.rcsb.org/pdb/home/home.do) mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/)")
    parser.add_argument('--config', required=True)
    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    #Specific args of each building block
    parser.add_argument('--output_pdb_path', required=True)
    ####

    args = parser.parse_args()
    if args.step:
        properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()[args.step]
    else:
        properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
        
    #Specific call of each building block
    MmbPdb(output_pdb_path=args.output_pdb_path, properties=properties).launch()
    ####

if __name__ == '__main__':
    main()
