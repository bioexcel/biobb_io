#!/usr/bin/env python

"""Module containing the ApiBindingSite class and the command line interface."""

import argparse
import json
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger

from biobb_io.api.common import (
    check_mandatory_property,
    check_output_path,
    download_binding_site,
    write_json,
)


class ApiBindingSite(BiobbObject):
    """
    | biobb_io ApiBindingSite
    | This class is a wrapper for the `PDBe REST API <https://www.ebi.ac.uk/pdbe/api/doc/#pdb_apidiv_call_16_calltitle>`_ Binding Sites endpoint.
    | This call provides details on binding sites in the entry as per STRUCT_SITE records in PDB files, such as ligand, residues in the site, description of the site, etc.

    Args:
        output_json_path (str): Path to the JSON file with the binding sites for the requested structure. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_binding_site.json>`_. Accepted formats: json (edam:format_3464).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB code.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.api_binding_site import api_binding_site
            prop = {
                'pdb_code': '4i23'
            }
            api_binding_site(output_json_path='/path/to/newBindingSites.json',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: PDBe REST API
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_json_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {"out": {"output_json_path": output_json_path}}

        # Properties specific for BB
        self.pdb_code = properties.get("pdb_code", None)
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """Checks all the input/output paths and parameters"""
        self.output_json_path = check_output_path(
            self.io_dict["out"]["output_json_path"],
            "output_json_path",
            False,
            out_log,
            self.__class__.__name__,
        )

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`ApiBindingSite <api.api_binding_site.ApiBindingSite>` api.api_binding_site.ApiBindingSite object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0
        # self.stage_files()

        check_mandatory_property(
            self.pdb_code, "pdb_code", self.out_log, self.__class__.__name__
        )

        self.pdb_code = self.pdb_code.strip().lower()
        url = "https://www.ebi.ac.uk/pdbe/api/pdb/entry/binding_sites/%s"

        # get JSON object
        json_string = download_binding_site(
            self.pdb_code, url, self.out_log, self.global_log
        )

        # get number of binding sites
        fu.log(
            "%d binding sites found" % (len(json.loads(json_string)[self.pdb_code])),
            self.out_log,
            self.global_log,
        )

        # write JSON file
        write_json(json_string, self.output_json_path, self.out_log, self.global_log)

        self.check_arguments(output_files_created=True, raise_exception=False)

        return 0


def api_binding_site(
    output_json_path: str, properties: Optional[dict] = None, **kwargs
) -> int:
    """Execute the :class:`ApiBindingSite <api.api_binding_site.ApiBindingSite>` class and
    execute the :meth:`launch() <api.api_binding_site.ApiBindingSite.launch>` method."""

    return ApiBindingSite(
        output_json_path=output_json_path, properties=properties, **kwargs
    ).launch()

    api_binding_site.__doc__ = ApiBindingSite.__doc__


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(
        description="This class is a wrapper for the PDBe REST API Binding Sites endpoint",
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
        "--output_json_path",
        required=True,
        help="Path to the JSON file with the binding sites for the requested structure. Accepted formats: json.",
    )

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    api_binding_site(output_json_path=args.output_json_path, properties=properties)


if __name__ == "__main__":
    main()
