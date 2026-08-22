---
name: tool-use
description: Select, call, validate, and document tools safely and efficiently with clear schemas, permissions, error handling, and evidence. Use whenever an agent can inspect or change an environment.
---

# Tool use

Use the smallest tool that can answer the current question. Tools should have one clear purpose, descriptive parameters, predictable output, explicit error states, and minimal overlap. Namespace tools by domain and return token-efficient results with identifiers, timestamps, and provenance.

Before a call, state intent, target, scope, risk, reversibility, permission, and expected evidence. After a call, validate the result against the plan and handle partial failure. Never infer that a tool succeeded because the call returned without an exception.

Separate read, propose, approve, execute, verify, and report operations. Apply least privilege, path and domain allowlists, rate limits, timeouts, dry-run mode, and audit logging. For shell or file actions, show the exact scope and preserve a rollback path.
