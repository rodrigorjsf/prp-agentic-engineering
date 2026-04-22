# Commercial Agent Context Engineering

**Summary**: Context engineering as infrastructure for multi-tenant, production agent systems — memory taxonomy, truth vs. acceleration layers, the full context engine loop, and why architectural solutions matter more than prompt engineering at scale.
**Sources**: context-engineering-commercial-agents-jeremy-daly.md
**Last updated**: 2026-04-21

---

Building agents for a single user on a laptop: almost anything works. Building commercial multi-tenant agents serving enterprises: almost nothing accidental survives. The difference is treating context as infrastructure — not an implementation detail. See [[context-engineering]] for the foundational concepts.

## Context Is Infrastructure

Models improve. APIs standardize. Tool use matures. But in commercial multi-tenant systems, these are not the determining factors. **Context is** (source: context-engineering-commercial-agents-jeremy-daly.md).

Everyone has access to the same frontier models. Claude. GPT. Gemini. APIs are public, prices are falling, capabilities converging. What differentiates systems is no longer the model — **it's the context.**

### The Three Non-Negotiables

1. **Structural Isolation** — Tenant boundaries enforced at the infrastructure layer, not the model layer
2. **Deterministic Replay** — Ability to reconstruct exactly what the agent knew at decision time
3. **Economic Predictability** — Ability to predict and bound cost per run

If your system cannot enforce tenant boundaries structurally, it will eventually leak. If it cannot run deterministic replays, you cannot debug or evolve it safely. If it cannot predict cost per run, it cannot scale sustainably (source: context-engineering-commercial-agents-jeremy-daly.md).

### The Failure Mode

Systems that optimize for *demo velocity* — indexing raw transcripts, reusing context wholesale, blurring truth and acceleration — discover cost, drift, and cross-tenant risk too late. Getting context wrong doesn't just produce worse answers. **You get silent corruption** (source: context-engineering-commercial-agents-jeremy-daly.md).

## Memory as a Scoped, Typed System

A robust commercial agent system classifies memory along two dimensions (source: context-engineering-commercial-agents-jeremy-daly.md):

1. **Scope**: who can see it (a security boundary)
2. **Type**: what kind of memory it is (semantic role)

### Memory Scopes (Security Boundaries)

These are structural isolation layers enforced at the storage and routing layers — **never delegated to the model:**

| Scope | Contents | Mutability |
|-------|----------|------------|
| **Global** | Safety rules, tool contracts, product ontology, agent "constitution" | Immutable at runtime; deployment-controlled; never writable by agents |
| **Tenant** | Organization policies, knowledge bases, playbooks, connector configurations | Shared within tenant; policy-gated promotion |
| **User** | Preferences, working style, personal notes, user-specific entitlements | Visible only to user; promotion-gated; TTL-based |
| **Session** | Tool outputs, intermediate plans, scratch buffers, temporary retrieval results | Short-lived; aggressive garbage collection; not durable unless promoted |

### Memory Types (Semantic Role)

- **Policy memory** — Normative rules and constraints. Global or tenant-scoped. Versioned and tightly controlled
- **Preference memory** — Stable personalization parameters. Usually user-scoped
- **Fact memory** — Durable assertions the agent may reuse. Must include provenance
- **Episodic memory** — Structured summaries of completed work. "Case resolved." "Migration completed." Reusable artifacts extracted from traces
- **Trace memory** — Raw, append-only execution events. Your flight recorder

> Memory without scope is exposure. Memory without type is entropy. (source: context-engineering-commercial-agents-jeremy-daly.md)

### Memory Layer Summary

| Layer | Scope | Typical Contents | Retention | Write Policy |
|-------|-------|-----------------|-----------|-------------|
| Constitution | Global | Safety rules, tool contracts, ontologies | Versioned | Write-locked |
| Org memory | Tenant | Playbooks, knowledge base, connectors | Policy-based | Gated promotion |
| Personal memory | User | Preferences, working style, drafts | TTL-based + user controls | Gated promotion |
| Runtime state | Session | Tool outputs, scratch space, plans | Hours–days | Auto GC |
| Episodes | User/Tenant | "Case resolved," derived summaries | Months+ | Explicit promotion |
| Traces | Tenant | Events, retrievals, tool calls, approvals | Policy-based (often long-lived) | Append-only |

