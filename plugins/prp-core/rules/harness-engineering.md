---
paths:
  - ".claude/**/*.md"
  - "**/*.prd.md"
  - "**/*.plan.md"
---
# Harness Engineering Conventions

Authoritative sources: `references/context-budget-policy.md`, `references/harness-taxonomy.md`.

## Smart Zone (Priority 1 — CRITICAL)

- Context < 40% capacity: normal execution.
- Context 40–70%: compact aggressively. Write current state to an artifact; start next phase with a fresh window.
- Context > 70%: delegate remaining work to a subagent; pass only the compacted artifact, not raw context.
- 3,000 filler tokens drop math accuracy from 0.92 → 0.68 (Levy et al., ACL 2024). Every token must earn its place.

## Harness Rails (Priority 2 — HIGH)

- Deterministic validation gates precede completion claims. Run `prp-verification-before-completion` before declaring any phase done.
- A behavioral rule repeated more than twice signals a harness gap. Fix the harness, not the wording.

## Subagent Isolation (Priority 3 — HIGH)

- Research, analysis, and exploration run in forked subagent contexts.
- Return only condensed output (~1,000 tokens) to the parent agent.
- Never carry raw tool output or exploration transcripts across phase boundaries.

## Artifact Discipline (Priority 4 — MEDIUM)

- Each phase (research → plan → implement → review) must produce a durable artifact before the next phase begins.
- Component taxonomy: artifact / advisory / utility — see `references/harness-taxonomy.md`.
- Brief size limits: discovery ≤ 50 lines, execution ≤ 30 lines, validation ≤ 20 lines.

## Progressive Disclosure (Priority 5 — MEDIUM)

- Never duplicate policy inline in skills or agents — link to `references/` instead.
- Skills link to reference files; reference files are the single source of truth.
