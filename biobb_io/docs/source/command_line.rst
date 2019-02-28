Biobb IO Command Line Help
==========================

Please refer to the `system & step
documentation <https://biobb-common.readthedocs.io/en/latest/system_step.html>`__
for more information of these two parameters.

pdb: Download PDB files from RCSB PDB API
-----------------------------------------

Get help
~~~~~~~~

Input:

.. code:: bash

    
    pdb -h


Output:

.. parsed-literal::

    usage: pdb [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] -o OUTPUT_PDB_PATH

    Wrapper for the PDB ('http://www.rcsb.org/pdb/home/home.do') mirror of the MMB
    group REST API ('http://mmb.irbbarcelona.org/api/') for additional help in the
    commandline usage please check ('https://biobb-io.readthedocs.io/en/latest/command_line.html')

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

Input:

.. code:: bash

    
    #Default config
    pdb -o 1aki.pdb


Output:

.. parsed-literal::

    2019-02-28 10:32:29,165 [MainThread  ] [INFO ]  Downloading: 1ubq from: https://files.rcsb.org/download/1ubq.pdb
    2019-02-28 10:32:29,801 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/1aki.pdb
    2019-02-28 10:32:29,801 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM', 'MODEL', 'ENDMDL']


Input:

.. code:: bash

    
    #JSON string
    pdb -c "{\"pdb_code\":\"1aki\", \"filter\":[\"ATOM\"]}" -o 1aki.pdb


Output:

.. parsed-literal::

    2019-02-28 10:32:31,181 [MainThread  ] [INFO ]  Downloading: 1aki from: https://files.rcsb.org/download/1aki.pdb
    2019-02-28 10:32:31,788 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/1aki.pdb
    2019-02-28 10:32:31,788 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM']


Input:

.. code:: bash

    
    #YAML file
    printf "pdb_code: 1aki\nfilter: [\"ATOM\"]" > conf.yml
    cat conf.yml

    pdb -c conf.yml -o 1aki.pdb


Output:

.. parsed-literal::

    pdb_code: 1aki
    filter: ["ATOM"]

Output:

.. parsed-literal::

    2019-02-28 10:32:35,954 [MainThread  ] [INFO ]  Downloading: 1aki from: https://files.rcsb.org/download/1aki.pdb
    2019-02-28 10:32:36,569 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/1aki.pdb
    2019-02-28 10:32:36,569 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM']


pdb_variants: Retreive variants from UNIPROT mapped to the selected PDB
-----------------------------------------------------------------------

Get help
~~~~~~~~

Input:

.. code:: bash

    
    pdb_variants -h


Output:

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

Input:

.. code:: bash

    
    #Default config
    pdb_variants -o mutations.txt


Output:

.. parsed-literal::

    2019-02-28 10:32:47,152 [MainThread  ] [INFO ]  PDB code: 2vgb correspond to uniprot id: P30613
    2019-02-28 10:32:47,152 [MainThread  ] [INFO ]  Fetching variants for uniprot_id: P30613 and pdb_code: 2vgb
    2019-02-28 10:32:49,329 [MainThread  ] [INFO ]  Found: 118 variants for uniprot id: P30613
    2019-02-28 10:32:49,331 [MainThread  ] [INFO ]  Found 459 mutations mapped to PDB: 2vgb
    2019-02-28 10:32:49,331 [MainThread  ] [INFO ]  Writting mutations to: mutations.txt


Input:

.. code:: bash

    
    #JSON string
    pdb_variants -c "{\"pdb_code\":\"2src\"}" -o mutations.txt


Output:

.. parsed-literal::

    2019-02-28 10:32:51,432 [MainThread  ] [INFO ]  PDB code: 2src correspond to uniprot id: P12931
    2019-02-28 10:32:51,432 [MainThread  ] [INFO ]  Fetching variants for uniprot_id: P12931 and pdb_code: 2src
    2019-02-28 10:32:52,228 [MainThread  ] [INFO ]  Found: 4 variants for uniprot id: P12931
    2019-02-28 10:32:52,228 [MainThread  ] [INFO ]  Found 4 mutations mapped to PDB: 2src
    2019-02-28 10:32:52,228 [MainThread  ] [INFO ]  Writting mutations to: mutations.txt


Input:

.. code:: bash

    
    #YAML file
    printf "pdb_code: 2src" > conf.yml
    cat conf.yml

    pdb_variants -c conf.yml -o mutations.txt


Output:

.. parsed-literal::

    pdb_code: 2src

Output:

.. parsed-literal::

    2019-02-28 10:32:55,134 [MainThread  ] [INFO ]  PDB code: 2src correspond to uniprot id: P12931
    2019-02-28 10:32:55,135 [MainThread  ] [INFO ]  Fetching variants for uniprot_id: P12931 and pdb_code: 2src
    2019-02-28 10:32:55,866 [MainThread  ] [INFO ]  Found: 4 variants for uniprot id: P12931
    2019-02-28 10:32:55,867 [MainThread  ] [INFO ]  Found 4 mutations mapped to PDB: 2src
    2019-02-28 10:32:55,867 [MainThread  ] [INFO ]  Writting mutations to: mutations.txt


