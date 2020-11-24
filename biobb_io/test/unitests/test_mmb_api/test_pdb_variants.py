from biobb_common.tools import test_fixtures as fx
from biobb_io.api.pdb_variants import PdbVariants

class TestMmbPdbVariants():
    def setUp(self):
        fx.test_setup(self,'pdb_variants')

    def tearDown(self):
        fx.test_teardown(self)

    def test_get_pdb_zip(self):
        PdbVariants(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_mutations_list_txt'])
