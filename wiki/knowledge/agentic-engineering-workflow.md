# Agentic Engineering Workflow

**Summary**: A synthesized overview of the Research-Plan-Implement (RPI) agentic engineering workflow pattern, showing how it independently emerged across multiple practitioners and organizations as the reliable answer to unstructured "vibe coding" with AI agents.
**Sources**: `docs/agentic-engineering/research-plan-implement-rpi.md`, `docs/agentic-engineering/research-plan-implement-review-tyler-burleigh.md`, `docs/agentic-engineering/building-agent-harness-martin-richards.md`, `docs/agentic-engineering/agentic-software-modernization-markus-harrer.md`
**Last updated**: 2026-04-21

---

## The Core Pattern

Across independent practitioners, organizations, and use cases, one workflow pattern emerged consistently as the reliable foundation for AI-assisted software development:

**Research → Plan → Implement** — with fresh context windows between each phase, human review at the highest-leverage checkpoints, and written artifacts as persistent sources of truth.

The convergence across unrelated teams is the strongest signal that the core insight is sound: **the bottleneck in AI-assisted development is not code generation — it's ensuring the model understands what to build before it starts** (source: research-plan-implement-review-tyler-burleigh.md).

## Why This Pattern Exists

### The Context Window Constraint

AI models are stateless. They only know what exists in their current context window. When that window becomes too full — above ~40% utilization per HumanLayer — the model enters a "Dumb Zone" where response quality degrades rapidly and hallucinations increase (source: agentic-software-modernization-markus-harrer.md).

This is the root cause that drives the workflow design. Every structural choice in the RPI pattern — fresh sessions per phase, compacted artifacts, subagent isolation — exists to manage context quality. See [[context-engineering]] for the full treatment.

### The Error Compounding Problem

Without structure, errors compound:

| Error Location | Downstream Impact |
|----------------|-------------------|
| Bad research | 1,000s of bad lines of code |
| Bad plan | 100s of bad lines of code |
| Bad code | 1 bad line of code |

This leverage model explains why reviewing ~400 lines of specification artifacts (200 research + 200 plan) delivers more value than reviewing 2,000 lines of generated code (source: research-plan-implement-rpi.md). Shift human review left, to the phases where errors are still cheap.

### The Vibe Coding Failure Mode

Without structure, AI coding tends to go the same way: give the model a prompt, it produces something close but not quite right, and you spend the rest of the session correcting it. As complexity grows, the back-and-forth compounds — the model carries forward bad assumptions, the context window fills with failed attempts, and you end up doing most of the work yourself (source: research-plan-implement-review-tyler-burleigh.md).

## Implementations of the Pattern

The same core pattern appears under different names and with different emphases:

| Implementation | Authors | Key Emphasis | Artifact Names |
|----------------|---------|--------------|----------------|
| [[rpi-workflow]] | Dex Horthy / HumanLayer | Context window management, FIC methodology | `research_doc.md`, `implementation_plan.md` |
| [[rpir-workflow]] | Tyler Burleigh | Explicit review sessions, multi-model scaling | `RESEARCH.md`, `PLAN.md`, `PLAN-CHECKLIST.md` |
| Atelier ([[agent-harness]]) | Martin C. Richards | Skill-based harness, annotation cycles | `spec.md`, `plan.json` |
| [[agentic-software-modernization]] | Markus Harrer | Legacy system constraints, codebase hygiene | `state.md`, traceability comments |

All converge on the same observation: the discipline matters more than the tools. The harness, workflow, or methodology just encodes that discipline so you don't have to remember it each time (source: building-agent-harness-martin-richards.md).

## Phase-by-Phase Structure

### Research Phase

**Goal**: Understand the codebase structure and information flow before touching any code.

**Key practices**:
- Use [[subagents]] for noisy operations (glob, grep, file reads) in isolated contexts
- Start with a fresh context window containing only the problem definition
- Output a compacted artifact (~200 lines) capturing: relevant files, information flow, key findings, recommended approach

