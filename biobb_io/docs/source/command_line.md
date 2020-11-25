# BioBB IO Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Pdb_variants
This class creates a text file containing a list of all the variants mapped to a PDB code from the corresponding UNIPROT entries.
### Get help
Command:
```python
pdb_variants -h
```
    usage: pdb_variants [-h] [-c CONFIG] -o OUTPUT_MUTATIONS_LIST_TXT
    
    Wrapper for the UNIPROT (http://www.uniprot.org/) mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/) for creating a list of all the variants mapped to a PDB code from the corresponding UNIPROT entries.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      -o OUTPUT_MUTATIONS_LIST_TXT, --output_mutations_list_txt OUTPUT_MUTATIONS_LIST_TXT
                            Output variants list text file name
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_mutations_list_txt** (*string*): Path to the TXT file containing an ASCII comma separated values of the mutations. File type: output. [Sample file](None). Accepted formats: TXT
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
pdb_variants --config config_pdb_variants.yml --output_mutations_list_txt output.txt
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
pdb_variants --config config_pdb_variants.json --output_mutations_list_txt output.txt
```

## Pdb_cluster_zip
This class is a wrapper for downloading a PDB cluster from the Protein Data Bank.
### Get help
Command:
```python
pdb_cluster_zip -h
```
    usage: pdb_cluster_zip [-h] [-c CONFIG] -o OUTPUT_PDB_ZIP_PATH
    
    Wrapper for the Protein Data Bank in Europe (https://www.ebi.ac.uk/pdbe/), the Protein Data Bank (https://www.rcsb.org/) and the MMB PDB mirror (http://mmb.irbbarcelona.org/api/) for downloading a PDB cluster.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      -o OUTPUT_PDB_ZIP_PATH, --output_pdb_zip_path OUTPUT_PDB_ZIP_PATH
                            Output ZIP file name
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_pdb_zip_path** (*string*): Path to the ZIP or PDB file containing the output PDB files. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/reference_output_pdb_zip_path.zip). Accepted formats: PDB, ZIP
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
pdb_cluster_zip --config config_pdb_cluster_zip.yml --output_pdb_zip_path reference_output_pdb_zip_path.zip
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
pdb_cluster_zip --config config_pdb_cluster_zip.json --output_pdb_zip_path reference_output_pdb_zip_path.zip
```

## Drugbank
This class is a wrapper for the Drugbank REST API.
### Get help
Command:
```python
drugbank -h
```
    usage: drugbank [-h] [-c CONFIG] -o OUTPUT_SDF_PATH
    
    Download a component in SDF format from the Drugbank (https://www.drugbank.ca/).
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      -o OUTPUT_SDF_PATH, --output_sdf_path OUTPUT_SDF_PATH
                            Path to the output SDF component file. Accepted formats: sdf.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_sdf_path** (*string*): Path to the output SDF component file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_sdf_path.sdf). Accepted formats: SDF
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
drugbank --config config_drugbank.yml --output_sdf_path output_sdf_path.sdf
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
drugbank --config config_drugbank.json --output_sdf_path output_sdf_path.sdf
```

## Ligand
This class is a wrapper for downloading a PDB ligand from the Protein Data Bank.
### Get help
Command:
```python
ligand -h
```
    usage: ligand [-h] [-c CONFIG] -o OUTPUT_PDB_PATH
    
    Wrapper for the Protein Data Bank in Europe (https://www.ebi.ac.uk/pdbe/) and the MMB PDB mirror (http://mmb.irbbarcelona.org/api/) for downloading a single PDB ligand.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      -o OUTPUT_PDB_PATH, --output_pdb_path OUTPUT_PDB_PATH
                            Path to the output PDB ligand file.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_pdb_path** (*string*): Path to the output PDB ligand file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/ligand_12d.pdb). Accepted formats: PDB
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
ligand --config config_ligand.yml --output_pdb_path ligand_12d.pdb
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
ligand --config config_ligand.json --output_pdb_path ligand_12d.pdb
```

## Memprotmd_sim_search
This class is a wrapper of the MemProtMD to perform advanced searches in the MemProtMD DB using its REST API.
### Get help
Command:
```python
memprotmd_sim_search -h
```
    usage: memprotmd_sim_search [-h] [-c CONFIG] -o OUTPUT_SIMULATIONS
    
    Wrapper for the MemProtMD DB REST API (http://memprotmd.bioch.ox.ac.uk/) to perform advanced searches.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      -o OUTPUT_SIMULATIONS, --output_simulations OUTPUT_SIMULATIONS
                            Output file name
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_simulations** (*string*): Path to the output JSON file. File type: output. [Sample file](None). Accepted formats: JSON
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
memprotmd_sim_search --config config_memprotmd_sim_search.yml --output_simulations output.json
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
memprotmd_sim_search --config config_memprotmd_sim_search.json --output_simulations output.json
```

## Memprotmd_sim_list
This class is a wrapper of the MemProtMD to get all available membrane-protein systems from its REST API.
### Get help
Command:
```python
memprotmd_sim_list -h
```
    usage: memprotmd_sim_list [-h] [-c CONFIG] -o OUTPUT_SIMULATIONS
    
    Wrapper for the MemProtMD DB REST API (http://memprotmd.bioch.ox.ac.uk/) to get all available membrane-protein systems (simulations).
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      -o OUTPUT_SIMULATIONS, --output_simulations OUTPUT_SIMULATIONS
                            Output file name
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_simulations** (*string*): Path to the output JSON file. File type: output. [Sample file](None). Accepted formats: JSON
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
memprotmd_sim_list --config config_memprotmd_sim_list.yml --output_simulations output.json
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
memprotmd_sim_list --config config_memprotmd_sim_list.json --output_simulations output.json
```

## Memprotmd_sim
This class is a wrapper of the MemProtMD to download a simulation using its REST API.
### Get help
Command:
```python
memprotmd_sim -h
```
    usage: memprotmd_sim [-h] [-c CONFIG] -o OUTPUT_SIMULATION
    
    Wrapper for the MemProtMD DB REST API (http://memprotmd.bioch.ox.ac.uk/) to download a simulation.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      -o OUTPUT_SIMULATION, --output_simulation OUTPUT_SIMULATION
                            Path to the output simulation in a ZIP file. Accepted formats: zip.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_simulation** (*string*): Path to the output simulation in a ZIP file. File type: output. [Sample file](None). Accepted formats: ZIP
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
memprotmd_sim --config config_memprotmd_sim.yml --output_simulation output.zip
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
memprotmd_sim --config config_memprotmd_sim.json --output_simulation output.zip
```

## Pdb
This class is a wrapper for downloading a PDB structure from the Protein Data Bank.
### Get help
Command:
```python
pdb -h
```
    usage: pdb.py scriptfile [arg] ...
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **output_pdb_path** (*string*): Path to the output PDB file. File type: output. [Sample file](https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/pdb_1ubq.pdb). Accepted formats: PDB
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
pdb --config config_pdb.yml --output_pdb_path pdb_1ubq.pdb
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
pdb --config config_pdb.json --output_pdb_path pdb_1ubq.pdb
```
