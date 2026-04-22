# Agent-to-Agent Protocol

**Summary**: A2A (Agent-to-Agent Protocol) is Google's open standard for enabling autonomous software agents to communicate, coordinate, and collaborate regardless of vendor or framework — complementing MCP's agent-to-tool layer with an agent-to-agent orchestration layer.
**Sources**: a2a-protocol-huggingface.md, mcp-vs-a2a-dzone.md
**Last updated**: 2026-04-22

---

## What Is A2A?

The Agent-to-Agent (A2A) Protocol is an open standard introduced by Google in early 2025 for multi-agent systems. Where [[mcp-specification]] standardizes how agents access tools and resources, A2A standardizes how agents communicate with each other (source: a2a-protocol-huggingface.md).

A2A enables autonomous software agents to discover, delegate, negotiate, and share tasks or state asynchronously, regardless of framework or vendor (source: mcp-vs-a2a-dzone.md).

## Core Concepts

**Agent Cards** are JSON descriptors that advertise an agent's capabilities, authentication requirements, and supported modalities (text, audio, video, structured data). They are exposed at `/.well-known/agent.json` (source: a2a-protocol-huggingface.md).

**Tasks** are the unit of work in A2A. Agents delegate tasks to one another; tasks can be synchronous or long-running/asynchronous (source: a2a-protocol-huggingface.md).

**Artifacts** are the outputs of completed tasks. Agents pass artifacts to downstream agents in a multi-step [[agent-workflows]] pattern, enabling chained processing pipelines (source: a2a-protocol-huggingface.md).

**Push Notifications** support real-time updates for long-running tasks via webhooks or Server-Sent Events (SSE) (source: a2a-protocol-huggingface.md).

## How A2A Differs from MCP

| Dimension | A2A | MCP |
|-----------|-----|-----|
| Full name | Agent-to-Agent Protocol | Model Context Protocol |
| Origin | Google (early 2025) | Anthropic (November 2024) |
| Primary purpose | Agent-to-agent coordination | Agent-to-tool/resource integration |
| Communication model | Peer-to-peer between agents | Client (agent) to server (tool) |
| State | Stateful tasks with lifecycle | Stateless-ish tool invocations |
| Discovery | Agent Cards at `/.well-known/agent.json` | MCP Registry / capability negotiation |
| Authentication | Per-agent auth, supports enterprise SSO | OAuth 2.1, CIMD, XAA |
| Modalities | Text, audio, video, structured data | Text, binary resources |
| Industry support | Google, broad ecosystem | Anthropic, 170+ AAIF members |

(source: a2a-protocol-huggingface.md)

## Use Cases Where A2A Shines

1. **Research pipelines**: A coordinator agent (A2A) delegates to a web research specialist, a code execution specialist, and a summarizer — each using MCP for their specific tool access (source: a2a-protocol-huggingface.md).

2. **Customer service orchestration**: A triage agent routes tickets to billing specialist, technical specialist, or escalation agent based on intent — each running independently with their own tools (source: a2a-protocol-huggingface.md).

3. **Data pipeline automation**: A planning agent spawns data extraction agents in parallel (A2A), collects artifacts, then delegates to transformation and reporting agents (source: a2a-protocol-huggingface.md).

These patterns align with [[subagents]] and [[agent-workflows]] best practices for multi-agent system design.

## A2A + MCP Combined Architecture

The two protocols are designed to be complementary. A2A handles the orchestration layer; MCP handles how each agent accesses its tools (source: a2a-protocol-huggingface.md):

```
┌─────────────────────────────────────────────────────────────────────┐
│                      ENTERPRISE AI PLATFORM                         │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    A2A ORCHESTRATION LAYER                  │    │
│  │   Orchestrator Agent                                        │    │
│  │        │ (A2A delegation)                                   │    │
│  │   ┌────┴────────────────────────┐                          │    │
│  │   V                             V                          │    │
│  │ Research Agent              Writer Agent                   │    │
│  │ (A2A peer)                  (A2A peer)                     │    │
│  └───────┬─────────────────────────┬───────────────────────── ┘    │
│          │ MCP tool access         │ MCP tool access                │
│  ┌───────▼─────────────────────────▼───────────────────────────┐    │
│  │                    MCP TOOL ACCESS LAYER                    │    │
│  │  Web Search   │  Database  │  File System  │  APIs          │    │
│  └─────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

## Industry Adoption

Companies exploring or adopting A2A (source: a2a-protocol-huggingface.md):
- **Google** (creator and primary advocate)
- **Salesforce** (AgentForce integration)
- **SAP** (Business AI)
- **ServiceNow** (Now Assist)
- **Workday**

## Governance

A2A and MCP operate on parallel tracks with separate governance bodies and separate specifications. No official bridge protocol exists yet, though community implementations use both. The industry consensus is that both protocols will coexist as complementary layers in enterprise AI architectures (source: a2a-protocol-huggingface.md).

## Resources

- [A2A Protocol GitHub](https://github.com/google-a2a/a2a-protocol)
- [A2A Protocol Specification](https://google-a2a.github.io/a2a-spec/)
- [Hugging Face: a2aprotocol organization](https://huggingface.co/a2aprotocol)

## Related pages

- [[mcp-vs-a2a]]
- [[mcp-specification]]
- [[agent-workflows]]
- [[subagents]]
- [[agent-best-practices]]
- [[mcp-programmatic-tool-calling]]
