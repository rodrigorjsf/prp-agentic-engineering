# Wiki Change Log

Append-only operation log. Most recent entries at top.

---

## 2026-04-22 — Wiki sync against current docs corpus

| File | Action | Description |
|------|--------|-------------|
| `harness-engineering.md` | created | Added a concise synthesis page for the `docs/harness-engineering/` corpus, covering the control-layer view of autonomous agents, deterministic rails, external state, and context firewalls. |
| `index.md` | updated | Removed stale compliance-routing entries, added `harness-engineering`, refreshed summaries, and corrected the total page count. |
| `log.md` | updated | Recorded the current docs-to-wiki sync. |
| `compliance-routing.md` | deleted | Pruned stale page tied to removed `docs/compliance/` sources. |
| `validation-routing-claude.md` | deleted | Pruned stale page tied to removed `docs/compliance/` sources. |
| Multiple knowledge pages | updated | Removed nonexistent `analysis-*` sources, corrected stale source paths, and pruned broken navigation links to missing wiki pages. |

Sources: `docs/` excluding `docs/superpowers/`

---

## 2026-04-21 — HumanLayer repository analysis

| Date | Page | Type | Sources |
|------|------|------|---------|
| 2026-04-21 | [[humanlayer-repository-analysis]] | Source summary | `docs/humanlayer-repository-analysis.md` |

Changes: Added a repository-analysis page for the local `humanlayer/` clone, covering CodeLayer positioning, the `hlyr` + `hld` runtime path, the primary `humanlayer-wui` surface, shared contract/database layers, tooling/release workflows, and the main consolidation risks.

---

## 2026-04-21 — Long Context Research batch

| File | Action | Description |
|------|--------|-------------|
| `lost-in-the-middle-paper.md` | created | Full wiki summary of Liu et al. (2024, TACL): U-shaped curve, experiments, mitigations, RAG implications. |
| `lost-in-the-middle-in-between.md` | created | Wiki summary of Baker et al. (2024, arXiv): in-between effect, multi-hop QA, combinatorial limits of mitigations. |
| `u-shaped-attention-curve.md` | created | Concept page for the U-shaped attention/performance curve: primacy, recency, middle neglect, placement guidelines. |
| `long-context-mitigation.md` | created | Comprehensive mitigation strategy page: 8 strategies with single-hop vs. multi-hop effectiveness ratings. |
| `context-engineering.md` | updated | Extended "Position Effects" section with deep-dive subsections on U-curve evidence and in-between compound effect; added 5 new cross-links in Related pages. |

Sources: `docs/long-context-research/`

---

## 2026-04-21 — Tool Calling batch

| Date | Page | Type | Sources |
|------|------|------|---------|
| 2026-04-21 | [[programmatic-tool-calling]] | Source summary | programmatic-tool-calling-claude-api.md, README.md |
| 2026-04-21 | [[tool-search-epsilla]] | Source summary | tool-search-redefining-agent-tool-calling-epsilla.md, README.md |
| 2026-04-21 | [[programmatic-tool-calling-sdk]] | Source summary | cameronking4-programmatic-tool-calling-github.md, README.md |
| 2026-04-21 | [[dynamic-tool-discovery]] | Concept | tool-search-redefining-agent-tool-calling-epsilla.md, programmatic-tool-calling-claude-api.md, mcp-programmatic-tool-calling-opensandbox-dev.md, README.md |
| 2026-04-21 | [[tool-calling-patterns]] | Concept | All four source files + README.md |

Sources: `docs/tool-calling/`

---

## 2026-04-21 — Spec-Driven Development cluster

Created 5 wiki pages from 3 source documents in `docs/spec-driven-development/`:

- **spec-driven-development.md** — Source summary of arXiv:2602.00180 (Piskala, AIWare 2026); academic treatment of SDD principles, three rigor levels, four-phase workflow, AI coding agent benefits, tool survey (BDD, OpenAPI, Spec Kit, Kiro, Tessl), case studies (financial services, enterprise BDD, automotive embedded), pitfalls, and decision framework.
- **spec-driven-development-practice.md** — Source summary of DEV Community practitioner guide; vibe coding vs. spec-first contrast, Spec Kit step-by-step walkthrough, real prompting examples, three-tool comparison, honest failure modes (review overhead, exploratory work, AI non-determinism).
- **spec-driven-development-critique.md** — Source summary of martinfowler.com "Exploring Gen AI" critical analysis; hands-on evaluation of Kiro, Spec Kit, Tessl; concrete failure modes: markdown review fatigue, false sense of control, agent non-compliance, functional/technical spec confusion.
- **spec-first-ai-development.md** — Concept page on the spec-first paradigm; AI mind-reading problem, developer role transformation, specs as super-prompts for agent workflows, self-spec methods, when spec-first works and doesn't.
- **code-to-contract.md** — Concept page on executable contract thinking; API contracts (OpenAPI, gRPC, Pact), BDD as contract enforcement, embedded spec-as-source, contracts as AI inputs, three contract enforcement levels.

Sources: `docs/spec-driven-development/`

---

