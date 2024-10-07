# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_io.api.mmcif import mmcif


class TestMmcif():
    def setup_class(self):
        fx.test_setup(self, 'mmcif')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_mmcif(self):
        mmcif(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_mmcif_path'])
        assert fx.equal(self.paths['output_mmcif_path'], self.paths['reference_output_mmcif_path'])
