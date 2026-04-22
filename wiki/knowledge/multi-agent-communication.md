# Multi-Agent Communication

**Summary**: How AI agents communicate with each other, covering message-passing patterns, orchestration models, task lifecycle management, and the protocol infrastructure (A2A, MCP) that enables scalable multi-agent systems.
**Sources**: `docs/agent-protocols/a2a-protocol-huggingface-space.md`, `docs/agent-protocols/ai-agent-protocols-2026-guide.md`, `docs/agent-protocols/advancing-agentic-ai-communication-protocols.md`, `docs/agent-protocols/architectural-paradigms-advanced-agentic-systems.md`
**Last updated**: 2026-04-21

---

## The Core Problem

Multi-agent communication requires solving two distinct problems (source: advancing-agentic-ai-communication-protocols.md):

1. **Agent-to-tool communication**: How does a single agent access external tools, data sources, and APIs?
2. **Agent-to-agent communication**: How do multiple agents collaborate, delegate tasks, and share context?

These are addressed by different standards: [[mcp-specification]] for agent-to-tool, and [[agent-to-agent-protocol]] (A2A) for agent-to-agent. See [[agent-protocol-standards]] for the full landscape.

## Message Passing Patterns

### Request/Response (Synchronous)

The simplest pattern: a client agent sends a request and waits for a response (source: a2a-protocol-huggingface-space.md).

```
Client Agent → message/send → Remote Agent
Client Agent ← task status ← Remote Agent
Client Agent → tasks/get (poll) → Remote Agent
Client Agent ← completed result ← Remote Agent
```

Suitable for short-lived tasks where the result is available quickly.

### Streaming (Server-Sent Events)

Used when tasks produce results incrementally or require real-time progress updates (source: a2a-protocol-huggingface-space.md).

```
Client Agent → message/stream → Remote Agent
Client Agent ← SSE stream of events ← Remote Agent
  Events: Task, Message, TaskStatusUpdateEvent, TaskArtifactUpdateEvent
```

Streaming reduces perceived latency and enables agents to begin processing partial results.

### Push Notifications (Async Webhook)

For very long-running tasks or when persistent connections are impractical (source: a2a-protocol-huggingface-space.md).

```
Client Agent → message/send + webhookUrl → Remote Agent
Remote Agent → HTTP POST on state change → Client Agent's webhook
```

Enables fully decoupled, asynchronous multi-agent workflows.

## Orchestration Patterns

### Hierarchical Orchestration

A supervisory (orchestrator) agent coordinates a set of specialist agents (source: ai-agent-protocols-2026-guide.md):

```
Orchestrator Agent
    │── A2A ──→ Planning Agent
    │── A2A ──→ Research Agent
    └── A2A ──→ Synthesis Agent
```

The orchestrator manages task delegation, result collection, and error recovery. Each specialist agent exposes its capabilities via an Agent Card and handles its own tool connectivity via MCP.

### Peer-to-Peer Delegation

Agents delegate to each other without a central orchestrator (source: a2a-protocol-huggingface-space.md). Agent A discovers Agent B's capabilities through its Agent Card and delegates tasks directly:

```
Agent A ── A2A ──→ Agent B (discovered via /.well-known/agent.json)
Agent B ── A2A ──→ Agent C (for sub-tasks)
```

### The Layered Stack

In production multi-agent systems, communication is organized in layers (source: ai-agent-protocols-2026-guide.md):

```
Layer 3 — Orchestration
  Supervisory agent coordinates via A2A, accesses monitoring tools via MCP

Layer 2 — Agent Coordination (A2A)
  Agents discover each other, delegate tasks, receive results

Layer 1 — Tool Access (MCP)
  Each agent connects to its own tools via MCP servers
```

## Agent Discovery

Agents must discover each other before they can communicate. A2A uses **Agent Cards** — JSON metadata documents hosted at `/.well-known/agent.json` — to expose capabilities, authentication requirements, and supported interaction modes (source: a2a-protocol-huggingface-space.md).

This approach mirrors how DNS and OpenAPI specs work: a well-known URL provides a machine-readable description of what the agent can do.

For open-network discovery (across organizational boundaries without a central registry), the Agent Network Protocol (ANP) uses Decentralized Identifiers (DIDs) and JSON-LD semantic graphs (source: advancing-agentic-ai-communication-protocols.md).

## Task Lifecycle Management

A2A defines a structured task lifecycle for delegated work (source: a2a-protocol-huggingface-space.md):

```
submitted → working → input-required → completed
                   └─────────────────→ failed
```

- **submitted**: Client has sent the task; server has acknowledged
- **working**: Remote agent is actively processing
- **input-required**: Agent needs additional information from the client before proceeding
- **completed**: Task finished successfully; artifacts are available
- **failed**: Task could not be completed

This lifecycle enables reliable, long-running operations that span minutes, hours, or days.

## Content Types and Multimodal Messaging

Agents exchange messages containing typed `Part` objects (source: a2a-protocol-huggingface-space.md):

| Part Type | Content |
|-----------|---------|
| `TextPart` | Plain text content |
| `FilePart` | Files as base64-encoded bytes or URI references |
| `DataPart` | Structured JSON data (forms, parameters) |

**Artifacts** represent outputs generated by a remote agent: documents, images, spreadsheets, or structured data — returned as Part objects, potentially streamed incrementally.

## Authentication and Security

Both MCP and A2A converge on OAuth 2.0 as the authentication standard (source: ai-agent-protocols-2026-guide.md):

- **MCP**: OAuth 2.0, OIDC Discovery
- **A2A**: OAuth 2.0, mTLS, JWTs
- Both support enterprise identity infrastructure without custom auth schemes

## Programmatic vs. Sequential Communication

A critical design pattern for multi-agent systems: prefer programmatic tool composition over sequential tool-calling (source: architectural-paradigms-advanced-agentic-systems.md).

**Sequential (avoid)**: Agent calls Tool A → waits → calls Tool B → waits → calls Tool C. High latency, multiple round trips, poor throughput.

**Programmatic (prefer)**: Agent writes a script composing A, B, and C → executes in one operation. Low latency, single execution context.

This is especially important for [[subagents]] that orchestrate multiple tool calls as part of a larger workflow. See [[anthropic-2026-full-connectivity]] for the philosophy behind this shift.

## Human-in-the-Loop Patterns

Multi-agent systems can incorporate human oversight at defined points:

- **MCP Elicitation**: MCP servers can request structured input from users mid-workflow (source: ai-agent-protocols-2026-guide.md). Enables approval gates, credential collection, and clarification requests.
- **A2A input-required**: The task lifecycle includes an `input-required` state for situations requiring human or client input before the remote agent can proceed.

For fluid, real-time human-agent collaboration scenarios, see [[human-agent-collaboration]] and its treatment of Theory of Mind reasoning.

## Related pages

- [[agent-protocol-standards]]
- [[mcp-specification]]
- [[agent-to-agent-protocol]]
- [[a2a-protocol]]
- [[mcp-vs-a2a]]
- [[agent-workflows]]
- [[subagents]]
- [[context-engineering]]
- [[human-agent-collaboration]]
- [[agent-best-practices]]