pdb_cluster_zip: Download the selected similarity cluster of the selected PDB
-----------------------------------------------------------------------------

Get help
~~~~~~~~

Input:

.. code:: bash

    
    pdb_cluster_zip -h


Output:

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
-  **cluster** (*str*) - (90) Cluster number for the :meth:``biobb_io.mmb_api.MmbPdb.get_pdb_cluster_zip`` method.
-  **url** (*str*) - (“https://files.rcsb.org/download/”) URL of the MMB PDB REST API.

Input:

.. code:: bash

    
    #Default config
    pdb_cluster_zip -o 2vgb_cluster90.zip


Output:

.. parsed-literal::

    2019-02-28 10:33:12,658 [MainThread  ] [INFO ]  Cluster: 90 of pdb_code: 2vgb
     List: {'2vgf', '2vgi', '4ima', '2vgg', '4ip7', '2vgb'}
    2019-02-28 10:33:12,659 [MainThread  ] [INFO ]  05da0d1e-1f13-4d62-9603-761c6c42a5bc directory successfully created
    2019-02-28 10:33:12,659 [MainThread  ] [INFO ]  Downloading: 2vgf from: https://files.rcsb.org/download/2vgf.pdb
    2019-02-28 10:33:13,949 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/05da0d1e-1f13-4d62-9603-761c6c42a5bc/2vgf.pdb
    2019-02-28 10:33:13,949 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM', 'MODEL', 'ENDMDL']
    2019-02-28 10:33:13,974 [MainThread  ] [INFO ]  Downloading: 2vgi from: https://files.rcsb.org/download/2vgi.pdb
    2019-02-28 10:33:15,195 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/05da0d1e-1f13-4d62-9603-761c6c42a5bc/2vgi.pdb
    2019-02-28 10:33:15,195 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM', 'MODEL', 'ENDMDL']
    ...
    2019-02-28 10:33:20,391 [MainThread  ] [INFO ]  Adding:
    2019-02-28 10:33:20,391 [MainThread  ] [INFO ]  ['/Users/pau/projects/biobb_io/biobb_io/docs/05da0d1e-1f13-4d62-9603-761c6c42a5bc/2vgb.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/05da0d1e-1f13-4d62-9603-761c6c42a5bc/2vgf.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/05da0d1e-1f13-4d62-9603-761c6c42a5bc/2vgg.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/05da0d1e-1f13-4d62-9603-761c6c42a5bc/2vgi.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/05da0d1e-1f13-4d62-9603-761c6c42a5bc/4ima.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/05da0d1e-1f13-4d62-9603-761c6c42a5bc/4ip7.pdb']
    2019-02-28 10:33:20,391 [MainThread  ] [INFO ]  to: /Users/pau/projects/biobb_io/biobb_io/docs/2vgb_cluster90.zip


Input:

.. code:: bash

    
    #JSON string
    pdb_cluster_zip -c "{\"pdb_code\":\"2src\", \"cluster\":95}" -o 2src_cluster95.zip


Output:

.. parsed-literal::

    2019-02-28 10:35:04,797 [MainThread  ] [INFO ]  Cluster: 95 of pdb_code: 2src
     List: {'3d7u', '3dqw', '2qq7', '1nzv', '1o46', '3el7', '3el8', '1o4o', '5bmm', '1o4j', '2qi8', '1a1b', '1a1c', '4hxj', '3of0', '2jyq', '4dgg', '3g5d', '1f1w', '1hct', '1o4i', '1fmk', '3dqx', '3u51', '4o2p', '5j5s', '1sha', '3geq', '5swh', '2ptk', '1o4p', '3g6h', '4mxy', '3u4w', '3uqg', '4lgh', '1o4f', '1o4m', '4mxo', '1rlq', '2h8h', '1o4n', '3qlg', '1o4a', '3en4', '1y57', '3lok', '3oez', '1o47', '5k9i', '3en7', '1o45', '3qlf', '2qlq', '1srl', '4mcv', '3d7t', '1o4d', '3f3u', '3g6g', '5d10', '2hwp', '2bdj', '4fic', '1o42', '5xp5', '5t0p', '3f6x', '4agw', '1prm', '1hcs', '4ybk', '1o41', '1yom', '1o44', '6f3f', '1a1e', '1o4e', '1a09', '1shd', '3f3v', '4lgg', '4ybj', '3tz8', '2src', '1is0', '5sys', '3en5', '1a1a', '1o4r', '1a07', '1o4k', '1o49', '4mxx', '1f2f', '2hwo', '1prl', '1o4l', '3f3w', '4mxz', '1o4g', '1rlp', '1yol', '4u5j', '1a08', '1sps', '1o48', '3en6', '1p13', '1o43', '3tz9', '3f3t', '1yi6', '5teh', '1shb', '1spr', '3tz7', '1o4q', '1yoj', '1o4b', '1ksw', '3uqf', '1nzl', '5d12', '3svv', '5d11', '1o4c', '5xp7', '2oiq', '1o4h', '4k11', '2bdf', '1srm'}
    2019-02-28 10:35:04,807 [MainThread  ] [INFO ]  4a3c8725-5d4e-4009-915b-00a0ca9bcd74 directory successfully created
    2019-02-28 10:35:04,807 [MainThread  ] [INFO ]  Downloading: 3d7u from: https://files.rcsb.org/download/3d7u.pdb
    2019-02-28 10:35:06,577 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/3d7u.pdb
    2019-02-28 10:35:06,577 [MainThread  ] [INFO ]  Filtering lines NOT starting with one of these words: ['ATOM', 'MODEL', 'ENDMDL']
    ...
    2019-02-28 10:36:58,645 [MainThread  ] [INFO ]  Adding:
    2019-02-28 10:36:58,645 [MainThread  ] [INFO ]  ['/Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/1a07.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/1a08.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/1a09.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/1a1a.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/4a3c8725-5d4e-4009-915b-00a0ca9bcd74/1a1b.pdb', ...]
    ...
    2019-02-28 10:36:58,645 [MainThread  ] [INFO ]  to: /Users/pau/projects/biobb_io/biobb_io/docs/2src_cluster95.zip


Input:

.. code:: bash

    
    #YAML file
    printf "pdb_code: 2src\ncluster: 95" > conf.yml
    cat conf.yml

    pdb_cluster_zip -c conf.yml -o 2src_cluster95.zip


Output:

.. parsed-literal::

    pdb_code: 2src
    cluster: 95

Output:

.. parsed-literal::

    2019-02-28 10:47:28,218 [MainThread  ] [INFO ]  Cluster: 95 of pdb_code: 2src
     List: {'1o4q', '3qlg', '2hwo', '1srl', '4fic', '3geq', '1prl', '5t0p', '3dqw', '4dgg', '1a1e', '4mcv', '1o4m', '5swh', '3lok', '1rlp', '1a09', '3f3w', '3f6x', '1a1a', '1o4e', '1o43', '1shb', '3d7t', '1o4g', '3dqx', '2ptk', '4mxy', '4agw', '5sys', '1a07', '1o4b', '1o4n', '3el7', '1nzl', '3f3t', '5d10', '2bdf', '1prm', '2qi8', '1o4l', '3u4w', '4mxz', '4lgg', '2qq7', '1is0', '3en6', '1o44', '2h8h', '2oiq', '4mxo', '1o4k', '4o2p', '1o46', '1o42', '3g5d', '3g6h', '5d11', '4mxx', '3tz9', '1a08', '3uqg', '1o45', '1sha', '3of0', '1a1c', '2hwp', '3svv', '1ksw', '4ybj', '1o4d', '1hcs', '3en7', '1srm', '1p13', '2qlq', '1o41', '1o4a', '1f1w', '1yom', '3el8', '1y57', '1nzv', '5bmm', '5d12', '1f2f', '1o4i', '3f3u', '1rlq', '1a1b', '5xp5', '5xp7', '2jyq', '5j5s', '1o4o', '1o4p', '4lgh', '1fmk', '3g6g', '3u51', '1sps', '1o49', '3en5', '1o4f', '3uqf', '1yol', '1hct', '1yoj', '1o4h', '3oez', '4k11', '1o4r', '3d7u', '3tz7', '3qlf', '1o4j', '4hxj', '6f3f', '1spr', '3en4', '1o47', '4u5j', '2src', '1o48', '5k9i', '3f3v', '1shd', '1yi6', '3tz8', '1o4c', '5teh', '2bdj', '4ybk'}
    2019-02-28 10:47:28,218 [MainThread  ] [INFO ]  f95988db-701f-4e59-83ab-3c750730109d directory successfully created
    2019-02-28 10:47:28,218 [MainThread  ] [INFO ]  Downloading: 1o4q from: https://files.rcsb.org/download/1o4q.pdb
    2019-02-28 10:47:28,922 [MainThread  ] [INFO ]  Writting pdb to: /Users/pau/projects/biobb_io/biobb_io/docs/f95988db-701f-4e59-83ab-3c750730109d/1o4q.pdb
    ...
    2019-02-28 10:49:26,697 [MainThread  ] [INFO ]  Adding:
    2019-02-28 10:49:26,697 [MainThread  ] [INFO ]  ['/Users/pau/projects/biobb_io/biobb_io/docs/f95988db-701f-4e59-83ab-3c750730109d/1a07.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/f95988db-701f-4e59-83ab-3c750730109d/1a08.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/f95988db-701f-4e59-83ab-3c750730109d/1a09.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/f95988db-701f-4e59-83ab-3c750730109d/1a1a.pdb', '/Users/pau/projects/biobb_io/biobb_io/docs/f95988db-701f-4e59-83ab-3c750730109d/1a1b.pdb', ...]
    ...
    2019-02-28 10:49:26,697 [MainThread  ] [INFO ]  to: /Users/pau/projects/biobb_io/biobb_io/docs/2src_cluster95.zip
