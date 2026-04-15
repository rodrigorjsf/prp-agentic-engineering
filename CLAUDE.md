# PRP Framework — AI-powered workflow automation plugin for Claude Code.

## Tooling

- Package manager: `uv`

## Skills

Skills are the primary interface. Invoke by name (e.g., "run the prp-plan skill").

| Workflow | Skills |
|----------|--------|
| Full pipeline | `prp-core-runner` (orchestrates: plan → implement → commit → PR) |
| Plan & Build | `prp-plan`, `prp-implement`, `prp-commit`, `prp-pr` |
| Research | `prp-codebase-question`, `prp-debug`, `prp-prd`, `prp-research-team` |
| Issues | `prp-issue-investigate`, `prp-issue-fix` |
| Review | `prp-review`, `prp-review-agents` |
| Autonomous | `prp-ralph` (start loop), `prp-ralph-cancel` (stop loop) |

## Context

- `plugins/prp-core/` — PRP Core plugin (v3.0.0): 15 skills, 10 agents, hooks
- `.claude/agents/` — 11 agents (10 from plugin + `gpui-researcher` project-specific)
- `.claude/skills/prp-core-runner/` — orchestration skill (project-only, not in plugin)

## PRP Methodology

**PRP = PRD + curated codebase intelligence + agent/runbook** — enables one-pass implementation.

When creating PRPs, include: goal, business value, user-visible behavior, all needed context (docs, examples, gotchas), implementation blueprint with task list, and executable validation commands.

When executing PRPs: load and understand all context → create plan with todos → implement following blueprint → validate at each step → fix failures before proceeding.
