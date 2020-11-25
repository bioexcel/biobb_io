from biobb_common.tools import test_fixtures as fx
from biobb_io.api.pdb_cluster_zip import PdbClusterZip

class TestPdbClusterZip():
    def setUp(self):
        fx.test_setup(self,'pdb_cluster_zip')

    def tearDown(self):
        fx.test_teardown(self)

    def test_pdb_cluster_zip(self):
        PdbClusterZip(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_zip_path'])
        assert fx.equal(self.paths['output_pdb_zip_path'], self.paths['reference_output_pdb_zip_path'])
