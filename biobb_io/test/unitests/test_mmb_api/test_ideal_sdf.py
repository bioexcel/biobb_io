# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_io.api.ideal_sdf import ideal_sdf


class TestIdealSdf():
    def setup_class(self):
        fx.test_setup(self, 'ideal_sdf')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_ideal_sdf(self):
        ideal_sdf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_sdf_path'])
        assert fx.equal(self.paths['output_sdf_path'], self.paths['reference_output_sdf_path'])
