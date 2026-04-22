# Agent Harness Design

**Summary**: Design patterns for building agent harnesses — the skills, workflows, and methodology layers that encode how an agent should think and build — covering isolation, context management, tool access, component taxonomy, and iterative evolution principles.
**Sources**: `docs/agentic-engineering/building-agent-harness-martin-richards.md`, `docs/agentic-engineering/research-plan-implement-rpi.md`, `docs/agentic-engineering/research-plan-implement-review-tyler-burleigh.md`
**Last updated**: 2026-04-22

---

## Overview

An agent harness is the structured layer sitting between a raw LLM and a complex software task. It encodes discipline: how to research, how to plan, how to implement, and when to stop. See [[agent-harness]] for the practitioner-level case for building one. This page focuses on the design patterns that make harnesses effective.

The core design principle is that **harness quality matters more than model choice** — LangChain improved their agent from 52.8% to 66.5% on Terminal Bench 2.0 by only changing the harness, keeping the model fixed (source: building-agent-harness-martin-richards.md).

## Component Taxonomy

Effective harnesses distinguish between three categories of components that serve different purposes and should not be designed the same way (source: building-agent-harness-martin-richards.md):

### Sequential Artifact-Producing Components (e.g., `spec:` skills)

These follow a rigid, ordered procedure and produce concrete documents or code:
- Invoked explicitly or triggered by a previous component
- Produce a durable artifact that downstream components consume
- Examples: research skill (→ `spec.md`), plan skill (→ `plan.json`), implement skill (→ code files)

**Design rule**: Give these strict templates for artifact format. Ambiguous output format creates downstream parsing failures.

### Advisory Context-Adaptive Components (e.g., `oracle:` skills)

These adapt to context rather than following a rigid procedure:
- Examples: `oracle:architect` (applies DDD patterns, thinks about component responsibilities), `oracle:challenge` (pushes back on your approach, pokes holes in design)
- Should not produce required artifacts — they produce insights that inform human or agent decisions

**Design rule**: Do not force these into artifact-producing molds. A thinking tool should adapt; forcing it into rigid procedure wastes its value (source: building-agent-harness-martin-richards.md).

### Utility Components (e.g., `code:` skills)

Simple, single-purpose tools invoked on demand:
- Examples: commit, review, format
- Should be stateless and idempotent where possible

**Design rule**: Keep utilities narrow. Collapsing everything into one format loses the distinction between sequential, advisory, and utility behavior.

## Context Isolation Patterns

### Fresh Context Windows Per Phase

The most critical harness design pattern: each major phase (research, plan, implement) must start with a fresh context window containing only the compacted artifact from the previous phase (source: research-plan-implement-rpi.md).

**Why**: Context quality directly determines output quality. Carrying raw search results, failed attempts, or prior exploration into a new phase degrades all downstream reasoning.

**Implementation**: Phase transitions are not just workflow steps — they are explicit context boundaries. The harness must enforce these boundaries, not just suggest them.

### Subagent Isolation for Noisy Operations

During the Research phase, [[subagents]] perform operations that generate significant context noise (glob, grep, file reads). These must run in isolated contexts and return only compacted summaries to the main context (source: research-plan-implement-rpi.md).

**Pattern**:
```
Main context (clean)
  └── Subagent context (noisy)
        ├── glob operations
        ├── grep operations
        └── file reads
        → Returns: compacted summary only
```

This is the primary [[context-engineering]] mechanism for preventing research phase operations from polluting the planning context.

### Active Context Compaction

When an agent strays off path, the correct response is never to correct it in-context — that adds noise (source: agentic-software-modernization-markus-harrer.md). The harness design should support a compaction escape hatch:

1. Agent summarizes current state into a compact file (`state.md`)
2. New context starts with only that summary
3. Fresh reasoning from a clean starting point

Harnesses should make this path explicit and easy, not an exceptional manual intervention.

## Artifact Design Patterns

### Compacted Research Documents

Research artifacts (~200 lines) should capture (source: research-plan-implement-rpi.md):

