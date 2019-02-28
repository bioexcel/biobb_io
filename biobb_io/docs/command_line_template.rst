Biobb IO Command Line Help
==========================

Please refer to the `system & step
documentation <https://biobb-common.readthedocs.io/en/latest/system_step.html>`__
for more information of these two parameters.

--------------

pdb
---

Download PDB files from RCSB PDB API

Get help
^^^^^^^^

.. code:: bash

    %%bash
    pdb -h


.. parsed-literal::

    usage: pdb [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] -o OUTPUT_PDB_PATH

    Wrapper for the PDB ('http://www.rcsb.org/pdb/home/home.do') mirror of the MMB
    group REST API ('http://mmb.irbbarcelona.org/api/') for additional help in the
    commandline usage please check ('https://biobb-
    io.readthedocs.io/en/latest/command_line.html')

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

-  **pdb_code** (*str*) - (‘1ubq’) RSCB PDB code. ie: “2VGB”
-  **filter** (*str*) - ([“ATOM”, “MODEL”, “ENDMDL”]) Array of groups to
   be keep. If value is None or False no filter will be applied. All the
   possible values are defined in the official PDB specification
   (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
-  **url** (*str*) - (“https://files.rcsb.org/download/”) URL of the MMB PDB REST API.

Default config
^^^^^^^^^^^^^^

.. code:: bash

    %%bash
    pdb -o 1aki.pdb


.. parsed-literal::

    2019-02-28 10:32:29,165 [MainThread  ] [INFO ]  Downloading: 1ubq from: https://files.rcsb.org/download/1ubq.pdb
    2019-02-28 10:32:29,801 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/1aki.pdb
    2019-02-28 10:32:29,801 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM', 'MODEL', 'ENDMDL']


JSON string config
^^^^^^^^^^^^^^^^^^

.. code:: bash

    %%bash
    pdb -c "{\"pdb_code\":\"1aki\", \"filter\":[\"ATOM\"]}" -o 1aki.pdb


.. parsed-literal::

    2019-02-28 10:32:31,181 [MainThread  ] [INFO ]  Downloading: 1aki from: https://files.rcsb.org/download/1aki.pdb
    2019-02-28 10:32:31,788 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/1aki.pdb
    2019-02-28 10:32:31,788 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM']


YAML file config
^^^^^^^^^^^^^^^^

.. code:: bash

    %%bash
    printf "pdb_code: 1aki\nfilter: [\"ATOM\"]" > conf.yml
    cat conf.yml

    pdb -c conf.yml -o 1aki.pdb


.. parsed-literal::

    pdb_code: 1aki
    filter: ["ATOM"]

.. parsed-literal::

    2019-02-28 10:32:35,954 [MainThread  ] [INFO ]  Downloading: 1aki from: https://files.rcsb.org/download/1aki.pdb
    2019-02-28 10:32:36,569 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/1aki.pdb
    2019-02-28 10:32:36,569 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM']


--------------

pdb_variants
------------

Retrieve variants from UNIPROT mapped to the selected PDB

Get help
^^^^^^^^

.. code:: bash

    %%bash
    pdb_variants -h


.. parsed-literal::

    usage: pdb_variants [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] -o
                        OUTPUT_MUTATIONS_LIST_TXT

    Wrapper for the PDB Variants (http://www.rcsb.org/pdb/home/home.do) mirror of
    the MMB group REST API (http://mmb.irbbarcelona.org/api/) for additional help
    in the commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')

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

-  **pdb_code** (*str*): (“2vgb”) RSCB PDB four letter code. ie: “2ki5”.
-  **url** (*str*): (“http://mmb.irbbarcelona.org/api”) URL of the MMB REST API.

Default config
^^^^^^^^^^^^^^

.. code:: bash

    %%bash
    pdb_variants -o mutations.txt


.. parsed-literal::

    2019-02-28 10:32:47,152 [MainThread  ] [INFO ]  PDB code: 2vgb correspond to uniprot id: P30613
    2019-02-28 10:32:47,152 [MainThread  ] [INFO ]  Fetching variants for uniprot_id: P30613 and pdb_code: 2vgb
    2019-02-28 10:32:49,329 [MainThread  ] [INFO ]  Found: 118 variants for uniprot id: P30613
    2019-02-28 10:32:49,331 [MainThread  ] [INFO ]  Found 459 mutations mapped to PDB: 2vgb
    2019-02-28 10:32:49,331 [MainThread  ] [INFO ]  Writting mutations to: mutations.txt


JSON string config
^^^^^^^^^^^^^^^^^^

.. code:: bash

    %%bash
    pdb_variants -c "{\"pdb_code\":\"2src\"}" -o mutations.txt


.. parsed-literal::

    2019-02-28 10:32:51,432 [MainThread  ] [INFO ]  PDB code: 2src correspond to uniprot id: P12931
    2019-02-28 10:32:51,432 [MainThread  ] [INFO ]  Fetching variants for uniprot_id: P12931 and pdb_code: 2src
    2019-02-28 10:32:52,228 [MainThread  ] [INFO ]  Found: 4 variants for uniprot id: P12931
    2019-02-28 10:32:52,228 [MainThread  ] [INFO ]  Found 4 mutations mapped to PDB: 2src
    2019-02-28 10:32:52,228 [MainThread  ] [INFO ]  Writting mutations to: mutations.txt


YAML file config
^^^^^^^^^^^^^^^^

.. code:: bash

    %%bash
    printf "pdb_code: 2src" > conf.yml
    cat conf.yml

    pdb_variants -c conf.yml -o mutations.txt


.. parsed-literal::

    pdb_code: 2src

.. parsed-literal::

    2019-02-28 10:32:55,134 [MainThread  ] [INFO ]  PDB code: 2src correspond to uniprot id: P12931
    2019-02-28 10:32:55,135 [MainThread  ] [INFO ]  Fetching variants for uniprot_id: P12931 and pdb_code: 2src
    2019-02-28 10:32:55,866 [MainThread  ] [INFO ]  Found: 4 variants for uniprot id: P12931
    2019-02-28 10:32:55,867 [MainThread  ] [INFO ]  Found 4 mutations mapped to PDB: 2src
    2019-02-28 10:32:55,867 [MainThread  ] [INFO ]  Writting mutations to: mutations.txt


--------------

pdb_cluster_zip
---------------

Download the selected similarity cluster of the selected PDB

Get help
~~~~~~~~

.. code:: bash

    %%bash
    pdb_cluster_zip -h


.. parsed-literal::

    usage: pdb_cluster_zip [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] -o
                           OUTPUT_PDB_ZIP_PATH

    Wrapper for the PDB Cluster (http://www.rcsb.org/pdb/home/home.do) mirror of
    the MMB group REST API (http://mmb.irbbarcelona.org/api/) for additional help
    in the commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')

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

-  **pdb_code** (*str*) - (‘2vgb’) RSCB PDB code. ie: “2VGB”
-  **filter** (*str*) - ([“ATOM”, “MODEL”, “ENDMDL”]) Array of groups to
   be keep. If value is None or False no filter will be applied. All the
   possible values are defined in the official PDB specification
   (http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
-  **cluster** (*str*) - (90) Cluster number for the
   :meth:``biobb_io.mmb_api.MmbPdb.get_pdb_cluster_zip`` method.
-  **url** (*str*) - (“https://files.rcsb.org/download/”) URL of the MMB PDB REST API.

Default config
^^^^^^^^^^^^^^

.. code:: bash

    %%bash
    pdb_cluster_zip -o 2vgb_cluster90.zip


.. parsed-literal::

    2019-02-28 10:33:12,658 [MainThread  ] [INFO ]  Cluster: 90 of pdb_code: 2vgb
     List: {'2vgf', '2vgi', '4ima', '2vgg', '4ip7', '2vgb'}
    2019-02-28 10:33:12,659 [MainThread  ] [INFO ]  05da0d1e-1f13-4d62-9603-761c6c42a5bc directory successfully created
    2019-02-28 10:33:12,659 [MainThread  ] [INFO ]  Downloading: 2vgf from: https://files.rcsb.org/download/2vgf.pdb
    ...
    2019-02-28 10:33:20,391 [MainThread  ] [INFO ]  Adding:
    2019-02-28 10:33:20,391 [MainThread  ] [INFO ]  ['/Users/pau/projects/biobb_io/biobb_io/docs/05da0d1e-1f13-4d62-9603-761c6c42a5bc/2vgb.pdb', ...]
    2019-02-28 10:33:20,391 [MainThread  ] [INFO ]  to: /Users/pau/projects/biobb_io/biobb_io/docs/2vgb_cluster90.zip


JSON string config
^^^^^^^^^^^^^^^^^^

.. code:: bash

    %%bash
    pdb_cluster_zip -c "{\"pdb_code\":\"2src\", \"cluster\":95}" -o 2src_cluster95.zip


.. parsed-literal::

    2019-02-28 10:35:04,797 [MainThread  ] [INFO ]  Cluster: 95 of pdb_code: 2src
     List: {'3d7u', '3dqw', '2qq7', ...}
    2019-02-28 10:35:04,807 [MainThread  ] [INFO ]  4a3c8725-5d4e-4009-915b-00a0ca9bcd74 directory successfully created
    2019-02-28 10:35:04,807 [MainThread  ] [INFO ]  Downloading: 3d7u from: https://files.rcsb.org/download/3d7u.pdb
    2019-02-28 10:35:06,577 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/3d7u.pdb
    2019-02-28 10:35:06,577 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM', 'MODEL', 'ENDMDL']
    2019-02-28 10:35:06,593 [MainThread  ] [INFO ]  Downloading: 3dqw from: https://files.rcsb.org/download/3dqw.pdb
    2019-02-28 10:35:07,656 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/3dqw.pdb
    2019-02-28 10:35:07,657 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM', 'MODEL', 'ENDMDL']
    ...
    2019-02-28 10:36:58,645 [MainThread  ] [INFO ]  Adding:
    2019-02-28 10:36:58,645 [MainThread  ] [INFO ]  ['/Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/1a07.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/1a08.pdb', ...]
    2019-02-28 10:36:58,645 [MainThread  ] [INFO ]  to: /Users/pau/projects/biobb_io/biobb_io/docs/2src_cluster95.zip


YAML file config
^^^^^^^^^^^^^^^^

.. code:: bash

    %%bash
    printf "pdb_code: 2src\ncluster: 95" > conf.yml
    cat conf.yml

    pdb_cluster_zip -c conf.yml -o 2src_cluster95.zip


.. parsed-literal::

    pdb_code: 2src
    cluster: 95

.. parsed-literal::

    2019-02-28 10:47:28,218 [MainThread  ] [INFO ]  Cluster: 95 of pdb_code: 2src
     List: {'1o4q', '3qlg', '2hwo', ... }
    2019-02-28 10:47:28,218 [MainThread  ] [INFO ]  f95988db-701f-4e59-83ab-3c750730109d directory successfully created
    2019-02-28 10:47:28,218 [MainThread  ] [INFO ]  Downloading: 1o4q from: https://files.rcsb.org/download/1o4q.pdb
    2019-02-28 10:47:28,922 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/f95988db-701f-4e59-83ab-3c750730109d/1o4q.pdb
    2019-02-28 10:47:28,923 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM', 'MODEL', 'ENDMDL']
    2019-02-28 10:47:28,925 [MainThread  ] [INFO ]  Downloading: 3qlg from: https://files.rcsb.org/download/3qlg.pdb
    2019-02-28 10:47:30,681 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/f95988db-701f-4e59-83ab-3c750730109d/3qlg.pdb
    2019-02-28 10:47:30,681 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM', 'MODEL', 'ENDMDL']
    2019-02-28 10:47:30,696 [MainThread  ] [INFO ]  Downloading: 2hwo from: https://files.rcsb.org/download/2hwo.pdb
    ...
    2019-02-28 10:49:26,697 [MainThread  ] [INFO ]  Adding:
    2019-02-28 10:49:26,697 [MainThread  ] [INFO ]  ['/Users/pau/projects/biobb_io/biobb_io/docs/f95988db-701f-4e59-83ab-3c750730109d/1a07.pdb', ... ]
    2019-02-28 10:49:26,697 [MainThread  ] [INFO ]  to: /Users/pau/projects/biobb_io/biobb_io/docs/2src_cluster95.zip
