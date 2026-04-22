# PRP Core Harness Architecture

This document describes the structural decisions behind the `prp-core` plugin and the repo-level evaluation harness.

## Component taxonomy

All plugin artifacts belong to one of three component classes defined in `plugins/prp-core/references/harness-taxonomy.md`:

| Class | Role | Examples |
|-------|------|---------|
| **Artifact** | Produces a durable, machine-readable output | `prp-plan`, `prp-implement`, `prp-review` |
| **Advisory** | Reviews and challenges decisions; no primary outputs | `prp-advisor`, `plan-critic` |
| **Utility** | Narrow, single-job helper | `prp-commit`, `prp-verification-before-completion` |

## Context budget policy

Skills follow the three-tier brief discipline documented in `plugins/prp-core/references/context-budget-policy.md`:

- **Discovery brief** ≤ 50 lines — filed before any subagent handoff
- **Execution brief** ≤ 30 lines — filed before implementation starts
- **Validation brief** ≤ 20 lines — filed before each completion claim

Noisy exploration (filesystem scanning, web research) must be isolated in subagents. Only the compact brief returns to the main context.

## Execution delegation modes

Four delegation modes are defined in `plugins/prp-core/references/execution-policy.md`:

| Mode | When to use |
|------|-------------|
| **Inline** | Simple, single-file operations with no noise |
| **Subagent** | Noisy exploration; only the artifact returns |
| **Parallel** | Independent scopes with no shared state |
| **Harness** | Deterministic batch verification across files |

## Agent prompt structure

Orchestration-heavy agents follow the one-job / hard-boundary / fixed-output structure documented in `plugins/prp-core/references/agent-prompt-style.md`:

1. `## CRITICAL: Your only job is to [single role]`
2. Explicit `DO NOT` boundary list
3. `## Core Responsibilities` — 3-5 bullets
4. `## Strategy` — numbered steps
5. `## Output Format` — fixed schema

This structure prevents scope creep, reduces token waste, and makes agent contracts testable.

## Artifact lifecycle

PRP artifacts are written to `.claude/PRPs/` by convention. Full path table and naming rules are in `plugins/prp-core/references/artifact-lifecycle.md`.

## Shared references vs. inline policy

Before this harness evolution, policy text appeared inline in multiple skill and agent files. That led to silent drift when one copy was updated without updating the others.

The current approach: policy lives once in `plugins/prp-core/references/`, and skills/agents link to it with a `## Context Contract` section. The mirror parity eval case in `tests/prp-core/prompt-cases.json` detects divergence automatically.

## Plugin vs. repo-local assets

| Location | Purpose | Ships in plugin? |
|----------|---------|-----------------|
| `plugins/prp-core/` | Installable payload | Yes |
| `.claude/` | Development mirror | No |
| `scripts/` | Repo-only tooling | No |
| `tests/` | Repo-only harness | No |
| `docs/` | Architecture docs | No |

Root-only extras (`prp-core-runner`, `update-review-instructions`, `gpui-researcher`, `rubber-duck`) are in `.claude/` only and do not ship with the plugin.
