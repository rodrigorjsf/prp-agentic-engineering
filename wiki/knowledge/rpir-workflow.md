# RPIR Workflow

**Summary**: The Research, Plan, Implement, Review (RPIR) workflow is Tyler Burleigh's extension of the [[rpi-workflow]] that adds explicit inter-phase review cycles, written artifact persistence, and a multi-agent scaling model, treating review as a first-class phase rather than an afterthought.
**Sources**: `docs/agentic-engineering/research-plan-implement-review-tyler-burleigh.md`
**Last updated**: 2026-04-21

---

## Overview

Tyler Burleigh's RPIR workflow separates AI coding work into distinct stages — research, planning, implementation, and review — with explicit review cycles and fresh context windows between each phase. The core insight is that **the bottleneck in AI-assisted development is not code generation but ensuring the model understands what to build before it starts** (source: research-plan-implement-review-tyler-burleigh.md).

Unlike a single-pass approach, RPIR builds written artifacts (`RESEARCH.md`, `PLAN.md`, `PLAN-CHECKLIST.md`) as persistent shared sources of truth across sessions. Each phase gets a dedicated context window — fresh enough to avoid carrying forward confusion from the previous phase.

For the three-phase predecessor, see [[rpi-workflow]]. For the synthesized community perspective, see [[agentic-engineering-workflow]].

## Core Principles

1. **AI agents are fallible and cut corners.** They miss things, take shortcuts, and make confident-sounding mistakes. A single pass is rarely enough — build in review cycles.
2. **Fresh context windows prevent compounding confusion.** Each new session means the model isn't carrying forward misunderstandings or stale assumptions.
3. **Written artifacts are the source of truth.** `RESEARCH.md`, `PLAN.md`, and `PLAN-CHECKLIST.md` are the shared ground truth between you and the model. Without them, context is lost between sessions.
4. **Separate research, planning, and implementation.** Mixing them leads the model to jump to code before understanding the problem.
5. **Small phases reduce blast radius.** A bug introduced in Phase 1 doesn't propagate silently through Phases 2–5.
6. **Your time is expensive, tokens are cheap.** Optimize for output quality, not token efficiency.
7. **Let AI review before you do.** By the time you look at it, the obvious problems are fixed and you can focus on what only a human would catch.
8. **Git history is your safety net.** Commit after each phase so you can always revert.
9. **Watch for over-engineering.** Models tend to add abstractions, error handling for impossible scenarios, or features beyond what was requested.

(source: research-plan-implement-review-tyler-burleigh.md)

## The Process (10 Steps)

### Setup
**Step 1 — Clear problem statement.** Describe the problem or feature with supporting context: paths to relevant files, reference documents, anything that clarifies "what, why, or how."

### Research Phase
**Step 2 — Research.** Ask the agent to research the codebase (existing projects) or do web research (greenfield), writing everything to `RESEARCH.md`. Read it yourself and revise as necessary — the model may miss things or get details wrong.

**Step 3 — Research review.** *New session.* Tell the agent: "Review RESEARCH.md for accuracy and completeness." Read its feedback, tell it to revise, answer questions, and tell it which points to ignore if any are off-base. Repeat until satisfied.

### Planning Phase
**Step 4 — Planning.** *New session.* Give the agent your problem statement, tell it to read `RESEARCH.md` and develop a plan, saving to `PLAN.md`. For complex work, also have it write `PLAN-CHECKLIST.md` breaking work into phases and tasks.

**Step 5 — Plan review.** *New session.* Tell the agent: "Review PLAN.md as a senior engineer." Read recommendations and clarifying questions, tell it to revise, and ignore off-base points. Repeat until the plan is solid.

### Implementation Phase
**Step 6 — Implementation.** *New session.* "Implement Phase 1 of PLAN.md, using PLAN-CHECKLIST.md to track your work."

**Step 7 — Implementation review.** *New session.* "Review the implementation of Phase 1 against PLAN.md as a senior engineer." Read feedback, tell it to address its own recommendations. Repeat until the phase is clean.

