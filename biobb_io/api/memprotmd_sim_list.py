#!/usr/bin/env python

"""Module containing the MemProtMDSimList class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import check_output_path, get_memprotmd_sim_list, write_json


class MemProtMDSimList(BiobbObject):
    """
    | biobb_io MemProtMDSimList
    | This class is a wrapper of the MemProtMD to get all available membrane-protein systems from its REST API.
    | Wrapper for the `MemProtMD DB REST API <http://memprotmd.bioch.ox.ac.uk/>`_ to get all available membrane-protein systems (simulations).

    Args:
        output_simulations (str): Path to the output JSON file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_sim_list.json>`_. Accepted formats: json (edam:format_3464).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.memprotmd_sim_list import memprotmd_sim_list
            prop = { }
            memprotmd_sim_list(output_simulations='/path/to/newSimulationlist.json',
                                properties=prop)

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

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {"out": {"output_simulations": output_simulations}}

        # Properties specific for BB
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """Checks all the input/output paths and parameters"""
        self.output_simulations = check_output_path(
            self.io_dict["out"]["output_simulations"],
            "output_simulations",
            False,
            out_log,
            self.__class__.__name__,
        )

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`MemProtMDSimList <api.memprotmd_sim_list.MemProtMDSimList>` api.memprotmd_sim_list.MemProtMDSimList object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0

        # get JSON object
        json_string = get_memprotmd_sim_list(self.out_log, self.global_log)

        # write JSON file
        write_json(json_string, self.output_simulations, self.out_log, self.global_log)

        self.check_arguments(output_files_created=True, raise_exception=False)

        return 0


def memprotmd_sim_list(
    output_simulations: str, properties: Optional[dict] = None, **kwargs
) -> int:
    """Execute the :class:`MemProtMDSimList <api.memprotmd_sim_list.MemProtMDSimList>` class and
    execute the :meth:`launch() <api.memprotmd_sim_list.MemProtMDSimList.launch>` method."""
    return MemProtMDSimList(**dict(locals())).launch()


memprotmd_sim_list.__doc__ = MemProtMDSimList.__doc__
main = MemProtMDSimList.get_main(memprotmd_sim_list, "Wrapper for the MemProtMD DB REST API (http://memprotmd.bioch.ox.ac.uk/) to get all available membrane-protein systems (simulations).")

if __name__ == "__main__":
    main()
