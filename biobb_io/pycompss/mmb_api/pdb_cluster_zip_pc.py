from pycompss.api.task import task
from biobb_common.tools import file_utils as fu
from mmb_api import pdb_cluster_zip

@task(output_pdb_zip_path=FILE_OUT)
def pdb_cluster_zip_pc(output_pdb_zip_path, properties, **kwargs):
    try:
        pdb_cluster_zip.MmbPdbClusterZip(output_pdb_zip_path=output_pdb_zip_path, properties=properties, **kwargs).launch()
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_pdb_zip_path)
