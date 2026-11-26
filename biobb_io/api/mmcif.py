#!/usr/bin/env python

"""Module containing the Mmcif class and the command line interface."""

from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher

from biobb_io.api.common import (
    check_mandatory_property,
    download_mmcif,
    write_file,
)


class Mmcif(BiobbObject):
    """
    | biobb_io Mmcif
    | This class is a wrapper for downloading a MMCIF structure from the Protein Data Bank.
    | Wrapper for the `Protein Data Bank in Europe <https://www.ebi.ac.uk/pdbe/>`_, the `Protein Data Bank <https://www.rcsb.org/>`_ and the `MMB PDB mirror <https://mdb-login.bsc.es/api/>`_ for downloading a single MMCIF structure.

    Args:
        output_mmcif_path (str): Path to the output MMCIF file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/ref_output.mmcif>`_. Accepted formats: cif (edam:format_1477), mmcif (edam:format_1477).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB code.
            * **api_id** (*str*) - ("pdbe") Identifier of the PDB REST API from which the MMCIF structure will be downloaded. Values: pdbe (`PDB in Europe REST API <https://www.ebi.ac.uk/pdbe/pdbe-rest-api>`_), pdb (`RCSB PDB REST API <https://data.rcsb.org/>`_), mmb (`MMB PDB mirror API <https://mdb-login.bsc.es/api/>`_).
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

    def __init__(self, output_mmcif_path: str, properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def stage_files(self) -> None:
        """The block does not use the sandbox: there are no files to stage."""

    def run(self) -> None:
        """Execute the :class:`Mmcif <api.mmcif.Mmcif>` api.mmcif.Mmcif object."""

        check_mandatory_property(
            self.pdb_code, "pdb_code", self.out_log, self.__class__.__name__
        )

        self.pdb_code = self.pdb_code.strip().lower()

        # Downloading PDB file
        mmcif_string = download_mmcif(
            self.pdb_code, self.api_id, self.out_log, self.global_log
        )
        write_file(mmcif_string, self.io_dict["out"]["output_mmcif_path"], self.out_log, self.global_log)


mmcif = launcher(Mmcif)

if __name__ == "__main__":
    Mmcif.main()
