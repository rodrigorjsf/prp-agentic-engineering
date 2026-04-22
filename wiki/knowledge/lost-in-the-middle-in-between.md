# Lost in the Middle, and In-Between Paper

**Summary**: Summary of Baker et al. (2024, arXiv) — extending "lost in the middle" to multi-hop QA and establishing that performance degrades not only with absolute position but also with the relative distance between evidence documents: the "in-between" effect.
**Sources**: lost-in-the-middle-and-in-between-arxiv.md, `docs/long-context-research/README.md`
**Last updated**: 2026-04-22

---

"Lost in the Middle, and In-Between: Enhancing Language Models' Ability to Reason Over Long Contexts in Multi-Hop QA" (Baker et al., arXiv 2412.10079, December 2024) extends the original [[lost-in-the-middle-paper]] findings to the multi-hop question answering (MHQA) setting. The key contribution is demonstrating an additional "in-between" effect: performance degrades not only with absolute position (distance from context edges) but also with the *relative distance between* multiple evidence documents within the same context.

## Authors and Publication

**Authors:** George Arthur Baker, Ankush Raut, Sagi Shaier, Lawrence E Hunter, Katharina von der Wense
**Affiliations:** University of Colorado Boulder; University of Chicago; Johannes Gutenberg University Mainz
**Published:** arXiv, December 2024 ([2412.10079](https://arxiv.org/abs/2412.10079))
**Code:** [github.com/Spongeorge/long-context-multihop](https://github.com/Spongeorge/long-context-multihop)

(source: lost-in-the-middle-and-in-between-arxiv.md)

## The In-Between Effect

The original [[lost-in-the-middle-paper]] established that performance is lowest when a single evidence document is in the center of the context. Baker et al. discover that in multi-hop QA, a second degradation axis exists:

> When two required pieces of evidence are **adjacent** in the context, performance is consistently **higher** than when they are separated by distractor documents — even when both are at the same absolute position (source: lost-in-the-middle-and-in-between-arxiv.md).

This "in-between" effect compounds with the original "lost in the middle" effect:

- Evidence too far from edges → degradation (original finding, [[u-shaped-attention-curve]])
- Evidence documents too far from each other → additional degradation (new finding)

## Datasets Evaluated

Three established multi-hop QA benchmarks were used (source: lost-in-the-middle-and-in-between-arxiv.md):

| Dataset | Hops Required | Notes |
|---------|--------------|-------|
| HotpotQA | 2 | Cross-document reasoning |
| 2WikiMultiHopQA | 2–4 | Multi-step inference chains |
| MuSiQue | 2–4 | Compositional questions |

Because official test sets are private, the authors split existing validation sets: first half for validation, second half for test.

## Models Evaluated

Results generalize across model families (source: lost-in-the-middle-and-in-between-arxiv.md):

- **MPT-7b-8k-instruct** — instruction-tuned with ALiBi positional embeddings replacing traditional positional embeddings
- **Llama-2-7b-longlora-8k-ft** — fine-tuned for 8k context without instruction tuning
- **GPT-3.5-turbo-1106** — 16k context window; closed-source OpenAI model

## Why Multi-Hop Compounds the Problem

Single-hop QA (one evidence document needed) is already affected by the [[u-shaped-attention-curve]]. Multi-hop QA multiplies the problem:

1. Each evidence document is individually susceptible to positional neglect.
2. The relative distance between evidence documents creates an additional degradation axis.
3. The combinatorial explosion of position orderings makes mitigation via re-ranking impractical:

| Reasoning Hops | Evidence Position Permutations |
|---------------|-------------------------------|
| 2-hop | 190 |
| 3-hop | 1,140 |
| 4-hop | 4,845 |

(source: lost-in-the-middle-and-in-between-arxiv.md)

## Mitigation Strategies Evaluated

### Chain-of-Thought Prompting

CoT prompting **helps identify relevant documents** but does not resolve positional bias. The model becomes better at locating which documents matter, but its ability to use those documents still degrades based on where they sit in the context. CoT is an incomplete solution for the in-between problem (source: lost-in-the-middle-and-in-between-arxiv.md).

### Knowledge Graph Triple Extraction

Uses LLaMA 2-7B to extract structured triples from each document, condensing content to factual relationships. This reduces context size but produces reasoning chains that are **too fragile** for reliable multi-hop QA — losing the nuance required for intermediate reasoning steps (source: lost-in-the-middle-and-in-between-arxiv.md).

### Document Summarization

BART-large-CNN (fine-tuned on CNN/Daily Mail) generates ≤50-token summaries per document. Context size is reduced, but critical details required for multi-hop inference are often lost (source: lost-in-the-middle-and-in-between-arxiv.md).

All tested mitigation strategies have significant limitations in the multi-hop setting. See [[long-context-mitigation]] for the broader landscape of strategies.

## Distinction from Related Work

This study differs from Levy et al. (2024), which also examines LLM performance degradation (source: lost-in-the-middle-and-in-between-arxiv.md):

| Dimension | Baker et al. (2024) | Levy et al. (2024) |
|-----------|---------------------|---------------------|
| Focus | Document position within fixed context | Overall input size |
| Datasets | HotpotQA, 2WikiMultiHopQA, MuSiQue | Custom FLenQA (true/false) |
| Hops | Up to 4 | Up to 2 |

## Implications for Agent Workflows

In [[agent-workflows]], multi-hop reasoning over retrieved documents is common — an agent may need to gather evidence from multiple sources and synthesize across reasoning steps. The in-between effect means:

- Simply placing both evidence pieces "near the edges" is insufficient if they are far apart from each other.
- [[long-context-mitigation]] strategies that work for single-hop RAG may not scale to multi-hop agentic reasoning.
- Context window design must account for **evidence clustering** — keeping related documents adjacent — not only document-to-edge distance.

This connects to [[context-rot]]: as context windows grow longer, the distance between interdependent evidence documents tends to increase, compounding both effects simultaneously. In [[million-token-context-window]] scenarios, the problem becomes severe.

## Related pages

- [[lost-in-the-middle-paper]]
- [[u-shaped-attention-curve]]
- [[long-context-mitigation]]
- [[context-engineering]]
- [[context-rot]]
- [[dead-context]]
- [[agent-workflows]]
- [[million-token-context-window]]