## Truth vs. Acceleration

The core distinction to preserve: **separate truth from acceleration** (source: context-engineering-commercial-agents-jeremy-daly.md).

### Canonical Stores (Truth)

**Canonical Event Log (Append-Only)** — Your flight recorder. Every agent run emits events: context retrieved, policies evaluated, tool calls made, approvals routed, outputs generated, memory promoted. Answers: What did the agent know at decision time? Which policy version applied? Why was this exception granted?

**Canonical Structured Memory Store** — Durable memory state: facts, preferences, episodic summaries, approved overrides, tenant-level knowledge. Every record must include: scope, class, provenance, retention policy, and sensitivity classification.

> If your vector store becomes your truth layer, you will eventually lose structural integrity.

### Derived Stores (Projection)

- **Retrieval Index (Vector/Hybrid Search)** — Your serving layer for recall. Must be rebuildable from canonical sources
- **Object Store** — Large payloads, attachments, extraction outputs. Content-addressed

**Hybrid search** (lexical + semantic) provides stronger precision and filtering than vector-only retrieval. The index must NOT be built directly from raw transcripts — they are noisy, redundant, and context-fragmented (source: context-engineering-commercial-agents-jeremy-daly.md).

## The Context Engine Loop

Every agent run should follow a predictable sequence — skip steps and you get drift (source: context-engineering-commercial-agents-jeremy-daly.md):

1. **Ingest** — Establish identity, scope, constraints, privacy mode. You DO NOT ask the model to filter data. You filter in the data plane
2. **Plan context needs** — Before retrieving anything, the agent plans what kind of context it needs. Prevents: "Retrieve everything and let the model figure it out"
3. **Retrieve** (isolation enforced here) — Filtering before ranking, not after. Every query must include: Tenant ID, scope visibility constraint, expiration checks, sensitivity boundaries
4. **Assemble working set** — Layered by priority: constitution → tenant policies → user preferences → retrieved facts/episodes → session state. Without layering and budgets, context windows become dumping grounds
5. **Semantic stabilization** — Before shrinking context, stabilize meaning: collapse verbose tool traces into structured summaries, extract typed episodic artifacts, convert dialogue into structured facts, normalize references, mark low-confidence artifacts, attach provenance metadata
6. **Agentic garbage collection** — After meaning is stabilized, optimize: enforce token budgets by layer, deduplicate redundant artifacts, drop stale session state, remove low-confidence provisional memory. **Agentic GC is not optimization — it is drift control**
7. **Infer and act** — Model + tools + policy enforcement + optional human approval
8. **Promotion gate** — Decide what becomes durable memory
9. **Emit trace envelope** — Record retrievals, actions, policies, versions, and cost surfaces
10. **Lifecycle garbage collection** — Expire session buffers, enforce retention, invalidate derived projections

## Key Architectural Principles

From field experience building multi-tenant production systems (source: context-engineering-commercial-agents-jeremy-daly.md):

- **Context boundaries are infrastructure, not application logic**
- **Isolation** is structural, not prompt-based
- **Replay** is the baseline for trust
- **Economics** must be predictable per run
- **Truth is rebuildable, acceleration is disposable**
- **What you exclude from context is becoming as important as what you include**

## Ecosystem Convergence

Production systems — Claude Code, Cursor, Letta, AWS AgentCore — all converge on the same architectural patterns under production pressure (source: context-engineering-commercial-agents-jeremy-daly.md):

- Typed, scoped memory layers
- Separation of event logs from structured state
- Explicit promotion gates
- Context budgets and priority ordering
- Aggressive pruning between turns
- Cryptographic isolation at projection layers

The same pressures produce the same load-bearing patterns.

## Relationship to Single-User Context Engineering

The principles of [[context-engineering]] — signal-to-noise, position effects, [[progressive-disclosure]], compaction — all apply in commercial systems, but with additional dimensions: tenant isolation as a security property, replay as an audit requirement, and cost control as a contractual obligation rather than a preference. Multi-tenant failure modes include silent cross-tenant data leakage, not just degraded reasoning. See [[context-rot]] for the reasoning degradation mechanisms that apply across both contexts.

## Related pages

- [[context-engineering]]
- [[context-rot]]
- [[progressive-disclosure]]
- [[agent-best-practices]]
- [[agent-workflows]]
- [[prompt-engineering]]
