"""Run a credential-free reference-host demonstration.

Usage:
    python3 -m runtime.reference_host
"""

from pathlib import Path
import tempfile

from .host import DeterministicProvider, ReferenceHost


def main() -> None:
    profile = {
        "run_id": "offline-demo",
        "mode": "focused",
        "model_policy": {"default_route": "deterministic", "escalation_rule": "never", "fallback_rule": "stop"},
        "tool_policy": {"allowed": [], "approval_required": [], "sandbox": True, "cleanup": "temporary"},
        "budgets": {"max_model_calls": 1, "max_tool_calls": 0, "max_minutes": 1, "max_retries": 0},
        "privacy": {"data_class": "demo", "retention": "temporary", "provider_consent": True},
        "delivery": {"first_slice_target": "response", "completion_gate": "evidence", "progress_visibility": "trace"},
        "recovery": {"checkpoint_store": "temporary-file", "cancel_signal": "stop", "rollback_rule": "restore checkpoint"},
    }
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        host = ReferenceHost(profile, DeterministicProvider("offline response"), root / "trace.jsonl", root / "checkpoint.json")
        result = host.run("Demonstrate the reference host", completion_evidence=["demo:deterministic-provider"])
        print(result)
        print(f"trace={root / 'trace.jsonl'}")
        print(f"checkpoint={root / 'checkpoint.json'}")


if __name__ == "__main__":
    main()
