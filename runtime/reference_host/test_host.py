import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from runtime.reference_host.host import CheckpointError, CheckpointStore, DeterministicProvider, ReferenceHost, ToolSpec
from runtime.reference_host.risk_controls import ActionIntent, ApprovalRecord, CancellationSignal, RedactedIncidentJournal, TrustEnvelope


def profile(run_id="test-run", max_model_calls=1, max_tool_calls=2):
    return {
        "run_id": run_id,
        "mode": "focused",
        "model_policy": {"default_route": "deterministic", "escalation_rule": "never", "fallback_rule": "stop"},
        "tool_policy": {"allowed": ["read_note", "write_note"], "approval_required": ["write_note"], "sandbox": True, "cleanup": "none"},
        "budgets": {"max_model_calls": max_model_calls, "max_tool_calls": max_tool_calls, "max_minutes": 1, "max_retries": 0},
        "privacy": {"data_class": "test", "retention": "temporary", "provider_consent": True},
        "delivery": {"first_slice_target": "response", "completion_gate": "evidence", "progress_visibility": "trace"},
        "recovery": {"checkpoint_store": "file", "cancel_signal": "stop", "rollback_rule": "restore checkpoint"},
    }


class ReferenceHostTests(unittest.TestCase):
    def make_host(self, provider, approvals=None, run_id="test-run"):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        return ReferenceHost(profile(run_id=run_id), provider, root / "trace.jsonl", root / "checkpoint.json", approvals=approvals)

    def tearDown(self):
        if hasattr(self, "temp"):
            self.temp.cleanup()

    def test_output_without_evidence_is_not_completion(self):
        host = self.make_host(DeterministicProvider("answer"))
        result = host.run("Do the task")
        self.assertFalse(result["completed"])
        self.assertEqual(result["status"], "stopped")
        events = [json.loads(line) for line in host.trace.path.read_text().splitlines()]
        self.assertEqual(events[-1]["event_type"], "run_stopped")
        self.assertNotIn("run_completed", [event["event_type"] for event in events])

    def test_evidence_is_required_for_completion(self):
        host = self.make_host(DeterministicProvider("answer"))
        result = host.run("Do the task", completion_evidence=["test:passed"])
        self.assertTrue(result["completed"])
        self.assertEqual(result["status"], "completed")
        events = [json.loads(line) for line in host.trace.path.read_text().splitlines()]
        self.assertEqual([event["sequence"] for event in events], list(range(len(events))))
        self.assertEqual(events[-1]["event_type"], "run_completed")
        self.assertEqual(events[-1]["evidence_refs"], ["test:passed"])

    def test_approval_blocks_side_effect_until_decision(self):
        calls = []
        tool = ToolSpec("write_note", "write:note", "consequential", lambda args: calls.append(args) or "written", requires_approval=True)
        host = self.make_host(DeterministicProvider("answer", {"name": "write_note", "arguments": {"text": "x"}}))
        host.tools["write_note"] = tool
        result = host.run("Write", completion_evidence=["not reached"])
        self.assertFalse(result["completed"])
        self.assertEqual(result["status"], "waiting_approval")
        self.assertEqual(calls, [])
        self.assertIn("approval_requested", host.trace.path.read_text())

    def test_approved_tool_executes(self):
        calls = []
        tool = ToolSpec("write_note", "write:note", "consequential", lambda args: calls.append(args) or "written", requires_approval=True)
        action = ActionIntent(
            run_id="test-run", intent="Write", tool="write_note", target="write_note", scope="unspecified",
            risk_class="consequential", reversible=False, permission="write:note", expected_evidence=("tool:write_note",),
            rollback="restore checkpoint", idempotency_key="test-run:write_note:1",
        )
        approval = ApprovalRecord(action.action_hash, True, "user", (datetime.now(timezone.utc) + timedelta(minutes=5)).isoformat())
        host = self.make_host(DeterministicProvider("answer", {"name": "write_note", "arguments": {"text": "x"}}), approvals={"write_note": approval})
        host.tools["write_note"] = tool
        result = host.run("Write", completion_evidence=["tool:write_note"])
        self.assertTrue(result["completed"])
        self.assertEqual(calls, [{"text": "x"}])

    def test_disallowed_tool_never_executes(self):
        calls = []
        tool = ToolSpec("delete_data", "delete:data", "irreversible", lambda args: calls.append(args))
        host = self.make_host(DeterministicProvider("answer", {"name": "delete_data", "arguments": {}}), approvals={"delete_data": True})
        host.tools["delete_data"] = tool
        result = host.run("Delete", completion_evidence=["not reached"])
        self.assertFalse(result["completed"])
        self.assertEqual(calls, [])
        self.assertEqual(result["status"], "stopped")

    def test_checkpoint_integrity_and_run_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            store = CheckpointStore(Path(directory) / "checkpoint.json")
            store.save("run-a", {"status": "paused"})
            self.assertEqual(store.load("run-a"), {"status": "paused"})
            with self.assertRaises(CheckpointError):
                store.load("run-b")

    def test_cancel_signal_stops_before_provider_call(self):
        with tempfile.TemporaryDirectory() as directory:
            cancel = Path(directory) / "cancel"
            cancel.touch()
            provider = DeterministicProvider("should not run")
            host = self.make_host(provider, run_id="cancel-run")
            host.cancel_signal = CancellationSignal(cancel)
            result = host.run("Stop now", completion_evidence=["not reached"])
            self.assertFalse(result["completed"])
            self.assertEqual(result["status"], "cancelled")
            self.assertEqual(provider.calls, 0)

    def test_tool_argument_and_destination_boundaries(self):
        calls = []
        tool = ToolSpec("send", "send:message", "consequential", lambda args: calls.append(args), requires_approval=False, argument_validator=lambda args: isinstance(args.get("message"), str) and bool(args["message"]), destination_allowlist=("approved.example",))
        host = self.make_host(DeterministicProvider("answer", {"name": "send", "arguments": {"message": "x", "destination": "evil.example"}}))
        host.tools["send"] = tool
        result = host.run("Send", completion_evidence=["not reached"])
        self.assertFalse(result["completed"])
        self.assertEqual(calls, [])

    def test_untrusted_content_cannot_become_authoritative(self):
        envelope = TrustEnvelope("web", "untrusted", "document", "doc-1", datetime.now(timezone.utc).isoformat(), ("inform",))
        self.assertFalse(envelope.authoritative)
        self.assertEqual(envelope.to_dict()["trust_level"], "untrusted")

    def test_action_journal_detects_tampering(self):
        with tempfile.TemporaryDirectory() as directory:
            from runtime.reference_host.risk_controls import ActionJournal
            path = Path(directory) / "actions.jsonl"
            journal = ActionJournal(path)
            journal.append({"kind": "intent", "action_hash": "abc"})
            path.write_text(path.read_text().replace("abc", "tampered"), encoding="utf-8")
            with self.assertRaises(ValueError):
                journal.append({"kind": "result", "action_hash": "abc"})

    def test_incident_journal_redacts_arbitrary_payload(self):
        with tempfile.TemporaryDirectory() as directory:
            journal = RedactedIncidentJournal(Path(directory) / "incidents.jsonl")
            journal.append_incident({"category": "privacy", "run_id": "r", "secret": "do-not-store", "uncertainty": "known"})
            record = json.loads((Path(directory) / "incidents.jsonl").read_text())
            self.assertNotIn("secret", record)
            self.assertEqual(record["category"], "privacy")

    def test_model_budget_is_enforced(self):
        provider = DeterministicProvider("answer")
        host = self.make_host(provider, run_id="budget-run")
        first = host.run("first", completion_evidence=["ok"])
        second = host.run("second", completion_evidence=["ok"])
        self.assertTrue(first["completed"])
        self.assertFalse(second["completed"])
        self.assertEqual(provider.calls, 1)


if __name__ == "__main__":
    unittest.main()
