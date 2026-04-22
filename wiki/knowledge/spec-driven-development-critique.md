# Spec-Driven Development — Critical Analysis

**Summary**: A hands-on critical analysis of three SDD tools (Kiro, GitHub Spec Kit, Tessl) from the Martin Fowler team, surfacing concrete failure modes, open questions, and the gap between SDD's promises and practical reality.
**Sources**: `docs/spec-driven-development/spec-driven-development-variant.md`
**Last updated**: 2026-04-22

---

## Overview

The Martin Fowler team's "Exploring Gen AI" series evaluated Kiro, GitHub Spec Kit, and Tessl by actually using them — going beyond tool documentation to surface real friction. The verdict is measured: SDD tooling shows promise but has significant unresolved issues before it can be recommended for typical production codebases (source: spec-driven-development-variant.md).

See the tooling overview and academic backing in [[spec-driven-development]] and the practitioner walkthrough in [[spec-driven-development-practice]].

---

## What "Spec" Actually Means

The definition of "spec" in SDD is still in flux. The closest to a consistent definition found across all three tools (source: spec-driven-development-variant.md):

> A spec is a structured, behavior-oriented artifact — or a set of related artifacts — written in natural language that expresses software functionality and serves as guidance to AI coding agents.

A useful distinction: **specs** differ from general **context documents** (rules files, high-level product/codebase descriptions). Context documents are relevant across all AI coding sessions; specs are only relevant to the tasks that create or change that particular functionality. Some tools call this context a **memory bank**.

---

## Tool Comparison

### Kiro

The simplest of the three — primarily spec-first with no clear strategy for spec maintenance after the task is done (source: spec-driven-development-variant.md).

**Workflow**: Requirements → Design → Tasks (one markdown document per step)
- Requirements: structured as user stories in "As a…" format with GIVEN/WHEN/THEN acceptance criteria
- Design: component architecture, data flow, data models, error handling, testing strategy
- Tasks: traceable to requirement numbers; UI elements to run tasks one by one

Kiro's memory bank concept is called "steering" (`product.md`, `structure.md`, `tech.md`).

**Critical finding**: When asked to fix a simple bug, Kiro turned it into 4 user stories with 16 acceptance criteria, including: *"As a developer, I want the transformation function to handle edge cases gracefully."* The overhead exceeded the problem.

### Spec-kit

GitHub's SDD implementation — the most customizable due to all artifacts landing directly in your workspace (source: spec-driven-development-variant.md).

**Workflow**: Constitution → 𝄆 Specify → Plan → Tasks 𝄇

The **constitution** is a powerful rules file — Spec Kit's "memory bank" — containing immutable project-level principles applied to every change.

Each spec generates many files: `data-model`, `plan`, `tasks`, `spec`, `research`, `api`, `component` — potentially 8+ files per feature. The workflow uses checklists extensively inside files to track clarifications, constitution violations, research tasks — a "definition of done" for each step.

**Critical finding**: For a feature that would be a 3–5 point story on a real team, Spec Kit generated so many markdown files to review that it felt like overkill. In the same time taken to run and review Spec Kit results, the feature could have been implemented with plain AI-assisted coding, with more sense of control.

### Tessl

The only tool explicitly aspiring to spec-anchored and spec-as-source — still in private beta (source: spec-driven-development-variant.md).

**Workflow**: `tessl document --code ...js` (reverse-engineer spec from code) → `tessl build` (regenerate code from spec)

Code is marked `// GENERATED FROM SPEC - DO NOT EDIT`. Tags like `@generate` and `@test` tell Tessl what to generate. The 1:1 mapping between spec and code files keeps abstraction level low, reducing LLM interpretation steps and error surface.

**Observed finding**: Non-determinism appeared even at this low abstraction level — generating code multiple times from the same spec produced different outputs. Iterating on the spec to make it more specific increased repeatability.

---

## Concrete Failure Modes

### One Workflow Does Not Fit All Sizes

Both Kiro and Spec Kit provide one opinionated workflow, but neither adapts to the actual size of the problem (source: spec-driven-development-variant.md). An effective SDD tool must provide **flexibility for different change sizes and types**.

### Reviewing Markdown vs. Reviewing Code

Spec Kit created repetitive, verbose markdown files — sometimes containing code already, sometimes redundant with existing code. Overall, they were tedious to review (source: spec-driven-development-variant.md).

> "To be honest: reviewing code directly is often preferable to reviewing all these markdown files."

### False Sense of Control

Despite extensive files, templates, prompts, and checklists, agents frequently did not follow all instructions. In one case, Spec Kit's agent read descriptions of existing classes as new specifications and generated them all over again, creating duplicates (source: spec-driven-development-variant.md).

The best way to stay in control remains **small, iterative steps** — which conflicts with the upfront, comprehensive spec design that SDD promotes.

### Functional vs. Technical Spec Confusion

SDD tools encourage separating functional spec (what the software does) from technical implementation (how it does it). In practice with Spec Kit, there was frequent confusion about when to stay functional and when to add technical detail. As the author notes: "We don't have a good track record as a profession to do this well" (source: spec-driven-development-variant.md).

---

## Tool Summary Assessment

| Tool | Spec Level | Complexity | Best For |
|------|-----------|------------|----------|
| Kiro | Spec-first | Low | Simple, well-defined tasks |
| Spec-kit | Spec-first (aspiring anchored) | High | Larger greenfield features |
| Tessl | Spec-anchored / Spec-as-source | Medium-High | Teams committed to spec-driven long-term |

(source: spec-driven-development-variant.md)

---

## Evaluating SDD Is Hard

Honest evaluation requires trying tools with different problem sizes, greenfield and brownfield codebases, and genuinely taking time to review and revise intermediate artifacts. Introducing Kiro or Spec Kit into an existing codebase is significantly more work than greenfield use, making brownfield evaluation harder (source: spec-driven-development-variant.md).

As GitHub's own blog states: "Crucially, your role isn't just to steer. It's to verify. At each phase, you reflect and refine."

---

## Open Questions

- Does SDD scale to real production codebases over time, not just isolated demos?
- Who is the actual target user — experienced developers or those who benefit from structured guidance?
- How does spec maintenance overhead compare to traditional code review overhead over months of usage?
- Can tools adapt their spec depth to the actual size and complexity of each change?

---

## Related pages

- [[spec-driven-development]]
- [[spec-driven-development-practice]]
- [[spec-first-ai-development]]
- [[code-to-contract]]
- [[agent-workflows]]
- [[agent-best-practices]]
- [[context-engineering]]
- [[context-rot]]
