
# BioBB IO Command Line Help

Generic usage:


```python
biobb_command [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] --in_file <in_file>  --out_file <out_file>
```

Please refer to the [system & step documentation](https://biobb-common.readthedocs.io/en/latest/system_step.html) for more information of these two parameters.

***

## ligand

This class is a wrapper for the MMB PDB mirror (http://mmb.irbbarcelona.org/api/)

### Get help


```python
ligand -h
```


```python
usage: ligand.py [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] -o OUTPUT_PDB_PATH

Wrapper for the PDB ('http://www.rcsb.org/pdb/home/home.do') mirror of the MMB group REST API ('http://mmb.irbbarcelona.org/api/') for additional help in the commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        This file can be a YAML file, JSON file or JSON string
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help

required arguments:
  -o OUTPUT_PDB_PATH, --output_pdb_path OUTPUT_PDB_PATH
                        Path to the output PDB ligand file.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **output_pdb_path** (_str_): Path to the output PDB ligand file.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition


Config parameters for this building block:

- **ligand_code** (*str*) - ("12D") RSCB PDB ligand code. ie: "12D"
- **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
- **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

### Default config


```python
ligand -o 12D.pdb
```

### YAML

#### File config


```python
properties:
  ligand_code: 12D
```


```python
ligand -c conf.yml -o 12D.pdb
```

### JSON

#### String config


```python
pdb -c '{"ligand_code":"12D"}' -o 12D.pdb
```

#### File config


```python
{
  "properties": {
    "ligand_code":"12D"
  }
}
```


```python
ligand -c conf.json -o 12D.pdb
```

## pdb

Download PDB files from RCSB PDB API

### Get help


```python
pdb -h
```


```python
usage: pdb [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] -o OUTPUT_PDB_PATH

Wrapper for the PDB ('http://www.rcsb.org/pdb/home/home.do') mirror of the MMB group REST API ('http://mmb.irbbarcelona.org/api/') for additional help in the commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        This file can be a YAML file, JSON file or JSON string
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help

required arguments:
  -o OUTPUT_PDB_PATH, --output_pdb_path OUTPUT_PDB_PATH
                        Output file name
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **output_pdb_path** (_str_): Path to the output PDB file.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition


Config parameters for this building block:

- **pdb_code** (*str*) - ('1ubq') RSCB PDB code. ie: "2VGB"
- **filter** (*str*) - (["ATOM", "MODEL", "ENDMDL"]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the official PDB specification (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
- **url** (*str*) - ("https://files.rcsb.org/download/") URL of the PDB REST API. Another option for this parameter is the MMB PDB mirror API ("http://mmb.irbbarcelona.org/api/pdb/")
- **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
- **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

### Default config


```python
pdb -o 1aki.pdb
```

### YAML

#### File config


```python
properties:
  pdb_code: 1aki
  filter: ["ATOM"]
```


```python
pdb -c conf.yml -o 1aki.pdb
```

### JSON

#### String config


```python
pdb -c '{"pdb_code":"1aki", "filter":["ATOM"]}' -o 1aki.pdb
```

#### File config


```python
{
  "properties": {
    "pdb_code":"1aki", 
    "filter":["ATOM"]
  }
}
```


```python
pdb -c conf.json -o 1aki.pdb
```

***

## pdb_variants

Retrieve variants from UNIPROT mapped to the selected PDB 

#### Get help


```python
pdb_variants -h
```


```python
usage: pdb_variants [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] -o OUTPUT_MUTATIONS_LIST_TXT

Wrapper for the PDB Variants (http://www.rcsb.org/pdb/home/home.do) mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/) for additional help in the commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        This file can be a YAML file, JSON file or JSON string
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help

required arguments:
  -o OUTPUT_MUTATIONS_LIST_TXT, --output_mutations_list_txt OUTPUT_MUTATIONS_LIST_TXT
                        Output variants list text file name
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **output_mutations_list_txt** (_str_): Path to the TXT file containing an ASCII comma separated values of the mutations.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

- **pdb_code** (*str*): ("2vgb") RSCB PDB four letter code. ie: "2ki5".
- **url** (*str*) - ("https://files.rcsb.org/download/") URL of the PDB REST API. Another option for this parameter is the MMB PDB mirror API ("http://mmb.irbbarcelona.org/api/pdb/").
- **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
- **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

### Default config


```python
pdb_variants -o mutations.txt
```

### YAML

#### File config


```python
properties:
  pdb_code: 2src
```


```python
pdb_variants -c conf.yml -o mutations.txt
```

### JSON

#### String config


```python
pdb_variants -c '{"pdb_code":"2src"}' -o mutations.txt
```

#### File config


```python
{
  "properties": {
    "pdb_code":"2src"
  }
}
```


```python
pdb_variants -c conf.json -o mutations.txt
```

***

## pdb_cluster_zip

Download the selected similarity cluster of the selected PDB 

### Get help


```python
pdb_cluster_zip -h
```


```python
usage: pdb_cluster_zip [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] -o OUTPUT_PDB_ZIP_PATH

Wrapper for the PDB Cluster (http://www.rcsb.org/pdb/home/home.do) mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/) for additional help in the commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        This file can be a YAML file, JSON file or JSON string
  --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
  --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help

required arguments:
  -o OUTPUT_PDB_ZIP_PATH, --output_pdb_zip_path OUTPUT_PDB_ZIP_PATH
                        Output ZIP file name
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **output_pdb_zip_path** (_str_): Path to the ZIP or PDB file containing the output PDB files.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

- **pdb_code** (*str*) - ('2vgb') RSCB PDB code. ie: "2VGB"
- **filter** (*str*) - (["ATOM", "MODEL", "ENDMDL"]) Array of groups to be kept. If value is None or False no filter will be applied. All the possible values are defined in the official PDB specification (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
- **cluster** (*str*) - (90) Cluster number for the :meth:`biobb_io.api.MmbPdb.get_pdb_cluster_zip` method.
- **url** (*str*) - ("https://files.rcsb.org/download/") URL of the PDB REST API. Another option for this parameter is the MMB PDB mirror API ("http://mmb.irbbarcelona.org/api/pdb/").
- **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
- **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

### Default config


```python
pdb_cluster_zip -o 2vgb_cluster90.zip
```

### YAML

#### File config


```python
properties:
  pdb_code: 2src
  cluster: 95
```


```python
pdb_cluster_zip -c conf.yml -o 2src_cluster95.zip
```

### JSON

#### String config


```python
pdb_cluster_zip -c '{"pdb_code":"2src", "cluster":95}' -o 2src_cluster95.zip
```

#### File config


```python
{
  "properties": {
    "pdb_code":"2src", 
    "cluster":95
  }
}
```


```python
pdb_cluster_zip -c conf.json -o 2src_cluster95.zip
```
