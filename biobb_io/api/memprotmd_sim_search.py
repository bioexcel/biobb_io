#!/usr/bin/env python

"""Module containing the MemProtMDSimSearch class and the command line interface."""

import argparse
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger

from biobb_io.api.common import check_output_path, get_memprotmd_sim_search, write_json


class MemProtMDSimSearch(BiobbObject):
    """
    | biobb_io MemProtMDSimSearch
    | This class is a wrapper of the MemProtMD to perform advanced searches in the MemProtMD DB using its REST API.
    | Wrapper for the `MemProtMD DB REST API <http://memprotmd.bioch.ox.ac.uk/>`_ to perform advanced searches.

    Args:
        output_simulations (str): Path to the output JSON file. File type: output. `Sample file <https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_sim_search.json>`_. Accepted formats: json (edam:format_3464).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **collection_name** (*str*) - ("refs") Name of the collection to query.
            * **keyword** (*str*) - (None) String to search for in the database metadata. Examples are families like gpcr or porin. Values: porin, outer membrane protein, membrane protein, gpcr (7-transmembrane domain receptors transducing extracellular signals into cells), ion channels, rhodopsin (The most famous GPCRs), abc, mip (Major Intrinsic Protein (MIP)/FNT superfamily: specific for the transport of water and small neutral solutes), ligand-gated (Ligand-dependent signal conversion from chemical signals to electric signals), ammonia (Regulating transepithelial ammonia secretion), mapeg (Eicosanoid and Glutathione metabolism proteins), transmembrane (Heme biosynthesis), protein, kinase (Tyrosine-protein kinases: regulate central nervous system; gene transcription and cell differentiation), glycoprotein (Expression of TCR complex), immunoglobulin (Recognition; binding and adhesion process of cells), integrin (Bridges for cell-cell and cell-extracellular matrix interaction), bnip3 (BNip3 protein family: protect cell from apoptosis), bcl-2 (Regulating cell-death; either induce apoptotic or inhibit apoptosis), atpase (ATPase regulators; P-P-bond hydrolysis-driven transporter), cytochrome (Terminal oxidase enzyme in electron transfer chain), nadp (Transmembrane proteins with NAD(P)-binding Rossmann-fold domains: monoamine oxidase; deaminates norepinephrine; epinephrine; serotonin and dopamine), a4 (Amyloid beta A4 protein; involved in alzheimer's diseases), lysosome (Lysosome-associated membrane glycoprotein: specific to lysosomes; CD107), necrosis (Tumor necrosis factor recepto: binding with TNF and NGF; interacting with a variety of signal molecules; highly associated with apoptosis), oxidoreductase (DHODH; biosynthesis of orotate), ceramidase (Neutral/alkaline ceramidase: converting sphingolipid to sphingosine), dehydrogenase (Aldehyde dehydrogenase:ALDH; Oxidation of aldehydes), mitochondrial, plastid.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_io.api.memprotmd_sim_search import memprotmd_sim_search
            prop = {
                'collection_name': 'refs',
                'keyword': 'porin'
            }
            memprotmd_sim_search(output_simulations='/path/to/newSimulationSearch.json',
                                properties=prop).launch()

    Info:
        * wrapped_software:
            * name: MemProtMD DB
            * license: Creative Commons
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, output_simulations, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {"out": {"output_simulations": output_simulations}}

        # Properties specific for BB
        self.collection_name = properties.get("collection_name", "refs")
        self.keyword = properties.get("keyword", None)
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """Checks all the input/output paths and parameters"""
        self.output_simulations = check_output_path(
            self.io_dict["out"]["output_simulations"],
            "output_simulations",
            False,
            out_log,
            self.__class__.__name__,
        )

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`MemProtMDSimSearch <api.memprotmd_sim_search.MemProtMDSimSearch>` api.memprotmd_sim_search.MemProtMDSimSearch object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0

        self.keyword = self.keyword.strip().lower()

        # get JSON object
        json_string = get_memprotmd_sim_search(
            self.collection_name, self.keyword, self.out_log, self.global_log
        )

        # write JSON file
        write_json(json_string, self.output_simulations, self.out_log, self.global_log)

        self.check_arguments(output_files_created=True, raise_exception=False)

        return 0


def memprotmd_sim_search(
    output_simulations: str, properties: Optional[dict] = None, **kwargs
) -> int:
    """Execute the :class:`MemProtMDSimSearch <api.memprotmd_sim_search.MemProtMDSimSearch>` class and
    execute the :meth:`launch() <api.memprotmd_sim_search.MemProtMDSimSearch.launch>` method."""

    return MemProtMDSimSearch(
        output_simulations=output_simulations, properties=properties, **kwargs
    ).launch()

    memprotmd_sim_search.__doc__ = MemProtMDSimSearch.__doc__


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(
        description="Wrapper for the MemProtMD DB REST API (http://memprotmd.bioch.ox.ac.uk/) to perform advanced searches.",
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
        "--output_simulations",
        required=True,
        help="Path to the output JSON file. Accepted formats: json.",
    )

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    memprotmd_sim_search(
        output_simulations=args.output_simulations, properties=properties
    )


if __name__ == "__main__":
    main()
