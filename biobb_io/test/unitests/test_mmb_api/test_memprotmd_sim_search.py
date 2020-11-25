from biobb_common.tools import test_fixtures as fx
from biobb_io.api.memprotmd_sim_search import MemProtMDSimSearch

class TestMemProtMDSimSearch():
    def setUp(self):
        fx.test_setup(self,'memprotmd_sim_search')

    def tearDown(self):
        fx.test_teardown(self)

    def test_memprotmd_sim_search(self):
        MemProtMDSimSearch(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_simulations'])
        assert fx.equal(self.paths['output_simulations'], self.paths['reference_output_simulations'])
