#!/usr/bin/env python

"""MmbPdbClusterZip Module"""
import os
import argparse
import logging
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import get_cluster_pdb_codes
from biobb_io.api.common import download_pdb
from biobb_io.api.common import write_pdb
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class MmbPdbClusterZip():
    """Wrapper class for the `MMB PDB mirror <http://mmb.irbbarcelona.org/api/>`_.

    Args:
        output_pdb_zip_path (str): Path to the ZIP or PDB file containing the output PDB files. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/reference_output_pdb_zip_path.zip>`_. Accepted formats: pdb, zip.
        properties (dic):
            | - **pdb_code** (*str*) - ("2vgb") RSCB PDB code. ie: "2VGB"
            | - **filter** (*str*) - (["ATOM", "MODEL", "ENDMDL"]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the official PDB specification (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
            | - **cluster** (*str*) - (90) Cluster number for the :meth:`biobb_io.api.MmbPdb.get_pdb_cluster_zip` method.
            | - **url** (*str*) - ("https://files.rcsb.org/download/") URL of the PDB REST API. Another option for this parameter is the MMB PDB mirror API ("http://mmb.irbbarcelona.org/api/pdb/").
            | - **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            | - **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """
    def __init__(self, output_pdb_zip_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # IN OUT files
        self.output_pdb_zip_path = output_pdb_zip_path

        # Properties specific for BB
        self.url = properties.get('url', "https://files.rcsb.org/download/")
        self.pdb_code = properties.get('pdb_code', '2vgb').strip().lower()
        self.filter = properties.get('filter', ["ATOM", "MODEL", "ENDMDL"])
        self.cluster = str(properties.get('cluster', 90))
        self.properties = properties

        # Common in all BB
        self.global_log = properties.get('global_log', None)
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    @launchlogger
    def launch(self) -> int:
        """
        Writes each PDB file content of each pdb_code in the cluster
        to a pdb_file then creates a zip_file output_pdb_zip_path.
        """
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # Check the properties
        fu.check_properties(self, self.properties)

        file_list = []
        #Downloading PDB_files
        pdb_code_list = get_cluster_pdb_codes(pdb_code=self.pdb_code, cluster=self.cluster, out_log=out_log, global_log=self.global_log)
        unique_dir = fu.create_unique_dir()
        for pdb_code in pdb_code_list:
            pdb_file = os.path.join(unique_dir, pdb_code+".pdb")
            pdb_string = download_pdb(pdb_code=pdb_code, url=self.url, out_log=out_log, global_log=self.global_log)
            write_pdb(pdb_string, pdb_file, self.filter, out_log, self.global_log)
            file_list.append(os.path.abspath(pdb_file))

        #Zipping files
        fu.log("Zipping the pdb files to: %s" % self.output_pdb_zip_path)
        fu.zip_list(self.output_pdb_zip_path, file_list, out_log=out_log)

        if self.remove_tmp:
            # remove temporary folder
            fu.rm(unique_dir)
            fu.log('Removed temporary folder: %s' % unique_dir, out_log)

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the PDB Cluster (http://www.rcsb.org/pdb/home/home.do) mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/) for additional help in the commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o','--output_pdb_zip_path', required=True, help="Output ZIP file name")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    #Specific call of each building block
    MmbPdbClusterZip(output_pdb_zip_path=args.output_pdb_zip_path, properties=properties).launch()

if __name__ == '__main__':
    main()
