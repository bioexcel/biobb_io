# BioBB IO Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Mmcif
This class is a wrapper for downloading a MMCIF structure from the Protein Data Bank.
### Get help
Command:
```python
mmcif -h
```
    /bin/sh: mmcif: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_mmcif_path** (*string*): Path to the output MMCIF file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/ref_output.mmcif). Accepted formats: CIF, MMCIF
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pdb_code** (*string*): (None) RSCB PDB code..
* **api_id** (*string*): (pdbe) Identifier of the PDB REST API from which the MMCIF structure will be downloaded. .
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_mmcif.yml)
```python
properties:
  api_id: pdbe
  pdb_code: 2VGB

```
#### Command line
```python
mmcif --config config_mmcif.yml --output_mmcif_path ref_output.mmcif
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_mmcif.json)
```python
{
  "properties": {
    "pdb_code": "2VGB",
    "api_id": "pdbe"
  }
}
```
#### Command line
```python
mmcif --config config_mmcif.json --output_mmcif_path ref_output.mmcif
```

## Pdb
This class is a wrapper for downloading a PDB structure from the Protein Data Bank.
### Get help
Command:
```python
pdb -h
```
    /bin/sh: pdb: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_pdb_path** (*string*): Path to the output PDB file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_pdb.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pdb_code** (*string*): (None) RSCB PDB code..
* **filter** (*string*): ([ATOM, MODEL, ENDMDL]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the official PDB specification..
* **api_id** (*string*): (pdbe) Identifier of the PDB REST API from which the PDB structure will be downloaded. .
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_pdb.yml)
```python
properties:
  api_id: pdbe
  filter:
  - ATOM
  - HETATM
  pdb_code: 2VGB

```
#### Command line
```python
pdb --config config_pdb.yml --output_pdb_path output_pdb.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_pdb.json)
```python
{
  "properties": {
    "pdb_code": "2VGB",
    "filter": [
      "ATOM",
      "HETATM"
    ],
    "api_id": "pdbe"
  }
}
```
#### Command line
```python
pdb --config config_pdb.json --output_pdb_path output_pdb.pdb
```

## Memprotmd_sim_list
This class is a wrapper of the MemProtMD to get all available membrane-protein systems from its REST API.
### Get help
Command:
```python
memprotmd_sim_list -h
```
    /bin/sh: memprotmd_sim_list: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_simulations** (*string*): Path to the output JSON file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_sim_list.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_memprotmd_sim_list.yml)
```python
properties:
  remove_tmp: false

```
#### Command line
```python
memprotmd_sim_list --config config_memprotmd_sim_list.yml --output_simulations output_sim_list.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_memprotmd_sim_list.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### Command line
```python
memprotmd_sim_list --config config_memprotmd_sim_list.json --output_simulations output_sim_list.json
```

## Memprotmd_sim
This class is a wrapper of the MemProtMD to download a simulation using its REST API.
### Get help
Command:
```python
memprotmd_sim -h
```
    /bin/sh: memprotmd_sim: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_simulation** (*string*): Path to the output simulation in a ZIP file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_sim.zip). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pdb_code** (*string*): (None) RSCB PDB code..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_memprotmd_sim.yml)
```python
properties:
  pdb_code: 1hzx

```
#### Command line
```python
memprotmd_sim --config config_memprotmd_sim.yml --output_simulation output_sim.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_memprotmd_sim.json)
```python
{
  "properties": {
    "pdb_code": "1hzx"
  }
}
```
#### Command line
```python
memprotmd_sim --config config_memprotmd_sim.json --output_simulation output_sim.zip
```

