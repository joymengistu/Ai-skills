---
name: dynamic-verification
description: Verify interactive software and agent outputs by executing the real artifact, exercising primary and failure flows, inspecting observable behavior, and comparing results against requirements. Use when static code inspection or a screenshot cannot prove the requested outcome.
---

# Dynamic verification

Verify the thing the user will actually use. Start from the requirement ledger and define observable checks for each must-have outcome.

For software, build or launch the artifact, inspect runtime errors, exercise the primary journey, test invalid input, empty and loading states, refresh or restart, permissions, responsive layout, accessibility path, and recovery from tool or network failure. For games, test controls, playability, progression, feedback, pause, restart, and win/lose behavior. For documents or media, inspect rendered pages, legibility, structure, and source fidelity. Treat build health, visual usability, intent alignment, and operational readiness as separate gates; passing one does not imply passing the others.

Record evidence such as URLs, screenshots, logs, traces, outputs, timestamps, and test steps. Include the exact requirement or acceptance criterion each observation supports. A project that compiles but does not respond correctly is not verified. A beautiful screen that omits the requested workflow is not complete. Do not claim an end-to-end test unless the full path was actually exercised.

When execution is unavailable, say what was inspected and what remains unverified. Never convert static plausibility into a claim of dynamic success.
