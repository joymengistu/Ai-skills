"""Environment-grounded outcome verification for the reference host."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Mapping, Protocol, Any


@dataclass(frozen=True)
class VerificationResult:
    status: str
    evidence_refs: tuple[str, ...] = ()
    details: Mapping[str, Any] | None = None

    def __post_init__(self) -> None:
        if self.status not in {"success", "partial", "failure", "unknown"}:
            raise ValueError(f"unsupported verification status: {self.status}")


class OutcomeVerifier(Protocol):
    def verify(self, task: str, state: Mapping[str, Any]) -> VerificationResult:
        """Inspect external state or artifacts without authorizing side effects."""


class FileStateVerifier:
    """Verify expected files under one confined, read-only root directory.

    ``expected_sha256`` maps relative paths to expected hexadecimal SHA-256
    digests. An empty expected digest means that existence is sufficient. The
    verifier never follows a path outside ``root`` and never writes files.
    """

    def __init__(self, root: str | Path, expected_sha256: Mapping[str, str]):
        self.root = Path(root).resolve()
        self.expected_sha256 = dict(expected_sha256)
        if not self.expected_sha256:
            raise ValueError("at least one expected file is required")
        for relative, digest in self.expected_sha256.items():
            if Path(relative).is_absolute() or ".." in Path(relative).parts:
                raise ValueError(f"expected file escapes verifier root: {relative}")
            if digest and (len(digest) != 64 or any(character not in "0123456789abcdef" for character in digest.lower())):
                raise ValueError(f"invalid sha256 digest for {relative}")

    def _safe_path(self, relative: str) -> Path:
        candidate = (self.root / relative).resolve()
        if candidate != self.root and self.root not in candidate.parents:
            raise ValueError(f"path escapes verifier root: {relative}")
        return candidate

    @staticmethod
    def _sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def verify(self, task: str, state: Mapping[str, Any]) -> VerificationResult:
        del task, state
        evidence: list[str] = []
        failures: list[str] = []
        for relative, expected in sorted(self.expected_sha256.items()):
            path = self._safe_path(relative)
            if not path.is_file():
                failures.append(f"missing:{relative}")
                continue
            actual = self._sha256(path)
            evidence.append(f"file:{relative}:sha256:{actual}")
            if expected and actual != expected.lower():
                failures.append(f"hash_mismatch:{relative}")
        if failures:
            return VerificationResult("failure", tuple(evidence), {"failures": failures})
        return VerificationResult("success", tuple(evidence), {"verified_files": sorted(self.expected_sha256)})


class CallableOutcomeVerifier:
    """Wrap a pure verifier function supplied by the host application."""

    def __init__(self, function):
        self.function = function

    def verify(self, task: str, state: Mapping[str, Any]) -> VerificationResult:
        result = self.function(task, state)
        if not isinstance(result, VerificationResult):
            raise TypeError("outcome verifier function must return VerificationResult")
        return result


__all__ = ["CallableOutcomeVerifier", "FileStateVerifier", "OutcomeVerifier", "VerificationResult"]
