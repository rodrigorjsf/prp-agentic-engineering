# RPI Workflow

**Summary**: The Research, Plan, Implement (RPI) workflow is a three-phase agentic engineering methodology developed by Dex Horthy at HumanLayer that structures AI coding work into sequential phases, each producing a compacted artifact, to maximize LLM output quality through disciplined context management.
**Sources**: `docs/agentic-engineering/research-plan-implement-rpi.md`
**Last updated**: 2026-04-21

---

## Overview

The RPI workflow is the operational backbone of the Frequent Intentional Compaction (FIC) methodology. It addresses the fundamental constraint that LLM output quality depends entirely on context quality — the model is a stateless function, so what's in the context window determines what comes out (source: research-plan-implement-rpi.md).

The three phases — Research → Plan → Implement — each produce a compacted artifact that becomes the sole input for the next phase. This structure eliminates context pollution and creates explicit human review checkpoints before errors can compound downstream. See [[rpir-workflow]] for Tyler Burleigh's extended version that adds an explicit Review phase.

## The Three Phases

### Phase 1: Research

The research phase begins with a **fresh context window** containing only the problem definition. [[subagents]] perform noisy operations (glob, grep, file reads) in isolated contexts, returning compacted summaries to prevent contaminating the main context with raw search noise (source: research-plan-implement-rpi.md).

**Output artifact**: `research_doc.md` (~200 lines)
**Context consumption**: High (file searches, code reading)
**Human review leverage**: ⭐⭐⭐⭐ (highest)

The research document captures:
- Problem summary
- Relevant files identified
- Information flow analysis (e.g., `parse() → validate() → execute_test()`)
- Key findings
- Recommended approach

### Phase 2: Plan

The plan phase starts with a **clean context window** containing the research document and the original problem definition. No raw file contents or search results pollute the context at this stage (source: research-plan-implement-rpi.md).

**Output artifact**: `implementation_plan.md` (~200 lines)
**Context consumption**: Medium (research doc + architecture analysis)
**Human review leverage**: ⭐⭐⭐ (high)

The plan document captures:
- Numbered, sequential implementation steps
- Exact file paths to modify
- Function signatures and integration points
- Testing and verification procedures

### Phase 3: Implement

The implementation phase starts with a **clean context window** containing only the implementation plan. For complex tasks requiring multiple [[context-engineering]] compaction cycles, the agent updates `progress.md` to track state across context resets (source: research-plan-implement-rpi.md).

**Output artifact**: Code files + tests
**Context consumption**: Low-Medium (plan doc + test outputs)
**Human review leverage**: ⭐ (lowest)

## The Leverage Model

The RPI workflow encodes a critical insight about error compounding (source: research-plan-implement-rpi.md):

| Error Location | Downstream Impact |
|----------------|-------------------|
| Bad research | 1,000s of bad lines of code |
| Bad plan | 100s of bad lines of code |
| Bad code | 1 bad line of code |

This means reviewing ~400 lines of specification artifacts (200 research + 200 plan) delivers more value than reviewing 2,000 lines of generated code. The leverage is highest at the earliest phases.

## Human Review Checkpoints

**Checkpoint 1 — Research Document**: Verify correct understanding of codebase structure, that relevant files are identified, and that information flow analysis is accurate. Cost of error: thousands of incorrectly architected lines.

**Checkpoint 2 — Implementation Plan**: Verify sound architectural approach, appropriate file selections, and complete testing strategy. Cost of error: hundreds of lines in wrong locations or wrong patterns.

**Checkpoint 3 — Code Review (Optional)**: Mental alignment with team, understanding of what changed and why. Cost of error: 1–10 lines of incorrect code (source: research-plan-implement-rpi.md).

## Progress Compaction for Complex Tasks

When implementation spans multiple context resets, `progress.md` tracks state:

```
progress/feature_progress.md
├─ Goal: Add cancellation support
├─ Completed Steps
│  ├─ [✓] Step 1: Add CancelToken struct
│  └─ [✓] Step 2: Thread token through runtime
├─ Current Step
│  └─ [→] Step 3: Integrate with async runtime
└─ Remaining Steps
   └─ [ ] Step 4: Add WASM bindings
```

This is a key [[context-engineering]] pattern: compact state before a context boundary rather than carrying forward a bloated history (source: research-plan-implement-rpi.md).

## Integration with FIC Methodology

| FIC Principle | Workflow Implementation |
|---------------|-------------------------|
| Context Quality = f(Correctness, Completeness, Size, Trajectory) | Research validates correctness; Plan ensures completeness; Phase boundaries control size |
| 40–60% Context Utilization | Each phase starts fresh at 10–15% utilization |
| Intentional Compaction | Phase transitions require explicit artifact creation |
| Human-in-the-Loop | Review gates at Research and Plan phases |
| Subagent Isolation | Research phase extensively uses [[subagents]] |

(source: research-plan-implement-rpi.md)

## Workflow Variations

While the canonical flow is Research → Plan → Implement, variations are common. The key principle is that each phase must produce a correctly-scoped, compacted artifact before the next phase begins. For a formalized review-augmented variant, see [[rpir-workflow]]. For the synthesized community perspective on this pattern, see [[agentic-engineering-workflow]].

## Related pages

- [[rpir-workflow]]
- [[agentic-engineering-workflow]]
- [[agent-harness]]
- [[agentic-software-modernization]]
- [[context-engineering]]
- [[subagents]]
- [[progressive-disclosure]]
- [[agent-workflows]]
- [[agent-best-practices]]
