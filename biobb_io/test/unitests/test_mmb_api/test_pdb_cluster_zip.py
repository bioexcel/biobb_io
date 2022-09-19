from biobb_common.tools import test_fixtures as fx
from biobb_io.api.pdb_cluster_zip import pdb_cluster_zip

class TestPdbClusterZip():
    def setup_class(self):
        fx.test_setup(self,'pdb_cluster_zip')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_pdb_cluster_zip(self):
        pdb_cluster_zip(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_pdb_zip_path'])
        assert fx.equal(self.paths['output_pdb_zip_path'], self.paths['reference_output_pdb_zip_path'])
