from biobb_common.tools import test_fixtures as fx
from biobb_io.api.drugbank import Drugbank

class TestDrugbank():
    def setUp(self):
        fx.test_setup(self,'drugbank')

    def tearDown(self):
        fx.test_teardown(self)

    def test_drugbank(self):
        Drugbank(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_sdf_path'])
        assert fx.equal(self.paths['output_sdf_path'], self.paths['reference_output_sdf_path'])
