# Provider adapter boundary

## Purpose

The provider adapter is a **translation seam**, not a model-quality layer. It converts provider-specific responses into a small normalized trace record that the benchmark and evaluator can compare. It must preserve provider-specific extensions without pretending they are cross-provider equivalent.

## Contract

`runtime/normalized-trace.schema.json` defines the common record. The current reference implementation is `runtime/reference_host/normalized_trace.py` and is integrated into `ReferenceHost`.

| Field | Meaning | Comparison rule |
|---|---|---|
| `event_kind` | Generation, tool call, handoff, guardrail, or unknown | Comparable only when the provider event maps confidently |
| `provider` / `model_ref` | Provider and model identity | Must match across baseline/candidate unless the experiment explicitly studies model changes |
| `span_id` / `parent_span_id` | Correlation for one event and its parent | Required for trajectory reconstruction |
| `usage` | Tokens, latency, retries, finish reason | Operational evidence; never quality proof by itself |
| `content_policy` | Redacted, metadata-only, or consent-scoped capture | Raw content is not stored by default |
| `content_digests` | One-way fingerprints for request, response, and tool request | Supports equality/correlation checks without retaining content |
| `redactions` | Content classes removed from the record | Must be explicit and reviewable |
| `non_comparable_fields` | Fields excluded from cross-provider scoring | Prevents accidental apples-to-oranges aggregation |
| `provider_extensions` | Safe provider-specific metadata | Keep isolated and mark comparability explicitly |

## Safety and privacy boundary

The current adapter hashes request/response/tool content and stores metadata by default. Explicit content capture is intentionally rejected by the generic adapter; a future consent-scoped implementation must establish data class, purpose, retention, access, deletion, and approval before enabling it. A trace records what happened; it does not authorize a tool action or prove that the outcome was correct.

## What this implementation proves

It proves that the reference host can emit a normalized, redacted response record without breaking the existing provider seam or safety tests. It does not prove lossless normalization, cross-provider comparability, privacy compliance in a hosted deployment, or improvement in model quality.

## Next adapter experiment

Implement one read-only hosted provider adapter behind `ProviderAdapter`, emit the normalized record, and run a small development/held-out subset with fixed model and budget. Compare the normalized trace completeness and privacy behavior before comparing task quality. Preserve raw provider fields only in a controlled extension area and report every field that cannot be compared fairly.
