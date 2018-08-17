from biobb_common.tools import test_fixtures as fx
from mmb_api.pdb_cluster_zip import MmbPdbClusterZip


class TestMmbPdbClusterZip(object):
    def setUp(self):
        fx.test_setup(self,'mmbpdbclusterzip')

    def tearDown(self):
        fx.test_teardown(self)

    def test_get_pdb_zip(self):
        MmbPdbClusterZip(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_zip_path'])
