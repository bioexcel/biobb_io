#!/usr/bin/env python

"""Module containing the Ligand class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *


class Ligand(BiobbObject):
    """
    | biobb_io Ligand
    | This class is a wrapper for downloading a PDB ligand from the Protein Data Bank.
    | Wrapper for the `Protein Data Bank in Europe <https://www.ebi.ac.uk/pdbe/>`_ and the `MMB PDB mirror <http://mmb.irbbarcelona.org/api/>`_ for downloading a single PDB ligand.

    Args:
        output_pdb_path (str): Path to the output PDB ligand file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_ligand.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **ligand_code** (*str*) - (None) RSCB PDB ligand code.
            * **api_id** (*str*) - ("pdbe") Identifier of the PDB REST API from which the PDB structure will be downloaded. Values: pdbe (`PDB in Europe REST API <https://www.ebi.ac.uk/pdbe/pdbe-rest-api>`_), mmb (`MMB PDB mirror API <http://mmb.irbbarcelona.org/api/>`_).
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.ligand import ligand
            prop = { 
                'ligand_code': 'CPB', 
                'api_id': 'pdbe' 
            }
            ligand(output_pdb_path='/path/to/newLigand.pdb', 
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
        self.ligand_code = properties.get('ligand_code', None)
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        
    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.output_pdb_path = check_output_path(self.io_dict["out"]["output_pdb_path"], "output_pdb_path", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Ligand <api.ligand.Ligand>` api.ligand.Ligand object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        check_mandatory_property(self.ligand_code, 'ligand_code', self.out_log, self.__class__.__name__)

        self.ligand_code = self.ligand_code.strip().lower()

        #Downloading PDB file
        pdb_string = download_ligand(self.ligand_code, self.api_id, self.out_log, self.global_log)
        write_pdb(pdb_string, self.output_pdb_path, None, self.out_log, self.global_log)

        return 0

def ligand(output_pdb_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`Ligand <api.ligand.Ligand>` class and
    execute the :meth:`launch() <api.ligand.Ligand.launch>` method."""

    return Ligand(output_pdb_path=output_pdb_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Wrapper for the Protein Data Bank in Europe (https://www.ebi.ac.uk/pdbe/) and the MMB PDB mirror (http://mmb.irbbarcelona.org/api/) for downloading a single PDB ligand.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    #Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-o', '--output_pdb_path', required=True, help="Path to the output PDB ligand file. Accepted formats: pdb.")

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    #Specific call of each building block
    ligand(output_pdb_path=args.output_pdb_path, 
            properties=properties)

if __name__ == '__main__':
    main()
