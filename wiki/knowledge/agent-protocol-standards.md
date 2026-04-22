# Agent Protocol Standards

**Summary**: An overview of the emerging standard protocols for AI agent communication — MCP, A2A, ACP, and ANP — covering their differences, complementarity, governance status, and guidance on when to use each.
**Sources**: `docs/agent-protocols/advancing-agentic-ai-communication-protocols.md`, `docs/agent-protocols/ai-agent-protocols-2026-guide.md`, `docs/agent-protocols/a2a-protocol-huggingface-space.md`
**Last updated**: 2026-04-21

---

## The Landscape in 2026

The agent protocol space has consolidated rapidly. Four protocols were competing as of mid-2025; by early 2026, the picture has simplified (source: ai-agent-protocols-2026-guide.md):

- **MCP** (Model Context Protocol) — the de facto agent-to-tool standard
- **A2A** (Agent-to-Agent Protocol) — the emerging agent-to-agent standard
- **ACP** — merged into A2A in September 2025; deprecated
- **ANP** — active in open-network/decentralized identity scenarios

The two dominant standards are **complementary, not competing**: MCP solves the agent-to-tool problem; A2A solves the agent-to-agent problem (source: a2a-protocol-huggingface-space.md).

## MCP: Agent-to-Tool

**Model Context Protocol** was created by Anthropic (November 2024) and donated to the Linux Foundation's Agentic AI Foundation (AAIF) in December 2025 (source: ai-agent-protocols-2026-guide.md).

| Attribute | Value |
|-----------|-------|
| Primary purpose | Agent ↔ Tool/Data/API |
| Transport | JSON-RPC over Streamable HTTP, stdio |
| Authentication | OAuth 2.0, OIDC Discovery |
| Discovery | MCP Registry, server.json |
| Key abstraction | Tools, Resources, Prompts |
| SDK languages | Python, TypeScript, C#, Java |
| Spec maturity | Stable (2025-11-25) |
| Monthly SDK downloads | 97M+ |

**What MCP does**: Provides a universal interface layer between AI agents and external systems. Every agent-tool integration formerly required a custom connector; MCP collapses M×N integrations to M+N (source: advancing-agentic-ai-communication-protocols.md).

**What MCP does NOT do**: Handle agent-to-agent communication. That is out of scope by design.

See [[mcp-specification]] for full documentation and [[anthropic-2026-full-connectivity]] for the philosophy behind agent-native MCP design.

## A2A: Agent-to-Agent

**Agent-to-Agent Protocol** was created by Google (April 2025) and donated to the Linux Foundation in June 2025 (source: ai-agent-protocols-2026-guide.md). The Technical Steering Committee includes Google, Microsoft, AWS, Cisco, Salesforce, ServiceNow, SAP, and IBM.

| Attribute | Value |
|-----------|-------|
| Primary purpose | Agent ↔ Agent |
| Transport | HTTP + JSON-RPC + SSE |
| Authentication | OAuth 2.0, mTLS, JWTs |
| Discovery | Agent Cards (JSON at `/.well-known/agent.json`) |
| Key abstraction | Tasks, Agent Cards |
| SDK languages | Python, TypeScript, Go, Java |
| Spec maturity | Stable (v0.3, July 2025) |

**What A2A does**: Enables agents from different vendors, frameworks, and organizations to collaborate on tasks without sharing internal logic. Each agent is treated as an opaque service (source: ai-agent-protocols-2026-guide.md).

See [[agent-to-agent-protocol]] and [[a2a-protocol]] for full documentation and [[mcp-vs-a2a]] for a direct comparison.

## ACP: Deprecated

**Agent Communication Protocol** was IBM Research's REST-native approach to agent interoperability, launched March 2025. In September 2025, IBM announced ACP would merge with A2A under the Linux Foundation (source: ai-agent-protocols-2026-guide.md).

- Do not build new systems on ACP
- Follow IBM's migration guide to A2A
- ACP's multipart/multimodal messaging capabilities now exist in A2A

## ANP: Open Network Discovery

**Agent Network Protocol** (by Agent Network Protocol Contributors) addresses scenarios where agents from unknown organizations must find and authenticate each other without a central registry (source: advancing-agentic-ai-communication-protocols.md).

| Attribute | Value |
|-----------|-------|
| Architecture | Decentralized (DIDs + JSON-LD semantic graphs) |
| Primary use | Agent discovery in open networks |
| Key feature | Decentralized Identifiers (DIDs) for identity |

ANP is relevant for public internet agent discovery scenarios where MCP and A2A's more centralized or enterprise-focused models may not apply.

## Complementarity Model

```
┌─────────────────────────────────────────────────┐
│              Enterprise Multi-Agent System        │
│                                                   │
│  Agent A ────── A2A ────── Agent B               │
│     │                         │                  │
│    MCP                       MCP                 │
│     │                         │                  │
│  Tool 1, 2, 3           Tool 4, 5, 6             │
└─────────────────────────────────────────────────┘
```

Each agent uses MCP to connect to its own tools and data sources, while A2A handles the agent-to-agent coordination layer (source: a2a-protocol-huggingface-space.md).

## Decision Framework

| Need | Protocol |
|------|---------|
| Agent needs tool access (database, API, SaaS) | MCP |
| Agents from different orgs need to collaborate | A2A |
| Human-in-the-loop mid-workflow | MCP (elicitation feature) |
| Long-running async agent workflows | A2A (task lifecycle + push notifications) |
| Agent discovery in open/public networks | ANP |
| Both tool access AND peer collaboration | MCP + A2A |

(source: ai-agent-protocols-2026-guide.md)

## Governance and Open Standards

Both MCP and A2A are now under the Linux Foundation umbrella (source: ai-agent-protocols-2026-guide.md):
- MCP → Agentic AI Foundation (AAIF), donated December 2025
- A2A → LF AI & Data, donated June 2025

This governance structure provides vendor-neutral stewardship and long-term stability for production deployments. The convergence of both protocols under the same umbrella organization suggests further integration and alignment is likely.

## Historical Predecessors

Earlier multi-agent communication standards include (source: advancing-agentic-ai-communication-protocols.md):
- **KQML** (1993): Knowledge Query and Manipulation Language — early communicative act library
- **FIPA** (2000): Foundation for Intelligent Physical Agents communicative act specification

Modern protocols build on these foundations but are designed for LLM-native, HTTP-first, cloud-scale environments.

## Related pages

- [[mcp-specification]]
- [[mcp-vs-a2a]]
- [[agent-to-agent-protocol]]
- [[a2a-protocol]]
- [[agent-communication-protocols]]
- [[ai-agent-protocols-2026]]
- [[multi-agent-communication]]
- [[agentic-systems-architectural-paradigms]]
- [[agent-best-practices]]
