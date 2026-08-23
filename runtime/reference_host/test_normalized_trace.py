import json
import tempfile
import unittest
from pathlib import Path

from runtime.reference_host.host import DeterministicProvider, NormalizedTraceAdapter, ReferenceHost


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


if __name__ == "__main__":
    unittest.main()
