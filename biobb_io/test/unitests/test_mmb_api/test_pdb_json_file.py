from biobb_common.tools import test_fixtures as fx
from mmb_api.pdb import MmbPdb
import os


class TestMmbPdb(object):
    def setUp(self):
        self.json_file_path="/tmp/test_pdb_json_file.json"
        with open(self.json_file_path,"w") as json_file:
            json_string='{"workflow_path":"/tmp/biobb/unitests", "paths":{"output_pdb_path":"output_pdb_path.pdb"}, "properties":{"pdb_code":"2VGB"}}'
            json_file.write(json_string)
        fx.test_setup(self,config=self.json_file_path)

    def tearDown(self):
        fx.test_teardown(self)
        os.remove(self.json_file_path)

    def test_get_pdb_zip(self):
        MmbPdb(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_pdb_path'])
