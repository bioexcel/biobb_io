#!/usr/bin/env python

"""Module containing the MemProtMDSim class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *

class MemProtMDSim():
    """
    | biobb_io MemProtMDSim
    | This class is a wrapper of the MemProtMD to download a simulation using its REST API.
    | Wrapper for the `MemProtMD DB REST API <http://memprotmd.bioch.ox.ac.uk/>`_ to download a simulation.

    Args:
        output_simulation (str): Path to the output simulation in a ZIP file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_sim.zip>`_. Accepted formats: zip (edam:format_3987).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB code.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.memprotmd_sim import memprotmd_sim
            prop = { 
                'pdb_code': '2VGB' 
            }
            memprotmd_sim(output_simulation='/path/to/newSimulation.zip', 
                        properties=prop)

    Info:
        * wrapped_software:
            * name: MemProtMD DB
            * license: Creative Commons
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_simulation, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.output_simulation = output_simulation

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
        self.output_simulation = check_output_path(self.output_simulation, "output_simulation", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`MemProtMDSim <api.memprotmd_sim.MemProtMDSim>` api.memprotmd_sim.MemProtMDSim object."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        check_mandatory_property(self.pdb_code, 'pdb_code', out_log, self.__class__.__name__)

        # get simulation files and save to output
        json_string = get_memprotmd_sim(self.pdb_code, self.output_simulation, out_log, self.global_log)

def memprotmd_sim(output_simulation: str, properties: dict = None, **kwargs) -> None:
    """Execute the :class:`MemProtMDSim <api.memprotmd_sim.MemProtMDSim>` class and
    execute the :meth:`launch() <api.memprotmd_sim.MemProtMDSim.launch>` method."""

    return MemProtMDSim(output_simulation=output_simulation,
                    properties=properties).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Wrapper for the MemProtMD DB REST API (http://memprotmd.bioch.ox.ac.uk/) to download a simulation.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_simulation', required=True, help="Path to the output simulation in a ZIP file. Accepted formats: zip.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    MemProtMDSim(output_simulation=args.output_simulation, properties=properties).launch()

if __name__ == '__main__':
    main()
