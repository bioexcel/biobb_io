# type: ignore
from biobb_common.tools import test_fixtures as fx
# from biobb_io.api.pdb_variants import pdb_variants


class TestMmbPdbVariants():
    def setup_class(self):
        fx.test_setup(self, 'pdb_variants')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_get_pdb_zip(self):
        pass
        # pdb_variants(properties=self.properties, **self.paths)
        # assert fx.not_empty(self.paths['output_mutations_list_txt'])
