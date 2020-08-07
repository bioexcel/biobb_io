#!/usr/bin/env python

"""Module containing the Pdb class and the command line interface."""
import logging
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import download_pdb
from biobb_io.api.common import write_pdb
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class Pdb():
    """Wrapper class for the PDB REST API.
    This class is a wrapper for the `PDB download page <https://www.rcsb.org/>`_.

    Args:
        output_pdb_path (str): Path to the output PDB file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/pdb_1ubq.pdb>`_. Accepted formats: pdb.
        properties (dic):
            | - **pdb_code** (*str*) - ("1ubq") RSCB PDB code.
            | - **filter** (*str*) - (["ATOM", "MODEL", "ENDMDL"]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the official PDB specification (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
            | - **url** (*str*) - ("https://files.rcsb.org/download/") URL of the PDB REST API. Another option for this parameter is the MMB PDB mirror API ("http://mmb.irbbarcelona.org/api/pdb/").
            | - **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            | - **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """
    def __init__(self, output_pdb_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.output_pdb_path = output_pdb_path

        # Properties specific for BB
        self.url = properties.get('url', "https://files.rcsb.org/download/")
        self.pdb_code = properties.get('pdb_code', '1ubq').strip().lower()
        self.filter = properties.get('filter', ["ATOM", "MODEL", "ENDMDL"])
        self.properties = properties

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    @launchlogger
    def launch(self) -> int:
        """Writes the PDB file content of the first pdb_code to output_pdb_path."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # Check the properties
        fu.check_properties(self, self.properties)

        # Downloading PDB file
        pdb_string = download_pdb(self.pdb_code, self.url, out_log, self.global_log)
        write_pdb(pdb_string, self.output_pdb_path, self.filter, out_log, self.global_log)

def main():
    """Command line interface."""
    parser = argparse.ArgumentParser(description="Wrapper for the PDB ('http://www.rcsb.org/pdb/home/home.do') mirror of the MMB group REST API ('http://mmb.irbbarcelona.org/api/') for additional help in the commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_pdb_path', required=True, help="Output file name")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    Pdb(output_pdb_path=args.output_pdb_path, properties=properties).launch()

if __name__ == '__main__':
    main()
