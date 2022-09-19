from biobb_common.tools import test_fixtures as fx
from biobb_io.api.drugbank import drugbank

class TestDrugbank():
    def setup_class(self):
        fx.test_setup(self,'drugbank')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_drugbank(self):
        drugbank(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_sdf_path'])
        assert fx.equal(self.paths['output_sdf_path'], self.paths['reference_output_sdf_path'])
