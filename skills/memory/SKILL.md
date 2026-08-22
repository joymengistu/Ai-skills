---
name: memory
description: Design and use scoped, consent-aware, inspectable, deletable memory for AI agents. Use when an agent needs continuity across turns or sessions.
---

# Memory

Store only information that is useful, stable enough to retain, and appropriate for the scope. Prefer explicit user preferences and project facts over speculative personality inferences. Separate general facts from structured keys, as in CLAI's `facts` and `special` memory pattern.

Every memory item should have provenance, scope, confidence, sensitivity, created/updated time, expiry or review rule, and deletion path. Do not store secrets, credentials, sensitive personal data, or high-impact inferences by default. Show users what is remembered when it matters and support correction and forget operations.

Inject memory as a compact, clearly labeled context block. Never let memory override the current user request, safety policy, or fresh evidence.
