#!/usr/bin/env python

"""Module containing the MmbPdb class and the command line interface."""
import logging
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_io.mmb_api.common import download_pdb
from biobb_io.mmb_api.common import write_pdb
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class MmbPdb():
    """Wrapper class for the PDB REST API.
    This class is a wrapper for the PDB (http://www.rcsb.org/pdb/home/home.do)
    download page.

    Args:
        output_pdb_path (str): Path to the output PDB file.
        properties (dic):
            | - **pdb_code** (*str*) - ('1ubq') RSCB PDB code. ie: "2VGB"
            | - **filter** (*str*) - (["ATOM", "MODEL", "ENDMDL"]) Array of groups to be keep. If value is None or False no filter will be applied. All the possible values are defined in the official PDB specification (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
            | - **url** (*str*) - ("https://files.rcsb.org/download/") URL of the MMB PDB REST API.
    """
    def __init__(self, output_pdb_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.output_pdb_path = output_pdb_path

        # Properties specific for BB
        self.url = properties.get('url', "https://files.rcsb.org/download/")
        self.pdb_code = properties.get('pdb_code', '1ubq').strip().lower()
        self.filt = properties.get('filter', ["ATOM", "MODEL", "ENDMDL"])

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

    def launch(self):
        """Writes the PDB file content of the first pdb_code to output_pdb_path."""
        out_log, _ = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        #Downloading PDB_files
        pdb_string = download_pdb(self.pdb_code, self.url, out_log, self.global_log)
        write_pdb(pdb_string, self.output_pdb_path, self.filt, out_log, self.global_log)

def main():
    """Command line interface."""
    parser = argparse.ArgumentParser(description="Wrapper for the PDB (http://www.rcsb.org/pdb/home/home.do) mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/)")
    parser.add_argument('--config', required=False)
    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    #Specific args of each building block
    parser.add_argument('--output_pdb_path', required=False)

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    #Specific call of each building block
    MmbPdb(output_pdb_path=args.output_pdb_path, properties=properties).launch()

if __name__ == '__main__':
    main()
