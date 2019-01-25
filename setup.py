import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_io",
    version="0.1.1",
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
    install_requires=['biobb_common>=0.0.8', 'requests',],
    python_requires='>=3',
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
    ),
)
