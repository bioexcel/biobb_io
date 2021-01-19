from biobb_common.tools import test_fixtures as fx
from biobb_io.api.binding_site import binding_site

class TestBindingSite():
    def setUp(self):
        fx.test_setup(self,'binding_site')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_binding_site(self):
        binding_site(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_json_path'])
        assert fx.equal(self.paths['output_json_path'], self.paths['reference_output_json_path'])