## Drugbank
This class is a wrapper for the Drugbank REST API.
### Get help
Command:
```python
drugbank -h
```
    /bin/sh: drugbank: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_sdf_path** (*string*): Path to the output SDF component file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_drugbank.sdf). Accepted formats: SDF
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **drugbank_id** (*string*): (None) Drugbank component id..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_drugbank.yml)
```python
properties:
  drugbank_id: DB00530

```
#### Command line
```python
drugbank --config config_drugbank.yml --output_sdf_path output_drugbank.sdf
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_drugbank.json)
```python
{
  "properties": {
    "drugbank_id": "DB00530"
  }
}
```
#### Command line
```python
drugbank --config config_drugbank.json --output_sdf_path output_drugbank.sdf
```

## Pdb_variants
This class creates a text file containing a list of all the variants mapped to a PDB code from the corresponding UNIPROT entries.
### Get help
Command:
```python
pdb_variants -h
```
    /bin/sh: pdb_variants: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_mutations_list_txt** (*string*): Path to the TXT file containing an ASCII comma separated values of the mutations. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_pdb_variants.txt). Accepted formats: TXT
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pdb_code** (*string*): (None) RSCB PDB four letter code..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_pdb_variants.yml)
```python
properties:
  pdb_code: 2vgb

```
#### Command line
```python
pdb_variants --config config_pdb_variants.yml --output_mutations_list_txt output_pdb_variants.txt
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_pdb_variants.json)
```python
{
  "properties": {
    "pdb_code": "2vgb"
  }
}
```
#### Command line
```python
pdb_variants --config config_pdb_variants.json --output_mutations_list_txt output_pdb_variants.txt
```

## Ideal_sdf
This class is a wrapper for downloading an ideal SDF ligand from the Protein Data Bank.
### Get help
Command:
```python
ideal_sdf -h
```
    /bin/sh: ideal_sdf: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_sdf_path** (*string*): Path to the output SDF file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/ref_output.sdf). Accepted formats: SDF
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **ligand_code** (*string*): (None) RSCB PDB ligand code..
* **api_id** (*string*): (pdbe) Identifier of the PDB REST API from which the SDF structure will be downloaded. .
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_ideal_sdf.yml)
```python
properties:
  api_id: pdbe
  ligand_code: HYZ

```
#### Command line
```python
ideal_sdf --config config_ideal_sdf.yml --output_sdf_path ref_output.sdf
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_ideal_sdf.json)
```python
{
  "properties": {
    "ligand_code": "HYZ",
    "api_id": "pdbe"
  }
}
```
#### Command line
```python
ideal_sdf --config config_ideal_sdf.json --output_sdf_path ref_output.sdf
```

## Binding_site
This class is a wrapper for the PDBe REST API Binding Sites endpoint.
### Get help
Command:
```python
binding_site -h
```
    /bin/sh: binding_site: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_json_path** (*string*): Path to the JSON file with the binding sites for the requested structure. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_binding_site.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pdb_code** (*string*): (None) RSCB PDB code..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_binding_site.yml)
```python
properties:
  pdb_code: 4i23

```
#### Command line
```python
binding_site --config config_binding_site.yml --output_json_path output_binding_site.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_binding_site.json)
```python
{
  "properties": {
    "pdb_code": "4i23"
  }
}
```
#### Command line
```python
binding_site --config config_binding_site.json --output_json_path output_binding_site.json
```

## Pdb_cluster_zip
This class is a wrapper for downloading a PDB cluster from the Protein Data Bank.
### Get help
Command:
```python
pdb_cluster_zip -h
```
    /bin/sh: pdb_cluster_zip: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_pdb_zip_path** (*string*): Path to the ZIP or PDB file containing the output PDB files. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_pdb_cluster.zip). Accepted formats: PDB, ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pdb_code** (*string*): (None) RSCB PDB code..
