from biobb_common.tools import test_fixtures as fx
from biobb_io.api.memprotmd_sim import MemProtMDSim

class TestMemProtMDSim():
    def setUp(self):
        fx.test_setup(self,'memprotmd_sim')

    def tearDown(self):
        fx.test_teardown(self)

    def test_memprotmd_sim(self):
        MemProtMDSim(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_simulation'])
        #assert fx.equal(self.paths['output_simulation'], self.paths['reference_output_simulation'])
