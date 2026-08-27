# Decisions

## Android capability split

**Status: [IMPLEMENTED]**

The Android guidance is divided into five focused skills: product quality, UX/accessibility, engineering, verification/release, and skill making. The reason is documented in the authored skill content: separate triggers and responsibilities improve composition and progressive disclosure compared with one oversized guide.

## Repository as source of truth

**Status: [IMPLEMENTED]**

The actual skill files live under `skills/`, the manifest registers them, and publication is represented by a Git commit. This preserves the work outside the conversation and makes it portable to another AI or developer.

## Preservation protocols

**Status: [IMPLEMENTED]**

The two user-provided preservation instructions are retained under `prompts/` as versioned text files. Their presence does not imply that every requested ecosystem artifact already existed; the current repository state is described explicitly in `PROJECT_SUMMARY.md` and `AI_HANDOFF.md`.

## Runtime claims

**Status: [IMPLEMENTED]**

The Android skills require evidence before claiming accessibility, security, performance, compatibility, or release readiness. Structural validation alone is not treated as runtime proof.

## Historical uncertainty

**Status: [UNKNOWN]**

The reason for some existing repository naming and historical contribution choices is not documented in the available context. Do not infer or rewrite those reasons without repository evidence.
