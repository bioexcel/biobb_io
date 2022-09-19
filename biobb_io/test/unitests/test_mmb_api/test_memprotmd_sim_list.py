from biobb_common.tools import test_fixtures as fx
from biobb_io.api.memprotmd_sim_list import memprotmd_sim_list

class TestMemProtMDSimList():
    def setup_class(self):
        fx.test_setup(self,'memprotmd_sim_list')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_memprotmd_sim_list(self):
        memprotmd_sim_list(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_simulations'])
        assert fx.equal(self.paths['output_simulations'], self.paths['reference_output_simulations'])
