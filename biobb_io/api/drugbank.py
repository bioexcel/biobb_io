#!/usr/bin/env python

"""Module containing the Drugbank class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *

class Drugbank():
    """
    | biobb_io Drugbank
    | This class is a wrapper for the `Drugbank <https://www.drugbank.ca/>`_ REST API.
    | Download a single component in SDF format from the `Drugbank <https://www.drugbank.ca/>`_ REST API.

    Args:
        output_sdf_path (str): Path to the output SDF component file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_drugbank.sdf>`_. Accepted formats: sdf (edam:format_3814).
        properties (dic):
            * **drugbank_id** (*str*) - (None) Drugbank component id.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Info:
        * wrapped_software:
            * name: Drugbank
            * license: Creative Commons
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_sdf_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.output_sdf_path = output_sdf_path

        # Properties specific for BB
        self.drugbank_id = properties.get('drugbank_id', None)
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
        self.output_sdf_path = check_output_path(self.output_sdf_path, "output_sdf_path", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Writes the SDF content of the first drugbank_id to output_sdf_path."""

        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        check_mandatory_property(self.drugbank_id, 'drugbank_id', out_log, self.__class__.__name__)

        self.drugbank_id = self.drugbank_id.strip().lower()
        url = "https://www.drugbank.ca/structures/small_molecule_drugs/%s.sdf?type=3d"

        #Downloading SDF file
        sdf_string = download_drugbank(self.drugbank_id, url, out_log, self.global_log)
        write_sdf(sdf_string, self.output_sdf_path, out_log, self.global_log)

def main():
    """Command line interface."""
    parser = argparse.ArgumentParser(description="Download a component in SDF format from the Drugbank (https://www.drugbank.ca/).", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_sdf_path', required=True, help="Path to the output SDF component file. Accepted formats: sdf.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    #Specific call of each building block
    Drugbank(output_sdf_path=args.output_sdf_path, properties=properties).launch()

if __name__ == '__main__':
    main()
