import hashlib
import tempfile
import unittest
from pathlib import Path

from runtime.reference_host.artifact_provenance import ArtifactIntegrityVerifier, ArtifactRecord


class ArtifactProvenanceTests(unittest.TestCase):
    def test_integrity_evidence_is_digest_backed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "out.txt").write_text("verified", encoding="utf-8")
            expected = hashlib.sha256(b"verified").hexdigest()
            record = ArtifactRecord("artifact-1", "document", "out.txt", "run-1", "only this file", requirement_refs=("req-1",))
            result = ArtifactIntegrityVerifier(root).verify(record, expected)
            self.assertEqual(result["status"], "verified_integrity")
            self.assertEqual(result["evidence_refs"], [f"artifact:artifact-1:sha256:{expected}"])

    def test_hash_mismatch_is_failure_but_still_records_observed_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "out.txt").write_text("actual", encoding="utf-8")
            record = ArtifactRecord("artifact-1", "code", "out.txt", "run-1", "only this file")
            result = ArtifactIntegrityVerifier(root).verify(record, "0" * 64)
            self.assertEqual(result["status"], "failed")
            self.assertTrue(result["evidence_refs"])
            self.assertTrue(result["failures"])

    def test_path_escape_is_rejected(self):
        with self.assertRaises(ValueError):
            ArtifactRecord("artifact-1", "code", "../secret", "run-1", "none")


if __name__ == "__main__":
    unittest.main()
