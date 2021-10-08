#!/usr/bin/env python

"""Module containing the Drugbank class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *


class Drugbank(BiobbObject):
    """
    | biobb_io Drugbank
    | This class is a wrapper for the `Drugbank <https://www.drugbank.ca/>`_ REST API.
    | Download a single component in SDF format from the `Drugbank <https://www.drugbank.ca/>`_ REST API.

    Args:
        output_sdf_path (str): Path to the output SDF component file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_drugbank.sdf>`_. Accepted formats: sdf (edam:format_3814).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **drugbank_id** (*str*) - (None) Drugbank component id.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.drugbank import drugbank
            prop = { 
                'drugbank_id': 'DB00530' 
            }
            drugbank(output_sdf_path='/path/to/newComponent.sdf', 
                    properties=prop)

    Info:
        * wrapped_software:
            * name: Drugbank
            * license: Creative Commons
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_sdf_path, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = { 
            "out": { "output_sdf_path": output_sdf_path } 
        }

        # Properties specific for BB
        self.drugbank_id = properties.get('drugbank_id', None)
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        
    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.output_sdf_path = check_output_path(self.io_dict["out"]["output_sdf_path"], "output_sdf_path", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Drugbank <api.drugbank.Drugbank>` api.drugbank.Drugbank object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        check_mandatory_property(self.drugbank_id, 'drugbank_id', self.out_log, self.__class__.__name__)

        self.drugbank_id = self.drugbank_id.strip().lower()
        url = "https://www.drugbank.ca/structures/small_molecule_drugs/%s.sdf?type=3d"

        #Downloading SDF file
        sdf_string = download_drugbank(self.drugbank_id, url, self.out_log, self.global_log)
        write_sdf(sdf_string, self.output_sdf_path, self.out_log, self.global_log)

        return 0

def drugbank(output_sdf_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`Drugbank <api.drugbank.Drugbank>` class and
    execute the :meth:`launch() <api.drugbank.Drugbank.launch>` method."""

    return Drugbank(output_sdf_path=output_sdf_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Download a component in SDF format from the Drugbank (https://www.drugbank.ca/).", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_sdf_path', required=True, help="Path to the output SDF component file. Accepted formats: sdf.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    #Specific call of each building block
    drugbank(output_sdf_path=args.output_sdf_path, 
            properties=properties)

if __name__ == '__main__':
    main()
