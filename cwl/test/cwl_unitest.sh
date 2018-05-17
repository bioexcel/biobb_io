export BIOBB_IO=$HOME/projects/biobb_io
export PATH=$BIOBB_IO/mmb_api:$PATH


cwltool $BIOBB_IO/cwl/mmb_api/pdb.cwl $BIOBB_IO/cwl/test/mmb_api/mmbpdb.yml
