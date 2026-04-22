# AGENTS.md as a Liability

**Summary**: Research-backed analysis of why growing AGENTS.md (and CLAUDE.md) files beyond a certain size actively harm AI agent performance through attention dilution, primacy bias, and the dumb zone.
**Sources**: agents-md-is-a-liability-paddo.md, advanced-context-engineering-coding-agents-dev.md
**Last updated**: 2026-04-21

---

Every time an agent makes a mistake, you add a rule. Every edge case gets a line. Every convention gets documented. You're at 300 lines, then 500, then 1000. This makes performance worse, not better. See [[agent-configuration-files]] for the structural overview and [[context-rot]] for the underlying mechanisms.

## The 500 Instruction Ceiling

The IFScale benchmark (Distyl AI, NeurIPS 2025) tested 20 frontier models on instruction following at scale. Task: generate a business report including specific keywords, each keyword counting as one instruction, scaled from 10 to 500 (source: agents-md-is-a-liability-paddo.md).

**The best frontier model scored 68% at 500 instructions. One in three instructions simply got skipped.**

Three distinct degradation patterns emerged:

| Pattern | Models | Behavior |
|---------|--------|----------|
| Threshold decay | o3, Gemini 2.5 Pro | Near-perfect until 100–250 instructions, then cliff |
| Linear decay | GPT-4.1, Claude Sonnet 4 | Steady, predictable decline from the start |
| Exponential decay | GPT-4o, LLaMA-4-Scout | Rapid collapse |

Every model showed **primacy bias**: earlier instructions receive more attention than later ones. As instruction density increases, errors shift from *modification* (doing it wrong) to *omission* (not doing it at all). **The model doesn't misinterpret your 400th rule. It doesn't see it** (source: agents-md-is-a-liability-paddo.md).

## Five Compounding Architectural Problems

### 1. Lost in the Middle

Stanford and Meta's 2023 research (TACL 2024) documented the U-shaped attention curve. Models attend strongly to the beginning and end of context; the middle is a dead zone. With 20 documents in context, placing the answer in the middle dropped accuracy by 20+ points. In one case, GPT-3.5-Turbo performed *worse with context than without it* — adding information actively hurt the model (source: agents-md-is-a-liability-paddo.md).

### 2. The Dumb Zone

Dex Horthy (HumanLayer) coined this after analyzing 100,000+ developer sessions. Past roughly 40% of context capacity, "the model starts drifting, hallucinating, and forgetting its own instructions." This is how attention works — token relationships scale quadratically. Each additional token makes every other token slightly harder to attend to (source: agents-md-is-a-liability-paddo.md).

> The more you use the context window, the worse the outcomes you'll get. — Dex Horthy, HumanLayer

### 3. Context Rot

Chroma Research identified three compounding mechanisms: lost-in-the-middle positional bias, attention dilution (softmax spreads attention thinner as context grows), and distractor interference (semantically similar but irrelevant content causes hallucinations). **Critical finding: degradation happens at every context length increment, not just near the limit. A 1M token window still rots at 50K tokens** (source: agents-md-is-a-liability-paddo.md). See [[context-rot]].

### 4. Attention Sinks

Xiao et al. (ICLR 2024) showed initial tokens receive disproportionate attention regardless of semantic content. Replace your first tokens with newline characters and the effect persists — it's positional, not semantic. **This is why instructions at the top of your AGENTS.md get followed more reliably: they're sitting on the attention sink** (source: agents-md-is-a-liability-paddo.md).

### 5. Attention Dilution

The transformer's softmax attention is a zero-sum game. Attention weights are positive and sum to 1. More tokens means less attention per token. **You can't add context without diluting attention to existing context.** Every line in your AGENTS.md competes with every other line for the model's focus (source: agents-md-is-a-liability-paddo.md).

## The Repetition Hack (and Its Limits)

Google Research (December 2025): repeating the prompt as `<QUERY><QUERY>` instead of `<QUERY>` yielded 47 wins out of 70 benchmark-model combinations, 0 losses. Gemini 2.0 Flash-Lite jumped from 21% to 97% on middle-of-list retrieval (source: agents-md-is-a-liability-paddo.md).

The mechanical explanation: autoregressive models process left to right; causal masking means each token can only attend to preceding tokens. When the model first reads instructions, it's blind to the following context. By repeating instructions after the context, the second copy can attend to everything — simulating bidirectional attention within a unidirectional architecture.

This is already used in production: Claude Code injects `<system-reminder>` tags throughout tool results; Claude.ai uses `<long_conversation_reminder>` tags. The downside: repetition eats context, which triggers the very problems you're trying to solve (source: agents-md-is-a-liability-paddo.md).

## What This Means for Your AGENTS.md

Actionable principles from the research convergence (source: agents-md-is-a-liability-paddo.md):

- **Shorter is better** — Every additional instruction dilutes attention to all others. A 200-line file with 5 critical rules is worse than a 50-line file with the same 5 rules and less noise
- **Front-load and back-load** — Primacy bias and recency bias are both real. Your most important rules belong at the very beginning and end. The middle is where rules go to die
- **Modularize** — Claude Code's Skills system, path-specific rules, and lazy-loaded context exist for a reason. Don't stuff everything into one file. Load domain-specific rules only when the domain is active. See [[progressive-disclosure]]
- **Prune aggressively** — Semantically related but irrelevant instructions are worse than unrelated ones (Chroma's distractor interference). Docker conventions don't help when the agent writes React — they actively hurt
- **Prefer positive instructions** — "Do NOT do X" fails more often than "always do Y"
- **The sweet spot: low hundreds** — Reasoning models maintain near-perfect performance through 100–250 instructions before degrading; non-reasoning models degrade earlier

> Agent-generated context quickly turns into noise rather than useful information. — JetBrains Research, NeurIPS 2025

## Architectural Solutions over Prompt Engineering

Every mitigation for context degradation — repetition, reminders, sub-agents, summarization — consumes more context, which makes the problem worse. You're fighting attention dilution by adding tokens that dilute attention (source: agents-md-is-a-liability-paddo.md).

Architectural solutions matter more:
- **RPI loop** (Research → Plan → Implement with fresh context per phase) works because it doesn't try to fit everything into one window. See [[context-engineering]] for the Research–Plan–Implement workflow
- **Observation masking** — JetBrains' "Complexity Trap" research showed hiding tool output details cuts costs 50% without degrading task performance

**Your AGENTS.md isn't a knowledge base. It's an attention budget. Spend it wisely** (source: agents-md-is-a-liability-paddo.md).

## The Ball of Mud Anti-Pattern

Agent misbehaves → you add a rule → it misbehaves differently → you add another rule → config becomes unmaintainable. Auto-generated files compound this: they start large and rules only accumulate. The fix is the **deletion test**: regularly review every instruction and ask "Would removing this cause the agent to make mistakes?" If not, cut it. See [[context-engineering]] for more on this anti-pattern.

## Related pages

- [[context-engineering]]
- [[context-rot]]
- [[progressive-disclosure]]
- [[agent-configuration-files]]
- [[agent-best-practices]]
- [[million-token-context-window]]
- [[dead-context]]
