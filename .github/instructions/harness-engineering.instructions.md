---
applyTo: "**"
---
# Harness Engineering Review Guidelines

## Smart Zone

- Flag any CLAUDE.md or rules file change that increases always-loaded context without a compensating removal.
- Flag additions of directory listings, skills inventories, or version numbers to always-loaded files.
- Flag inline policy duplication that should reference `plugins/prp-core/references/` instead.

## Harness Rails

- Flag any new behavioral instruction that should instead be a hook, test, or lint constraint.
- Verify that shipped skills link to `plugins/prp-core/references/` for policy rather than duplicating inline.
- Flag changes to deterministic contracts (hook sentinels, eval cases, schema validators) without corresponding test updates.

## Subagent Isolation

- Flag skills that return raw tool output to the parent context instead of condensed summaries.
- Verify that advisory agents (review, analysis) include a `## CRITICAL: Your only job is to [role]` header.

## Plugin Boundary

- Flag any content that crosses the `plugins/prp-core/` ↔ root `.claude/` boundary without explicit justification.
- Verify root-only extras (`prp-core-runner`, `update-review-instructions`, `gpui-researcher`, `rubber-duck`) are not documented or shipped as plugin payload.

## Artifact Discipline

- Flag plan or implementation work that skips producing a durable artifact (PRP, plan file, research note) before the next phase begins.
- Verify the eval harness (`tests/prp-core/prompt-cases.json`) is updated when new skills or agents are added.
