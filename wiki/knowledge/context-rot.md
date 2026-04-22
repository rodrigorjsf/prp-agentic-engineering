# Context Rot

**Summary**: The empirically validated phenomenon where LLM performance degrades as tokens accumulate in the context window, caused by attention scaling, training distribution mismatch, and position interpolation effects.
**Sources**: research-context-rot-and-management.md, research-context-engineering-comprehensive.md, agents-md-is-a-liability-paddo.md, pi-context-zone-github.md
**Last updated**: 2026-04-21

---

Context rot is not theoretical — it is measured across all 18 tested LLMs (Chroma Research, 2025). Even trivial tasks (word replication, basic retrieval) degrade as context grows.

## Three Architectural Causes

1. **n² scaling of self-attention** — Every new token attends to every previous token; compute grows quadratically
2. **Training distribution mismatch** — Models trained primarily on shorter sequences; long contexts are out-of-distribution
3. **Position interpolation degradation** — Extended context techniques (RoPE scaling, ALiBi) introduce approximation errors at extreme positions

## Key Measurements

| Metric                       | Value              | Source                    |
| ---------------------------- | ------------------ | ------------------------- |
| Accuracy at 3K filler tokens | 0.92 → 0.68        | Levy et al., ACL 2024     |
| Middle-position recall loss  | 10–20%             | Liu et al., TACL 2023     |
| All 18 models degrade        | Consistent pattern | Chroma Research, 2025     |
| Critical threshold           | ~3,000 tokens      | Four failure modes emerge |

## Four Failure Modes at Threshold

When context exceeds ~3,000 tokens of accumulated noise:

1. **Refusal** — Model declines to answer, citing insufficient information
2. **Label bias** — Model defaults to most common training label
3. **CoT breakdown** — Chain-of-thought reasoning produces fluent but illogical steps
4. **Coverage loss** — Model addresses only a subset of provided information

## Context Poisoning

- **Failed approach accumulation**: After 2 failed corrections, better to `/clear` and restart than continue
- **Contradictory instructions**: Model picks one rule arbitrarily — no predictable resolution
- **Stale documentation**: Worse than no documentation; changing file paths invalidate documented locations
- **Counter-intuitive finding**: Shuffled haystacks *improve* performance vs. coherent text (disrupted narrative forces token-level attention)

## Management Strategies

| Strategy                   | Mechanism                       | When to Use                            |
| -------------------------- | ------------------------------- | -------------------------------------- |
| Compaction (summarization) | Ask Claude to summarize context | Multi-turn sessions, ~95% capacity     |
| External memory            | JSON state files, git history   | Long-running agents, cross-session     |
| [[subagents]]              | Isolated context windows        | Complex research, parallel exploration |
| [[progressive-disclosure]] | Load-on-demand via skills/rules | Configuration, instructions            |
| Clear and restart          | `/clear` command                | After 2+ failed corrections            |

## Compression Research

- LLMLingua: up to **20× compression** with minimal loss
- LongLLMLingua: **+21.4% performance** with ~4× fewer tokens on NaturalQuestions; **94% cost reduction** on LooGLE
- Contextual Retrieval: **35%** failure reduction with contextual embeddings; **67%** with reranking

## The 500-Instruction Ceiling

The IFScale benchmark (Distyl AI, NeurIPS 2025) tested 20 frontier models against instruction-following at scale: the best frontier model scored 68% at 500 instructions — **one in three instructions simply got skipped** (source: agents-md-is-a-liability-paddo.md).

Key finding: as instruction density increases, errors shift from *modification* (doing it wrong) to *omission* (not doing it at all). The model doesn't misinterpret the 400th rule — it doesn't see it. Three degradation patterns emerge by model type:

| Pattern | Models | Behavior |
|---------|--------|----------|
| Threshold decay | o3, Gemini 2.5 Pro | Near-perfect until 100–250 instructions, then cliff |
| Linear decay | GPT-4.1, Claude Sonnet 4 | Steady decline from start |
| Exponential decay | GPT-4o, LLaMA-4-Scout | Rapid collapse |

Every model shows **primacy bias**: earlier instructions receive more attention. See [[agents-md-liability]] for the full analysis and actionable principles.

## The Smart / Warm / Dumb Zone Framework

The dumb zone — coined by Dex Horthy after analyzing 100,000+ developer sessions — is an operational framework for understanding context rot's impact on reasoning quality (source: pi-context-zone-github.md):

| Zone | Context Used | What Happens |
|------|-------------|--------------|
| 🧠 Smart | 0–40% | Peak reasoning. Follows instructions, catches edge cases, accurate tool selection |
| ⚠️ Warm | 40–70% | Degrading. F1 scores drop ~45%. Instruction drift, shallow pattern matching, relies on pre-training over actual context |
| 🧟 Dumb | 70%+ | Broken. Hallucination rates spike to 40%. Infinite debug loops. Confidently wrong. Auto-compaction triggers but is lossy |

### Model-Specific Smart Zone Boundaries (MRCR v2, 8-needle, March 2026)

| Model | Window | MRCR @ 128K | MRCR @ 256K | MRCR @ 1M | Smart Zone |
|-------|--------|-------------|-------------|-----------|-----------|
| Claude Opus 4.6 | 1M | ~94% | 93% | **78%** | ~70% (most resilient) |
| Claude Sonnet 4.6 | 1M | — | — | 65% | ~50–60% |
| GPT-5.4 | 1M | 86% | 79% | 37% | ~30–40% |
| Gemini 3.1 Pro | 2M | 85% | ~50% | 26% | ~25–30% |
| DeepSeek V3 | 128K | **95%** | N/A | N/A | Near 100% within window |

Claude Opus 4.6's Context Compaction architecture resists context rot better than any other model — 78% at 1M where GPT-5.4 drops to 37% and Gemini to 26%. But even Opus degrades. The 40% rule is conservative and works as a universal default (source: pi-context-zone-github.md). See [[million-token-context-window]] for extended analysis.

### What Causes Context Rot (Expanded)

Four compounding mechanisms beyond the three architectural causes (source: pi-context-zone-github.md):

1. **Attention dilution** — Transformer attention is a fixed budget. More tokens = less focus per token
2. **Lost in the middle** — Models remember the beginning and end of context but forget the middle (U-shaped curve)
3. **Trajectory poison** — Conversation history full of the model's mistakes and your corrections. The model learns to predict more mistakes
4. **KV cache compression** — At high utilization, models compress older context, losing the "why" behind decisions

## Attention Sinks

Xiao et al. (ICLR 2024): initial tokens receive disproportionate attention regardless of their semantic content. Replace your first tokens with newline characters and the effect persists — it's positional, not semantic. This is why instructions at the top of AGENTS.md get followed more reliably: they're sitting on the attention sink (source: agents-md-is-a-liability-paddo.md).

## Related pages

- [[context-engineering]]
- [[progressive-disclosure]]
- [[prompt-engineering]]
- [[agents-md-liability]]
- [[million-token-context-window]]
- [[dead-context]]
