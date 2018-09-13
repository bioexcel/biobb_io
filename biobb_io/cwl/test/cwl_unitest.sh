#!/usr/bin/env bash

BIOBB_IO=$HOME/projects/biobb_io/biobb_io
cwltool $BIOBB_IO/cwl/mmb_api/pdb.cwl $BIOBB_IO/cwl/test/mmb_api/mmbpdb.yml
cwltool $BIOBB_IO/cwl/mmb_api/pdb_variants.cwl $BIOBB_IO/cwl/test/mmb_api/mmbpdbvariants.yml
cwltool $BIOBB_IO/cwl/mmb_api/pdb_cluster_zip.cwl $BIOBB_IO/cwl/test/mmb_api/mmbpdbclusterzip.yml
