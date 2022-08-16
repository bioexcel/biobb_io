#!/usr/bin/env python

"""Module containing the AlphaFold class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_io.api.common import *


class AlphaFold(BiobbObject):
    """
    | biobb_io AlphaFold
    | This class is a wrapper for downloading a PDB structure from the AlphaFold Protein Structure Database.
    | Wrapper for the `AlphaFold Protein Structure Database <https://alphafold.ebi.ac.uk/>`_ for downloading a single PDB structure from its corresponding Uniprot code.

    Args:
        output_pdb_path (str): Path to the output PDB file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_alphafold.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **uniprot_code** (*str*) - (None) Uniprot code.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.alphafold import alphafold
            prop = { 
                'uniprot_code': 'P00489'
            }
            alphafold(output_pdb_path='/path/to/newStructure.pdb', 
                properties=prop)

    Info:
        * wrapped_software:
            * name: AlphaFold Protein Structure Database
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
        self.uniprot_code = properties.get('uniprot_code', None)
        self.properties = properties

        # Check the properties
        self.check_properties(properties)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.output_pdb_path = check_output_path(self.io_dict["out"]["output_pdb_path"], "output_pdb_path", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`AlphaFold <api.alphafold.AlphaFold>` api.alphafold.AlphaFold object."""
        
        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        check_mandatory_property(self.uniprot_code, 'uniprot_code', self.out_log, self.__class__.__name__)

        self.uniprot_code = self.uniprot_code.strip().upper()

        check_uniprot_code(self.uniprot_code, self.out_log, self.__class__.__name__)

        # Downloading PDB file
        pdb_string = download_af(self.uniprot_code, self.out_log, self.global_log, self.__class__.__name__)
        write_pdb(pdb_string, self.output_pdb_path, None, self.out_log, self.global_log)

        return 0

def alphafold(output_pdb_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`AlphaFold <api.alphafold.AlphaFold>` class and
    execute the :meth:`launch() <api.alphafold.AlphaFold.launch>` method."""

    return AlphaFold(output_pdb_path=output_pdb_path,
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
    alphafold(output_pdb_path=args.output_pdb_path, 
        properties=properties)

if __name__ == '__main__':
    main()
