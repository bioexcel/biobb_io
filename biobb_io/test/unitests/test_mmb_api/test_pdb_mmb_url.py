from biobb_common.tools import test_fixtures as fx
from api.pdb import Pdb

class TestMmbPdb():
    def setUp(self):
        fx.test_setup(self,'pdb_url')

    def tearDown(self):
        fx.test_teardown(self)

    def test_get_pdb_zip(self):
        Pdb(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal(self.paths['output_pdb_path'], self.paths['reference_output_pdb_path'])
