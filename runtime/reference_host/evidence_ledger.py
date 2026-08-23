"""Small provider-neutral evidence-ledger primitives for the reference host.

The adapter validates ledger structure and preserves claim-to-source relations.
It is intentionally reference-grade and does not claim cryptographic truth.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping

CLAIM_TYPES = {"fact", "definition", "measurement", "interpretation", "hypothesis", "unknown"}
SOURCE_TIERS = {"A", "B", "C", "D", "E"}
STATUSES = {"unverified", "supported", "strong", "contradicted", "outdated", "conflicting"}
CONFIDENCES = {"low", "medium", "high"}
FRESHNESS = {"live", "fast_changing", "active_policy", "research", "stable", "unknown"}


@dataclass(frozen=True)
class EvidenceRecord:
    evidence_id: str
    claim_id: str
    claim_type: str
    claim: str
    source_ref: str
    support_status: str
    confidence: str
    scope: str
    source_tier: str | None = None
    evidence_span: str = ""
    retrieval_activity: str = ""
    transformation_refs: tuple[str, ...] = ()
    derived_from: tuple[str, ...] = ()
    corroboration_refs: tuple[str, ...] = ()
    contradiction_refs: tuple[str, ...] = ()
    independence_group: str = ""
    published_at: str | None = None
    updated_at: str | None = None
    accessed_at: str | None = None
    freshness_class: str = "unknown"
    verification_refs: tuple[str, ...] = ()
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.evidence_id or not self.claim_id or not self.claim or not self.source_ref or not self.scope:
            raise ValueError("evidence_id, claim_id, claim, source_ref, and scope are required")
        if self.claim_type not in CLAIM_TYPES:
            raise ValueError(f"unsupported claim_type: {self.claim_type}")
        if self.source_tier is not None and self.source_tier not in SOURCE_TIERS:
            raise ValueError(f"unsupported source_tier: {self.source_tier}")
        if self.support_status not in STATUSES:
            raise ValueError(f"unsupported support_status: {self.support_status}")
        if self.confidence not in CONFIDENCES:
            raise ValueError(f"unsupported confidence: {self.confidence}")
        if self.freshness_class not in FRESHNESS:
            raise ValueError(f"unsupported freshness_class: {self.freshness_class}")
        if self.support_status in {"supported", "strong"} and not self.evidence_span:
            raise ValueError("supported evidence requires an evidence_span")
        if self.confidence == "high" and self.support_status in {"unverified", "conflicting"}:
            raise ValueError("high confidence is incompatible with unverified or conflicting status")

    def to_dict(self) -> dict[str, Any]:
        record = asdict(self)
        for key in ("transformation_refs", "derived_from", "corroboration_refs", "contradiction_refs", "verification_refs"):
            record[key] = list(record[key])
        return record


@dataclass
class EvidenceLedger:
    ledger_id: str
    run_id: str
    records: list[EvidenceRecord] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def add(self, record: EvidenceRecord) -> None:
        if any(existing.evidence_id == record.evidence_id for existing in self.records):
            raise ValueError(f"duplicate evidence_id: {record.evidence_id}")
        self.records.append(record)

    def claims(self) -> set[str]:
        return {record.claim_id for record in self.records}

    def validate_links(self) -> None:
        evidence_ids = {record.evidence_id for record in self.records}
        for record in self.records:
            links = (*record.transformation_refs, *record.derived_from, *record.corroboration_refs, *record.contradiction_refs, *record.verification_refs)
            missing = sorted(ref for ref in links if ref.startswith("evidence:") and ref.removeprefix("evidence:") not in evidence_ids)
            if missing:
                raise ValueError(f"missing evidence links for {record.evidence_id}: {missing}")

    def to_dict(self) -> dict[str, Any]:
        self.validate_links()
        return {
            "schema_version": "1.0",
            "ledger_id": self.ledger_id,
            "run_id": self.run_id,
            "created_at": self.created_at,
            "records": [record.to_dict() for record in self.records],
        }


def validate_ledger(payload: Mapping[str, Any]) -> EvidenceLedger:
    if payload.get("schema_version") != "1.0":
        raise ValueError("unsupported or missing evidence ledger schema_version")
    ledger = EvidenceLedger(str(payload.get("ledger_id", "")), str(payload.get("run_id", "")), created_at=str(payload.get("created_at", "")))
    if not ledger.ledger_id or not ledger.run_id:
        raise ValueError("ledger_id and run_id are required")
    for raw in payload.get("records", []):
        values = dict(raw)
        for key in ("transformation_refs", "derived_from", "corroboration_refs", "contradiction_refs", "verification_refs"):
            values[key] = tuple(values.get(key, []))
        ledger.add(EvidenceRecord(**values))
    ledger.validate_links()
    return ledger
