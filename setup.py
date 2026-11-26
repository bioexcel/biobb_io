import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_io",
    version="5.3.2",
    author="Biobb developers",
    author_email="pau.andrio@bsc.es",
    description="Biobb_io is the Biobb module collection to fetch data to be consumed by the rest of the Biobb building blocks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_io",
    project_urls={
        "Documentation": "http://biobb-io.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/",
    },
    packages=setuptools.find_packages(exclude=["docs", "test"]),
    package_data={"biobb_io": ["py.typed"]},
    install_requires=["biobb_common==5.3.1"],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "alphafold = biobb_io.api.alphafold:AlphaFold.main",
            "api_binding_site = biobb_io.api.api_binding_site:ApiBindingSite.main",
            "canonical_fasta = biobb_io.api.canonical_fasta:CanonicalFasta.main",
            "ideal_sdf = biobb_io.api.ideal_sdf:IdealSdf.main",
            "ligand = biobb_io.api.ligand:Ligand.main",
            "mddb = biobb_io.api.mddb:MDDB.main",
            "memprotmd_sim_list = biobb_io.api.memprotmd_sim_list:MemProtMDSimList.main",
            "memprotmd_sim_search = biobb_io.api.memprotmd_sim_search:MemProtMDSimSearch.main",
            "memprotmd_sim = biobb_io.api.memprotmd_sim:MemProtMDSim.main",
            "mmcif = biobb_io.api.mmcif:Mmcif.main",
            "pdb_cluster_zip = biobb_io.api.pdb_cluster_zip:PdbClusterZip.main",
            "pdb_variants = biobb_io.api.pdb_variants:PdbVariants.main",
            "pdb = biobb_io.api.pdb:Pdb.main",
            "structure_info = biobb_io.api.structure_info:StructureInfo.main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
)
