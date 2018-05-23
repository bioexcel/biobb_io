#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand:
  - pdb_variants.py
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
    default: "mmbpdbvariants"
  conf_file:
    type: File
    inputBinding:
      position: 3
      prefix: --conf_file
  output_mutations_list_txt:
    type: string
    inputBinding:
      position: 4
      prefix: --output_mutations_list_txt
outputs:
  output_mutations_list_file:
    type: File
    outputBinding:
      glob: $(inputs.output_mutations_list_txt)
