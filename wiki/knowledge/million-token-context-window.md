# Million-Token Context Window

**Summary**: What large context windows actually mean in practice — genuine benefits, hard limits from attention dilution, benchmark degradation curves, and why discipline still outperforms capacity.
**Sources**: million-token-context-window-syntackle.md, context-stops-being-scarce-paddo.md, pi-context-zone-github.md
**Last updated**: 2026-04-21

---

Million-token context windows are now available across all major providers, but the headline number obscures a more nuanced reality: accepting 1M tokens is not the same as reasoning well over 1M tokens. The gains are real, but so are the limits. See [[context-rot]] for the underlying mechanisms.

## What Actually Changed

Anthropic made the 1M context window generally available for Claude Opus 4.6 and Sonnet 4.6 at flat pricing — no multiplier, no beta header (source: context-stops-being-scarce-paddo.md). The pricing structure:

| Model | Window | Input | Output | Pricing |
|-------|--------|-------|--------|---------|
| Claude Opus 4.6 | 1M | $5/M | $25/M | Flat |
| Claude Sonnet 4.6 | 1M | $3/M | $15/M | Flat |
| GPT-5.4 | 1M | — | — | 2× above 272K |
| Gemini 2.5 Pro | 1M | — | — | Tiered above 200K |

The differentiator is pricing structure, not raw capacity. Claude is the only family where both flagship and mid-tier offer 1M at flat rates (source: context-stops-being-scarce-paddo.md).

## The Compaction Problem: What More Context Actually Buys

Claude Code compacts conversation history when context fills — it summarizes earlier messages to make room. Each compaction is a lossy compression: the agent keeps the gist but loses specifics (source: context-stops-being-scarce-paddo.md).

**Claude Code math:**
- Reserve: ~33K tokens buffer
- Compaction triggers: ~83.5% usage
- At 200K: ~134K usable before first compaction
- At 1M: ~802K usable before first compaction

Jon Bell (Anthropic CPO) reported a 15% decrease in compaction events with 1M. But compaction degrades non-linearly — one compaction is fine, three in a session means the agent works from a summary of a summary of a summary (source: context-stops-being-scarce-paddo.md). Fewer compactions means longer stretches of productive autonomy without human correction.

## The Benchmark Reality

Despite the claims, performance degrades as context fills. On MRCR v2 (8-needle), the gold standard for measuring reasoning quality across context lengths (source: pi-context-zone-github.md):

| Model | @ 128K | @ 256K | @ 1M | Smart Zone Ends |
|-------|--------|--------|------|----------------|
| Claude Opus 4.6 | ~94% | 93% | **78%** | ~70% |
| Claude Sonnet 4.6 | — | — | 65% | ~50–60% |
| GPT-5.4 | 86% | 79% | 37% | ~30–40% |
| Gemini 3.1 Pro | 85% | ~50% | 26% | ~25–30% |
| DeepSeek V3 | **95%** | N/A | N/A | Near 100% (within window) |

Even the best model (Opus 4.6) drops from ~92% at 256K to ~78% at 1M. GPT-5.4 falls from ~80% at 128K to ~37% at 1M — massive degradation (source: million-token-context-window-syntackle.md).

## Why It Happens: Attention Dilution

The transformer's self-attention assigns relevance scores that must add up to 100%. With 4K tokens, it's easy to give meaningful attention to what matters. With 1M tokens, that same 100% spreads across a million candidates. The important stuff — if it's in the middle — must compete with an enormous surrounding text and often loses (source: million-token-context-window-syntackle.md).

Positional encoding methods like RoPE create a **recency bias**: tokens closer to the end receive more natural attention than those far away. This is structural, not a bug (source: million-token-context-window-syntackle.md). See [[context-rot]] for the full five-mechanism breakdown.

The "lost in the middle" research (Liu et al., 2024) documented a U-shaped performance curve: performance drops by more than 30% when relevant information shifts from context edges to center (source: context-stops-being-scarce-paddo.md).

Anthropic's own finding: Claude 2.1's long-context accuracy jumped from 27% to 98% by adding a single prompt nudge — *"Here is the most relevant sentence in the context."* The model had the information; it just wasn't attending to it (source: context-stops-being-scarce-paddo.md).

## The Dumb Zone

The 12-factor agents framework: fill your context window past 40% and you enter the "dumb zone" — signal-to-noise degrades, attention fragments, agents make mistakes. This is architectural, not model-specific (source: context-stops-being-scarce-paddo.md).

Princeton NLP's HELMET benchmark tested 59 models and found most degrade noticeably past 32K on summarization tasks. Open-source models collapse entirely (source: context-stops-being-scarce-paddo.md).

The three operational zones (source: pi-context-zone-github.md):

| Zone | Context Used | What Happens |
|------|-------------|--------------|
| 🧠 Smart | 0–40% | Peak reasoning. Follows instructions, catches edge cases, accurate tool selection |
| ⚠️ Warm | 40–70% | Degrading. F1 scores drop ~45%. Instruction drift, shallow pattern matching |
| 🧟 Dumb | 70%+ | Broken. Hallucination rates spike to 40%. Infinite debug loops. Confidently wrong |

## What Changes in Practice

Context scarcity shaped old AI coding workflows — be concise, front-load important context, accept the agent will forget things. With abundant context, the workflow shifts (source: context-stops-being-scarce-paddo.md):

- **Longer uninterrupted sessions** — An agent that remembers your morning's architectural discussion when you implement something in the afternoon
- **Bigger codebases in context** — At 1M tokens, ~15,000 lines of code with room for conversation; constraint shifts from "what fits" to "what's relevant"
- **Fewer manual interventions** — Each compaction event is a moment where humans must correct the agent's compressed understanding

## The Paradox: Most Valuable When Unused

The 1M window is most valuable when you don't use most of it. The win isn't cramming more in — it's having headroom so important information stays in the high-attention zone longer (source: context-stops-being-scarce-paddo.md).

Anthropic's own context engineering guidance recommends subagent isolation, just-in-time context loading, and aggressive compaction over simply filling the window. The 1M ceiling is a safety net, not a target.

> Context engineering > context stuffing (source: context-stops-being-scarce-paddo.md)

The trend line: context windows went 4K → 1M in three years. The next unlock probably isn't 10M tokens — it's better attention over tokens you already have (source: context-stops-being-scarce-paddo.md).

## Practical Guidelines

- Don't blindly dump everything into the context window just because you can (source: million-token-context-window-syntackle.md)
- For tasks requiring specific details in large, frequently-changing documents, a well-designed RAG pipeline will often outperform raw long context
- Flat pricing removes the economic incentive for discipline — stay disciplined anyway
- When a capability stops costing extra, it stops being a feature and starts being assumed. That's when workflows actually change (source: context-stops-being-scarce-paddo.md)

## Related pages

- [[context-rot]]
- [[context-engineering]]
- [[context-scarcity-end]]
- [[dead-context]]
- [[progressive-disclosure]]
- [[agents-md-liability]]
