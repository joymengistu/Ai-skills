# Manus Dependencies

## Current dependencies

**[PARTIAL]** Skill authoring used the local Manus skill-creator workflow and validator at `/home/ubuntu/skills/skill-creator/scripts/quick_validate.py`. This is an authoring convenience, not a runtime dependency of the published Android Markdown skills.

Repository publication in this task used GitHub access configured for the current environment. That access is an execution-environment dependency, not content required to understand or use the skills.

## No known runtime-only dependency

The Android skill suite consists of portable Markdown files and manifest entries. It does not require Manus APIs, Manus infrastructure, or Manus-only application runtime behavior.

## Replacement requirements

Outside Manus, replace the local validator with an equivalent YAML/frontmatter and package-structure checker, and use standard GitHub or Git credentials for publication. Preserve equivalent validation evidence and commit provenance.

## Boundary rule

If future work introduces Manus APIs, hosted services, scheduled execution, connector configuration, or proprietary model calls, add the service, purpose, data boundary, portability impact, and replacement plan here before treating it as part of the architecture.
