# Citation Cross-Check and Contradiction-Resolution Protocol

Use this protocol when sources disagree, a source is corrected, a later version changes a claim, or evidence supports only part of a conclusion. The goal is not to force consensus; it is to identify whether the disagreement is real, scoped, temporal, definitional, methodological, or caused by transformation.

## Contradiction record

```yaml
contradiction_record:
  contradiction_id: "contradiction-001"
  claim_id: "claim-001"
  source_refs: ["source-a", "source-b"]
  source_families: ["family-a", "family-b"]
  disagreement_type: direct|scope|temporal|definition|method|population|version|transformation|apparent
  evidence_spans: []
  comparison:
    question: "Exact proposition being compared"
    terms: "Definitions and units"
    populations: "Who or what was studied"
    environment: "Version, tool, location, or conditions"
    method: "How evidence was produced"
    dates: "Publication, update, and access dates"
  resolution: prefer_source|scope_claim|split_claim|mark_conflicting|mark_outdated|needs_more_evidence
  rationale: "Short evidence-based explanation"
  affected_records: []
  next_check: "Date, version, or evidence trigger"
```

## Cross-check sequence

1. State the exact claim in a form that could be true or false. Split compound claims before comparing them.
2. Retrieve the underlying sources rather than relying on snippets or copied summaries.
3. Group sources by original source family. Repeated wording, shared data, common press releases, and derivative citations are not independent confirmations.
4. Compare definitions, scope, population, method, environment/version, dates, and transformations before calling the evidence contradictory.
5. Classify the disagreement as direct, scope, temporal, definition, method, population, version, transformation, or apparent.
6. Prefer the source that is more relevant, direct, current for the claim class, methodologically appropriate, and independently corroborated. Source tier informs the decision but never replaces claim-specific judgment.
7. If the disagreement cannot be resolved, preserve both records, set the claim to `conflicting` or `needs_more_evidence`, lower confidence, and state what evidence would resolve it.
8. If a newer version invalidates an older record, mark the old record `outdated` and preserve its history rather than deleting it.
9. Update derived summaries and downstream decisions that depended on the affected claim. Do not let a previously generated conclusion remain silently authoritative.

## Resolution rules

| Situation | Correct handling |
|---|---|
| Sources use different definitions | Split or normalize the claims; do not call them contradictory until terms match |
| Results differ by population, environment, or version | Scope the claims and preserve both results |
| A later authoritative revision corrects an earlier source | Mark the earlier record outdated, retain provenance, and use the newer version for current claims |
| One source is primary and another is a copied summary | Prefer the primary source and record the derivative relationship |
| Methods or data quality differ materially | Explain the method difference and avoid averaging incomparable results |
| Evidence remains genuinely inconsistent | Mark the claim conflicting, lower confidence, and report the unresolved disagreement |

## Reporting contract

A cross-checked result should state: the claim, sources consulted, independent source families, agreement or disagreement type, preferred scope or source when justified, confidence, freshness, and unresolved questions. Never write “research confirms” when only one source, one source family, or indirect evidence supports the statement.

## Anti-patterns

Do not choose the newest source automatically when it is less relevant. Do not choose the highest-tier source automatically when its scope does not match. Do not average incompatible measurements. Do not hide a contradiction behind a long bibliography. Do not delete inconvenient evidence. Do not turn a model-generated summary into an independent source.

## Boundaries

This protocol improves auditability and calibrated reporting; it does not determine truth mechanically. Difficult scientific, medical, legal, financial, or policy disagreements may require domain experts and should not be resolved by the agent alone.
