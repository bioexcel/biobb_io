#!/usr/bin/env python

"""PdbClusterZip Module"""

import os
from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu

from biobb_io.api.common import (
    check_mandatory_property,
    download_pdb,
    filter_pdb,
    get_cluster_pdb_codes,
    write_file,
)


class PdbClusterZip(BiobbObject):
    """
    | biobb_io PdbClusterZip
    | This class is a wrapper for downloading a PDB cluster from the Protein Data Bank.
    | Wrapper for the `Protein Data Bank in Europe <https://www.ebi.ac.uk/pdbe/>`_, the `Protein Data Bank <https://www.rcsb.org/>`_ and the `MMB PDB mirror <https://mdb-login.bsc.es/api/>`_ for downloading a PDB cluster.

    Args:
        output_pdb_zip_path (str): Path to the ZIP file containing the output PDB files. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_pdb_cluster.zip>`_. Accepted formats: zip (edam:format_3987).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **pdb_code** (*str*) - (None) RSCB PDB code.
            * **filter** (*str*) - (["ATOM", "MODEL", "ENDMDL"]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the official PDB specification (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
            * **cluster** (*int*) - (90) Sequence Similarity Cutoff. Values: 50 (structures having less than 50% sequence identity to each other), 70 (structures having less than 70% sequence identity to each other), 90 (structures having less than 90% sequence identity to each other), 95 (structures having less than 95% sequence identity to each other).
            * **api_id** (*str*) - ("pdbe") Identifier of the PDB REST API from which the PDB structure will be downloaded. Values: pdbe (`PDB in Europe REST API <https://www.ebi.ac.uk/pdbe/pdbe-rest-api>`_), pdb (`RCSB PDB REST API <https://data.rcsb.org/>`_), mmb (`MMB PDB mirror API <https://mdb-login.bsc.es/api/>`_).
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.pdb_cluster_zip import pdb_cluster_zip
            prop = {
                'pdb_code': '2VGB',
                'filter': ['ATOM', 'MODEL', 'ENDMDL'],
                'cluster': 90,
                'api_id': 'pdbe'
            }
            pdb_cluster_zip(output_pdb_zip_path='/path/to/newStructures.zip',
                            properties=prop)

    Info:
        * wrapped_software:
            * name: Protein Data Bank
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_pdb_zip_path: str, properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def stage_files(self) -> None:
        """The block does not use the sandbox: there are no files to stage."""

    def run(self) -> None:
        """Execute the :class:`PdbClusterZip <api.pdb_cluster_zip.PdbClusterZip>` api.pdb_cluster_zip.PdbClusterZip object."""

        check_mandatory_property(
            self.pdb_code, "pdb_code", self.out_log, self.__class__.__name__
        )

        self.pdb_code = self.pdb_code.strip().lower()

        file_list = []
        # Downloading PDB_files
        pdb_code_list = get_cluster_pdb_codes(
            pdb_code=self.pdb_code,
            cluster=self.cluster,
            out_log=self.out_log,
            global_log=self.global_log,
        )
        unique_dir = self.create_tmp_dir()
        for pdb_code in pdb_code_list:
            pdb_file = os.path.join(unique_dir, pdb_code + ".pdb")
            pdb_string = download_pdb(
                pdb_code=pdb_code,
                api_id=self.api_id,
                out_log=self.out_log,
                global_log=self.global_log,
            )
            pdb_string = filter_pdb(pdb_string, self.filter, self.out_log, self.global_log)
            write_file(pdb_string, pdb_file, self.out_log, self.global_log)
            file_list.append(os.path.abspath(pdb_file))

        # Zipping files
        fu.log("Zipping the pdb files to: %s" % self.io_dict["out"]["output_pdb_zip_path"])
        fu.zip_list(self.io_dict["out"]["output_pdb_zip_path"], file_list, out_log=self.out_log)


pdb_cluster_zip = launcher(PdbClusterZip)

if __name__ == "__main__":
    PdbClusterZip.main()
