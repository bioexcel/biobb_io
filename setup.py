import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_io",
    version="3.8.0",
    author="Biobb developers",
    author_email="pau.andrio@bsc.es",
    description="Biobb_io is the Biobb module collection to fetch data to be consumed by the rest of the Biobb building blocks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_io",
    project_urls={
        "Documentation": "http://biobb_io.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/"
    },
    packages=setuptools.find_packages(exclude=['docs',]),
    install_requires=['biobb_common==3.8.1'],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "alphafold = biobb_io.api.alphafold:main",
            "api_binding_site = biobb_io.api.api_binding_site:main",
            "canonical_fasta = biobb_io.api.canonical_fasta:main",
            "drugbank = biobb_io.api.drugbank:main",
            "ideal_sdf = biobb_io.api.ideal_sdf:main",
            "ligand = biobb_io.api.ligand:main",
            "memprotmd_sim_list = biobb_io.api.memprotmd_sim_list:main",
            "memprotmd_sim_search = biobb_io.api.memprotmd_sim_search:main",
            "memprotmd_sim = biobb_io.api.memprotmd_sim:main",
            "mmcif = biobb_io.api.mmcif:main",
            "pdb_cluster_zip = biobb_io.api.pdb_cluster_zip:main",
            "pdb_variants = biobb_io.api.pdb_variants:main",
            "pdb = biobb_io.api.pdb:main",
            "structure_info = biobb_io.api.structure_info:main"
        ]
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
    ),
)
