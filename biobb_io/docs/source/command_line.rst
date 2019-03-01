BioBB IO Command Line Help
==========================

Generic usage:

.. parsed-literal::

    biobb_command [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] --in_file <in_file>  --out_file <out_file>

Please refer to the `system & step
documentation <https://biobb-common.readthedocs.io/en/latest/system_step.html>`__
for more information of these two parameters.

--------------

pdb
---

Download PDB files from RCSB PDB API

Get help
^^^^^^^^

Command:

.. code:: bash

    
    pdb -h

.. parsed-literal::

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

Config
^^^^^^

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **pdb_code** (*str*) - (‘1ubq’) RSCB PDB code. ie: “2VGB”
-  **filter** (*str*) - ([“ATOM”, “MODEL”, “ENDMDL”]) Array of groups to
   be kept. If value is None or False no filter will be applied. All the
   possible values are defined in the official PDB specification
   (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
-  **url** (*str*) - (“https://files.rcsb.org/download/”) URL of the PDB
   REST API. Another option for this parameter is the MMB PDB mirror API
   (“http://mmb.irbbarcelona.org/api/pdb/”)

Default config
^^^^^^^^^^^^^^

Command:

.. code:: bash

    
    pdb -o 1aki.pdb

JSON string config
^^^^^^^^^^^^^^^^^^

Command:

.. code:: bash

    
    pdb -c '{"pdb_code":"1aki", "filter":["ATOM"]}' -o 1aki.pdb

JSON file config
^^^^^^^^^^^^^^^^

conf.json:

.. parsed-literal::

    {"pdb_code":"1aki", "filter":["ATOM"]}

Command:

.. code:: bash

    
    pdb -c conf.json -o 1aki.pdb

YAML file config
^^^^^^^^^^^^^^^^

conf.yml:

.. parsed-literal::

    pdb_code: 1aki
    filter: ["ATOM"]

Command:

.. code:: bash

    
    pdb -c conf.yml -o 1aki.pdb

--------------

pdb_variants
------------

Retrieve variants from UNIPROT mapped to the selected PDB

Get help
^^^^^^^^

Command:

.. code:: bash

    
    pdb_variants -h

.. parsed-literal::

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

Config
^^^^^^

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **pdb_code** (*str*): (“2vgb”) RSCB PDB four letter code. ie: “2ki5”.
-  **url** (*str*) - (“https://files.rcsb.org/download/”) URL of the PDB
   REST API. Another option for this parameter is the MMB PDB mirror API
   (“http://mmb.irbbarcelona.org/api/pdb/”).

Default config
^^^^^^^^^^^^^^

Command:

.. code:: bash

    
    pdb_variants -o mutations.txt

JSON string config
^^^^^^^^^^^^^^^^^^

Command:

.. code:: bash

    
    pdb_variants -c '{"pdb_code":"2src"}' -o mutations.txt

JSON file config
^^^^^^^^^^^^^^^^

conf.json:

.. parsed-literal::

    {"pdb_code":"2src"}

Command:

.. code:: bash

    
    pdb_variants -c conf.json -o mutations.txt

YAML file config
^^^^^^^^^^^^^^^^

conf.yml:

.. parsed-literal::

    pdb_code: 2src

Command:

.. code:: bash

    
    pdb_variants -c conf.yml -o mutations.txt

--------------

pdb_cluster_zip
---------------

Download the selected similarity cluster of the selected PDB

Get help
~~~~~~~~

Command:

.. code:: bash

    
    pdb_cluster_zip -h

.. parsed-literal::

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

Config
^^^^^^

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **pdb_code** (*str*) - (‘2vgb’) RSCB PDB code. ie: “2VGB”
-  **filter** (*str*) - ([“ATOM”, “MODEL”, “ENDMDL”]) Array of groups to
   be keep. If value is None or False no filter will be applied. All the
   possible values are defined in the official PDB specification
   (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
-  **cluster** (*str*) - (90) Cluster number for the
   :meth:``biobb_io.api.MmbPdb.get_pdb_cluster_zip`` method.
-  **url** (*str*) - (“https://files.rcsb.org/download/”) URL of the PDB
   REST API. Another option for this parameter is the MMB PDB mirror API
   (“http://mmb.irbbarcelona.org/api/pdb/”).

Default config
^^^^^^^^^^^^^^

Command:

.. code:: bash

    
    pdb_cluster_zip -o 2vgb_cluster90.zip

JSON string config
^^^^^^^^^^^^^^^^^^

Command:

.. code:: bash

    
    pdb_cluster_zip -c '{"pdb_code":"2src", "cluster":95}' -o 2src_cluster95.zip

JSON file config
^^^^^^^^^^^^^^^^

conf.json:

.. parsed-literal::

    {"pdb_code":"2src", "cluster":95}

Command:

.. code:: bash

    
    pdb_cluster_zip -c conf.json -o 2src_cluster95.zip

YAML file config
^^^^^^^^^^^^^^^^

Command:

.. code:: bash

    
    pdb_cluster_zip -c conf.yml -o 2src_cluster95.zip
