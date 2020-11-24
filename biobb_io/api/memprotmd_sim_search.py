#!/usr/bin/env python

"""Module containing the MemProtMDSimSearch class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *

class MemProtMDSimSearch():
    """
    | biobb_io MemProtMDSimSearch
    | This class is a wrapper of the MemProtMD to perform advanced searches in the MemProtMD DB using its REST API.
    | Wrapper for the `MemProtMD DB REST API <http://memprotmd.bioch.ox.ac.uk/>`_ to perform advanced searches.

    Args:
        output_simulations (str): Path to the output JSON file. File type: output. `Sample file <>`_. Accepted formats: json.
        properties (dic):
            * **collection_name** (*str*) - ("refs") Remove temporal files.
            * **keyword** (*str*) - (None) Remove temporal files.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Info:
        * wrapped_software:
            * name: MemProtMD DB
            * license: Creative Commons
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_simulations, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.output_simulations = output_simulations

        # Properties specific for BB
        self.collection_name = properties.get('collection_name', 'refs')
        self.keyword = properties.get('keyword', None)
        self.properties = properties

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.output_simulations = check_output_path(self.output_simulations, "output_simulations", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Writes all the simulation in JSON format to the output_simulations file"""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        # get JSON object
        json_string = get_memprotmd_sim_search(self.collection_name, self.keyword, out_log, self.global_log)

        # write JSON file
        write_json(json_string, self.output_simulations, self.out_log, self.global_log)

def main():
    """Command line interface."""
    parser = argparse.ArgumentParser(description="Wrapper for the MemProtMD DB REST API (http://memprotmd.bioch.ox.ac.uk/) to perform advanced searches.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_simulations', required=True, help="Output file name")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    MemProtMDSimSearch(output_simulations=args.output_simulations, properties=properties).launch()

if __name__ == '__main__':
    main()
