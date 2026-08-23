import json
import tempfile
import unittest
from pathlib import Path

from host import CheckpointError, CheckpointStore, DeterministicProvider, ReferenceHost, ToolSpec


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
        host = self.make_host(DeterministicProvider("answer", {"name": "write_note", "arguments": {"text": "x"}}), approvals={"write_note": True})
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
