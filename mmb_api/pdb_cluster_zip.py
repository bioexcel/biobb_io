import requests
import os
import json
from biobb_common.tools import file_utils as fu
from common import get_cluster_pdb_codes
from common import download_pdb
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
            | - **filter** (*str*) - ("filter=/1&group=ATOM") Filter for the :meth:`mmb_api.MmbPdb.get_pdb_zip` method following the J(s)Mol format.
            | - **cluster** (*str*) - (90) Cluster number for the :meth:`mmb_api.MmbPdb.get_pdb_cluster_zip` method.
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
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step)
        file_list = []
        #Downloading PDB_files
        pdb_code_list = get_cluster_pdb_codes(self.pdb_code, self.url, self.cluster, out_log, self.global_log)
        for pdb_code in pdb_code_list:
            pdb_string = self.download_pdb(self.pdb_code, self.url, self.fil, out_log, self.global_log)
            pdb_file = pdb_code+'.pdb'

            out_log.info("\nWritting: "+pdb_code+"\nto: "+os.path.abspath(pdb_file))
            if self.global_log:
                self.global_log.info(22*' '+"Writting: "+pdb_code+"\nto: "+os.path.abspath(pdb_file))

            with open(pdb_file, 'w') as f:
                f.write(pdb_string)

            file_list.append(os.path.abspath(pdb_file))

        #Zipping files
        out_log.info("Zipping the pdb files to: "+self.output_pdb_zip_path)
        if self.global_log:
            self.global_log.info("Zipping the pdb files to: "+self.output_pdb_zip_path)
        fu.zip_list(self.output_pdb_zip_path, file_list)
