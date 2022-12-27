# Biobb IO changelog

## What's new in version [3.9.0](https://github.com/bioexcel/biobb_io/releases/tag/v3.9.0)?
In version 3.9.0 the dependency biobb_common has been updated to 3.9.0 version. 

### New features

* Update to biobb_common 3.9.0 (general)
* All inputs/outputs are checked for correct file format, extension and type (general)

## What's new in version [3.8.0](https://github.com/bioexcel/biobb_io/releases/tag/v3.8.0)?
In version 3.8.0 the dependency biobb_common has been updated to 3.8.1 version. 

### New features

* Update to biobb_common 3.8.1 (general)

## What's new in version [3.7.0](https://github.com/bioexcel/biobb_io/releases/tag/v3.7.0)?
In version 3.7.0 the dependency biobb_common has been updated to 3.7.0 version. 

### New features

* Update to biobb_common 3.7.0 (general)

## What's new in version [3.6.0](https://github.com/bioexcel/biobb_io/releases/tag/v3.6.0)?
In version 3.6.0 the dependency biobb_common has been updated to 3.6.0 version. 

### New features

* Update to biobb_common 3.6.0 (general)

## What's new in version [3.5.2](https://github.com/bioexcel/biobb_io/releases/tag/v3.5.2)?
In version 3.5.2 there have been small changes.

### New features

* Modified BindingSite tool name to ApiBindingSite for the sake of avoiding possible conflicts with other tools.
* Modified some broken links of the PDBe REST API.

## What's new in version [3.5.1](https://github.com/bioexcel/biobb_io/releases/tag/v3.5.1)?
In version 3.5.1 there have been added the new tools for binding sites, canonical FASTA, download structure in mmcif format, download ideal sdf for ligands and download structure info in JSON format.

### New features

* New BindingSite tool for searching binding sites through the PDBe REST API
* New CanonicalFasta for downloading the canonical FASTA of a structure from the Protein Data Bank
* New Mmcif tool for downloading a structure in MMCIF format 
* New IdealSdf tool for downloading a ligand in SDF format
* New StructureInfo tool for getting all the available info of a structure in JSON format

## What's new in version [3.5.0](https://github.com/bioexcel/biobb_io/releases/tag/v3.5.0)?
In version 3.5.0 the dependency biobb_common has been updated to 3.5.1 version. Also, there have been added the new tools for MemProtMD DB REST API. There have been also implemented the new version of docstrings, therefore the JSON Schemas have been modified.

### New features

* Update to biobb_common 3.5.1 (general)
* New MemProtMD DB REST API tools
* New extended and improved JSON schemas (Galaxy and CWL-compliant) (general)

### Other changes

* New docstrings

## What's new in version [3.0.1](https://github.com/bioexcel/biobb_io/releases/tag/v3.0.1)?
In version 3.0.1 the dependency biobb_common has been updated to 3.0.1 version. New tool for downloading components from the Drugbank.

### New features

* Update to biobb_common 3.0.1
* New Drugbank tool

### Other changes

* Bug fixes in MmbPdbClusterZip
* Bug fixes in MmbPdbVariants

## What's new in version [3.0.0](https://github.com/bioexcel/biobb_io/releases/tag/v3.0.0)?
In version 3.0.0 Python has been updated to version 3.7. Big changes in the documentation style and content. Finally a new conda installation recipe has been introduced.

### New features

* Update to Python 3.7 (general)
* New conda installer (installation)
* Adding type hinting for easier usage (API)
* Deprecating os.path in favour of pathlib.path (modules)
* New command line documentation (documentation)

### Other changes

* New documentation styles (documentation)