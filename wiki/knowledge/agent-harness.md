# Agent Harness

**Summary**: An agent harness is a set of skills, workflows, and methodology that teaches an AI agent how you think and how you build — and building one well matters more than which model you choose, as demonstrated by LangChain's 52.8% → 66.5% Terminal Bench improvement using the same model with a better harness.
**Sources**: `docs/agentic-engineering/building-agent-harness-martin-richards.md`
**Last updated**: 2026-04-22

---

## Overview

Martin C. Richards argues that agent productivity depends less on which AI model you use and more on how you "harness" it. The agents that produce good work are the ones that know how their operator works — conventions, patterns, preferences. The ones that fail are the ones dropped into a codebase with no context and expected to read minds (source: building-agent-harness-martin-richards.md).

The insight is blunt: complaining that an agent wrote bad code without giving it context is like calling a new hire incompetent on their first day because they didn't already know your codebase.

For the broader synthesis of the newer harness-engineering corpus, see [[harness-engineering]].

For design patterns behind building harnesses, see [[agent-harness-design]]. For how harnesses implement [[rpi-workflow]] and [[rpir-workflow]], see those pages.

## Harness > Model

LangChain improved their coding agent from **52.8% to 66.5%** on Terminal Bench 2.0 by only changing the harness, keeping the model fixed. Same model, better harness, better results (source: building-agent-harness-martin-richards.md).

Mitchell Hashimoto named this practice **harness engineering** in February 2026. OpenAI and Martin Fowler (Thoughtworks) subsequently adopted the term.

- **Hashimoto's definition (reactive):** Anytime an agent makes a mistake, engineer a fix so it doesn't happen again.
- **Richards' definition (proactive):** A harness is a set of skills, workflows, and methodology that teaches your agent how you think and how you build. It makes success the more likely outcome rather than the lucky one.

## The Core Pattern: Independent Discovery

The research → plan → implement loop was independently discovered across multiple practitioners (source: building-agent-harness-martin-richards.md):

- **[[rpi-workflow]] (HumanLayer)** — Research → Plan → Implement, with explicit context compaction
- **[[rpir-workflow]] (Superpowers, 40k+ stars)** — Same shape with review cycles
- **Atelier (Richards)** — Annotation cycle before code is written

Boris Tane's formulation captures the core principle:

> Never let Claude write code until you've reviewed and approved a written plan.

His annotation cycle: research the codebase, write a plan in markdown, **annotate the plan back and forth until it's right**, then implement. The plan becomes shared mutable state between you and the agent.

The convergence says more about the pattern than about any one implementation. **The harness doesn't need to be complicated. It needs to exist.**

## Atelier: Richards' Implementation

Atelier implements the research → plan → implement loop through four sequential skills (source: building-agent-harness-martin-richards.md):

**`spec:research`** — Explores the codebase, reads existing patterns, surfaces relevant context, and produces `spec.md`. The research artifact everything downstream depends on.

**`spec:plan`** — Takes the research and breaks it into tasks, producing `plan.json`. A good plan means the agent can commit to a specific approach and execute without constant course-correction. A bad plan means expensive mid-implementation back-and-forth.

**`spec:implement`** — Executes the plan with TDD. Each task gets built, tested, verified.

**`spec:finish`** — Validates the whole implementation and runs a review pass.

**`spec:orchestrator`** — Handles skill routing, deciding which skill to load based on what you're doing.

```
graph LR
    R[spec:research] --> P[spec:plan]
    R -- "review & annotate" --> H[human]
    H -- "update spec" --> R
    P --> I[spec:implement]
    I --> F[spec:finish]
    I -- "gaps found" --> P
```

**This isn't waterfall.** Backflow is expected. You review the research, annotate it, and loop with the agent until the spec is right. Implementation can still find gaps in the plan and push back — that's what separates it from rigid spec-driven development that breaks when reality arrives (source: building-agent-harness-martin-richards.md).

## Harness Component Types

Atelier has 34 skills organized into three namespaces that reflect different types of harness components (source: building-agent-harness-martin-richards.md):

**`spec:` skills — Sequential, artifact-producing.** They produce documents, plans, code. They're meant to be followed closely and invoked explicitly or triggered by a previous skill.

**`oracle:` skills — Advisory, context-adaptive.** `oracle:architect` applies DDD patterns and thinks about component responsibilities. `oracle:challenge` pushes back on your approach and pokes holes in your design. These adapt to context rather than following a rigid procedure.

**`code:` skills — Utilities.** Review, commit, the kind of thing you reach for when you need it.

> A spec workflow needs structure and artifacts, a thinking tool should adapt, and a commit helper just needs to work when called. Collapsing everything into one format loses that distinction.

Skills auto-load when relevant. Say "create a spec for user auth" and the agent matches that to `spec:research`. Language-specific skills (Drizzle, Fastify, FastAPI, SQLAlchemy) activate based on what you're working in (source: building-agent-harness-martin-richards.md).

## Evolution of Atelier

Understanding the evolution helps avoid known dead-ends (source: building-agent-harness-martin-richards.md):

**August 2025 (v1):** Rigid. Subagents chained in sequence, waterfall-style. Context-reader feeds requirements-gatherer feeds spec-writer. Worked narrowly but couldn't handle the back-and-forth real development requires.

**January 2026:** Moved to a living `spec.md` model with delta tracking for brownfield changes (`ADDED`, `MODIFIED`, `REMOVED` markers). Closer, but still too ceremonial.

**Current version:** Dropped the ceremony. Skills changed the paradigm — before skills, you had agents, commands, and reference docs, and tried to chain them yourself. Skills let you capture knowledge in a form the agent can find on its own. Describe what you want to do, and the agent loads the relevant skill by context.

## Building Your Own Harness

Install Atelier if you want: `npx skills add martinffx/atelier`. Or grab specific skills: `npx skills add martinffx/atelier --skill spec:research`.

But the real suggestion is to **build your own.** The value of Atelier isn't in the specific skills — it's in the idea that your agent's harness should be engineered with the same care as the software it produces (source: building-agent-harness-martin-richards.md).

Start with the research → plan → implement loop. Get that working in your own way. Add skills for how you write code, how you test, how you think about design.

> The discipline matters more than the tools. The harness just encodes that discipline so you don't have to remember it each time.

## Related pages

- [[agent-harness-design]]
- [[harness-engineering]]
- [[rpi-workflow]]
- [[rpir-workflow]]
- [[agentic-engineering-workflow]]
- [[agent-best-practices]]
- [[subagents]]
- [[context-engineering]]
- [[progressive-disclosure]]
- [[agent-workflows]]
