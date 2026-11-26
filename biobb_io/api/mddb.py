#!/usr/bin/env python

"""Module containing the MDDB class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher

from biobb_io.api.common import (
    check_mandatory_property,
    download_mddb_top,
    write_pdb,
    download_mddb_trj,
    write_bin,
    download_mddb_file,
)


class MDDB(BiobbObject):
    """
    | biobb_io MDDB
    | This class is a wrapper for downloading a trajectory / topology pair from the MDDB Database.
    | Wrapper for the `MDDB Database <https://mmb.mddbr.eu/>`_ for downloading a trajectory and its corresponding topology.

    Args:
        output_top_path (str): Path to the output toplogy file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_mddb.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_trj_path (str): Path to the output trajectory file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_mddb.xtc>`_. Accepted formats: mdcrd (edam:format_3878), trr (edam:format_3910), xtc (edam:format_3875).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **project_id** (*str*) - (None) Project accession or identifier.
            * **node_id** (*str*) - ("mmb") MDDB node identifier.
            * **trj_format** (*str*) - ("xtc") Trajectory format. Values: mdcrd (AMBER trajectory format), trr (Trajectory of a simulation experiment used by GROMACS), xtc (Portable binary format for trajectories produced by GROMACS package).
            * **frames** (*str*) - ("") Specify a frame range for the returned trajectory. Ranges are defined by dashes, and multiple ranges can be defined separated by commas. It can also be defined as the start:end:step format (ie: '10:20:2').
            * **selection** (*str*) - ("*") Specify a NGL-formatted selection for the returned trajectory. See here for the kind of selection that can be used: http://nglviewer.org/ngl/api/manual/usage/selection-language.html.
            * **extra_files** (*list*) - ([]) List of extra files to download. It should be a tuple with the name of the file and the path to be saved.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.mddb import mddb
            prop = {
                'project_id': 'A0001',
                'trj_format': 'xtc'
            }
            mddb(output_top_path='/path/to/newTopology.pdb',
                 output_trj_path='/path/to/newTrajectory.pdb',
                 properties=prop)

    Info:
        * wrapped_software:
            * name: MDDB Database
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    custom_flags = {"output_top_path": "-o", "output_trj_path": "-t"}

    def __init__(self, output_top_path: str, output_trj_path: str, properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def stage_files(self) -> None:
        """The block does not use the sandbox: there are no files to stage."""

    def run(self) -> None:
        """Execute the :class:`MDDB <api.mddb.MDDB>` api.mddb.MDDB object."""

        check_mandatory_property(
            self.project_id, "project_id", self.out_log, self.__class__.__name__
        )

        self.project_id = self.project_id.strip().upper()

        # Downloading topology file
        top_string = download_mddb_top(
            self.project_id,
            self.node_id,
            self.selection,
            self.out_log,
            self.global_log,
            self.__class__.__name__
        )
        write_pdb(top_string, self.io_dict["out"]["output_top_path"], None, self.out_log, self.global_log)

        # Downloading trajectory file
        trj_string = download_mddb_trj(
            self.project_id,
            self.node_id,
            self.trj_format,
            self.frames,
            self.selection,
            self.out_log,
            self.global_log,
            self.__class__.__name__,
        )
        write_bin(trj_string, self.io_dict["out"]["output_trj_path"], self.out_log, self.global_log)

        for (extra_file, extra_path) in self.extra_files:
            file_string = download_mddb_file(
                self.project_id,
                self.node_id,
                extra_file,
                self.out_log,
                self.global_log,
                self.__class__.__name__,
            )
            write_bin(file_string, extra_path, self.out_log, self.global_log)


mddb = launcher(MDDB)

if __name__ == "__main__":
    MDDB.main()
