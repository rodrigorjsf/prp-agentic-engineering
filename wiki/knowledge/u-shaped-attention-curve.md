# U-Shaped Attention Curve

**Summary**: The characteristic U-shaped performance curve in long-context LLMs — recall quality is highest at context start and end (primacy and recency effects) and lowest in the middle, forming the empirical foundation of the "lost in the middle" phenomenon.
**Sources**: lost-in-the-middle-acl.md, lost-in-the-middle-arxiv.md, lost-in-the-middle-and-in-between-arxiv.md, `docs/long-context-research/README.md`
**Last updated**: 2026-04-22

---

The U-shaped attention curve is the empirical pattern observed when measuring how well a language model uses information placed at different positions in a long context. Performance is consistently highest at the edges (beginning and end) and lowest in the middle — forming a "U" shape when plotted against position. This was formally established by [[lost-in-the-middle-paper]] (Liu et al., 2024, TACL) and has since been confirmed across all major LLM families.

## The Three Components

### 1. Primacy Effect

Information near the **beginning** of the context window receives the highest baseline attention. Models attend most strongly to early tokens, as the causal attention mechanism allows all later tokens to attend to earlier ones — creating cumulative weight on early positions. This produces the left arm of the U-curve (source: lost-in-the-middle-acl.md).

**Practical implication:** Critical instructions, system prompts, and the most relevant retrieved documents belong at the **start** of the context.

### 2. Recency Effect

Information near the **end** of the context window receives secondary strong attention — a well-documented phenomenon from sequence modeling. The most recent tokens are always in the model's immediate working memory. This produces the right arm of the U-curve (source: lost-in-the-middle-researchgate.md).

**Practical implication:** Queries, final instructions, and critical formatting requirements belong at the **end** of the context.

### 3. Lost in the Middle (Middle Neglect)

Information in the **center** of the context is systematically underutilized. In multi-document QA experiments, performance drops by **over 20 percentage points** when the relevant document is placed in the center of a 20-document context vs. the edges. This is not a small statistical effect — it represents a fundamental failure mode of current transformer architectures under long-context conditions (source: lost-in-the-middle-acl.md).

## Quantitative Evidence

From the original Liu et al. (2024) experiments on NaturalQuestions-Open with 20 documents (source: lost-in-the-middle-acl.md, lost-in-the-middle-arxiv.md):

| Document Position | Relative Performance |
|------------------|---------------------|
| Position 1 (start) | ~Highest |
| Position 5 | Declining |
| Position 10 (middle) | ~Lowest (~20%+ drop) |
| Position 15 | Recovering |
| Position 20 (end) | ~Second-highest |

The key-value retrieval task confirms the same curve on synthetic data, establishing that this is a general property of model attention — not a dataset artifact (source: lost-in-the-middle-acl.md).

## Models Affected

The U-shaped curve has been documented across (source: lost-in-the-middle-acl.md, lost-in-the-middle-and-in-between-arxiv.md):

- GPT-3.5-Turbo (ChatGPT)
- Claude (Anthropic)
- MPT-7b-8k-instruct
- Llama-2-7b-longlora-8k-ft
- Other "long-context" model variants

**No examined model** was immune to the positional bias, including those explicitly marketed as long-context capable. The U-shaped curve persists across model families and scales.

## The In-Between Compound Effect

Baker et al. (2024) — see [[lost-in-the-middle-in-between]] — extend the finding to multi-hop QA and discover a second degradation axis: the *relative distance between* multiple evidence documents. When two required evidence pieces are adjacent, performance is higher than when they are separated — even when both are at the same absolute position (source: lost-in-the-middle-and-in-between-arxiv.md).

This creates a 2D degradation surface for multi-hop tasks:

- **X-axis:** Distance of each evidence document from context edges (the original U-curve)
- **Y-axis:** Distance between evidence documents from each other (the "in-between" effect)

## Relationship to Context Engineering

The U-shaped curve is the empirical basis for key [[context-engineering]] guidelines:

1. **Critical information at edges:** Place the most important context at position 0 or position N.
2. **Reference data in the middle:** Use the "dead zone" for less critical documents, citations, or background context that the model only needs to skim.
3. **20%+ performance gain from ordering alone:** Simply reordering retrieved documents can improve RAG quality by 20–30% without any change to retrieval quality (source: lost-in-the-middle-acl.md).

This directly informs [[progressive-disclosure]] — rather than dumping all context at once, progressively narrowing context keeps critical information near the query and edges.

## Connection to Million-Token Windows

As context windows grow — [[million-token-context-window]] models now offer 1M+ tokens — the middle neglect problem becomes more severe, not less. A document placed at position 250,000 in a 500,000-token context faces extreme middle neglect. Positional bias does not diminish with larger windows; the "lost zone" simply grows larger (source: README.md).

This is a key driver of [[context-rot]]: in very long contexts, most of the window becomes a "lost zone" where information may as well be absent from the model's working memory. See also [[dead-context]] for the concept of tokens that consume budget without contributing to reasoning.

## Practical Placement Guidelines

Based on the research, the following guidelines apply to any system that inserts content into an LLM context window:

| Content Type | Recommended Position | Reason |
|-------------|---------------------|--------|
| System instructions | Start | Primacy effect; maximum retention |
| Task constraints | Start | Critical; cannot be missed |
| Most relevant retrieved documents | Start | Highest recall quality |
| Background reference documents | Middle | Low criticality; acceptable recall loss |
| Distractor/noise documents | Middle | Their influence is minimal there |
| Query / user question | End | Recency effect; stays in working memory |
| Final formatting instructions | End | Last-seen formatting is most followed |

These guidelines are the foundation of [[long-context-mitigation]] placement strategies.

## Related pages

- [[lost-in-the-middle-paper]]
- [[lost-in-the-middle-in-between]]
- [[long-context-mitigation]]
- [[context-engineering]]
- [[context-rot]]
- [[dead-context]]
- [[million-token-context-window]]
- [[progressive-disclosure]]
- [[agent-workflows]]
