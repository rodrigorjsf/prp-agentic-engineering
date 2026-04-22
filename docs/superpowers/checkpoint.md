1. ADD GRAPHiFY DOC

/graphify add https://medium.com/the-ai-forum/harness-engineering-building-the-operating-system-for-autonomous-agents-1e20c105f689

2. Update plan based on new docs


3. Execute PLAN
Continue from the PRP harness planning session in `rodrigorjsf/prp-agentic-engineering`.
 
 ## Goal
 
 Implement the verified plan to evolve `plugins/prp-core/` into a clearer, lower-rot, better-tested PRP harness with:
 - shared harness references,
 - stronger context-budget and delegation contracts,
 - selective HumanLayer-inspired agent prompt structure,
 - a repo-only prompt-evaluation harness,
 - reconciled mirror rules/docs,
 - updated plugin documentation.
 
 ## Source artifacts
 
 Read these first:
 1. `docs/superpowers/specs/2026-04-21-prp-core-harness-evolution-design.md`
 2. `docs/superpowers/plans/2026-04-21-prp-core-harness-evolution.md`
 3. `plugins/prp-core/README.md`
 4. `plugins/prp-core/CLAUDE.md`
 
 Session plan mirror:
 - `/home/rodrigo/.copilot/session-state/8ec3a2e2-bf12-44f0-b4aa-120d3d399ae6/plan.md`
 
 ## Verified decisions
 
 - `plugins/prp-core/` is the shipped boundary. Root `.claude/` is a development mirror.
 - Repo-only eval assets must stay outside the shipped plugin payload.
 - HumanLayer is a **structural prompt-design comparator only**. Reuse one-job / hard-boundary / strategy / output-format patterns where useful. Do **not** import 
HumanLayer runtime, repo, or tool assumptions.
 - Mirror overlap already exists in:
   - `.claude/rules/artifact-paths.md`
   - `.claude/rules/agent-conventions.md`
   - `.claude/hooks/README.md`
   Reconcile these with the new shared references so there is one source of truth.
 - The research-team hook and skill must keep the same 6 required sections:
   - `## Research Question`
   - `## Research Question Decomposition`
   - `## Team Composition`
   - `## Research Tasks`
   - `## Team Orchestration Guide`
   - `## Acceptance Criteria`
 
 ## Graphify-grounded constraints
 
 The plan was verified with fresh graph queries. Keep these findings in mind:
 - Strong support exists for:
   - staged research → plan → implement → validate flow,
   - progressive disclosure,
   - bounded artifacts,
   - subagent isolation,
   - strict tool use / structured outputs for deterministic contracts.
 - The current graph shows **no direct path**:
   - from `Smart/Warm/Dumb Zone` to `HumanLayer Repository Analysis`,
   - from `Progressive Disclosure` to `Programmatic Tool Calling`.
   Treat those as separate evidence streams unless new graph evidence appears.
 - The plan already includes graphify grounding queries. Use them during implementation instead of making unsupported claims.
 
 ## Current task state
 
 No implementation has started yet. Planning and verification are done.
 
 Ready todo:
 - `shared-harness-contracts` — create shipped + mirror reference files:
   - `plugins/prp-core/references/harness-taxonomy.md`
   - `plugins/prp-core/references/context-budget-policy.md`
   - `plugins/prp-core/references/execution-policy.md`
   - `plugins/prp-core/references/artifact-lifecycle.md`
   - `plugins/prp-core/references/agent-prompt-style.md`
   - mirror copies under `.claude/references/`
 
 Blocked later tasks depend on that first phase.
 
 ## Implementation order
 
 Follow the plan order:
 1. Shared harness contracts
 2. Repo-only prompt evaluation harness
 3. Skill + agent contract refactors
 4. Guardrail consolidation
 5. Documentation refresh
 
 ## Important plan details
 
 - The implementation plan includes explicit graphify queries near the top and at each phase.
 - Do not leak repo-only script paths into shipped skills.
 - Keep shipped and mirror files aligned where the plan says they must match.
 - Prefer shared references over repeated inline policy text.
 - Keep root/project instructions lean to protect the smart zone.
 
 ## First action
 
 Start with **Task 1** from `docs/superpowers/plans/2026-04-21-prp-core-harness-evolution.md`, update todo status before working, and implement the shared 
reference layer in both `plugins/prp-core/references/` and `.claude/references/`.