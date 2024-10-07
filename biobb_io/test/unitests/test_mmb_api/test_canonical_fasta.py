# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_io.api.canonical_fasta import canonical_fasta


class TestCanonicalFasta():
    def setup_class(self):
        fx.test_setup(self, 'canonical_fasta')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_canonical_fasta(self):
        canonical_fasta(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_fasta_path'])
        assert fx.equal(self.paths['output_fasta_path'], self.paths['reference_output_fasta_path'])
