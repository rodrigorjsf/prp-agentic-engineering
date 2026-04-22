# Spec-First AI Development

**Summary**: The spec-first paradigm — why writing clear, structured specifications before code matters when working with AI coding assistants, and how it transforms the developer's role from code producer to spec author and AI orchestrator.
**Sources**: `docs/spec-driven-development/spec-driven-development-arxiv.md`, `docs/spec-driven-development/spec-driven-development-main.md`, `docs/spec-driven-development/spec-driven-development-variant.md`
**Last updated**: 2026-04-21

---

## The Core Problem: AI Can't Read Minds

Large language models are excellent at pattern completion but poor at mind reading (source: spec-driven-development-arxiv.md). When you give an AI agent a vague prompt — "Add photo sharing to my app" — the model must guess dozens of unstated decisions:

- What format? What permissions model? What size limits?
- Cloud storage or local? Compression? Resizing?

The result is plausible-looking code that makes dozens of assumptions, many of them wrong. This is "vibe coding" — relying on loose prompts that lead to inconsistent or erroneous outputs (source: spec-driven-development-arxiv.md).

Spec-first development addresses this at the root: **give the AI an unambiguous, executable contract, and it can generate code that matches intent** (source: spec-driven-development-arxiv.md).

This principle directly informs the [[context-engineering]] discipline — the quality of context you provide determines the quality of AI output.

---

## What Spec-First Actually Means

In spec-first development, a specification is written **before** coding begins to guide the initial implementation (source: spec-driven-development-arxiv.md). The spec is not documentation of what was built; it is the declaration of what should be built, written before the first line of code.

A spec-first spec (source: spec-driven-development-variant.md):
- Is structured and behavior-oriented
- Is written in natural language (not pseudo-code)
- Expresses software functionality as guidance to an AI coding agent
- Is scoped to the feature or task at hand — not a global project description

Good specs share four properties (source: spec-driven-development-arxiv.md):
- **Behavior-focused**: what happens, not how
- **Testable**: each requirement is verifiable
- **Unambiguous**: different readers reach the same interpretation
- **Complete enough** to cover essential cases without over-specifying

---

## Spec-First vs. Spec-Anchored vs. Spec-as-Source

Spec-first is only the entry level of the [[spec-driven-development]] spectrum. It provides immediate value but does not protect against long-term drift between spec and code (source: spec-driven-development-arxiv.md). Teams who see value from spec-first often graduate to:

- **Spec-anchored**: spec maintained alongside code throughout the lifecycle; tests enforce alignment
- **Spec-as-source**: spec is the only human-edited artifact; code is entirely generated

Most teams today are at spec-first — and that is where the practical payoff starts (source: spec-driven-development-main.md).

---

## Why Spec-First Matters Now

The emergence of AI coding assistants has made spec-first newly relevant, even though the idea predates AI — TDD and BDD have advocated for it for years (source: spec-driven-development-arxiv.md). Three converging forces make 2025–2026 the inflection point:

1. **AI coding assistants are ubiquitous** — the bottleneck has shifted from "can we write the code?" to "can we specify what the code should do?"
2. **Tooling matured** — Spec Kit, Kiro, and Tessl all shipped dedicated SDD workflows in 2025–2026
3. **Error cost evidence** — controlled studies show human-refined specs reduce LLM-generated code errors by up to 50% (source: spec-driven-development-arxiv.md)

---

## The Developer's New Role

SDD fundamentally reshapes what it means to be a software developer (source: spec-driven-development-arxiv.md):

| Traditional Role | Spec-First Role |
|------------------|-----------------|
| Code producer | Spec author and AI orchestrator |
| Greenfield: writes implementation | Greenfield: designs system through specifications |
| Brownfield: edits existing code | Brownfield: encodes existing behavior as specs before making changes |

The developer's primary skill becomes writing clear, precise specifications — not writing code directly.

---

## Specs as Super-Prompts

In agentic workflows, specifications function as **super-prompts** (source: spec-driven-development-arxiv.md):
- Break complex problems into modular components aligned with agents' context windows
- Enable parallel agent execution on non-overlapping tasks
- Allow teams to partition work at the spec level, letting multiple AI agents implement different components simultaneously

This connects spec-first thinking to multi-agent [[agent-workflows]] and the parallelism strategies described in [[agentic-engineering-workflow]].

---

## The Spec-First Workflow in Practice

The minimal viable spec-first workflow — no special tooling required (source: spec-driven-development-main.md):

1. Before your next feature, write a one-page spec in plain markdown
2. Define inputs, outputs, constraints, and edge cases
3. Pass the spec as context alongside your prompt to the AI agent
4. Review the agent's output against the spec, not against vague intuition

**Without spec (vibe coding):**
> "Build a rate limiter middleware for Express."

**With spec (spec-first):**
> "Implement the rate limiter defined in `.spec/features/rate-limiter.md`, which specifies a sliding window algorithm, 100 requests per minute per API key, 429 responses with Retry-After headers, and Redis-backed state for horizontal scaling."

The second prompt leaves no room for the agent to improvise on decisions that should be yours (source: spec-driven-development-main.md).

---

## Specs, Memory Banks, and Context Documents

An important distinction for [[context-engineering]] (source: spec-driven-development-variant.md):

- **Specs** — scoped to a specific feature or task; only relevant when creating or changing that functionality
- **Memory banks / context documents** — global project context (rules files, architecture descriptions, conventions) relevant across all AI coding sessions

Tools express this distinction differently:
- Spec Kit calls its global context a **constitution**
- Kiro calls it **steering** (`product.md`, `structure.md`, `tech.md`)
- Tessl uses a global context alongside per-feature specs

Conflating the two leads to overly broad specs that become noise rather than signal.

---

## When Spec-First Works — and When It Doesn't

**Best fit** (source: spec-driven-development-main.md, spec-driven-development-arxiv.md):
- Greenfield features with well-understood requirements
- New API endpoints, CRUD modules, integration layers
- AI-assisted development (dramatic improvement in output quality)
- Complex requirements stakeholders can validate before code is written

**Poor fit**:
- Throwaway prototypes — spec overhead exceeds value
- Exploratory work — you don't yet know what you're building
- Simple, obvious implementations
- Tight iteration loops where writing a spec adds more latency than it removes

---

## Self-Spec: LLMs Writing Their Own Specs

An emerging technique: **self-spec methods** where the LLM authors its own specification before generating code (source: spec-driven-development-arxiv.md). The workflow:
1. Agent produces a spec from a high-level prompt
2. Human reviews and refines the spec
3. Same or different agent implements against the refined spec

This preserves human oversight at the spec-review stage rather than the code-review stage — where ambiguity is cheaper to fix.

---

## Related pages

- [[spec-driven-development]]
- [[spec-driven-development-practice]]
- [[spec-driven-development-critique]]
- [[code-to-contract]]
- [[context-engineering]]
- [[agent-workflows]]
- [[agentic-engineering-workflow]]
- [[rpi-workflow]]
- [[rpir-workflow]]
- [[agent-best-practices]]
