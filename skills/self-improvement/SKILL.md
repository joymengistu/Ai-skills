---
name: self-improvement
description: Diagnose agent failures from traces, feedback, and evaluations, then propose bounded, reversible, evidence-backed improvements. Use after observed failures or during controlled optimization.
---

# Self-improvement

Collect a failure example, classify the cause, identify the smallest intervention, predict side effects, and test on held-out cases. Common causes include poor task framing, missing context, ambiguous tools, stale memory, bad routing, weak verification, unsafe permissions, and communication mismatch.

Prefer changes in this order: improve data/context, clarify tool contracts, adjust routing, add a verifier, refine the skill, then revise the core prompt. Keep a changelog, baseline metrics, confidence, affected cases, and rollback. Do not optimize only for aggregate scores; inspect distributional harm and user experience.

The agent may propose changes, generate patches, or run sandboxed experiments. A human or authorized release process must approve changes to safety, privacy, authority, or evaluation policy.
