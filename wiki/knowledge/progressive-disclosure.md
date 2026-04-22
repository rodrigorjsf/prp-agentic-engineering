# Progressive Disclosure

**Summary**: An information architecture principle applied to LLM context management — load only what's needed for the current task, organized in tiers from always-loaded to on-demand to invoked, dramatically reducing token waste and improving agent focus.
**Sources**: a-guide-to-agents.md, Evaluating-AGENTS-paper.md, research-agent-workflows-and-patterns.md, research-context-engineering-comprehensive.md, progressive-disclosure-ai-agents.md
**Last updated**: 2026-04-22

---

Progressive disclosure is the single most impactful technique for managing agent configuration. The [[evaluating-agents-paper]] found that large, comprehensive configuration files *reduce* task success by ~3% while increasing costs by 20%+. Minimal, well-structured configurations outperform comprehensive ones.

## The Problem: Configuration Bloat

- Typical overgrown AGENTS.md: **600+ words, 9.7 sections** (AGENTBENCH data)
- All tokens in config files load on **every request**, regardless of relevance
- Frontier LLMs follow ~150–200 instructions consistently; beyond that, compliance degrades
- LLM-generated context files perform better when they are the **only** documentation (implies redundancy problem)

## Three Loading Tiers

| Tier          | Loaded When                         | Content                                                      | Budget                       |
| ------------- | ----------------------------------- | ------------------------------------------------------------ | ---------------------------- |
| **Always**    | Every request                       | Project description, build commands, critical invariants     | 15–40 lines (root CLAUDE.md) |
| **On-demand** | When matching files are touched     | Language-specific rules, component patterns, API conventions | 10–30 lines per rule file    |
| **Invoked**   | Explicitly called or auto-triggered | Full workflow instructions, reference material, templates    | Up to 500 lines per skill    |

## Implementation Patterns in the Current Docs

### Claude Code

- **Root CLAUDE.md** → Always loaded (target: 15–40 lines)
- **`.claude/rules/`** → Path-scoped rules with glob patterns; load only when matching files are read
- **Skills (SKILL.md)** → Invoked by name or auto-triggered by description match
- **[[claude-code-subagents]]** → Isolated context windows, return only summaries

## Ideal Target: The Minimal Config

The ideal AGENTS.md/CLAUDE.md is a **one-liner project description + package manager + build commands** (<10 tokens). Everything else belongs in scoped files:

```
This is a TypeScript React app. Use pnpm. Run tests with pnpm test.
```

Domain-specific rules go in separate files (e.g., `.claude/rules/typescript.md` with `paths: ["**/*.ts"]`).

## Monorepo Pattern

- Root config describes overall structure and shared conventions
- Package-level configs contain package-specific guidelines
- Agents navigate hierarchies efficiently without bloating the main prompt

## Evidence

The [[evaluating-agents-paper]] (ETH Zurich, 2026) measured:

- LLM-generated context: **−0.5% to −3%** success rate vs. no context, with **20–23% cost increase**
- Developer-provided context: **+4% average** success rate vs. no context
- Context files encourage broader exploration but don't improve direction-finding

## Four Implementation Patterns

From production experience with AI agent workflows, four core patterns implement progressive disclosure (source: progressive-disclosure-ai-agents.md):

### Pattern 1: Index-First Loading

Instead of loading reference files directly, start the agent with an index describing what files exist and what each contains. The agent reads the index, identifies which file it needs for the current subtask, then fetches only that file.

The index must be genuinely informative — not just a list of filenames, but structured descriptions of what each resource covers and *when* it's relevant. Works especially well for documentation-heavy workflows: API references, style guides, process documentation, schema files.

### Pattern 2: The Scout Pattern

Before loading any reference material, a lightweight pre-screening step assesses what the current task actually requires. A minimal-context scout analyzes the task, identifies relevant reference files, and returns a manifest. The main agent then loads only what the scout identified.

Especially useful when tasks arrive from external sources (user input, webhook triggers, upstream agent outputs) and you can't hardcode context requirements into the workflow.

### Pattern 3: Phase-Based Context Loading

Tasks with natural phases (research, planning, execution, review) have different context requirements per phase. Load context phase by phase, not all at once:
- **Research:** information-gathering tools and background documentation
- **Planning:** research output plus structural templates
- **Execution:** plan plus implementation references
- **Review:** output criteria plus the execution output

This matches the Research–Plan–Implement workflow described in [[context-engineering]].

### Pattern 4: Skill Files Without Embedded Reference Material

The common mistake: skill files containing both the process steps *and* the reference material those steps require. The better approach keeps skill files as pure process definitions — references listed but not embedded.

Your skill.md should describe *what to do*, not contain all the material needed to do it. That separation is what makes progressive disclosure possible at the skill level.

## Building a Context Trigger System

Progressive disclosure requires a mechanism for deciding when to load what. Three components (source: progressive-disclosure-ai-agents.md):

1. **Condition detection** — The agent (or governing layer) detects that specific content is needed. Can be explicit (a step says "load [reference-x] before proceeding") or inferred
2. **Fetch mechanism** — Something actually retrieves the content at task time, not at initialization. File read, retrieval call, sub-agent invocation, or database query
3. **Load confirmation and scoping** — Loaded content is scoped to the current task phase, not persisted indefinitely. Without scoping, progressive disclosure gradually becomes front-loading — material accumulates across steps until the window is as full as it would have been at the start

## The Context Rot Connection

Loading too much context at once causes [[context-rot]] through three mechanisms (source: progressive-disclosure-ai-agents.md):
- **Attention dilutes** — The model's ability to focus on what matters degrades as the window fills
- **Contradictions compound** — More context means more chances for earlier guidance to conflict with later guidance
- **Signal-to-noise ratio drops** — Irrelevant reference material actively competes for the model's attention, not just passively taking up space

The result is the **inverted U failure pattern**: more context initially helps output quality but then actively hurts it past a certain threshold.

## Progressive Disclosure in Multi-Agent Systems

Progressive disclosure scales well into multi-agent systems, where context management becomes even more critical (source: progressive-disclosure-ai-agents.md):

- An orchestrator routing tasks doesn't need access to API documentation that a code-generation sub-agent needs
- A review agent doesn't need the full research corpus that a synthesis agent worked from

The principle here is **context isolation between agents**, not just within a single agent's session. Each agent receives a context appropriate to its role, assembled just before it runs, rather than inheriting a shared bloated context from a parent orchestrator.

## When Progressive Disclosure Isn't the Right Tool

Not all tasks benefit from the overhead (source: progressive-disclosure-ai-agents.md):

- **Short, self-contained tasks** — If the entire task context fits comfortably in 5–10% of the context window, front-loading is simpler
- **Tasks with high interdependency** across reference materials — If step 3 depends on something from step 1's reference material, and both are needed simultaneously for step 4, a context compaction strategy may work better
- **Latency-sensitive workflows** — May not tolerate the overhead of dynamic fetching; pre-warming context for predictable task types is one approach

## Related pages

- [[context-engineering]]
- [[context-rot]]
- [[evaluating-agents-paper]]
- [[agent-configuration-files]]
- [[claude-code-memory]]
- [[agents-md-liability]]
- [[dead-context]]
