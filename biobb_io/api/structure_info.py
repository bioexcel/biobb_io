#!/usr/bin/env python

"""Module containing the StructureInfo class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *

class StructureInfo():
    """
    | biobb_io StructureInfo
    | This class is a wrapper for getting all the available information of a structure from the Protein Data Bank.
    | Wrapper for the `MMB PDB mirror <http://mmb.irbbarcelona.org/api/>`_ for getting all the available information of a structure from the Protein Data Bank.

    Args:
        output_json_path (str): Path to the output JSON file with all the structure information. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/ref_str_info.json>`_. Accepted formats: json (edam:format_3464).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB structure code.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.structure_info import structure_info
            prop = { 
                'pdb_code': '2vgb'
            }
            structure_info(output_json_path='/path/to/newStructure.sdf', 
                        properties=prop)

    Info:
        * wrapped_software:
            * name: Protein Data Bank
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_json_path, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.output_json_path = output_json_path

        # Properties specific for BB
        self.pdb_code = properties.get('pdb_code', None)
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
        self.output_json_path = check_output_path(self.output_json_path, "output_json_path", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`StructureInfo <api.structure_info.StructureInfo>` api.structure_info.StructureInfo object."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        check_mandatory_property(self.pdb_code, 'pdb_code', out_log, self.__class__.__name__)

        self.pdb_code = self.pdb_code.strip().lower()
        url = "http://mmb.irbbarcelona.org/api/pdb/%s.json"

        # Downloading PDB file
        json_string = download_str_info(self.pdb_code, url, out_log, self.global_log)
        write_json(json_string, self.output_json_path, out_log, self.global_log)

        return 0

def structure_info(output_json_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`StructureInfo <api.structure_info.StructureInfo>` class and
    execute the :meth:`launch() <api.structure_info.StructureInfo.launch>` method."""

    return StructureInfo(output_json_path=output_json_path,
                properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="This class is a wrapper for getting all the available information of a structure from the Protein Data Bank.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_json_path', required=True, help="Path to the output JSON file with all the structure information. Accepted formats: json.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    structure_info(output_json_path=args.output_json_path, 
        properties=properties)

if __name__ == '__main__':
    main()
