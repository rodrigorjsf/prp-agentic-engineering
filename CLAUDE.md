# PRP Framework — AI-powered workflow automation plugin for Claude Code.

- **graphify**: `/graphify` → invoke `skill: "graphify"` before anything else.

## Priorities (highest first)

1. **Smart Zone** [CRITICAL] — Keep context window < 40% capacity. Compact before reaching limit; delegate heavy work to subagents with fresh windows.
2. **Harness-First** [HIGH] — Deterministic rails (tests, hooks, linters) over corrective prompting. Prove completion via verification, not self-reported confidence.
3. **Subagent Isolation** [HIGH] — Research and analysis in isolated contexts; return only condensed summaries (~1,000 tokens) to the parent agent.
4. **Artifact-First** [MEDIUM] — PRPs, plans, and review artifacts are first-class outputs. Each phase writes a durable artifact before the next phase starts.
5. **Progressive Disclosure** [MEDIUM] — Load context in tiers. Authoritative policy: `plugins/prp-core/references/`.

## Context

- `plugins/prp-core/` is the packaged plugin distribution.
- Root `.claude/` mirrors plugin artifacts for local development; root-only extras: `prp-core-runner`, `update-review-instructions`, `gpui-researcher`, `rubber-duck`.
- Use `plugins/prp-core/CLAUDE.md` when changing the shipped plugin payload.

## PRP Methodology

**PRP = PRD + curated codebase intelligence + agent/runbook** — enables one-pass implementation.

Run the `prp-advisor` skill before writing any `*.prd.md` or `*.plan.md` file or committing to any interpretation.

When creating PRPs: include goal, business value, user-visible behavior, all needed context, implementation blueprint with task list, and executable validation commands.

When executing PRPs: load context → create plan with todos → implement → validate at each step → fix failures before proceeding.
