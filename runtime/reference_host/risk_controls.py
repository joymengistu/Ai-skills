"""Model-agnostic safety primitives used by the reference host.

These controls reduce blast radius; they do not prove that a model is aligned
or that prompt injection has been detected perfectly.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping
import hashlib
import json
import os
import tempfile
import uuid


TRUST_LEVELS = {"trusted", "known", "untrusted", "unknown"}


@dataclass(frozen=True)
class TrustEnvelope:
    origin: str
    trust_level: str
    content_kind: str
    source_id: str
    received_at: str
    allowed_effects: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.trust_level not in TRUST_LEVELS:
            raise ValueError(f"unsupported trust level: {self.trust_level}")
        if not self.origin or not self.source_id:
            raise ValueError("origin and source_id are required")

    @property
    def authoritative(self) -> bool:
        return self.trust_level == "trusted" and "authorize" in self.allowed_effects

    def to_dict(self) -> dict[str, Any]:
        return asdict(self) | {"allowed_effects": list(self.allowed_effects), "authoritative": self.authoritative}


@dataclass(frozen=True)
class ActionIntent:
    run_id: str
    intent: str
    tool: str
    target: str
    scope: str
    risk_class: str
    reversible: bool
    permission: str
    expected_evidence: tuple[str, ...]
    rollback: str
    idempotency_key: str
    state_version: str = "1"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self) | {"expected_evidence": list(self.expected_evidence)}

    @property
    def action_hash(self) -> str:
        encoded = json.dumps(self.to_dict(), sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True)
class ApprovalRecord:
    action_hash: str
    approved: bool
    approver: str
    expires_at: str
    approval_id: str = ""

    def __post_init__(self) -> None:
        if not self.action_hash or not self.approver or not self.expires_at:
            raise ValueError("approval requires action_hash, approver, and expires_at")

    @property
    def expired(self) -> bool:
        try:
            expiry = datetime.fromisoformat(self.expires_at.replace("Z", "+00:00"))
            return datetime.now(timezone.utc) >= expiry
        except ValueError:
            return True

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["approval_id"] = self.approval_id or f"approval-{uuid.uuid4().hex}"
        return value


class CancellationSignal:
    """File-backed kill switch suitable for a local reference host."""

    def __init__(self, path: str | os.PathLike[str] | None):
        self.path = Path(path) if path else None

    @property
    def requested(self) -> bool:
        return bool(self.path and self.path.exists())


class ActionJournal:
    """Append action intents/results without deleting prior evidence."""

    def __init__(self, path: str | os.PathLike[str]):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _last_hash(self) -> str | None:
        if not self.path.exists() or not self.path.read_text(encoding="utf-8").strip():
            return None
        return self.verify()

    def verify(self) -> str | None:
        """Verify every record and return the final hash."""
        if not self.path.exists():
            return None
        previous = None
        for line in self.path.read_text(encoding="utf-8").splitlines():
            try:
                record = json.loads(line)
                if record.get("previous_hash") != previous:
                    raise ValueError("action journal chain is broken")
                recorded_hash = str(record.pop("record_hash"))
                encoded = json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8")
                if hashlib.sha256(encoded).hexdigest() != recorded_hash:
                    raise ValueError("action journal is malformed or tampered")
                previous = recorded_hash
            except (KeyError, TypeError, json.JSONDecodeError):
                raise ValueError("action journal is malformed or tampered")
        return previous

    def append(self, record: Mapping[str, Any]) -> None:
        body = dict(record)
        body["previous_hash"] = self._last_hash()
        encoded = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
        body["record_hash"] = hashlib.sha256(encoded).hexdigest()
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(body, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())


class RedactedIncidentJournal(ActionJournal):
    """Small journal that stores safe metadata, never arbitrary secret payloads."""

    SAFE_KEYS = {"incident_id", "category", "run_id", "action_hash", "cause", "status", "evidence_refs", "uncertainty"}

    def append_incident(self, record: Mapping[str, Any]) -> None:
        safe = {key: value for key, value in record.items() if key in self.SAFE_KEYS}
        safe.setdefault("incident_id", f"incident-{uuid.uuid4().hex}")
        safe.setdefault("status", "open")
        self.append(safe)


def parse_approval(value: Any) -> ApprovalRecord | None:
    if isinstance(value, ApprovalRecord):
        return value
    if not isinstance(value, Mapping):
        return None
    try:
        return ApprovalRecord(
            action_hash=str(value["action_hash"]),
            approved=bool(value["approved"]),
            approver=str(value["approver"]),
            expires_at=str(value["expires_at"]),
            approval_id=str(value.get("approval_id", "")),
        )
    except (KeyError, TypeError, ValueError):
        return None


__all__ = ["ActionIntent", "ActionJournal", "ApprovalRecord", "CancellationSignal", "RedactedIncidentJournal", "TrustEnvelope", "parse_approval"]
