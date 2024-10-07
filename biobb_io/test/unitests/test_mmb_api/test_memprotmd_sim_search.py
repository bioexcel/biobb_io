# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_io.api.memprotmd_sim_search import MemProtMDSimSearch


class TestMemProtMDSimSearch():
    def setup_class(self):
        fx.test_setup(self, 'memprotmd_sim_search')

    def teardown_class(self):
        # fx.test_teardown(self)
        pass

    def test_memprotmd_sim_search(self):
        MemProtMDSimSearch(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_simulations'])
        assert fx.validate_json(self.paths['output_simulations'], self.paths['reference_output_simulations'])
