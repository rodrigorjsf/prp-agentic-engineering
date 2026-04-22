# PRP Core Harness Evolution Design

**Status:** Draft for review  
**Scope:** `plugins/prp-core/` shipped plugin, mirrored `.claude/` assets, and repo-only evaluation/docs surfaces  
**Primary goal:** Evolve the plugin into a clearer, faster, and more testable PRP harness without increasing context rot

## Problem

`prp-core` already covers planning, implementation, review, issue work, research, and Ralph loops. Its strongest flows use bounded briefs and clean-context handoffs. Its weakest flows still bundle orchestration, validation, reporting, and GitHub updates into one skill. The result is uneven context hygiene, repeated workflow logic, and no durable prompt-evaluation loop.

## Current-state snapshot

Three facts shape the design:

1. The shipped plugin is the real product boundary. `plugins/prp-core/` is the installable payload, and root `.claude/` is a development mirror with extras.
2. The plugin already has good building blocks. `prp-plan` and `prp-prd` prove that bounded briefs, clean-context writers, and specialist agents work well here.
3. The repo lacks a repeatable way to test prompt contracts. Today the plugin can evolve, drift, or regress faster than its docs can prove.

## Design principles

### 1. Keep the harness staged

The plugin should continue to model a staged workflow: research -> plan -> implement -> validate/review. Each phase should pass forward a compact artifact, not raw exploration chatter.

### 2. Separate component classes

The harness should distinguish:

- **Sequential artifact skills** that create durable outputs.
- **Advisory components** that challenge or refine decisions.
- **Utility components** that do one narrow job, such as commit, PR creation, or final verification.

This taxonomy should be explicit in docs and reflected in skill structure.

### 3. Treat context as a budget

The design should keep most workflows in the smart zone by default. That means minimal always-loaded instructions, isolated noisy work, bounded briefs, and explicit compaction points before each major handoff.

### 4. Make delegation policy explicit

The plugin should say when to stay inline, when to fan out to subagents, when to parallelize, and when a repo-only script is the right control surface for deterministic batch checks.

### 5. Borrow high-signal agent prompt structure selectively

HumanLayer's agent prompts are a good reference for structure, not for wholesale copying. Their strongest traits are:

- one explicit job per agent,
- hard negative boundaries,
- minimal tool access,
- named responsibilities,
- a short strategy section,
- a fixed output shape.

`prp-core` should adopt that structure where it makes existing agents clearer, especially the analysis, exploration, critique, and advisor agents. It should not import HumanLayer-specific repo assumptions, thoughts-directory concepts, or runtime behavior.
It should also preserve PRP-specific frontmatter and capabilities unless direct evidence shows a change is safe. The adaptation target is prompt structure, not HumanLayer's tool/runtime contract.

### 6. Test prompt contracts as code

The repo should gain a prompt-evaluation routine that checks workflow prompts, required references, hook section schemas, mirror parity, and key contract strings against fixtures. The harness should stop relying on manual spot checks alone.

### 7. Keep shipped payload lean

The installable plugin should ship user-facing skills, agents, hooks, and concise references. Repo-only evaluation helpers, fixture corpora, and CI scripts should stay outside the shipped payload.

## Target architecture

## A. Shared reference layer

Add a small shared reference layer for shipped behavior:

- `plugins/prp-core/references/harness-taxonomy.md`
- `plugins/prp-core/references/context-budget-policy.md`
- `plugins/prp-core/references/execution-policy.md`
- `plugins/prp-core/references/artifact-lifecycle.md`
- `plugins/prp-core/references/agent-prompt-style.md`

These files should hold cross-cutting policy once. Skills should point to them instead of repeating the same guidance in long form. The `.claude/` mirror should carry matching copies for local development.

## B. Context-budget contract for orchestration-heavy skills

Bring the bounded-brief pattern from `prp-plan` and `prp-prd` to the orchestration-heavy flows:

- `prp-implement`
- `prp-review`
- `prp-review-agents`
- `prp-issue-investigate`
- `prp-issue-fix`
- `prp-codebase-question`
- `prp-research-team`

Each should define:

- the maximum size of its intermediate summary,
- the point where noisy subagent output must be compacted,
- the conditions for parallel work,
- the conditions for falling back to a deterministic repo-only helper script.

## C. Repo-only prompt evaluation harness

Create a repo-only evaluation surface with:

- a script runner,
- scenario fixtures,
- contract definitions,
- an optional CI workflow.

This layer should verify both static contracts and golden-path workflow behavior. It should live outside the shipped plugin so the installable payload stays lean.

## D. Agent prompt normalization

Normalize the highest-leverage PRP agents against the HumanLayer-style structure:

- `plugins/prp-core/agents/codebase-analyst.md`
- `plugins/prp-core/agents/codebase-explorer.md`
- `plugins/prp-core/agents/plan-critic.md`
- `plugins/prp-core/agents/prp-advisor.md`
- `plugins/prp-core/agents/web-researcher.md`

The target is not new behavior. The target is a clearer contract: one job, explicit boundaries, minimal tools, a short strategy, and a stable output shape.
The normalization must stay structural. It must not silently drop PRP-specific `tools`, `maxTurns`, `skills`, or other frontmatter that the current plugin relies on.

## E. Documentation split

The plugin docs should move toward progressive disclosure:

- `plugins/prp-core/README.md` stays concise and user-facing.
- `plugins/prp-core/CLAUDE.md` stays package-scoped and brief.
- a repo doc explains the harness architecture, context policy, evaluation model, and research rationale.

This split keeps the install surface clean while preserving the why behind the design.

## F. Guardrails without rule sprawl

The design should prefer shared references and skill-local contracts over a pile of broad always-loaded rules. Add or expand rules only when path-scoped auto-loading is genuinely required, and reconcile existing mirror rules so they do not duplicate the new reference layer.

## What this design will change

- Clearer workflow ownership between artifact skills, advisory components, and utilities.
- More consistent context compaction across the shipped plugin.
- A documented delegation policy instead of skill-by-skill improvisation.
- A sharper and more uniform agent prompt design for the highest-leverage PRP agents.
- A repeatable static prompt-contract loop that also checks mirror parity and hook/schema alignment.
- Better docs that explain current state, research basis, and objectives without bloating the installable surface.

## What this design will not change

- It will not turn `prp-core` into a daemon- or UI-based product like HumanLayer.
- It will not ship a large eval corpus inside the plugin payload.
- It will not add broad root-level instruction bloat to `CLAUDE.md`.

## Success criteria

The evolution is successful when:

1. Orchestration-heavy skills use the same context-budget and delegation contract.
2. Shared workflow logic moves into concise shared references instead of being duplicated.
3. Repo-only prompt tests catch drift before docs and skill behavior diverge.
4. Plugin docs describe the shipped harness clearly, and link to deeper repo docs for rationale.
5. The shipped payload remains lean enough to avoid worsening context rot.
