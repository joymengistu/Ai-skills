# Source Hierarchy, Freshness, and Independence Policy

Use this policy whenever the agent researches a factual, technical, product, policy, or comparative question. A citation is an address to evidence, not a guarantee that the claim is true. Source selection, retrieval time, version, scope, contradiction status, and transformation history must remain visible.

## Why this policy exists

The W3C PROV model treats provenance as information about entities, activities, and responsible agents that can support assessments of quality, reliability, and trustworthiness.[1] GO FAIR guidance emphasizes persistent identifiers, rich metadata, qualified references, standardized retrieval, access controls where needed, and detailed provenance for reusable data.[2] NIST frames trustworthiness as a lifecycle concern across the design, development, use, and evaluation of AI systems.[3] Recent agent-provenance research argues that final-answer correctness alone does not reveal which evidence, tools, memory, or execution steps shaped a result.[4]

These sources support a design direction, not a measured claim that this repository or any model is automatically more accurate. The implementation must still be evaluated on representative tasks.

## Source tiers

| Tier | Typical source | Use | Required caution |
|---|---|---|---|
| **A — Primary authoritative** | Standards body, government publication, official specification, original dataset, original paper, first-party source for its own product | Definitions, requirements, current first-party facts, normative claims | Authority is scoped; a primary source can still be incomplete, biased, outdated, or promotional |
| **B — Direct technical evidence** | Reproducible experiment, maintained project documentation, source code, benchmark artifact, release note, official issue or changelog | Implementation behavior, measured results, version-specific claims | Check version, environment, test method, and whether the result generalizes |
| **C — Scholarly synthesis** | Systematic review, survey, peer-reviewed synthesis, methods paper | Research landscape, competing findings, conceptual frameworks | Check inclusion criteria, publication status, date, and whether claims are direct or summarized |
| **D — High-quality secondary analysis** | Expert analysis, reputable technical reporting, transparent engineering postmortem | Context, discovery, triangulation, observable product behavior | Never let a secondary summary outrank the underlying source when the original is available |
| **E — Discovery-only** | Search snippets, unsourced posts, social media, anonymous claims, marketing copy, forum comments | Leads, hypotheses, terminology, candidate links | Do not use alone as support for a material repository claim |

A source tier is one dimension of evidence quality. Relevance, method, specificity, date, completeness, independence, and contradiction status must also be recorded.

## Claim-to-source matching

Match the source to the claim’s scope. Use a standard for a standards definition, a first-party release note for version behavior, a primary study for its reported result, and a measured local test for a repository-specific behavior. Do not use an impressive source to support a different claim merely because the topics overlap.

For a material or contested claim, prefer two or more independent evidence paths. Independence means more than different URLs: check whether sources share the same original report, author, organization, dataset, benchmark, press release, or unverified assertion. Correlated copies count as one evidence family.

## Freshness policy

Record both `published_at` or `updated_at` and `accessed_at`. Freshness is claim-relative rather than a universal expiration timer.

| Claim class | Default review window | Freshness action |
|---|---:|---|
| Live operational state, current price, availability, security issue, or breaking event | Minutes to days | Re-fetch immediately before acting or reporting; use no-cache retrieval when stale data could harm the decision |
| API, library, model, platform, or product behavior | 30–90 days or each relevant release | Pin version and environment; prefer current official documentation and a local reproduction |
| Active policy, regulation, standards draft, or public roadmap | 1–6 months or on announced revision | Check the current publication and status; distinguish draft from final |
| Research findings and surveys | 6–24 months, or sooner for fast-moving fields | Preserve publication/version date; search for later replication, correction, or contradiction |
| Stable historical facts or established definitions | Review on contradiction or source revision | Keep original date and source version; do not invent decay merely because a fact is old |

These windows are operating defaults, not evidence-based laws. The agent must shorten them when the cost of stale information is high and lengthen them only with a recorded rationale.

## Research record

Every material claim should be representable as:

```yaml
research_record:
  claim_id: "claim-001"
  claim: "A scoped factual statement"
  claim_type: fact|definition|measurement|interpretation|hypothesis|unknown
  source:
    source_id: "source-001"
    tier: A|B|C|D|E
    publisher_or_author: "...
    title: "..."
    url: "https://..."
    published_at: "YYYY-MM-DD or unknown"
    updated_at: "YYYY-MM-DD or unknown"
    accessed_at: "YYYY-MM-DD"
    version_or_revision: "..."
    evidence_span: "Page, section, quote, table, or test output"
  scope: "What the source actually supports"
  freshness_class: live|fast_changing|active_policy|research|stable
  independence_group: "Original source family identifier"
  retrieval_activity: "How it was found and obtained"
  transformations: []
  corroboration: []
  contradictions: []
  confidence: low|medium|high
  status: unverified|supported|strong|contradicted|outdated|conflicting
  license_or_access_notes: "..."
  next_check: "Date or trigger"
```

When an agent summarizes, translates, extracts, or combines sources, record the transformation and retain the original evidence span. This follows the provenance principle that generated entities should remain connected to the activities and agents that produced them.[1] Keep source records accessible even when the underlying content later becomes unavailable, consistent with FAIR’s metadata emphasis.[2]

## Independence and contradiction workflow

1. Identify the exact claim and the strongest available primary source.
2. Search for independent corroboration, replication, later revisions, and credible contradiction.
3. Group copied or derivative reports by original source family.
4. Record disagreements without averaging them away. Compare scope, method, date, population, environment, and definitions.
5. Downgrade confidence when sources conflict or the evidence is indirect.
6. State what additional evidence would resolve the conflict.

Do not count the number of citations as a substitute for evidential diversity. Five pages repeating one press release are not five independent confirmations.

## Reporting contract

For important findings, report the claim, evidence tier, source scope, access date, confidence, freshness, corroboration or contradiction, and unresolved limitation. Use `FACT`, `EVIDENCE`, `INFERENCE`, `HYPOTHESIS`, and `UNKNOWN` labels when the boundaries could otherwise be misunderstood.

## Boundaries

This policy does not prove truth, eliminate source bias, replace domain expertise, or create live access to unavailable sources. It cannot make a model’s memory authoritative. A source can be high-tier yet wrong for the current question, and a low-tier source can reveal a lead that later becomes useful primary evidence.

## References

[1]: https://www.w3.org/TR/prov-dm/ "W3C PROV-DM: The PROV Data Model"
[2]: https://www.go-fair.org/fair-principles/ "GO FAIR Principles"
[3]: https://www.nist.gov/itl/ai-risk-management-framework "NIST AI Risk Management Framework"
[4]: https://arxiv.org/html/2606.04990v4 "From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents"
