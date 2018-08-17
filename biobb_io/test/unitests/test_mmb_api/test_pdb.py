from biobb_common.tools import test_fixtures as fx
from mmb_api.pdb import MmbPdb


class TestMmbPdb(object):
    def setUp(self):
        fx.test_setup(self,'mmbpdb')

    def tearDown(self):
        fx.test_teardown(self)

    def test_get_pdb_zip(self):
        MmbPdb(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_path'])
