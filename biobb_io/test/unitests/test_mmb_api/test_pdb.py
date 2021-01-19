from biobb_common.tools import test_fixtures as fx
from biobb_io.api.pdb import pdb

class TestPdb():
    def setUp(self):
        fx.test_setup(self,'pdb')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_pdb(self):
        pdb(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal(self.paths['output_pdb_path'], self.paths['reference_output_pdb_path'])
