# Agentic Software Modernization

**Summary**: Agentic AI can genuinely modernize legacy software (COBOL, RPG, etc.), but only with disciplined preparation — the [[rpi-workflow]], active context compaction, iterative critic-agent loops, codebase hygiene investment, and strict traceability links from new code back to original business logic.
**Sources**: `docs/agentic-engineering/agentic-software-modernization-markus-harrer.md`
**Last updated**: 2026-04-21

---

## Overview

Markus Harrer's analysis draws on Stanford studies (120k+ developers) and leading AI engineering firms (OpenHands, HumanLayer) to argue that agentic AI can automate exhausting software modernization, but not the way most people imagine. Simply unleashing AI agents on an old codebase and hoping for a miracle is a recipe for disaster (source: agentic-software-modernization-markus-harrer.md).

Successful Agentic Software Modernization requires a fundamental shift: **away from vibe coding towards disciplined preparation and execution.**

## The Core Problem: The Context Bottleneck

AI models (LLMs) are stateless — they only know what exists in their current context window. In complex legacy systems, it is impossible to fit the entire context (millions of lines of code, dependencies, business logic) into this window (source: agentic-software-modernization-markus-harrer.md).

When the window becomes too full (above ~40% utilization per Dex Horthy of HumanLayer), the model enters the **'Dumb Zone'** where response quality degrades rapidly and hallucinations increase. See [[context-engineering]] for strategies to manage this constraint.

A more fundamental problem identified by Stanford studies is **Entropy**: when AI agents work within existing low-quality codebases, the produced code mirrors the low standards of the existing environment — creating a death spiral that automates the creation of technical debt rather than eliminating it (source: agentic-software-modernization-markus-harrer.md).

The art of Agentic Software Modernization is not about generating more legacy code faster, but about **surgically managing the AI agent's access to the right context** to understand and improve the system.

## Emerging Practices

### 1. Implement the RPI Workflow

The biggest trap is letting the agent code immediately. Instead, divide the process into strict phases (source: agentic-software-modernization-markus-harrer.md):

**Phase 1 — Research (Understanding):** The agent analyzes only the existing codebase to understand how a feature works. Output is not code but a summary explaining where relevant logic resides. Data-driven software analytics can help analyze large-scale systems. Enriching the codebase summary beforehand (signaling outdated parts, no-go areas, code that fits current system ideas) guides the agent more precisely.

**Phase 2 — Plan (Intent Compression):** Based on the research, the agent creates a detailed plan of which files need to be changed and how. This plan represents the "compressed intent" of the modification. In the best case, scope down activities enough to switch from **agentic workloads** (non-deterministic) towards **rule-based search-and-replace workloads** — letting an agent craft change recipes and execute those deterministically.

**Phase 3 — Implement (Coding):** Only now does the agent change or write code, based strictly on the approved plan or deterministic transformation rules.

> If the plan is non-existent, wrong, or too vague, 1,000 lines of generated code are worthless and tedious to review. Invest human intelligence in reviewing research and planning steps early — not just reviewing final code.

See [[rpi-workflow]] and [[rpir-workflow]] for detailed implementations of this pattern.

### 2. Use Iterative Refinement with Critic Agents

Never attempt a complex migration (e.g., COBOL to Java) in a single "One-Shot" prompt. The OpenHands team demonstrated this almost always leads to hallucinations (source: agentic-software-modernization-markus-harrer.md).

Instead, use an iterative loop with specialized roles:

- **Engineer Agent:** Attempts to solve the task (e.g., migrating code)
- **Critic Agent:** A separate agent that *only reads*. It analyzes generated code, runs tests, and provides harsh feedback with scores

The process: Engineer delivers → Critic evaluates and sends feedback → Engineer improves → Repeat until quality standard is met.

Leverage compilation errors, code duplication detection, and architectural violation checks as mechanical levers to guide the agent rather than relying solely on LLM judgment. This maps to the review phase in [[rpir-workflow]].

### 3. Invest in Codebase Hygiene First

Stanford data (Yegor Denisov-Blanch) shows a clear correlation (source: agentic-software-modernization-markus-harrer.md):