* **filter** (*string*): ([ATOM, MODEL, ENDMDL]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the official PDB specification (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html).
* **cluster** (*integer*): (90) Sequence Similarity Cutoff. .
* **api_id** (*string*): (pdbe) Identifier of the PDB REST API from which the PDB structure will be downloaded. .
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_pdb_cluster_zip.yml)
```python
properties:
  api_id: pdbe
  cluster: 90
  filter:
  - ATOM
  - MODEL
  - ENDMDL
  pdb_code: 2vgb

```
#### Command line
```python
pdb_cluster_zip --config config_pdb_cluster_zip.yml --output_pdb_zip_path output_pdb_cluster.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_pdb_cluster_zip.json)
```python
{
  "properties": {
    "pdb_code": "2vgb",
    "filter": [
      "ATOM",
      "MODEL",
      "ENDMDL"
    ],
    "cluster": 90,
    "api_id": "pdbe"
  }
}
```
#### Command line
```python
pdb_cluster_zip --config config_pdb_cluster_zip.json --output_pdb_zip_path output_pdb_cluster.zip
```

## Ligand
This class is a wrapper for downloading a PDB ligand from the Protein Data Bank.
### Get help
Command:
```python
ligand -h
```
    /bin/sh: ligand: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_pdb_path** (*string*): Path to the output PDB ligand file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_ligand.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **ligand_code** (*string*): (None) RSCB PDB ligand code..
* **api_id** (*string*): (pdbe) Identifier of the PDB REST API from which the PDB structure will be downloaded. .
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_ligand.yml)
```python
properties:
  api_id: pdbe
  ligand_code: IBP

```
#### Command line
```python
ligand --config config_ligand.yml --output_pdb_path output_ligand.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_ligand.json)
```python
{
  "properties": {
    "ligand_code": "IBP",
    "api_id": "pdbe"
  }
}
```
#### Command line
```python
ligand --config config_ligand.json --output_pdb_path output_ligand.pdb
```

## Canonical_fasta
This class is a wrapper for downloading a FASTA structure from the Protein Data Bank.
### Get help
Command:
```python
canonical_fasta -h
```
    /bin/sh: canonical_fasta: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_fasta_path** (*string*): Path to the canonical FASTA file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/canonical_fasta.fasta). Accepted formats: FASTA
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pdb_code** (*string*): (None) RSCB PDB code..
* **api_id** (*string*): (pdbe) Identifier of the PDB REST API from which the PDB structure will be downloaded. .
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_canonical_fasta.yml)
```python
properties:
  api_id: pdbe
  pdb_code: 4i23

```
#### Command line
```python
canonical_fasta --config config_canonical_fasta.yml --output_fasta_path canonical_fasta.fasta
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_canonical_fasta.json)
```python
{
  "properties": {
    "pdb_code": "4i23",
    "api_id": "pdbe"
  }
}
```
#### Command line
```python
canonical_fasta --config config_canonical_fasta.json --output_fasta_path canonical_fasta.fasta
```

## Structure_info
This class is a wrapper for getting all the available information of a structure from the Protein Data Bank.
### Get help
Command:
```python
structure_info -h
```
    /bin/sh: structure_info: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_json_path** (*string*): Path to the output JSON file with all the structure information. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/ref_str_info.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pdb_code** (*string*): (None) RSCB PDB structure code..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_structure_info.yml)
```python
properties:
  pdb_code: 2VGB

```
#### Command line
```python
structure_info --config config_structure_info.yml --output_json_path ref_str_info.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_structure_info.json)
```python
{
  "properties": {
    "pdb_code": "2VGB"
  }
}
```
#### Command line
```python
structure_info --config config_structure_info.json --output_json_path ref_str_info.json
```

## Memprotmd_sim_search
This class is a wrapper of the MemProtMD to perform advanced searches in the MemProtMD DB using its REST API.
### Get help
Command:
```python
memprotmd_sim_search -h
```
    /bin/sh: memprotmd_sim_search: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_simulations** (*string*): Path to the output JSON file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_sim_search.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **collection_name** (*string*): (refs) Name of the collection to query..
* **keyword** (*string*): (None) String to search for in the database metadata. Examples are families like gpcr or porin. .
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_memprotmd_sim_search.yml)
```python
properties:
  collection_name: refs
  keyword: porin

```
#### Command line
```python
memprotmd_sim_search --config config_memprotmd_sim_search.yml --output_simulations output_sim_search.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_io/blob/master/biobb_io/test/data/config/config_memprotmd_sim_search.json)
```python
{
  "properties": {
    "collection_name": "refs",
    "keyword": "porin"
  }
}
```
#### Command line
```python
memprotmd_sim_search --config config_memprotmd_sim_search.json --output_simulations output_sim_search.json
```