```
research_doc.md
├─ Problem Summary
├─ Relevant Files Identified
│  └─ file paths with roles
├─ Information Flow Analysis
│  └─ function/module call chains
├─ Key Findings
└─ Recommended Approach
```

**Design rule**: Optimize for correctness over completeness. A shorter artifact that is accurate is more valuable than a longer one with errors.

### Compacted Implementation Plans

Plan artifacts (~200 lines) should capture (source: research-plan-implement-rpi.md):

```
implementation_plan.md
├─ Step 1: [Description]
│  ├─ File: exact/path/to/file.ext
│  ├─ Function: function_name()
│  └─ Tests: test_file.ext
├─ Step 2: ...
└─ Step N: ...
```

**Design rule**: Specify exact file paths and function names. Ambiguous plans produce ambiguous code.

### Progress Tracking for Long Tasks

For implementations spanning multiple context resets, `progress.md` provides state continuity (source: research-plan-implement-rpi.md):

```
progress.md
├─ Goal: [Feature description]
├─ Completed Steps: [✓] step list
├─ Current Step: [→] active step
├─ Remaining Steps: [ ] future steps
└─ Current Issue: [blocker if any]
```

### Annotated Living Documents (Burleigh Pattern)

Tyler Burleigh's annotation approach treats plan documents as shared mutable state between human and agent (source: research-plan-implement-review-tyler-burleigh.md):

1. Agent produces initial plan
2. Human adds inline annotations directly into the document
3. Agent updates based on annotations
4. Repeat until aligned

**Design rule**: Plan documents should be designed for annotation — use clear section headers, avoid dense prose, prefer lists that are easy to comment within.

## Skill Routing and Auto-Loading

Effective harnesses route to the right skill automatically based on context (source: building-agent-harness-martin-richards.md):

- Saying "create a spec for user auth" → agent matches to `spec:research`
- Working in a FastAPI project → FastAPI-specific skill auto-loads
- Working in a Drizzle project → Drizzle-specific skill auto-loads

**Design principle**: Skills should be discoverable by description, not just by exact name. The harness orchestrator component (e.g., `spec:orchestrator` in Atelier) handles this routing.

## Backflow and Non-Waterfall Design

Effective harnesses explicitly support backflow between phases — they are not waterfall (source: building-agent-harness-martin-richards.md):

```
Research ←→ Human annotation ←→ Research (repeat)
    ↓
Plan ←→ Human annotation ←→ Plan (repeat)
    ↓
Implement → finds gap → Plan (update and continue)
    ↓
Finish (validate + review)
```

**Design rule**: Implementation finding gaps in the plan and pushing back is expected and healthy. The harness should make going back to update the plan easy, not feel like a failure.

## Multi-Model Specialization

As harnesses scale, different components should use different models (source: research-plan-implement-review-tyler-burleigh.md):

| Component Type | Model Recommendation | Reason |
|----------------|---------------------|---------|
| Research | Strongest available | Requires synthesis and judgment |
| Planning | Strongest available | Requires synthesis and judgment |
| Implementation | Faster/cheaper | Guided by plan, largely mechanical |
| Review | Different from implementer | Uncorrelated error profiles catch more bugs |

**Design rule**: Model selection should be a harness configuration, not a per-session manual choice.

## Iterative Harness Evolution

Building a harness is itself an iterative process. Known failure patterns to avoid (source: building-agent-harness-martin-richards.md):

**Avoid rigidity (v1 mistake):** Subagents chained in strict waterfall sequence work in narrow cases but can't handle the back-and-forth that real development requires.

**Avoid over-ceremony:** Delta tracking with explicit `ADDED`/`MODIFIED`/`REMOVED` markers felt precise but became too ceremonial in practice.

**Start minimal:** Begin with the research → plan → implement loop. Get it working well before adding advisory or utility layers. The discipline matters more than the sophistication.

## Related pages

- [[agent-harness]]
- [[harness-engineering]]
- [[agentic-engineering-workflow]]
- [[rpi-workflow]]
- [[rpir-workflow]]
- [[context-engineering]]
- [[subagents]]
- [[progressive-disclosure]]
- [[agent-workflows]]
- [[agent-best-practices]]
- [[agentic-software-modernization]]
