# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_io.api.mddb import mddb


class TestMDDB():
    def setup_class(self):
        fx.test_setup(self, 'mddb')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_mddb(self):
        mddb(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_top_path'])
        assert fx.equal(self.paths['output_top_path'], self.paths['reference_output_top_path'])
        assert fx.not_empty(self.paths['output_trj_path'])
        assert fx.equal(self.paths['output_trj_path'], self.paths['reference_output_trj_path'])
