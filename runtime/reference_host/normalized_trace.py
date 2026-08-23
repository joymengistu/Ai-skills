"""Provider-neutral trace normalization with conservative content handling."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from typing import Any, Mapping


CONTENT_POLICIES = {"redacted_by_default", "metadata_only", "explicitly_captured"}


@dataclass(frozen=True)
class NormalizedTraceAdapter:
    """Normalize a provider response without treating telemetry as authority.

    The adapter emits a compact common core. Raw request/response/tool content
    is never included unless the caller explicitly selects
    ``explicitly_captured``. Provider-specific fields remain extensions and
    are not silently treated as cross-provider comparable.
    """

    provider: str
    model_ref: str = "unknown"
    content_policy: str = "redacted_by_default"

    def __post_init__(self) -> None:
        if not self.provider.strip():
            raise ValueError("provider must be non-empty")
        if not self.model_ref.strip():
            raise ValueError("model_ref must be non-empty")
        if self.content_policy not in CONTENT_POLICIES:
            raise ValueError(f"unsupported content policy: {self.content_policy}")
        if self.content_policy == "explicitly_captured":
            raise ValueError("explicit content capture requires an explicit consent-scoped adapter")

    @staticmethod
    def _digest(value: Any) -> str:
        encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
        return "sha256:" + hashlib.sha256(encoded).hexdigest()

    @staticmethod
    def _int_or_none(value: Any) -> int | None:
        if value is None:
            return None
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            return None
        return parsed if parsed >= 0 else None

    @staticmethod
    def _number_or_none(value: Any) -> float | None:
        if value is None:
            return None
        try:
            parsed = float(value)
        except (TypeError, ValueError):
            return None
        return parsed if parsed >= 0 else None

    def normalize_response(
        self,
        *,
        span_id: str,
        response: Any,
        request_fingerprint: Any,
        parent_span_id: str | None = None,
    ) -> dict[str, Any]:
        if not span_id.strip():
            raise ValueError("span_id must be non-empty")
        usage: Mapping[str, Any] = getattr(response, "usage", {}) or {}
        normalized_usage = {
            "input_tokens": self._int_or_none(usage.get("input_tokens")),
            "output_tokens": self._int_or_none(usage.get("output_tokens")),
            "total_tokens": self._int_or_none(usage.get("total_tokens")),
            "latency_ms": self._number_or_none(usage.get("latency_ms")),
            "retry_count": self._int_or_none(usage.get("retry_count")),
            "finish_reason": usage.get("finish_reason") if isinstance(usage.get("finish_reason"), str) else None,
        }
        tool_request = getattr(response, "tool_request", None)
        record: dict[str, Any] = {
            "event_kind": "tool_call" if tool_request is not None else "llm_generation",
            "provider": self.provider,
            "model_ref": str(usage.get("model", self.model_ref)),
            "span_id": span_id,
            "parent_span_id": parent_span_id,
            "usage": normalized_usage,
            "content_policy": self.content_policy,
            "content_digests": {
                "request": self._digest(request_fingerprint),
                "response": self._digest(getattr(response, "text", "")),
                "tool_request": self._digest(tool_request) if tool_request is not None else None,
            },
            "redactions": ["request_content", "response_content", "tool_arguments"],
            "non_comparable_fields": ["provider_extensions"],
            "provider_extensions": {"usage_keys": sorted(str(key) for key in usage.keys())},
        }
        return record


__all__ = ["CONTENT_POLICIES", "NormalizedTraceAdapter"]
