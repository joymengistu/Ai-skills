import json
import tempfile
import unittest
from pathlib import Path

from runtime.reference_host.host import DeterministicProvider, NormalizedTraceAdapter, ReferenceHost
from runtime.reference_host.verifiers import FileStateVerifier
import hashlib


class NormalizedTraceTests(unittest.TestCase):
    def test_adapter_redacts_content_and_normalizes_usage(self):
        adapter = NormalizedTraceAdapter(provider="test-provider", model_ref="test-model")
        response = type("Response", (), {
            "text": "secret response",
            "usage": {"model": "test-model", "input_tokens": 4, "output_tokens": 6, "total_tokens": 10, "latency_ms": 12.5, "retry_count": 1, "finish_reason": "stop"},
            "tool_request": None,
        })()
        record = adapter.normalize_response(
            span_id="span-1",
            response=response,
            request_fingerprint={"prompt": "secret request"},
        )
        self.assertEqual(record["event_kind"], "llm_generation")
        self.assertEqual(record["usage"]["total_tokens"], 10)
        self.assertEqual(record["content_policy"], "redacted_by_default")
        self.assertNotIn("secret response", json.dumps(record))
        self.assertTrue(record["content_digests"]["response"].startswith("sha256:"))
        self.assertIn("response_content", record["redactions"])

    def test_adapter_rejects_unscoped_explicit_capture(self):
        with self.assertRaises(ValueError):
            NormalizedTraceAdapter(provider="p", model_ref="m", content_policy="explicitly_captured")

    def test_file_state_verifier_checks_hashes_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "artifact.txt"
            artifact.write_text("verified")
            digest = hashlib.sha256(b"verified").hexdigest()
            result = FileStateVerifier(root, {"artifact.txt": digest}).verify("task", {})
            self.assertEqual(result.status, "success")
            self.assertTrue(any(ref.startswith("file:artifact.txt:sha256:") for ref in result.evidence_refs))
            failed = FileStateVerifier(root, {"artifact.txt": "0" * 64}).verify("task", {})
            self.assertEqual(failed.status, "failure")
            with self.assertRaises(ValueError):
                FileStateVerifier(root, {"../escape.txt": ""})

    def test_host_emits_normalized_trace_with_redaction_markers(self):
        profile = {
            "run_id": "run-normalized",
            "mode": "focused",
            "model_policy": {"default_route": "test", "escalation_rule": "never", "fallback_rule": "stop"},
            "tool_policy": {"allowed": [], "approval_required": [], "sandbox": True, "cleanup": "remove-temp"},
            "budgets": {"max_model_calls": 1, "max_tool_calls": 0, "max_minutes": 1, "max_retries": 0},
            "privacy": {"data_class": "test", "retention": "temporary", "provider_consent": True},
            "delivery": {"first_slice_target": "response", "completion_gate": "evidence", "progress_visibility": "trace"},
            "recovery": {"checkpoint_store": "temp", "cancel_signal": "none", "rollback_rule": "stop"},
        }
        with tempfile.TemporaryDirectory() as directory:
            trace_path = Path(directory) / "trace.jsonl"
            host = ReferenceHost(
                profile,
                DeterministicProvider(text="safe"),
                trace_path,
                Path(directory) / "checkpoint.json",
                trace_adapter=NormalizedTraceAdapter(provider="deterministic", model_ref="fixture-model"),
            )
            result = host.run("read-only task", completion_evidence=["fixture:test"])
            self.assertTrue(result["completed"])
            events = [json.loads(line) for line in trace_path.read_text().splitlines()]
            decision = next(event for event in events if event["event_type"] == "decision_proposed")
            normalized = decision["payload"]["normalized_trace"]
            self.assertEqual(normalized["provider"], "deterministic")
            self.assertEqual(decision["redaction"], normalized["redactions"])
            self.assertNotIn("safe", json.dumps(normalized))

    def test_host_requires_successful_outcome_verification(self):
        profile = {
            "run_id": "run-verified",
            "mode": "focused",
            "model_policy": {"default_route": "test", "escalation_rule": "never", "fallback_rule": "stop"},
            "tool_policy": {"allowed": [], "approval_required": [], "sandbox": True, "cleanup": "remove-temp"},
            "budgets": {"max_model_calls": 1, "max_tool_calls": 0, "max_minutes": 1, "max_retries": 0},
            "privacy": {"data_class": "test", "retention": "temporary", "provider_consent": True},
            "delivery": {"first_slice_target": "response", "completion_gate": "verifier", "progress_visibility": "trace"},
            "recovery": {"checkpoint_store": "temp", "cancel_signal": "none", "rollback_rule": "stop"},
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "artifact.txt"
            artifact.write_text("verified")
            digest = hashlib.sha256(b"verified").hexdigest()
            host = ReferenceHost(
                profile,
                DeterministicProvider(text="claim"),
                root / "trace.jsonl",
                root / "checkpoint.json",
                outcome_verifier=FileStateVerifier(root, {"artifact.txt": digest}),
            )
            result = host.run("create artifact", completion_evidence=[])
            self.assertTrue(result["completed"])
            self.assertTrue(any(ref.startswith("file:artifact.txt:sha256:") for ref in result["evidence_refs"]))
            failed_host = ReferenceHost(
                {**profile, "run_id": "run-unverified"},
                DeterministicProvider(text="claim"),
                root / "failed-trace.jsonl",
                root / "failed-checkpoint.json",
                outcome_verifier=FileStateVerifier(root, {"artifact.txt": "0" * 64}),
            )
            failed = failed_host.run("create artifact", completion_evidence=[])
            self.assertFalse(failed["completed"])
            self.assertEqual(failed["outcome_status"], "failure")


if __name__ == "__main__":
    unittest.main()
