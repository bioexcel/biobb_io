#!/usr/bin/env python

"""Module containing the Mmcif class and the command line interface."""

import argparse
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger

from biobb_io.api.common import (
    check_mandatory_property,
    check_output_path,
    download_mmcif,
    write_mmcif,
)


class Mmcif(BiobbObject):
    """
    | biobb_io Mmcif
    | This class is a wrapper for downloading a MMCIF structure from the Protein Data Bank.
    | Wrapper for the `Protein Data Bank in Europe <https://www.ebi.ac.uk/pdbe/>`_, the `Protein Data Bank <https://www.rcsb.org/>`_ and the `MMB PDB mirror <http://mmb.irbbarcelona.org/api/>`_ for downloading a single MMCIF structure.

    Args:
        output_mmcif_path (str): Path to the output MMCIF file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/ref_output.mmcif>`_. Accepted formats: cif (edam:format_1477), mmcif (edam:format_1477).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB code.
            * **api_id** (*str*) - ("pdbe") Identifier of the PDB REST API from which the MMCIF structure will be downloaded. Values: pdbe (`PDB in Europe REST API <https://www.ebi.ac.uk/pdbe/pdbe-rest-api>`_), pdb (`RCSB PDB REST API <https://data.rcsb.org/>`_), mmb (`MMB PDB mirror API <http://mmb.irbbarcelona.org/api/>`_).
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.mmcif import mmcif
            prop = {
                'pdb_code': '2VGB',
                'api_id': 'pdbe'
            }
            mmcif(output_mmcif_path='/path/to/newStructure.mmcif',
                properties=prop)

    Info:
        * wrapped_software:
            * name: Protein Data Bank
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_mmcif_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {"out": {"output_mmcif_path": output_mmcif_path}}

        # Properties specific for BB
        self.api_id = properties.get("api_id", "pdbe")
        self.pdb_code = properties.get("pdb_code", None)
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """Checks all the input/output paths and parameters"""
        self.output_mmcif_path = check_output_path(
            self.io_dict["out"]["output_mmcif_path"],
            "output_mmcif_path",
            False,
            out_log,
            self.__class__.__name__,
        )

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Mmcif <api.mmcif.Mmcif>` api.mmcif.Mmcif object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0

        check_mandatory_property(
            self.pdb_code, "pdb_code", self.out_log, self.__class__.__name__
        )

        self.pdb_code = self.pdb_code.strip().lower()

        # Downloading PDB file
        mmcif_string = download_mmcif(
            self.pdb_code, self.api_id, self.out_log, self.global_log
        )
        write_mmcif(mmcif_string, self.output_mmcif_path, self.out_log, self.global_log)

        self.check_arguments(output_files_created=True, raise_exception=False)

        return 0


def mmcif(output_mmcif_path: str, properties: Optional[dict] = None, **kwargs) -> int:
    """Execute the :class:`Mmcif <api.mmcif.Mmcif>` class and
    execute the :meth:`launch() <api.mmcif.Mmcif.launch>` method."""

    return Mmcif(
        output_mmcif_path=output_mmcif_path, properties=properties, **kwargs
    ).launch()

    mmcif.__doc__ = Mmcif.__doc__


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(
        description="This class is a wrapper for downloading a MMCIF structure from the Protein Data Bank.",
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
        "--output_mmcif_path",
        required=True,
        help="Path to the output MMCIF file. Accepted formats: cif, mmcif.",
    )

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    mmcif(output_mmcif_path=args.output_mmcif_path, properties=properties)


if __name__ == "__main__":
    main()
