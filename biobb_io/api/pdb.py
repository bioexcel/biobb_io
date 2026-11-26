#!/usr/bin/env python

"""Module containing the Pdb class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher

from biobb_io.api.common import (
    check_mandatory_property,
    download_pdb,
    write_pdb,
)


class Pdb(BiobbObject):
    """
    | biobb_io Pdb
    | This class is a wrapper for downloading a PDB structure from the Protein Data Bank.
    | Wrapper for the `Protein Data Bank in Europe <https://www.ebi.ac.uk/pdbe/>`_, the `Protein Data Bank <https://www.rcsb.org/>`_ and the `MMB PDB mirror <https://mdb-login.bsc.es/api/>`_ for downloading a single PDB structure.

    Args:
        output_pdb_path (str): Path to the output PDB file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_pdb.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB code.
            * **filter** (*str*) - (["ATOM", "MODEL", "ENDMDL"]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the `official PDB specification <http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)>`_.
            * **api_id** (*str*) - ("pdbe") Identifier of the PDB REST API from which the PDB structure will be downloaded. Values: pdbe (`PDB in Europe REST API <https://www.ebi.ac.uk/pdbe/pdbe-rest-api>`_), pdb (`RCSB PDB REST API <https://data.rcsb.org/>`_), mmb (`MMB PDB mirror API <https://mdb-login.bsc.es/api/>`_).
            * **assembly** (*str*) - (None) Biological Assembly ID to be downloaded. If None or False the asemitric unit will be downloaded.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

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

    def __init__(self, output_pdb_path: str, properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def stage_files(self) -> None:
        """The block does not use the sandbox: there are no files to stage."""

    def run(self) -> None:
        """Execute the :class:`Pdb <api.pdb.Pdb>` api.pdb.Pdb object."""

        check_mandatory_property(
            self.pdb_code, "pdb_code", self.out_log, self.__class__.__name__
        )

        self.pdb_code = self.pdb_code.strip().lower()

        # Downloading PDB file
        pdb_string = download_pdb(
            self.pdb_code, self.api_id, self.assembly, self.out_log, self.global_log,
        )
        write_pdb(
            pdb_string, self.io_dict["out"]["output_pdb_path"], self.filter, self.out_log, self.global_log
        )


pdb = launcher(Pdb)

if __name__ == "__main__":
    Pdb.main()
