#!/usr/bin/env python

"""Module containing the MDDB class and the command line interface."""

import argparse
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger

from biobb_io.api.common import (
    check_mandatory_property,
    check_output_path,
    download_mddb_top,
    write_pdb,
    download_mddb_trj,
    write_bin
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
            * **frames** (*str*) - (None) Specify a frame range for the returned trajectory. Ranges are defined by dashes, and multiple ranges can be defined separated by commas. It can also be defined as the start:end:step format (ie: '10:20:2').
            * **selection** (*str*) - (None) Specify a NGL-formatted selection for the returned trajectory. See here for the kind of selection that can be used: http://nglviewer.org/ngl/api/manual/usage/selection-language.html.
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

    def __init__(self, output_top_path, output_trj_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {"out": {"output_top_path": output_top_path, "output_trj_path": output_trj_path}}

        # Properties specific for BB
        self.project_id = properties.get("project_id", None)
        self.node_id = properties.get("node_id", "mmb")
        self.trj_format = properties.get("trj_format", "xtc")
        self.frames = properties.get("frames", "")
        self.selection = properties.get("selection", "*")
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """Checks all the input/output paths and parameters"""
        self.output_top_path = check_output_path(
            self.io_dict["out"]["output_top_path"],
            "output_top_path",
            False,
            out_log,
            self.__class__.__name__,
        )
        self.output_trj_path = check_output_path(
            self.io_dict["out"]["output_trj_path"],
            "output_trj_path",
            False,
            out_log,
            self.__class__.__name__,
        )

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`MDDB <api.mddb.MDDB>` api.mddb.MDDB object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0

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
        write_pdb(top_string, self.output_top_path, None, self.out_log, self.global_log)

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
        write_bin(trj_string, self.output_trj_path, self.out_log, self.global_log)

        self.check_arguments(output_files_created=True, raise_exception=False)

        return 0


def mddb(output_top_path: str, output_trj_path: str, properties: Optional[dict] = None, **kwargs) -> int:
    """Execute the :class:`MDDB <api.mddb.MDDB>` class and
    execute the :meth:`launch() <api.mddb.MDDB.launch>` method."""

    return MDDB(
        output_top_path=output_top_path, output_trj_path=output_trj_path, properties=properties, **kwargs
    ).launch()

    mddb.__doc__ = MDDB.__doc__


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(
        description="This class is a wrapper for downloading a trajectory / topology pair from the MDDB Database.",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999),
    )
    parser.add_argument(
        "-c",
        "--config",
        required=False,
        help="This file can be a YAML file, JSON file or JSON string",
    )

    # Specific args of each building block
    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument(
        "-o",
        "--output_top_path",
        required=True,
        help="Path to the output toplogy file. Accepted formats: pdb.",
    )
    required_args.add_argument(
        "-t",
        "--output_trj_path",
        required=True,
        help="Path to the output trajectory file. Accepted formats: mdcrd, trr, xtc.",
    )

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    mddb(output_top_path=args.output_top_path, output_trj_path=args.output_trj_path, properties=properties)


if __name__ == "__main__":
    main()
