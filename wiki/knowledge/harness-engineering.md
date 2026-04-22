# Harness Engineering

**Summary**: Harness engineering treats the model as only one part of an autonomous system and focuses on the surrounding control layer — context management, deterministic validation, external state, specialized roles, and controlled execution environments.
**Sources**: `docs/harness-engineering/harness-engineering.md`, `docs/harness-engineering/harnessengineering-building-the-operating-system-for-autonomous-agents.md`, `docs/harness-engineering/skill-issue-harness-engineering-for-coding-agents.md`
**Last updated**: 2026-04-22

---

Harness engineering is the shift from "just prompting" an LLM toward building the operating system around it. The model remains the reasoning engine, but reliability comes from the harness that constrains how it sees context, uses tools, stores state, and proves completion.

## Core Shift

| Vibe-style interaction | Harness engineering |
|---|---|
| Keeps failed attempts and logs in the same chat | Resets context aggressively and carries forward only compacted artifacts |
| Corrects mistakes by adding more chat instructions | Adds deterministic rails such as tests, linters, hooks, and budgets |
| Treats code generation as the main output | Treats specs, plans, progress files, and review artifacts as first-class outputs |

## What the Harness Contains

The current docs consistently describe the harness as the layer around the model:

- **Context controls** — progressive disclosure, compaction, and fresh windows between phases
- **Deterministic rails** — tests, type checks, linters, schema validation, and stop/review gates
- **External state** — durable research notes, plans, progress files, and git history
- **Specialized roles** — subagents or teammate roles with narrow responsibilities
- **Controlled environments** — sandboxes, worktrees, permission boundaries, and reproducible execution surfaces

## Design Principles

### 1. Keep the model in the smart zone

Long tasks degrade when the context fills with noise. Harness engineering responds with intentional compaction: write down the state, start the next phase with a fresh window, and avoid carrying raw exploration traces farther than necessary.

### 2. Prefer back-pressure over corrective prompting

If an agent can claim success without tests, artifacts, or review, the system is underspecified. A good harness forces the agent to prove completion through verification steps rather than relying on self-reported confidence.

### 3. Use subagents as context firewalls

Research-heavy or high-latency work should happen in isolated contexts. The parent agent gets back only the condensed result, not the entire search transcript.

### 4. Make workflow artifacts first-class

Research, planning, implementation, and review each need durable outputs. These artifacts let later phases start cleanly and give humans something compact to inspect before code changes snowball.

## Workflow Shape

The harness-engineering docs align with the [[agentic-engineering-workflow]] pattern:

1. **Research** — find definitions, data flow, and constraints
2. **Plan** — turn findings into explicit steps and validation checks
3. **Implement** — execute in small increments with verification
4. **Review** — validate the combined result, often with a different role or model

The point is not ceremony. The point is preventing confusion from compounding across a long autonomous run.

## Operational Heuristics

- Success logs should stay short; failure output should be detailed
- Repeated mistakes should drive harness improvements, not just stronger wording
- Parallelism helps only when tasks are genuinely isolated
- A better harness can outperform a model upgrade on the same task

## Related pages

- [[agent-harness]]
- [[agent-harness-design]]
- [[agentic-engineering-workflow]]
- [[context-engineering]]
- [[subagents]]
- [[mcp-transport]]
