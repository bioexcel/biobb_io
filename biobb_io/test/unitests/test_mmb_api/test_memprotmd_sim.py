from biobb_common.tools import test_fixtures as fx
from biobb_io.api.memprotmd_sim import memprotmd_sim


class TestMemProtMDSim():
    def setup_class(self):
        fx.test_setup(self, 'memprotmd_sim')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_memprotmd_sim(self):
        memprotmd_sim(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_simulation'])
        # assert fx.equal(self.paths['output_simulation'], self.paths['reference_output_simulation'])
