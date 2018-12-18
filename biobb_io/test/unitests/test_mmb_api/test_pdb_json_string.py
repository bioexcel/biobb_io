from biobb_common.tools import test_fixtures as fx
from mmb_api.pdb import MmbPdb


class TestMmbPdb(object):
    def setUp(self):
        json_config='{"working_dir_path":"/tmp/biobb/unitests", "paths":{"output_pdb_path":"output_pdb_path.pdb", "reference_output_pdb_path":"file:test_reference_dir/mmb_api/pdb_1ubq.pdb"}, "properties":{"pdb_code":"1UBQ"}}'
        fx.test_setup(self,config=json_config)

    def tearDown(self):
        fx.test_teardown(self)

    def test_get_pdb_zip(self):
        MmbPdb(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_path'])
        assert fx.equal(self.paths['output_pdb_path'], self.paths['reference_output_pdb_path'])
