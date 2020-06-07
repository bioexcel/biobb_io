from biobb_common.tools import test_fixtures as fx
from biobb_io.api.ligand import Ligand

class TestPdb():
    def setUp(self):
        fx.test_setup(self,'ligand')

    def tearDown(self):
        fx.test_teardown(self)

    def test_ligand(self):
        Ligand(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal_txt(self.paths['output_pdb_path'], self.paths['reference_output_pdb_path'])
