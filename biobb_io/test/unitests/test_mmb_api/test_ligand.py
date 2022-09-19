from biobb_common.tools import test_fixtures as fx
from biobb_io.api.ligand import ligand

class TestLigand():
    def setup_class(self):
        fx.test_setup(self,'ligand')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_ligand(self):
        ligand(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal_txt(self.paths['output_pdb_path'], self.paths['reference_output_pdb_path'])
