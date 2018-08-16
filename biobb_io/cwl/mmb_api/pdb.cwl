#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand:
  - pdb.py
inputs:
  system:
    type: string
    inputBinding:
      position: 1
      prefix: --system
    default: "linux"
  step:
    type: string
    inputBinding:
      position: 2
      prefix: --step
    default: "mmbpdb"
  conf_file:
    type: File
    inputBinding:
      position: 3
      prefix: --conf_file
  output_pdb_path:
    type: string
    inputBinding:
      position: 4
      prefix: --output_pdb_path
outputs:
  output_pdb_file:
    type: File
    outputBinding:
      glob: $(inputs.output_pdb_path)
