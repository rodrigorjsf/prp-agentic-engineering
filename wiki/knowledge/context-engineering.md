# Context Engineering

**Summary**: The discipline of managing all context fed to an LLM — instructions, examples, retrieved data, tool outputs — to maximize signal density per token and minimize degradation from noise, staleness, and position effects.
**Sources**: research-context-engineering-comprehensive.md, research-context-rot-and-management.md, a-guide-to-agents.md, research-whitespace-and-formatting.md, context-engineering-most-important-skill-dev.md, advanced-context-engineering-coding-agents-dev.md, context-engineering-commercial-agents-jeremy-daly.md
**Last updated**: 2026-04-21

---

Context engineering has replaced "prompt engineering" as the dominant framing for working with LLMs. Where prompt engineering focuses on crafting a single input, context engineering manages the entire context window across turns, tools, and sessions.

## Core Principle

Every token must earn its place. The test: "Would removing this cause the agent to make mistakes?" If not, cut it. Irrelevant content actively harms reasoning — simple math accuracy drops from **0.92 → 0.68** with just 3,000 filler tokens (source: Levy et al., ACL 2024).

## The Token Budget

- Frontier LLMs follow ~**150–200 instructions** with consistency; smaller models handle fewer (source: Humanlayer research)
- Adding instruction N interacts with all existing instructions via **n² pairwise attention relationships** — context growth is superlinear in cognitive load
- Configuration files (CLAUDE.md, AGENTS.md) load on **every request** — bloat directly wastes budget
- Target under 200 lines per config file (~2,000–4,000 tokens)
- Comprehensive prompt compression achieves 4–20× reduction; naive minification destroys the structure compression preserves
- Practical threshold: reasoning quality degrades around **3,000 filler tokens** (Levy et al., ACL 2024)

## Position Effects (Lost in the Middle)

Performance follows a U-shaped curve across the context window:

| Position | Recall Quality                      | Recommendation                        |
| -------- | ----------------------------------- | ------------------------------------- |
| Start    | High (primacy effect)               | Critical instructions, system prompts |
| Middle   | 10–20% drop (Liu et al., TACL 2023) | Reference data, documents             |
| End      | High (recency effect)               | Queries, final instructions           |

Place long documents at the top and queries at the bottom — this exploits the primacy/recency effect and improves performance by ~30%.

### Deep Dive: The U-Shaped Performance Curve

Liu et al. (2024, TACL) formally established the [[u-shaped-attention-curve]] in a systematic study across multi-document QA (NaturalQuestions-Open, 20 documents) and synthetic key-value retrieval. Key quantitative findings (source: lost-in-the-middle-acl.md):

- Performance at the **center** (position 10 of 20) drops **over 20 percentage points** vs. the edges.
- The curve holds across every tested model — GPT-3.5-Turbo, Claude, Llama-2, MPT — with **no model immune**.
- Even models explicitly marketed as "long-context" retain the U-shaped bias.
- The effect is not dataset-specific: the same curve appears on synthetic key-value retrieval data.

For the full paper treatment, see [[lost-in-the-middle-paper]].

### The In-Between Compound Effect (Multi-Hop)

Baker et al. (2024, arXiv 2412.10079) extended the finding to multi-hop QA and discovered a second degradation axis: the *relative distance between* multiple evidence documents (source: lost-in-the-middle-and-in-between-arxiv.md):

- When two required evidence documents are **adjacent**, performance is consistently higher than when they are separated by distractor documents — **even when both are at the same absolute position**.
- This creates a 2D degradation surface: distance-from-edge × distance-between-evidence.
- The combinatorial explosion of position permutations (190 for 2-hop, 4,845 for 4-hop) makes re-ranking-based mitigations impractical for multi-hop settings.
- Chain-of-thought prompting improves document *identification* but does not resolve positional bias.

This "in-between" effect matters for [[agent-workflows]]: agentic multi-hop reasoning over retrieved documents faces both axes of degradation simultaneously. For the full paper treatment, see [[lost-in-the-middle-in-between]].

### Mitigation Strategies

The most effective mitigations, in order of practical utility (source: lost-in-the-middle-acl.md, lost-in-the-middle-and-in-between-arxiv.md):

1. **Position-aware placement** — Always place the most critical document first and the query last. Free; no additional compute; 20–30% improvement from ordering alone.
2. **Query-Aware Contextualization** — Place the query both before and after the document list. Highly effective for key-value retrieval; limited for complex QA.
3. **[[progressive-disclosure]]** — Load context in tiers; prevent large "middles" from forming architecturally.
4. **Document re-ranking** — Effective for single-hop; combinatorially intractable for multi-hop.
5. **Permutation self-consistency** — N× inference cost; intractable at 3+ hops.

For the full mitigation landscape, see [[long-context-mitigation]].

## Four Strategies for Context Management

