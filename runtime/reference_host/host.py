"""Small executable reference host for the Ai-skills runtime contracts.

This module intentionally uses only the Python standard library. It provides
portable seams for hosted providers and tools without claiming to be a full
production agent framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol

from .risk_controls import (
    ActionIntent,
    ActionJournal,
    ApprovalRecord,
    CancellationSignal,
    TrustEnvelope,
    parse_approval,
)
import hashlib
import json
import os
import tempfile
import time
import uuid


RISK_CLASSES = {"read_only", "reversible", "consequential", "irreversible", "unknown"}


class HostError(RuntimeError):
    """Base error for reference-host failures."""


class PolicyError(HostError):
    """Raised when a tool or action violates the run policy."""


class ApprovalRequired(HostError):
    """Raised when an action needs a human decision before execution."""


class BudgetExceeded(HostError):
    """Raised before a call would exceed the configured run budget."""


class CheckpointError(HostError):
    """Raised when a checkpoint is malformed or belongs to another run."""


@dataclass(frozen=True)
class ProviderRequest:
    run_id: str
    task: str
    context: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ProviderResponse:
    text: str
    usage: Mapping[str, Any] = field(default_factory=dict)
    tool_request: Mapping[str, Any] | None = None


class ProviderAdapter(Protocol):
    def complete(self, request: ProviderRequest) -> ProviderResponse:
        """Return a normalized response from any hosted model provider."""


class DeterministicProvider:
    """Offline provider used for tests and examples.

    ``tool_request`` is optional and lets tests exercise the approval path
    without network access or real credentials.
    """

    def __init__(self, text: str = "deterministic response", tool_request: Mapping[str, Any] | None = None):
        self.text = text
        self.tool_request = tool_request
        self.calls = 0

    def complete(self, request: ProviderRequest) -> ProviderResponse:
        self.calls += 1
        return ProviderResponse(
            text=self.text,
            usage={"provider": "deterministic", "model_calls": 1},
            tool_request=self.tool_request,
        )


class CallableProvider:
    """Adapter for callers that already own a hosted-provider client."""

    def __init__(self, function: Callable[[ProviderRequest], ProviderResponse]):
        self.function = function
        self.calls = 0

    def complete(self, request: ProviderRequest) -> ProviderResponse:
        self.calls += 1
        response = self.function(request)
        if not isinstance(response, ProviderResponse):
            raise TypeError("provider function must return ProviderResponse")
        return response


@dataclass
class ToolSpec:
    name: str
    permission: str
    risk_class: str
    handler: Callable[[Mapping[str, Any]], Any]
    requires_approval: bool = False
    description: str = ""
    argument_validator: Callable[[Mapping[str, Any]], bool] | None = None
    data_scope: str = "unspecified"
    destination_allowlist: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.risk_class not in RISK_CLASSES:
            raise ValueError(f"unsupported risk class: {self.risk_class}")
        if not self.name or not self.permission:
            raise ValueError("tool name and permission are required")


class TraceWriter:
    """Append schema-shaped JSONL events with monotonic sequence numbers."""

    def __init__(self, path: str | os.PathLike[str], run_id: str):
        self.path = Path(path)
        self.run_id = run_id
        self.sequence = 0
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def emit(
        self,
        actor: str,
        event_type: str,
        risk_class: str,
        payload: Mapping[str, Any] | None = None,
        evidence_refs: list[str] | None = None,
        approval_ref: str | None = None,
        idempotency_key: str | None = None,
        state_hash: str | None = None,
    ) -> dict[str, Any]:
        if risk_class not in RISK_CLASSES:
            raise ValueError(f"unsupported risk class: {risk_class}")
        event = {
            "schema_version": "1.0",
            "run_id": self.run_id,
            "parent_run_id": None,
            "sequence": self.sequence,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "actor": actor,
            "event_type": event_type,
            "risk_class": risk_class,
            "payload": dict(payload or {}),
            "evidence_refs": list(evidence_refs or []),
            "approval_ref": approval_ref,
            "idempotency_key": idempotency_key,
            "state_hash": state_hash,
            "redaction": [],
        }
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, sort_keys=True) + "\n")
        self.sequence += 1
        return event


class CheckpointStore:
    """Atomic JSON checkpoint store with run-identity and integrity checks."""

    def __init__(self, path: str | os.PathLike[str]):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _hash(state: Mapping[str, Any]) -> str:
        encoded = json.dumps(state, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def save(self, run_id: str, state: Mapping[str, Any]) -> str:
        state_copy = json.loads(json.dumps(state))
        state_hash = self._hash(state_copy)
        document = {"run_id": run_id, "state": state_copy, "state_hash": state_hash}
        fd, temporary = tempfile.mkstemp(prefix="checkpoint-", dir=str(self.path.parent))
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(document, handle, sort_keys=True)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self.path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
        return state_hash

    def load(self, run_id: str) -> dict[str, Any]:
        if not self.path.exists():
            raise CheckpointError("checkpoint does not exist")
        try:
            document = json.loads(self.path.read_text(encoding="utf-8"))
            state = document["state"]
            if document["run_id"] != run_id:
                raise CheckpointError("checkpoint belongs to another run")
            if document["state_hash"] != self._hash(state):
                raise CheckpointError("checkpoint integrity check failed")
            return state
        except (KeyError, TypeError, json.JSONDecodeError) as exc:
            raise CheckpointError("malformed checkpoint") from exc


class BudgetGuard:
    def __init__(self, budgets: Mapping[str, Any]):
        self.budgets = dict(budgets)
        self.model_calls = 0
        self.tool_calls = 0
        self.retries = 0
        self.started = time.monotonic()

    def _check_time(self) -> None:
        maximum = float(self.budgets["max_minutes"])
        if time.monotonic() - self.started > maximum * 60:
            raise BudgetExceeded("time budget exceeded")

    def model_call(self) -> None:
        self._check_time()
        if self.model_calls >= int(self.budgets["max_model_calls"]):
            raise BudgetExceeded("model-call budget exceeded")
        self.model_calls += 1

    def tool_call(self) -> None:
        self._check_time()
        if self.tool_calls >= int(self.budgets["max_tool_calls"]):
            raise BudgetExceeded("tool-call budget exceeded")
        self.tool_calls += 1

    def retry(self) -> None:
        self._check_time()
        if self.retries >= int(self.budgets["max_retries"]):
            raise BudgetExceeded("retry budget exceeded")
        self.retries += 1


class ReferenceHost:
    """Minimal host that enforces the most important Ai-skills contracts."""

    def __init__(
        self,
        profile: Mapping[str, Any],
        provider: ProviderAdapter,
        trace_path: str | os.PathLike[str],
        checkpoint_path: str | os.PathLike[str],
        tools: Mapping[str, ToolSpec] | None = None,
        approvals: Mapping[str, Any] | None = None,
        cancel_path: str | os.PathLike[str] | None = None,
        journal_path: str | os.PathLike[str] | None = None,
    ):
        self.profile = self._validate_profile(profile)
        self.provider = provider
        self.trace = TraceWriter(trace_path, self.profile["run_id"])
        self.checkpoints = CheckpointStore(checkpoint_path)
        self.tools = dict(tools or {})
        self.approvals = dict(approvals or {})
        self.budget = BudgetGuard(self.profile["budgets"])
        configured_cancel = self.profile["recovery"].get("cancel_signal")
        self.cancel_signal = CancellationSignal(cancel_path or (configured_cancel if isinstance(configured_cancel, str) and configured_cancel.startswith("/") else None))
        self.journal = ActionJournal(journal_path) if journal_path else None

    @staticmethod
    def _validate_profile(profile: Mapping[str, Any]) -> dict[str, Any]:
        required = ["run_id", "mode", "model_policy", "tool_policy", "budgets", "privacy", "delivery", "recovery"]
        missing = [key for key in required if key not in profile]
        if missing:
            raise ValueError(f"profile missing required keys: {', '.join(missing)}")
        if not profile["run_id"]:
            raise ValueError("run_id must be non-empty")
        for key in ("max_model_calls", "max_tool_calls", "max_minutes", "max_retries"):
            if key not in profile["budgets"]:
                raise ValueError(f"budget missing {key}")
        return json.loads(json.dumps(profile))

    def _check_cancel(self) -> None:
        if self.cancel_signal.requested:
            raise HostError("cancellation requested")

    def _checkpoint(self, state: Mapping[str, Any]) -> str:
        state_hash = self.checkpoints.save(self.profile["run_id"], state)
        self.trace.emit("system", "checkpoint_saved", "read_only", {"state_keys": sorted(state.keys())}, state_hash=state_hash)
        return state_hash

    def _execute_tool(self, request: Mapping[str, Any], task: str) -> tuple[str, Any]:
        name = str(request.get("name", ""))
        arguments = request.get("arguments", {})
        if not isinstance(arguments, Mapping):
            raise PolicyError("tool arguments must be an object")
        self._check_cancel()
        spec = self.tools.get(name)
        if spec is None:
            raise PolicyError(f"tool is not registered: {name}")
        policy = self.profile["tool_policy"]
        allowed = set(policy["allowed"])
        if name not in allowed and spec.permission not in allowed:
            raise PolicyError(f"tool is not allowed by profile: {name}")
        if spec.argument_validator is not None and not spec.argument_validator(arguments):
            raise PolicyError(f"tool arguments failed validation: {name}")
        destination = str(arguments.get("destination", ""))
        if spec.destination_allowlist and destination and destination not in set(spec.destination_allowlist):
            raise PolicyError(f"tool destination is not allowed: {destination}")
        self.budget.tool_call()
        action = ActionIntent(
            run_id=self.profile["run_id"], intent=task, tool=name,
            target=destination or name, scope=spec.data_scope,
            risk_class=spec.risk_class, reversible=spec.risk_class in {"read_only", "reversible"},
            permission=spec.permission, expected_evidence=(f"tool:{name}",),
            rollback=self.profile["recovery"].get("rollback_rule", "stop"),
            idempotency_key=f"{self.profile['run_id']}:{name}:{self.budget.tool_calls}",
        )
        if self.journal:
            self.journal.append({"kind": "intent", "action_hash": action.action_hash, **action.to_dict()})
        approval_needed = (
            name in policy["approval_required"]
            or spec.requires_approval
            or spec.risk_class in {"consequential", "irreversible", "unknown"}
        )
        if approval_needed:
            approval_ref = f"approval-{uuid.uuid4().hex}"
            self.trace.emit("system", "approval_requested", spec.risk_class, {"tool": name}, approval_ref=approval_ref)
            decision = parse_approval(self.approvals.get(name))
            if decision is None or decision.action_hash != action.action_hash or decision.expired:
                raise ApprovalRequired(f"valid, unexpired approval required for tool: {name}")
            if not decision.approved:
                self.trace.emit("system", "approval_rejected", spec.risk_class, {"tool": name}, approval_ref=approval_ref)
                raise PolicyError(f"approval rejected for tool: {name}")
            self.trace.emit("system", "approval_received", spec.risk_class, {"tool": name, "approver": decision.approver}, approval_ref=approval_ref)
        self.trace.emit("tool", "tool_started", spec.risk_class, {"tool": name})
        try:
            result = spec.handler(arguments)
        except Exception as exc:  # pragma: no cover - exact exception is preserved in trace only
            self.trace.emit("tool", "tool_failed", spec.risk_class, {"tool": name, "error_type": type(exc).__name__})
            raise HostError(f"tool failed: {name}") from exc
        self.trace.emit("tool", "tool_completed", spec.risk_class, {"tool": name, "action_hash": action.action_hash})
        if self.journal:
            self.journal.append({"kind": "result", "action_hash": action.action_hash, "tool": name, "status": "completed"})
        return name, result

    def run(
        self,
        task: str,
        context: Mapping[str, Any] | None = None,
        completion_evidence: list[str] | None = None,
    ) -> dict[str, Any]:
        if not task.strip():
            raise ValueError("task must be non-empty")
        context = dict(context or {})
        if self.cancel_signal.requested:
            self.trace.emit("system", "run_stopped", "read_only", {"reason": "cancellation requested"})
            return {"run_id": self.profile["run_id"], "status": "cancelled", "completed": False, "reason": "cancellation requested"}
        self.trace.emit("system", "run_started", "read_only", {"mode": self.profile["mode"]})
        self.trace.emit("agent", "context_acquired", "read_only", {"context_keys": sorted(context.keys())})
        state: dict[str, Any] = {"task": task, "context": context, "status": "running"}
        try:
            self.budget.model_call()
            response = self.provider.complete(ProviderRequest(self.profile["run_id"], task, context))
            state["response"] = {"text": response.text, "usage": dict(response.usage)}
            self.trace.emit("agent", "decision_proposed", "read_only", {"has_tool_request": response.tool_request is not None})
            if response.tool_request is not None:
                try:
                    name, result = self._execute_tool(response.tool_request, task)
                    state["tool_result"] = {"tool": name, "result": result}
                except ApprovalRequired as exc:
                    state["status"] = "waiting_approval"
                    self._checkpoint(state)
                    self.trace.emit("system", "run_paused", "consequential", {"reason": str(exc)})
                    return {"run_id": self.profile["run_id"], "status": state["status"], "completed": False, "text": response.text}
                except (PolicyError, BudgetExceeded, HostError) as exc:
                    state["status"] = "stopped"
                    self._checkpoint(state)
                    self.trace.emit("system", "run_stopped", "unknown", {"reason": str(exc)})
                    return {"run_id": self.profile["run_id"], "status": state["status"], "completed": False, "text": response.text}
            evidence = list(completion_evidence or [])
            if not evidence:
                state["status"] = "stopped"
                self._checkpoint(state)
                self.trace.emit("system", "run_stopped", "read_only", {"reason": "completion_evidence_required"})
                return {"run_id": self.profile["run_id"], "status": state["status"], "completed": False, "text": response.text}
            state["evidence_refs"] = evidence
            state["status"] = "completed"
            state_hash = self._checkpoint(state)
            self.trace.emit("reviewer", "verification_completed", "read_only", {"evidence_count": len(evidence)}, evidence_refs=evidence, state_hash=state_hash)
            self.trace.emit("system", "run_completed", "read_only", {"evidence_count": len(evidence)}, evidence_refs=evidence, state_hash=state_hash)
            return {"run_id": self.profile["run_id"], "status": state["status"], "completed": True, "text": response.text, "evidence_refs": evidence}
        except HostError as exc:
            state["status"] = "cancelled" if "cancellation" in str(exc) else "stopped"
            self._checkpoint(state)
            self.trace.emit("system", "run_stopped", "read_only", {"reason": str(exc)})
            return {"run_id": self.profile["run_id"], "status": state["status"], "completed": False, "reason": str(exc)}
        except BudgetExceeded as exc:
            state["status"] = "stopped"
            self._checkpoint(state)
            self.trace.emit("system", "run_stopped", "read_only", {"reason": str(exc)})
            return {"run_id": self.profile["run_id"], "status": state["status"], "completed": False, "reason": str(exc)}


__all__ = [
    "ApprovalRequired",
    "BudgetExceeded",
    "CallableProvider",
    "CheckpointError",
    "CheckpointStore",
    "DeterministicProvider",
    "HostError",
    "PolicyError",
    "ProviderRequest",
    "ProviderResponse",
    "ReferenceHost",
    "ToolSpec",
    "TraceWriter",
]
