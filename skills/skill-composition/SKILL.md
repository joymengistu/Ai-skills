---
name: skill-composition
description: Compose a minimal compatible bundle of skills for a goal by checking inputs, outputs, dependencies, ordering, permissions, side effects, evidence flow, and failure recovery. Use when an agent needs multiple capabilities or must build a reusable workflow.
---

# Skill composition

Treat a skill as a contract, not a keyword. For each candidate identify the artifact it consumes, the artifact it produces, required state, dependencies, permissions, risk, verification evidence, and safe failure behavior.

Build a directed workflow. Use sequential composition when later work depends on shared mutable state or previous observations. Use parallel composition only for independent, side-effect-free work with mergeable outputs. Reject bundles with incompatible ports, unresolved dependencies, conflicting permissions, unbounded side effects, duplicate authority, or no recovery path.

Prefer the smallest bundle that covers the requirement ledger. Preserve provenance and version for each component. Pass evidence and uncertainty between skills, not just raw outputs. Keep one owner for shared files, external mutations, contradictions, and final completion judgment.

Before execution, report selected skills, why each is needed, ordering, assumptions, risks, budget, and fallback. After execution, evaluate the composition as a whole; a collection of individually valid skills can still fail through interface mismatch or orchestration overhead.
