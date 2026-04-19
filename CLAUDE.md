# PRP Framework — AI-powered workflow automation plugin for Claude Code.

## Skills

Skills are the primary interface. Invoke by name (e.g., "run the prp-plan skill").

| Workflow | Skills |
|----------|--------|
| Full pipeline | `prp-core-runner` (orchestrates: plan → implement → commit → PR) |
| Plan & Build | `prp-plan`, `prp-implement`, `prp-commit`, `prp-pr` |
| Advisor | `prp-advisor` |
| Validation | `prp-verification-before-completion` |
| Research | `prp-codebase-question`, `prp-debug`, `prp-prd`, `prp-research-team` |
| Issues | `prp-issue-investigate`, `prp-issue-fix` |
| Review | `prp-review`, `prp-review-agents` |
| Autonomous | `prp-ralph` (start loop), `prp-ralph-cancel` (stop loop) |

## Context

- `plugins/prp-core/` is the packaged plugin distribution.
- Root `.claude/` mirrors plugin artifacts for local development and also contains project-only extras such as `prp-core-runner`, `update-review-instructions`, and `gpui-researcher`.
- Use `plugins/prp-core/CLAUDE.md` when changing the shipped plugin payload.

## PRP Methodology

**PRP = PRD + curated codebase intelligence + agent/runbook** — enables one-pass implementation.

When creating PRPs, include: goal, business value, user-visible behavior, all needed context (docs, examples, gotchas), implementation blueprint with task list, and executable validation commands.

When executing PRPs: load and understand all context → create plan with todos → implement following blueprint → validate at each step → fix failures before proceeding.