- **Clean environments** (high test coverage, good modularity, typing) → AI can autonomously drive a large share of sprint tasks
- **"Dirty" environments** (high entropy, technical debt) → AI struggles, produces more errors, and can accelerate technical debt (the "Rework" trap)

High-leverage hygiene moves before scaling AI:
- Rename cryptic one-letter variables to reflect actual technical or business domain
- Build out higher-level concepts or refactor towards well-known patterns/idioms
- Focus on safe refactorings that don't break code (most structural renames qualify)

### 4. Practice Active Context Compaction

When an agent strays off the path, the human impulse is to correct it within the same chat. **This is a mistake.** Every failed attempt clutters the context window with noise (source: agentic-software-modernization-markus-harrer.md).

The better approach — **active context compaction** (context reset):

1. Have the agent summarize the current state and findings into a compact file (`state.md` or similar)
2. Start a completely new chat with a fresh context
3. Feed only the summary in as the starting point

This keeps the agent in the "Smart Zone" of its context window. See [[context-engineering]] and [[progressive-disclosure]] for the broader patterns behind this approach. For models with limited context windows (DeepSeek, Minimax, Moonshot), active context compaction and rigid external state management is essential for good results.

### 5. Maintain Traceability Links

When migrating legacy code (e.g., COBOL to Java), the connection to the original business logic must never be lost. OpenHands recommends that the agent insert comments in the new code linking exactly to the line numbers of the old code where that logic originated (source: agentic-software-modernization-markus-harrer.md).

When using graph analytics or creating flowcharts, ensure that line numbers, identifiers, or filenames are used in generated outputs so you can quickly verify they are not hallucinated.

## Traps to Avoid

### 1. Vibe Coding

"Vibe Coding" describes back-and-forth chatting guided more by feelings than specifications ("Make that prettier," "No, that feels wrong"). This leads to bloated context windows and confused models. AI Engineering in legacy system environments requires precision, not vibes (source: agentic-software-modernization-markus-harrer.md).

### 2. Underestimating Rework

Stanford studies show that while AI tools increase output (more Pull Requests), they often dramatically increase rework — time developers spend repairing or rewriting AI-generated code. Measuring only speed/volume misses the massive cost of quality assurance (source: agentic-software-modernization-markus-harrer.md).

### 3. Blind Line-by-Line Code Review

In a world where an agent can generate 20,000 lines of TypeScript in minutes, traditional human line-by-line review is no longer scalable. Dex Horthy's **Hierarchy of Leverage** states: **1 Bad Line of Plan == 100 Bad Lines of Code.** Shift human review "left" to the research results and plan, before code is even written (source: agentic-software-modernization-markus-harrer.md).

In the research stage, look for rule-based changes — most structural changes are equal over the completed codebase. Review change pattern by change pattern, not line by line.

### 4. Expecting Magic in Niche Languages

AI model performance depends heavily on training data. For popular languages (Python, Java, JavaScript) they work excellently. For niche languages or old dialects (specific COBOL variants, obscure DSLs, RPG), AI can actually **decrease productivity** — the agent hallucinates and humans spend all their time correcting it (source: agentic-software-modernization-markus-harrer.md).

Check StackOverflow tags and the TIOBE programming popularity index. Every language not in the top 10 for the last few years needs a different approach: broader reverse engineering towards specs or tests, or a traditional transpiler approach to convert the niche language to a more popular language that an AI agent can then work with.

## The Role Shift: From Coder to Architect of Intent

Agentic Software Modernization works, but it requires discipline. The role of the human developer is shifting — we are becoming less writers of syntax and more the **architects of the intent** (source: agentic-software-modernization-markus-harrer.md).

Think of AI agents in legacy systems as new senior developers that can do amazing things but need decent onboarding: step-by-step introduction to the system, background context on the existing code, and careful introduction to the nasty parts of the systems over time.

> Those who just click "Refactor all this" will end up in chaos.

## Related pages

- [[rpi-workflow]]
- [[rpir-workflow]]
- [[agentic-engineering-workflow]]
- [[agent-harness]]
- [[agent-harness-design]]
- [[context-engineering]]
- [[progressive-disclosure]]
- [[agent-best-practices]]
- [[agent-workflows]]
- [[subagents]]
