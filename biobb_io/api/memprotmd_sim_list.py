#!/usr/bin/env python

"""Module containing the MemProtMDSimList class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_io.api.common import get_memprotmd_sim_list, write_file


class MemProtMDSimList(BiobbObject):
    """
    | biobb_io MemProtMDSimList
    | This class is a wrapper of the MemProtMD to get all available membrane-protein systems from its REST API.
    | Wrapper for the `MemProtMD DB REST API <http://memprotmd.bioch.ox.ac.uk/>`_ to get all available membrane-protein systems (simulations).

    Args:
        output_simulations (str): Path to the output JSON file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_sim_list_schema_validator.json>`_. Accepted formats: json (edam:format_3464).
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

    def __init__(self, output_simulations: str, properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def stage_files(self) -> None:
        """The block does not use the sandbox: there are no files to stage."""

    def run(self) -> None:
        """Execute the :class:`MemProtMDSimList <api.memprotmd_sim_list.MemProtMDSimList>` api.memprotmd_sim_list.MemProtMDSimList object."""

        # get JSON object
        json_string = get_memprotmd_sim_list(self.out_log, self.global_log)

        # write JSON file
        write_file(json_string, self.io_dict["out"]["output_simulations"], self.out_log, self.global_log)


memprotmd_sim_list = launcher(MemProtMDSimList)

if __name__ == "__main__":
    MemProtMDSimList.main()