**Human leverage**: Highest. A mistake here creates thousands of lines of incorrectly architected code downstream (source: research-plan-implement-rpi.md).

**Anti-pattern**: Letting the agent jump directly to implementation. "Never let Claude write code until you've reviewed and approved a written plan" (source: building-agent-harness-martin-richards.md).

### Plan Phase

**Goal**: Convert research findings into a precise, ordered implementation blueprint.

**Key practices**:
- Start with a fresh context window containing only the research artifact and problem definition
- Define numbered, sequential steps with exact file paths and function signatures
- Include testing and verification procedures
- For legacy systems, target rule-based change recipes over non-deterministic agentic workloads (source: agentic-software-modernization-markus-harrer.md)

**Human leverage**: High. A mistake here creates hundreds of lines in wrong locations or wrong patterns.

### Implement Phase

**Goal**: Execute the plan with minimal deviation.

**Key practices**:
- Start with a fresh context window containing only the implementation plan
- Run tests after each step
- Use `progress.md` to track state across context resets for complex tasks
- Apply [[progressive-disclosure]] — load only what the current step needs
- Active context compaction: when an agent strays, summarize to `state.md` and start a fresh chat rather than correcting in-context (source: agentic-software-modernization-markus-harrer.md)

**Human leverage**: Lowest at this phase — but review loops with Critic Agents can catch issues mechanically (source: agentic-software-modernization-markus-harrer.md).

## Key Supporting Practices

### Fresh Context Windows Between Phases

Every phase transition should begin a new context window. Carrying forward the previous phase's exploration noise contaminates the context and degrades the model's reasoning. This is especially critical when correcting mistakes — correcting in-context is almost always wrong (source: research-plan-implement-review-tyler-burleigh.md).

### Written Artifacts as Shared Truth

Artifacts persist across sessions and give the model a clear reference point. Without them, context is lost between sessions and the model has to re-infer your intent every time (source: research-plan-implement-review-tyler-burleigh.md).

### Subagent Isolation

During the Research phase, [[subagents]] perform noisy discovery operations in isolated contexts and return only compacted summaries to the main context. This is the primary [[context-engineering]] tool for preventing context pollution from file search operations (source: research-plan-implement-rpi.md).

### Multi-Model Role Specialization

As workflows scale, different models handle different roles. Research, planning, and review require synthesis and judgment — use your strongest model. Implementation guided by a detailed plan is largely mechanical — use a faster, cheaper model. Models with different architectures produce largely uncorrelated errors, so using different models for implement and review catches more bugs (source: research-plan-implement-review-tyler-burleigh.md).

### Harness Engineering

The workflow should be encoded in a [[agent-harness]] — a set of skills, workflows, and methodology — so the discipline doesn't have to be remembered each time. LangChain improved their agent from 52.8% to 66.5% on Terminal Bench 2.0 by only changing the harness, keeping the model fixed (source: building-agent-harness-martin-richards.md).

## Autonomous Scaling

The workflow scales from human-in-the-loop to near-fully-autonomous depending on plan detail (source: research-plan-implement-review-tyler-burleigh.md):

| Plan detail | Safe autonomy level |
|-------------|---------------------|
| High-level goal | Human-in-the-loop for every step |
| Phased plan with architecture decisions made | Autonomous per phase, review between phases |
| Detailed plan with file paths and function signatures | Autonomous implementation, human reviews PR |
| Exact specifications with test cases | Fully autonomous with automated verification |

## Related pages

- [[rpi-workflow]]
- [[rpir-workflow]]
- [[agent-harness]]
- [[agent-harness-design]]
- [[agentic-software-modernization]]
- [[claude-cookbook]]
- [[context-engineering]]
- [[subagents]]
- [[progressive-disclosure]]
- [[agent-workflows]]
- [[agent-best-practices]]
- [[mcp-specification]]
