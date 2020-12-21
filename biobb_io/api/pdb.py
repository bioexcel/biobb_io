#!/usr/bin/env python

"""Module containing the Pdb class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *

class Pdb():
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

        # Input/Output files
        self.output_pdb_path = output_pdb_path

        # Properties specific for BB
        self.api_id = properties.get('api_id', 'pdbe')
        self.pdb_code = properties.get('pdb_code', None)
        self.filter = properties.get('filter', ['ATOM', 'MODEL', 'ENDMDL'])
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
        self.output_pdb_path = check_output_path(self.output_pdb_path, "output_pdb_path", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Pdb <api.pdb.Pdb>` api.pdb.Pdb object."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        check_mandatory_property(self.pdb_code, 'pdb_code', out_log, self.__class__.__name__)

        self.pdb_code = self.pdb_code.strip().lower()

        # Downloading PDB file
        pdb_string = download_pdb(self.pdb_code, self.api_id, out_log, self.global_log)
        write_pdb(pdb_string, self.output_pdb_path, self.filter, out_log, self.global_log)

def pdb(output_pdb_path: str, properties: dict = None, **kwargs) -> None:
    """Execute the :class:`Pdb <api.pdb.Pdb>` class and
    execute the :meth:`launch() <api.pdb.Pdb.launch>` method."""

    return Pdb(output_pdb_path=output_pdb_path,
                properties=properties).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Wrapper for the Protein Data Bank in Europe (https://www.ebi.ac.uk/pdbe/), the Protein Data Bank (https://www.rcsb.org/) and the MMB PDB mirror (http://mmb.irbbarcelona.org/api/) for downloading a single PDB structure.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_pdb_path', required=True, help="Path to the output PDB file. Accepted formats: pdb.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    Pdb(output_pdb_path=args.output_pdb_path, 
        properties=properties).launch()

if __name__ == '__main__':
    main()
