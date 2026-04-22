# Spec-Driven Development — Practitioner Guide

**Summary**: A practitioner's guide to SDD in 2026, contrasting vibe coding with the spec-first approach and walking through GitHub Spec Kit, AWS Kiro, and Tessl with honest assessment of where SDD breaks down.
**Sources**: `docs/spec-driven-development/spec-driven-development-main.md`
**Last updated**: 2026-04-22

---

## Vibe Coding vs. Spec-First

"Vibe coding" is the pattern of describing what you want, accepting the AI's output, and shipping — then spending the next week debugging assumptions the model made because you never stated them (source: spec-driven-development-main.md).

Spec-driven development is the counter-approach: write a structured, behavior-oriented specification first, then let the AI generate code to match it. The core insight is that **language models are excellent at pattern completion but bad at mind reading** (source: spec-driven-development-main.md).

Without a spec, asking an AI to "build a REST API for user management" leaves thousands of decisions unstated: authentication method, error response format, pagination strategy, rate limiting, input validation rules. The agent fills gaps with its training data, which may not match your requirements.

The key difference from vibe coding is **where you spend your time**: in vibe coding, you iterate on code after generation; in SDD, you invest in the spec before generation. The total time is often comparable — but the spec is reusable and serves as documentation after the project ships (source: spec-driven-development-main.md).

Related: [[spec-first-ai-development]], [[context-engineering]], [[agent-best-practices]]

---

## The Three Levels

Most teams today start at **spec-first**, which is where the practical payoff begins (source: spec-driven-development-main.md):

| Level | Description |
|-------|-------------|
| **Spec-first** | Write spec for the immediate task |
| **Spec-anchored** | Maintain spec as a living document alongside code |
| **Spec-as-source** | Spec becomes the canonical artifact; code is entirely generated |

See [[spec-driven-development]] for the academic treatment of all three levels.

---

## Three Tools, Three Approaches

### GitHub Spec Kit

The most customizable option — an open-source CLI integrating with Copilot, Claude Code, and Gemini CLI via slash commands (source: spec-driven-development-main.md):

- `/specify` — generates a detailed specification from your description
- `/plan` — creates a technical implementation plan given your stack and constraints
- `/tasks` — breaks the plan into small, reviewable chunks with acceptance criteria from the spec
- Agent implements each task sequentially, using spec and plan as context

Spec Kit enforces architectural rules through a **"constitutional foundation"** — a set of project-level constraints the agent must obey. This parallels the memory bank concept described in [[agent-configuration-files]].

### Amazon Kiro

The simplest entry point — a VS Code extension by AWS that produces three markdown documents: requirements, design, and tasks (source: spec-driven-development-main.md).

The workflow is linear and lightweight. The tradeoff: Kiro generated **16 acceptance criteria for a simple bug fix**. The overhead can exceed the problem.

### Tessl Framework

The most ambitious approach — still in closed beta. Pursues spec-as-source by reverse-engineering specs from existing code and maintaining a **1:1 mapping between spec files and code files** (source: spec-driven-development-main.md).

Generated code is marked `// GENERATED FROM SPEC - DO NOT EDIT`. Developers would maintain only specs, never touching code directly.

The practical reality across all three: **AI agents still inconsistently follow instructions**. A spec reduces the gap between intent and implementation, but it does not eliminate non-determinism. The spec is a guardrail, not a guarantee.

---

## Getting Started with Spec Kit

Step-by-step for the most accessible tool (source: spec-driven-development-main.md):

1. **Install**: CLI available via npm; `specify init` creates a `.specify/` directory with templates
2. **Write your first spec**: Run `/specify`, describe the feature with specific behavior, constraints, edge cases; review and approve the generated spec before any code is written
3. **Generate a plan**: Run `/plan` with your tech stack; output is a step-by-step plan referencing your spec
4. **Break into tasks**: Run `/tasks` to split the plan into small, reviewable work units each with clear objectives and acceptance criteria
5. **Implement**: Agent works through tasks sequentially; you review each completed task against the spec

---

## The Difference in Practice

**Vibe coding prompt:**
> "Build a rate limiter middleware for Express."

**Spec-first prompt:**
> "Implement the rate limiter defined in `.spec/features/rate-limiter.md`, which specifies a sliding window algorithm, 100 requests per minute per API key, 429 responses with Retry-After headers, and Redis-backed state for horizontal scaling."

The second prompt leaves no room for the agent to improvise on decisions that should be yours (source: spec-driven-development-main.md).

> **Key insight**: Move the ambiguity from code review to spec review, where it is cheaper to fix. (source: spec-driven-development-main.md)

---

## Real-World Examples

- **Anthropic** used GCC test suites to spec a Rust-based C compiler
- **Vercel** used curated shell script tests for a TypeScript bash emulator
- **Pydantic** applied the same approach to a Python sandbox for AI agents

A well-defined spec plus an existing test suite gets an AI agent far on a greenfield build (source: spec-driven-development-main.md).

---

## Where SDD Breaks Down

SDD is not a universal improvement. Honest friction points (source: spec-driven-development-main.md):

### Review Overhead Scales with Spec Verbosity

Kiro's 16 acceptance criteria for a bug fix is not an edge case. Spec Kit produces extensive markdown for mid-sized features. If reviewing the spec takes longer than reviewing the code would have, the process is working against you.

### Poor Fit for Exploratory Work

Prototyping, UI experiments, and data pipeline debugging benefit from fast, loose iteration. Writing a detailed spec before you know what you are building adds latency to a process that should be cheap and fast.

### Non-Determinism Persists

Even with a detailed spec, agents sometimes ignore directives or over-interpret them. The spec improves consistency but does not solve the fundamental reliability problem.

As Vercel's CTO put it: "Software is free now. Free as in puppies." Generation is cheap. Maintenance is where the work lives.

---

## The Sweet Spot

SDD in its current form works best for **greenfield features with well-understood requirements**: new API endpoints, CRUD modules, integration layers. It is less useful for exploratory work or codebases where existing architecture is poorly documented (source: spec-driven-development-main.md).

**Starting point without tooling**: Before your next feature, write a one-page spec in plain markdown before prompting your AI agent. Define inputs, outputs, constraints, and edge cases. Pass that spec as context alongside your prompt. You do not need Spec Kit or Kiro to start.

---

## Related pages

- [[spec-driven-development]]
- [[spec-driven-development-critique]]
- [[spec-first-ai-development]]
- [[code-to-contract]]
- [[context-engineering]]
- [[agent-workflows]]
- [[agent-best-practices]]
- [[agentic-engineering-workflow]]