1. **[[progressive-disclosure]]** — Load instructions conditionally (skills, path-scoped rules, subagent summaries) instead of dumping everything into the main prompt
2. **Compaction** — Summarize accumulated context when nearing the window limit. The lightest-touch approach is **tool result clearing** (replacing verbose tool outputs with summaries). For conversations, ask the model to summarize. The simplest approach matches sophisticated alternatives.
3. **Structured note-taking** — Agent writes notes persisted outside the context window (JSON state files, progress.txt, git commits). The agent can reload specific notes on demand rather than carrying all history in context. This is [[prompt-engineering]]'s state tracking applied to context management.
4. **[[subagents]]** — Route complex research to isolated contexts; return only summaries (1,000–2,000 tokens) instead of tens of thousands of exploration tokens. JIT documentation is a variant: let the agent generate docs during planning, then use those docs (not the raw exploration) in execution.

### Choosing a Strategy

| Symptom                                   | Strategy               |
| ----------------------------------------- | ---------------------- |
| Context grows large across many turns     | Compaction             |
| Agent forgets earlier decisions           | Structured note-taking |
| Single task needs deep exploration        | Subagents              |
| Instructions compete with data for tokens | Progressive disclosure |

## The 'Ball of Mud' Anti-Pattern

A common failure mode (documented in Anthropic's agent guide): the agent misbehaves → you add a rule → it misbehaves differently → you add another rule → the config becomes an unmaintainable mess. Auto-generated files compound this problem because they start large and rules only accumulate.

The fix is the **deletion test**: regularly review every instruction and ask "Would removing this cause the agent to make mistakes?" If removing it has no effect, it was noise. This connects directly to the [[evaluating-agents-paper]]'s finding that LLM-generated context files hurt performance.

## Formatting: Structure Over Minimalism

Whitespace is nearly free. A blank line costs 1 token (same as 4× blank lines). Structural formatting measurably improves output:

| Format           | Token Cost vs. Plain Text | Value                     |
| ---------------- | ------------------------- | ------------------------- |
| Markdown headers | +81%                      | Clear section boundaries  |
| XML tags         | +165%                     | Unambiguous delimiters    |
| YAML vs. JSON    | YAML saves ~30%           | Lower overhead for config |

Well-formatted 1,000-token prompt beats a wall-of-text 900-token prompt. Cut content, not formatting.

## The Five Pillars (Production Systems)

From production experience building real AI applications, context engineering has five operational pillars (source: context-engineering-most-important-skill-dev.md):

1. **Context Selection** — Every token must earn its place. Semantic retrieval with relevance filtering beats dumping everything in. Dynamic tool loading (4 tools vs. 50 reduces ~7,400 tokens of definitions) applies the same principle
2. **Context Structuring** — Same information structured differently produces dramatically different results. Exploit primacy and recency effects: critical instructions at start and end, less critical reference data in the middle
3. **Memory Architecture** — Three-tier model: working memory (context window), short-term memory (session store, 10–50 compressed entries), long-term memory (persistent store, effectively unlimited). See [[commercial-agent-context]] for the full taxonomy in multi-tenant systems
4. **Context Compression** — Summarization, semantic chunking, progressive summarization, key-value extraction. Makes more fit without losing signal
5. **Context Validation** — Validate token counts before sending, log what was included/excluded, monitor for context-related failures, A/B test context strategies

## The Research–Plan–Implement Workflow

A systematic approach to compaction at every stage (source: advanced-context-engineering-coding-agents-dev.md):

| Phase | Goal | Output |
|-------|------|--------|
| **Research** | Understand how the system *actually* works; identify authoritative files | Short research artifact; validated findings |
| **Plan** | List exact steps with concrete files/snippets and validation after each change | Solid plan that constrains agent behavior |
| **Implement** | Mechanical execution | Small context, high reliability |

Key insight: **Planning is the highest-leverage activity.** A solid plan dramatically constrains agent behavior. Bad plans produce dozens of bad lines. Bad research produces hundreds (source: advanced-context-engineering-coding-agents-dev.md).

This workflow works because it doesn't try to fit everything into one window — each phase gets a fresh, appropriately-scoped context.

## Context as Infrastructure (Commercial Systems)

In commercial multi-tenant agent systems, context engineering becomes infrastructure with three non-negotiables: structural tenant isolation, deterministic replay, and economic predictability per run (source: context-engineering-commercial-agents-jeremy-daly.md). See [[commercial-agent-context]] for the full framework.

The system prompt as a "desk" analogy: every component (system instructions, retrieved knowledge, tool definitions, conversation history, current query) competes for the same finite space. Add too much conversation history and you crowd out retrieved knowledge. Load too many tool definitions and you leave no room for examples (source: context-engineering-most-important-skill-dev.md).

## Related pages

- [[context-rot]]
- [[progressive-disclosure]]
- [[prompt-engineering]]
- [[whitespace-and-formatting]]
- [[multilingual-performance]]
- [[million-token-context-window]]
- [[dead-context]]
- [[agents-md-liability]]
- [[commercial-agent-context]]
- [[lost-in-the-middle-paper]]
- [[lost-in-the-middle-in-between]]
- [[u-shaped-attention-curve]]
- [[long-context-mitigation]]
- [[agent-workflows]]
