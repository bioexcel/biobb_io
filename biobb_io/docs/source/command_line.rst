
.. code:: ipython3

    %%html
    <style>
        .prompt{width: 0px; min-width: 0px; visibility: collapse}
    </style>



.. raw:: html

    <style>
        .prompt{width: 0px; min-width: 0px; visibility: collapse}
    </style>



.. code:: bash

    %%bash
    pdb -h


.. parsed-literal::

    usage: pdb [-h] [-c CONFIG] [--system SYSTEM] [--step STEP] -o OUTPUT_PDB_PATH
    
    Wrapper for the PDB (http://www.rcsb.org/pdb/home/home.do) mirror of the MMB
    group REST API (http://mmb.irbbarcelona.org/api/)
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
      --system SYSTEM
      --step STEP
    
    required arguments:
      -o OUTPUT_PDB_PATH, --output_pdb_path OUTPUT_PDB_PATH
                            Output file name


.. code:: bash

    %%bash
    which pdb


.. parsed-literal::

    /anaconda3/envs/dev/bin/pdb


.. code:: bash

    %%bash
    ls -la /anaconda3/envs/dev/bin/pdb


.. parsed-literal::

    lrwxr-xr-x  1 pau  staff  52 Jan 31 18:56 /anaconda3/envs/dev/bin/pdb -> /Users/pau/projects/biobb_io/biobb_io/mmb_api/pdb.py


.. code:: bash

    %%bash
    pdb -h


.. parsed-literal::

    usage: pdb [-h] [--config CONFIG] [--system SYSTEM] [--step STEP]
               --output_pdb_path OUTPUT_PDB_PATH
    
    Wrapper for the PDB (http://www.rcsb.org/pdb/home/home.do) mirror of the MMB
    group REST API (http://mmb.irbbarcelona.org/api/)
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG
      --system SYSTEM
      --step STEP
      --output_pdb_path OUTPUT_PDB_PATH

