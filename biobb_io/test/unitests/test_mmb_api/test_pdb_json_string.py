from biobb_common.tools import test_fixtures as fx
from mmb_api.pdb import MmbPdb


class TestMmbPdb(object):
    def setUp(self):
        json_config='{"workflow_path":"/tmp/biobb/unitests", "paths":{"output_pdb_path":"output_pdb_path.pdb"}, "properties":{"pdb_code":"2VGB"}}'
        fx.test_setup(self,config=json_config)

    def tearDown(self):
        fx.test_teardown(self)

    def test_get_pdb_zip(self):
        MmbPdb(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_path'])
