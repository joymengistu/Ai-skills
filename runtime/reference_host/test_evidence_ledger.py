import unittest

from runtime.reference_host.evidence_ledger import EvidenceLedger, EvidenceRecord, validate_ledger


class EvidenceLedgerTests(unittest.TestCase):
    def test_supported_record_requires_span_and_serializes_tuples(self):
        ledger = EvidenceLedger("ledger-1", "run-1")
        ledger.add(EvidenceRecord(
            evidence_id="e-1",
            claim_id="c-1",
            claim_type="fact",
            claim="A bounded claim",
            source_ref="source-1",
            source_tier="A",
            evidence_span="section 1",
            support_status="supported",
            confidence="high",
            scope="Only the stated scope",
        ))
        payload = ledger.to_dict()
        self.assertEqual(payload["records"][0]["transformation_refs"], [])
        self.assertEqual(payload["records"][0]["confidence"], "high")

    def test_duplicate_ids_and_missing_links_fail_closed(self):
        ledger = EvidenceLedger("ledger-1", "run-1")
        record = EvidenceRecord(
            evidence_id="e-1", claim_id="c-1", claim_type="hypothesis",
            claim="A testable hypothesis", source_ref="source-1",
            support_status="unverified", confidence="low", scope="test scope",
            derived_from=("evidence:e-missing",),
        )
        ledger.add(record)
        with self.assertRaises(ValueError):
            ledger.add(record)
        with self.assertRaises(ValueError):
            ledger.to_dict()

    def test_payload_round_trip(self):
        payload = {
            "schema_version": "1.0",
            "ledger_id": "ledger-1",
            "run_id": "run-1",
            "created_at": "2026-08-23T00:00:00Z",
            "records": [{
                "evidence_id": "e-1", "claim_id": "c-1", "claim_type": "definition",
                "claim": "A definition", "source_ref": "source-1", "source_tier": "A",
                "evidence_span": "section 1", "support_status": "supported", "confidence": "high",
                "scope": "bounded", "freshness_class": "stable",
            }],
        }
        ledger = validate_ledger(payload)
        self.assertEqual(ledger.to_dict()["ledger_id"], "ledger-1")


if __name__ == "__main__":
    unittest.main()
