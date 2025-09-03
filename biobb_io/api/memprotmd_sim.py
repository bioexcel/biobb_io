#!/usr/bin/env python

"""Module containing the MemProtMDSim class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger

from biobb_io.api.common import (
    check_mandatory_property,
    check_output_path,
    get_memprotmd_sim,
)


class MemProtMDSim(BiobbObject):
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
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

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

    def __init__(self, output_simulation, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {"out": {"output_simulation": output_simulation}}

        # Properties specific for BB
        self.pdb_code = properties.get("pdb_code", None)
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """Checks all the input/output paths and parameters"""
        self.output_simulation = check_output_path(
            self.io_dict["out"]["output_simulation"],
            "output_simulation",
            False,
            out_log,
            self.__class__.__name__,
        )

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`MemProtMDSim <api.memprotmd_sim.MemProtMDSim>` api.memprotmd_sim.MemProtMDSim object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0

        check_mandatory_property(
            self.pdb_code, "pdb_code", self.out_log, self.__class__.__name__
        )

        # get simulation files and save to output
        get_memprotmd_sim(
            self.pdb_code, self.output_simulation, self.out_log, self.global_log
        )

        self.check_arguments(output_files_created=True, raise_exception=False)

        return 0


def memprotmd_sim(
    output_simulation: str, properties: Optional[dict] = None, **kwargs
) -> int:
    """Execute the :class:`MemProtMDSim <api.memprotmd_sim.MemProtMDSim>` class and
    execute the :meth:`launch() <api.memprotmd_sim.MemProtMDSim.launch>` method."""
    return MemProtMDSim(**dict(locals())).launch()


memprotmd_sim.__doc__ = MemProtMDSim.__doc__
main = MemProtMDSim.get_main(memprotmd_sim, "Wrapper for the MemProtMD DB REST API (http://memprotmd.bioch.ox.ac.uk/) to download a simulation.")

if __name__ == "__main__":
    main()
