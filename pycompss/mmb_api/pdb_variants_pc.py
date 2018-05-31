from pycompss.api.task import task
from biobb_common.tools import file_utils as fu
from mmb_api import pdb_variants

@task(output_mutations_list_txt=FILE_OUT)
def pdb_variants_pc(output_mutations_list_txt, properties, **kwargs):
    try:
        pdb_variants.MmbPdbVariants(output_mutations_list_txt=output_mutations_list_txt, properties=properties, **kwargs).launch()
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_mutations_list_txt)
