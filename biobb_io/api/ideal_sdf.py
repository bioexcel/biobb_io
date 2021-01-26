#!/usr/bin/env python

"""Module containing the IdealSdf class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *

class IdealSdf():
    """
    | biobb_io IdealSdf
    | This class is a wrapper for downloading an ideal SDF ligand from the Protein Data Bank.
    | Wrapper for the `Protein Data Bank in Europe <https://www.ebi.ac.uk/pdbe/>`_ and the `Protein Data Bank <https://www.rcsb.org/>`_ for downloading a single ideal SDF ligand.

    Args:
        output_sdf_path (str): Path to the output SDF file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/ref_output.sdf>`_. Accepted formats: sdf (edam:format_3814).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **ligand_code** (*str*) - (None) RSCB PDB ligand code.
            * **api_id** (*str*) - ("pdbe") Identifier of the PDB REST API from which the SDF structure will be downloaded. Values: pdbe (`PDB in Europe REST API <https://www.ebi.ac.uk/pdbe/pdbe-rest-api>`_), pdb (`RCSB PDB REST API <https://data.rcsb.org/>`_).
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.ideal_sdf import ideal_sdf
            prop = { 
                'ligand_code': 'HYZ', 
                'api_id': 'pdbe' 
            }
            ideal_sdf(output_sdf_path='/path/to/newStructure.sdf', 
                        properties=prop)

    Info:
        * wrapped_software:
            * name: Protein Data Bank
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_sdf_path, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.output_sdf_path = output_sdf_path

        # Properties specific for BB
        self.api_id = properties.get('api_id', 'pdbe')
        self.ligand_code = properties.get('ligand_code', None)
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
        """Execute the :class:`IdealSdf <api.ideal_sdf.IdealSdf>` api.ideal_sdf.IdealSdf object."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        check_mandatory_property(self.ligand_code, 'ligand_code', out_log, self.__class__.__name__)

        self.ligand_code = self.ligand_code.strip()

        # Downloading PDB file
        sdf_string = download_ideal_sdf(self.ligand_code, self.api_id, out_log, self.global_log)
        write_sdf(sdf_string, self.output_sdf_path, out_log, self.global_log)

        return 0

def ideal_sdf(output_sdf_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`IdealSdf <api.ideal_sdf.IdealSdf>` class and
    execute the :meth:`launch() <api.ideal_sdf.IdealSdf.launch>` method."""

    return IdealSdf(output_sdf_path=output_sdf_path,
                properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="This class is a wrapper for downloading an ideal SDF ligand from the Protein Data Bank.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_sdf_path', required=True, help="Path to the output SDF file. Accepted formats: sdf.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    ideal_sdf(output_sdf_path=args.output_sdf_path, 
        properties=properties)

if __name__ == '__main__':
    main()
