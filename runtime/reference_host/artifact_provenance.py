"""Confined artifact identity and integrity evidence for the reference host."""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import hashlib
from typing import Any, Mapping


@dataclass(frozen=True)
class ArtifactRecord:
    artifact_id: str
    kind: str
    locator: str
    created_by: str
    scope: str
    requirement_refs: tuple[str, ...] = ()
    input_refs: tuple[str, ...] = ()
    source_refs: tuple[str, ...] = ()
    transformation_refs: tuple[str, ...] = ()
    media_type: str = "application/octet-stream"
    retention: str = "host-defined"

    def __post_init__(self) -> None:
        if not self.artifact_id or not self.kind or not self.locator or not self.created_by or not self.scope:
            raise ValueError("artifact_id, kind, locator, created_by, and scope are required")
        if Path(self.locator).is_absolute() or ".." in Path(self.locator).parts:
            raise ValueError("artifact locator must be a confined relative path")

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        for key in ("requirement_refs", "input_refs", "source_refs", "transformation_refs"):
            value[key] = list(value[key])
        return value


class ArtifactIntegrityVerifier:
    """Verify artifact existence and SHA-256 integrity within one read-only root."""

    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()

    def _safe_path(self, locator: str) -> Path:
        candidate = (self.root / locator).resolve()
        if candidate != self.root and self.root not in candidate.parents:
            raise ValueError(f"artifact locator escapes root: {locator}")
        return candidate

    @staticmethod
    def _sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def verify(self, record: ArtifactRecord, expected_sha256: str | None = None) -> Mapping[str, Any]:
        path = self._safe_path(record.locator)
        if not path.is_file():
            return {"artifact_id": record.artifact_id, "status": "failed", "evidence_refs": [], "failures": [f"missing:{record.locator}"]}
        digest = self._sha256(path)
        evidence_ref = f"artifact:{record.artifact_id}:sha256:{digest}"
        failures = []
        if expected_sha256 and digest != expected_sha256.lower():
            failures.append(f"hash_mismatch:{record.locator}")
        return {
            "artifact_id": record.artifact_id,
            "status": "failed" if failures else "verified_integrity",
            "evidence_refs": [evidence_ref],
            "sha256": digest,
            "size_bytes": path.stat().st_size,
            "failures": failures,
            "note": "Integrity evidence does not prove semantic, behavioral, accessibility, or operational correctness.",
        }


__all__ = ["ArtifactIntegrityVerifier", "ArtifactRecord"]
