#!/usr/bin/env python
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
import os
from biobb_io.mmb_api.common import get_cluster_pdb_codes
from biobb_io.mmb_api.common import download_pdb
import logging
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class MmbPdbClusterZip(object):
    """Wrapper class for the MMB group PDB REST API.
    This class is a wrapper for the PDB (http://www.rcsb.org/pdb/home/home.do)
    mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/)

    Args:
        output_pdb_zip_path (str): Path to the ZIP or PDB file containing the output PDB files.
        properties (dic):
            | - **pdb_code** (*str*) - RSCB PDB code. ie: "2VGB"
            | - **filter** (*str*) - ("filter=/1&group=ATOM") Filter for the :meth:`biobb_io.mmb_api.MmbPdb.get_pdb_zip` method following the J(s)Mol format.
            | - **cluster** (*str*) - (90) Cluster number for the :meth:`biobb_io.mmb_api.MmbPdb.get_pdb_cluster_zip` method.
            | - **url** (*str*) - ("http://mmb.irbbarcelona.org/api/pdb/") URL of the MMB PDB REST API.
    """
    def __init__(self, output_pdb_zip_path, properties, **kwargs):
        self.output_pdb_zip_path = output_pdb_zip_path
        self.url = properties.get('url',"http://mmb.irbbarcelona.org/api/pdb/")
        self.pdb_code = properties.get('pdb_code').strip().lower()
        self.filt = properties.get('filter', 'filter=/1&group=ATOM')
        self.cluster = str(properties.get('cluster', 90))
        self.global_log= properties.get('global_log', None)
        self.prefix = properties.get('prefix',None)
        self.step = properties.get('step',None)
        self.path = properties.get('path','')

    def launch(self):
        """
        Writes each PDB file content of each pdb_code in the cluster
        to a pdb_file then creates a zip_file output_pdb_zip_path.
        """
        out_log, _ = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step)
        file_list = []
        #Downloading PDB_files
        pdb_code_list = get_cluster_pdb_codes(self.pdb_code, self.url, self.cluster, out_log, self.global_log)
        for pdb_code in pdb_code_list:
            pdb_string = download_pdb(pdb_code, self.url, self.filt, out_log, self.global_log)
            pdb_file = pdb_code+'.pdb'

            out_log.info("\nWritting: "+pdb_code+" to: "+os.path.abspath(pdb_file))
            if self.global_log:
                self.global_log.info(fu.get_logs_prefix()+"Writting: "+pdb_code+" to: "+os.path.abspath(pdb_file))

            with open(pdb_file, 'w') as f:
                f.write(pdb_string)

            file_list.append(os.path.abspath(pdb_file))

        #Zipping files
        out_log.info("Zipping the pdb files to: "+self.output_pdb_zip_path)
        if self.global_log:
            self.global_log.info("Zipping the pdb files to: "+self.output_pdb_zip_path)
        fu.zip_list(self.output_pdb_zip_path, file_list)

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the PDB Cluster (http://www.rcsb.org/pdb/home/home.do) mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/)")
    parser.add_argument('--conf_file', required=True)
    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    #Specific args of each building block
    parser.add_argument('--output_pdb_zip_path', required=True)
    ####

    args = parser.parse_args()
    if args.step:
        properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()[args.step]
    else:
        properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()

    #Specific call of each building block
    MmbPdbClusterZip(output_pdb_zip_path=args.output_pdb_zip_path, properties=properties).launch()
    ####

if __name__ == '__main__':
    main()
