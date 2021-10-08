#!/usr/bin/env python

"""Module containing the Pdb class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *


class Pdb(BiobbObject):
    """
    | biobb_io Pdb
    | This class is a wrapper for downloading a PDB structure from the Protein Data Bank.
    | Wrapper for the `Protein Data Bank in Europe <https://www.ebi.ac.uk/pdbe/>`_, the `Protein Data Bank <https://www.rcsb.org/>`_ and the `MMB PDB mirror <http://mmb.irbbarcelona.org/api/>`_ for downloading a single PDB structure.

    Args:
        output_pdb_path (str): Path to the output PDB file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_pdb.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB code.
            * **filter** (*str*) - (["ATOM", "MODEL", "ENDMDL"]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the `official PDB specification <http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)>`_.
            * **api_id** (*str*) - ("pdbe") Identifier of the PDB REST API from which the PDB structure will be downloaded. Values: pdbe (`PDB in Europe REST API <https://www.ebi.ac.uk/pdbe/pdbe-rest-api>`_), pdb (`RCSB PDB REST API <https://data.rcsb.org/>`_), mmb (`MMB PDB mirror API <http://mmb.irbbarcelona.org/api/>`_).
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.pdb import pdb
            prop = { 
                'pdb_code': '2VGB', 
                'filter': ['ATOM', 'MODEL', 'ENDMDL'], 
                'api_id': 'pdbe' 
            }
            pdb(output_pdb_path='/path/to/newStructure.pdb', 
                properties=prop)

    Info:
        * wrapped_software:
            * name: Protein Data Bank
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_pdb_path, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = { 
            "out": { "output_pdb_path": output_pdb_path } 
        }

        # Properties specific for BB
        self.api_id = properties.get('api_id', 'pdbe')
        self.pdb_code = properties.get('pdb_code', None)
        self.filter = properties.get('filter', ['ATOM', 'MODEL', 'ENDMDL'])
        self.properties = properties

        # Check the properties
        self.check_properties(properties)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.output_pdb_path = check_output_path(self.io_dict["out"]["output_pdb_path"], "output_pdb_path", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Pdb <api.pdb.Pdb>` api.pdb.Pdb object."""
        
        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        check_mandatory_property(self.pdb_code, 'pdb_code', self.out_log, self.__class__.__name__)

        self.pdb_code = self.pdb_code.strip().lower()

        # Downloading PDB file
        pdb_string = download_pdb(self.pdb_code, self.api_id, self.out_log, self.global_log)
        write_pdb(pdb_string, self.output_pdb_path, self.filter, self.out_log, self.global_log)

        return 0

def pdb(output_pdb_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`Pdb <api.pdb.Pdb>` class and
    execute the :meth:`launch() <api.pdb.Pdb.launch>` method."""

    return Pdb(output_pdb_path=output_pdb_path,
                properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="This class is a wrapper for downloading a PDB structure from the Protein Data Bank.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_pdb_path', required=True, help="Path to the output PDB file. Accepted formats: pdb.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    pdb(output_pdb_path=args.output_pdb_path, 
        properties=properties)

if __name__ == '__main__':
    main()
