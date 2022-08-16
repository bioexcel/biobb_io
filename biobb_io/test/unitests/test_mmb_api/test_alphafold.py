from biobb_common.tools import test_fixtures as fx
from biobb_io.api.alphafold import alphafold

class TestAlphaFold():
    def setUp(self):
        fx.test_setup(self,'alphafold')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_alphafold(self):
        alphafold(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal(self.paths['output_pdb_path'], self.paths['reference_output_pdb_path'])
