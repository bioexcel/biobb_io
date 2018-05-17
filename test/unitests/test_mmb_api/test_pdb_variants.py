from os.path import join as opj
from biobb_common.tools import test_fixtures as fx
from mmb_api.pdb_cluster_zip import MmbPdbClusterZip


class TestMmbPdbVariants(object):
    def setUp(self):
        fx.test_setup(self,'mmbpdbvariants')

    def tearDown(self):
        pass
        fx.test_teardown(self)

    def test_get_pdb_zip(self):
        MmbPdbVariants(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_mutations_list_txt'])
