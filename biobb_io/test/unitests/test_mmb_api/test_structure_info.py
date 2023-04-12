from biobb_common.tools import test_fixtures as fx
from biobb_io.api.structure_info import structure_info


class TestStructureInfo():
    def setup_class(self):
        fx.test_setup(self, 'structure_info')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_structure_info(self):
        structure_info(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_json_path'])
        assert fx.equal(self.paths['output_json_path'], self.paths['reference_output_json_path'])
