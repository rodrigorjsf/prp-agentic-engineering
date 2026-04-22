# Lost in the Middle Paper

**Summary**: Full summary of Liu et al. (2024, TACL) — the landmark paper establishing that LLMs underperform when relevant information is in the middle of long input contexts, exhibiting a characteristic U-shaped performance curve.
**Sources**: lost-in-the-middle-acl.md, lost-in-the-middle-arxiv.md, lost-in-the-middle-researchgate.md
**Last updated**: 2026-04-21

---

"Lost in the Middle: How Language Models Use Long Contexts" (Liu et al., 2024) is the foundational paper establishing the [[u-shaped-attention-curve]] phenomenon in long-context LLMs. Published in Transactions of the Association for Computational Linguistics (TACL), Volume 12, pp. 157–173 (DOI: 10.1162/tacl_a_00638), it demonstrates that performance is highest when relevant information appears at the beginning or end of the context window and degrades significantly when it appears in the middle — even for models explicitly designed for long contexts.

## Authors and Publication

**Authors:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang (Stanford University / Meta AI)
**Published:** TACL 2024 (arXiv preprint: July 2023)
**arXiv:** [2307.03172](https://arxiv.org/abs/2307.03172) — 18 pages, 16 figures
**ACL Anthology:** [2024.tacl-1.9](https://aclanthology.org/2024.tacl-1.9)

(source: lost-in-the-middle-acl.md, lost-in-the-middle-arxiv.md)

## Core Finding

Performance can degrade by **over 20 percentage points** in multi-document QA when the answer document is positioned in the center of a 20-document context vs. the edges. This finding holds across all tested models — ChatGPT, Claude, and others — with no model immune to the bias (source: lost-in-the-middle-researchgate.md).

The pattern is consistent: accuracy is highest at document position 1 and position 20, with the sharpest dip around the midpoint (position 10). This forms the characteristic **U-shaped performance curve** described in [[u-shaped-attention-curve]].

## Experiments

### Task 1: Multi-Document Question Answering

- **Dataset:** NaturalQuestions-Open
- **Setup:** A correct answer document is inserted at one of 20 positions; 19 distractor documents fill the rest.
- **Result:** Performance follows the U-curve; placing the answer in the center of the 20-document context produces the lowest accuracy (source: lost-in-the-middle-acl.md).

### Task 2: Key-Value Retrieval

- **Setup:** Synthetic JSON objects contain 75–140 key-value pairs; the model must retrieve the value for a specific key.
- **Result:** The same U-shaped positional bias emerges on synthetic data, confirming the effect is not dataset-specific (source: lost-in-the-middle-acl.md).

## Models Evaluated

All examined models — including those explicitly marketed as long-context capable — exhibited positional bias. The effect was observed on:

- GPT-3.5-Turbo (ChatGPT)
- Claude (Anthropic)
- Llama-2 variants
- MPT-7b

No model could reliably process relevant information equally well across all positions (source: lost-in-the-middle-acl.md).

## Mitigation Strategies Proposed

### Query-Aware Contextualization

The paper's primary proposed mitigation: place the query **both before and after** the document list — at the start and end of the context simultaneously. This exploits both primacy and recency effects.

- **Effective for:** Key-value retrieval tasks.
- **Limited for:** Multi-document QA — less effective due to the complexity of real NLP tasks (source: lost-in-the-middle-and-in-between-arxiv.md).

### New Evaluation Protocols

The paper introduces position-aware evaluation protocols for long-context LLMs — measuring performance at each position in the context window rather than aggregating across positions. This influenced subsequent benchmarking work and is now a standard approach in long-context evaluation.

## Practical Implications for RAG Systems

For [[context-engineering]] practitioners building RAG systems:

1. **Most relevant documents should be placed at the beginning or end** of the context — not in the middle.
2. **Document ordering in retrieved sets matters** as much as retrieval quality itself.
3. **Increasing context window size alone does not resolve positional bias** — even the largest long-context models retain the U-shaped degradation.
4. **The [[u-shaped-attention-curve]] must be accounted for** when designing production retrieval pipelines.

These findings directly inform [[long-context-mitigation]] strategies used in modern RAG architectures.

## Connection to Context Rot

The "lost in the middle" effect is one of the primary mechanisms behind [[context-rot]]: as context windows grow, information in the middle becomes increasingly invisible to the model — creating a form of dead content that takes up tokens without contributing to reasoning. See also [[dead-context]].

## Impact and Follow-On Work

This paper is among the most-cited in LLM context research. It catalyzed Baker et al. (2024) — see [[lost-in-the-middle-in-between]] — which extends the findings to multi-hop QA and introduces the "in-between" effect: performance degrades not only with absolute position but also with the relative distance *between* evidence documents.

## Related pages

- [[u-shaped-attention-curve]]
- [[lost-in-the-middle-in-between]]
- [[long-context-mitigation]]
- [[context-engineering]]
- [[context-rot]]
- [[dead-context]]
- [[million-token-context-window]]
- [[agent-workflows]]
