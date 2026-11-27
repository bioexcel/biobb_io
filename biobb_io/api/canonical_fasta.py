#!/usr/bin/env python

"""Module containing the CanonicalFasta class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher

from biobb_io.api.common import (
    check_mandatory_property,
    download_fasta,
    write_file,
)


class CanonicalFasta(BiobbObject):
    """
    | biobb_io CanonicalFasta
    | This class is a wrapper for downloading a FASTA structure from the Protein Data Bank.
    | Wrapper for the `Protein Data Bank <https://www.rcsb.org/>`_ and the `MMB PDB mirror <https://mdb-login.bsc.es/api/>`_ for downloading a single FASTA structure.

    Args:
        output_fasta_path (str): Path to the canonical FASTA file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/canonical_fasta.fasta>`_. Accepted formats: fasta (edam:format_1929).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB code.
            * **api_id** (*str*) - ("pdbe") Identifier of the PDB REST API from which the PDB structure will be downloaded. Values: pdbe (`PDB in Europe REST API <https://www.ebi.ac.uk/pdbe/pdbe-rest-api>`_), pdb (`RCSB PDB REST API <https://data.rcsb.org/>`_), mmb (`MMB PDB mirror API <https://mdb-login.bsc.es/api/>`_).
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.canonical_fasta import canonical_fasta
            prop = {
                'pdb_code': '4i23',
                'api_id': 'pdb'
            }
            canonical_fasta(output_fasta_path='/path/to/newFasta.fasta',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: Protein Data Bank
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_fasta_path: str, properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def stage_files(self) -> None:
        """The block does not use the sandbox: there are no files to stage."""

    def run(self) -> None:
        """Execute the :class:`CanonicalFasta <api.canonical_fasta.CanonicalFasta>` api.canonical_fasta.CanonicalFasta object."""

        check_mandatory_property(
            self.pdb_code, "pdb_code", self.out_log, self.__class__.__name__
        )

        self.pdb_code = self.pdb_code.strip().lower()

        # Downloading PDB file
        pdb_string = download_fasta(
            self.pdb_code, self.api_id, self.out_log, self.global_log
        )
        write_file(pdb_string, self.io_dict["out"]["output_fasta_path"], self.out_log, self.global_log)


canonical_fasta = launcher(CanonicalFasta)

if __name__ == "__main__":
    CanonicalFasta.main()