**Step 8 — Commit.** Once satisfied with a phase, commit all changes. Repeat steps 6–8 for each phase.

### Final Phase
**Step 9 — Final review.** *New session.* "Review all changes on this branch as a senior engineer." This holistic review may catch issues that only emerge when the pieces come together.

**Step 10 — Refactoring (optional).** *New session.* "Review all changes on this branch and identify high-leverage refactoring opportunities." Save findings to `REFACTOR_PLAN.md`.

(source: research-plan-implement-review-tyler-burleigh.md)

## Comparison with RPI

| Dimension | [[rpi-workflow]] (HumanLayer/Horthy) | RPIR (Burleigh) |
|-----------|---------------------------------------|-----------------|
| Core focus | [[context-engineering]] / context window management | Review cycle discipline |
| Key concept | "Dumb Zone" above ~40% context utilization | Fresh sessions between every phase |
| Artifacts | `research_doc.md`, `implementation_plan.md`, `progress.md` | `RESEARCH.md`, `PLAN.md`, `PLAN-CHECKLIST.md` |
| Review | Checkpoints at research + plan | Explicit review session after every phase |
| Human role | Review gates at R and P phases | Active revision at every review step |
| Scaling | [[subagents]] for isolation | Multi-model with role specialization |

Both methodologies emerged as responses to unstructured "vibe coding" producing unreliable results. The convergence across independent practitioners suggests the core pattern is sound (source: research-plan-implement-review-tyler-burleigh.md).

## Tooling: Git Worktrees

Git worktrees let you check out multiple branches into separate directories. This enables running multiple agents in parallel, each on a different feature branch in its own worktree, without file conflicts (source: research-plan-implement-review-tyler-burleigh.md):

```bash
git worktree add ../myproject-feature-x feature-x
git worktree add ../myproject-feature-y feature-y
# When done:
git worktree remove ../myproject-feature-x
```

## Tooling: LSP Plugins

Claude Code supports Language Server Protocol plugins that give the agent code intelligence identical to VS Code — jump to definition, find references, and real-time type error detection (source: research-plan-implement-review-tyler-burleigh.md):

| Language | Plugin | Binary required |
|----------|--------|----------------|
| Python | `pyright-lsp` | `pyright-langserver` |
| Go | `gopls-lsp` | `gopls` |
| TypeScript | `typescript-lsp` | `typescript-language-server` |
| Rust | `rust-analyzer-lsp` | `rust-analyzer` |

## Scaling with Multiple Agents

**Use different models for different roles.** Models with different architectures produce largely uncorrelated errors. Use one model to implement and a different model to review (source: research-plan-implement-review-tyler-burleigh.md).

**Match model capability to task complexity.** Research, planning, and review require synthesis and judgment. Implementation — guided by a detailed plan — is largely mechanical. Use your strongest model for high-leverage phases.

**A more automated workflow:**
1. **Research and planning** — Agent produces `RESEARCH.md` and `PLAN.md`. Human reviews and approves. (Highest leverage.)
2. **Implementation loop** — Implementer agent executes; reviewer agent (different model) reviews against `PLAN.md`; they iterate. No human involvement required.
3. **Pull request** — Human reviews cumulative changes as a PR.

| Plan detail | Safe autonomy level |
|-------------|---------------------|
| High-level goal | Human-in-the-loop for every step |
| Phased plan with architecture decisions made | Autonomous per phase, review between phases |
| Detailed plan with file paths and function signatures | Autonomous implementation, human reviews PR |
| Exact specifications with test cases | Fully autonomous with automated verification |

(source: research-plan-implement-review-tyler-burleigh.md)

## Related pages

- [[rpi-workflow]]
- [[agentic-engineering-workflow]]
- [[agent-harness]]
- [[agent-best-practices]]
- [[context-engineering]]
- [[subagents]]
- [[agent-workflows]]
- [[agentic-software-modernization]]
