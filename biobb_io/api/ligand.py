#!/usr/bin/env python

"""Module containing the Ligand class and the command line interface."""
import logging
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import download_ligand
from biobb_io.api.common import write_pdb

class Ligand():
    """Wrapper class for the PDB REST API.
    This class is a wrapper for the `MMB PDB mirror <http://mmb.irbbarcelona.org/api/>`_.

    Args:
        output_pdb_path (str): Path to the output PDB ligand file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/ligand_12d.pdb>`_. Accepted formats: pdb.
        properties (dic):
            | - **ligand_code** (*str*) - ("12D") RSCB PDB ligand code. ie: "12D"
            | - **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            | - **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """
    def __init__(self, output_pdb_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.output_pdb_path = output_pdb_path

        # Properties specific for BB
        self.url = properties.get('url', "http://mmb.irbbarcelona.org/api/pdbMonomer/")
        self.ligand_code = properties.get('ligand_code', '12D').strip().lower()
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
        """Writes the PDB file content of the first ligand_code to output_pdb_path."""

        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # Check the properties
        fu.check_properties(self, self.properties)

        #Downloading PDB_files
        pdb_string = download_ligand(self.ligand_code, self.url, out_log, self.global_log)
        write_pdb(pdb_string, self.output_pdb_path, None, out_log, self.global_log)

def main():
    """Command line interface."""
    parser = argparse.ArgumentParser(description="Wrapper for the PDB ('http://www.rcsb.org/pdb/home/home.do') mirror of the MMB group REST API ('http://mmb.irbbarcelona.org/api/') for additional help in the commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_pdb_path', required=True, help="Path to the output PDB ligand file.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    #Specific call of each building block
    Ligand(output_pdb_path=args.output_pdb_path, properties=properties).launch()

if __name__ == '__main__':
    main()
