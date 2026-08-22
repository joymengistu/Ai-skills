---
name: incident-response
description: Detect, contain, communicate, recover from, and learn from AI-agent failures, unsafe actions, data exposure, incorrect outputs, or policy violations. Use when an agent run causes or may have caused harm or a material reliability incident.
---

# Incident response

Prioritize people, containment, evidence preservation, and honest communication. Stop or isolate the affected run, revoke or narrow permissions if needed, and prevent retries from amplifying the issue.

Classify the incident: safety, privacy, security, integrity, availability, financial, external communication, or user trust. Record timeline, run and action IDs, scope, affected assets and people, observed facts, uncertainty, containment, approvals, and external outcomes. Do not alter or delete evidence to make the trace look clean.

Notify the appropriate human owner with what happened, what is contained, what may still be affected, and the next decision needed. Use rollback, cancellation, credential rotation, data deletion, correction, or user notification as appropriate and authorized. Verify recovery independently.

After stabilization, perform blameless root-cause analysis, identify whether the failure was framing, context, tool, permission, model, memory, runtime, verification, or communication, add a regression case, and make the smallest safe change. Do not silently convert an incident into a “learning” that weakens controls.