## 2026-04-21 — Agentic Engineering batch

Created 7 wiki pages from 5 source documents in `docs/agentic-engineering/`.

| File | Type | Source |
|------|------|--------|
| `rpi-workflow.md` | Source summary | `research-plan-implement-rpi.md` |
| `rpir-workflow.md` | Source summary | `research-plan-implement-review-tyler-burleigh.md` |
| `agent-harness.md` | Source summary | `building-agent-harness-martin-richards.md` |
| `claude-cookbook.md` | Source summary | `claude-cookbook-anthropic.md` |
| `agentic-software-modernization.md` | Source summary | `agentic-software-modernization-markus-harrer.md` |
| `agentic-engineering-workflow.md` | Concept | All 4 source docs above |
| `agent-harness-design.md` | Concept | `building-agent-harness-martin-richards.md`, `research-plan-implement-rpi.md`, `research-plan-implement-review-tyler-burleigh.md` |

Sources: `docs/agentic-engineering/`

---

## 2026-04-21 — Structured Outputs (Anthropic) batch

**Sources read**: 4 files from `docs/structured-outputs/`

**Pages created**: 6 knowledge pages

| File | Type | Notes |
|------|------|-------|
| `structured-outputs-anthropic.md` | Source summary | Main structured outputs guide: JSON outputs, strict tool use, SDK helpers, schema limits, caching, HIPAA |
| `anthropic-tool-use.md` | Source summary | Tool definition best practices, input_examples, tool_choice options, model response handling |
| `anthropic-strict-tool-use.md` | Source summary | strict: true mechanics, guarantees, use cases, complexity limits, HIPAA rules |
| `anthropic-output-consistency.md` | Source summary | Six consistency techniques: format spec, prefilling, few-shot, retrieval, chaining, character prompts |
| `json-schema-for-ai.md` | Concept | Schema design patterns, supported features, complexity limits, SDK transformation pipeline |
| `tool-use-patterns.md` | Concept | Eight tool use patterns: forced, any, strict, auto, consolidated, namespaced, examples, combined |

Sources: `docs/structured-outputs/` (Anthropic API only)

---

## 2026-04-21 — Agent Protocols & Communication batch

| File | Type | Source document |
|------|------|----------------|
| `agent-communication-protocols.md` | Source summary | `advancing-agentic-ai-communication-protocols.md` |
| `ai-agent-protocols-2026.md` | Source summary | `ai-agent-protocols-2026-guide.md` |
| `agentic-systems-architectural-paradigms.md` | Source summary | `architectural-paradigms-advanced-agentic-systems.md` |
| `anthropic-2026-full-connectivity.md` | Source summary | `anthropic-engineer-2026-forecast-full-connectivity-mcp.md` |
| `a2a-protocol.md` | Source summary | `a2a-protocol-huggingface-space.md` |
| `human-agent-collaboration.md` | Source summary | `fluid-human-agent-collaboration-pmc.md` |
| `agent-protocol-standards.md` | Concept | synthesized from multiple sources |
| `multi-agent-communication.md` | Concept | synthesized from multiple sources |

Sources: `docs/agent-protocols/`

---

## 2026-04-21 — Context Engineering docs ingested

Sources: 9 files from `docs/context-engineering/`

Pages created:
- `million-token-context-window.md`
- `agents-md-liability.md`
- `context-scarcity-end.md`
- `dead-context.md`
- `commercial-agent-context.md`

Pages updated:
- `context-engineering.md` — added 3 new sources, Five Pillars section, Research–Plan–Implement workflow section, Context as Infrastructure section, and 4 new cross-links
- `progressive-disclosure.md` — added Four Implementation Patterns section, Context Trigger System section, Context Rot Connection section, Multi-Agent section, and When Not to Use section
- `context-rot.md` — added 2 new sources, 500-Instruction Ceiling section, Smart/Warm/Dumb Zone framework with model benchmarks, Attention Sinks section, and 3 new cross-links

---

## 2026-04-21 — MCP docs ingested

Sources: 13 files from `docs/mcp/`

Pages created:
- `mcp-specification.md`
- `mcp-vs-a2a.md`
- `mcp-dev-summit.md` (combines long-live-mcp-aqfer.md + long-live-mcp-aws.md)
- `mcp-skills-vs-mcp.md`
- `mcp-typescript-sdk.md`
- `mcp-servers.md` (combines modelcontextprotocol-servers-github.md + anthropic-mcp-github-topics.md)
- `mcp-skills-interest-group.md` (combines skills-over-mcp-meeting-notes-2248.md + skills-over-mcp-office-hours-2460.md)
- `agent-to-agent-protocol.md`
- `mcp-transport.md`
- `mcp-programmatic-tool-calling.md`

Changes: Added 10 substantive wiki knowledge pages covering the MCP ecosystem — protocol specification, transport mechanisms, TypeScript SDK, server ecosystem, Skills vs MCP architecture, the Skills Over MCP working group standards process, A2A protocol comparison, MCP Dev Summit 2026 recap, and programmatic tool calling. All pages cross-link to existing wiki pages and to each other.
