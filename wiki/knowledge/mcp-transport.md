# MCP Transport

**Summary**: MCP supports two official transport mechanisms — STDIO for local deployments and Streamable HTTP for remote deployments — with a June 2026 roadmap bringing stateless transport (MRTR) that unlocks serverless environments like AWS Lambda and Cloudflare Workers.
**Sources**: mcp-http2-http3-reddit.md, long-live-mcp-aqfer.md, mcp-typescript-sdk-github.md
**Last updated**: 2026-04-22

---

## Overview

The [[mcp-specification]] officially supports two transports, matching the two primary deployment contexts (source: mcp-http2-http3-reddit.md):

- **STDIO** — for local deployments (process-to-process communication)
- **Streamable HTTP** — for remote deployments over the network

Custom transports are supported for teams with specialized requirements, including potential HTTP/3 implementations.

## STDIO Transport

STDIO is the original MCP transport. The client and server communicate via standard input/output streams — ideal for local tool integrations where the MCP server runs as a child process (source: mcp-http2-http3-reddit.md).

**Best for**: Local IDE integrations, CLI tools, prototyping.

```typescript
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
const transport = new StdioServerTransport();
await server.connect(transport);
```

STDIO sidesteps all HTTP transport requirements and is the recommended starting point for prototyping or local tools (source: mcp-http2-http3-reddit.md).

## Streamable HTTP Transport

Streamable HTTP enables remote MCP deployments. It was a significant step forward from STDIO, unlocking cloud-hosted MCP servers (source: mcp-http2-http3-reddit.md).

**Current state**:
- Operates over HTTP/1.1 and HTTP/2
- Full MCP streaming effectively requires HTTP/2 or higher for correct full-duplex operation
- HTTP/1.1 works but only gives synchronous request/response — no true streaming or mid-request notifications
- HTTP/3 is being actively explored but is not part of the official specification (source: mcp-http2-http3-reddit.md)

**Community best practice**: If you want full MCP capability (streaming, notifications, interactive/incremental workflows), deploy your server with HTTP/2 enabled (source: mcp-http2-http3-reddit.md).

```typescript
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";

app.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
  res.on("finish", () => server.close());
});
```

## Current Challenges with Stateful Transport

The current stateful model creates real-world friction for enterprise deployments (source: mcp-http2-http3-reddit.md):

- **Scaling friction**: Stateful connections force "sticky" routing that pins traffic to specific servers, preventing effective auto-scaling
- **Serverless incompatibility**: AWS Lambda and Cloudflare Workers spin up per-request; long-held connections cannot be maintained
- **High barrier for simple tools**: Developers building simple ephemeral tools are required to manage complex backend storage
- **Infrastructure complexity**: Load balancers must parse full JSON-RPC payloads to route traffic instead of using standard HTTP patterns

## The June 2026 Roadmap: Stateless Transport

The MCP Transport Working Group published a December 2025 roadmap describing the evolution toward stateless transport (source: mcp-http2-http3-reddit.md). These changes were confirmed at the [[mcp-dev-summit]].

### MRTR: Multi Round-Trip Requests (SEP-2322)

The most important change for serverless deployments (source: long-live-mcp-aqfer.md):

> **Today**: A tool call is like a phone call — the client and server stay on the line. If the connection drops, the call is lost. This is structurally incompatible with serverless runtimes.
>
> **MRTR**: Turns the phone call into an email thread. Each message carries the full context of prior messages. The server can ask a question and close the thread; the client returns later — five seconds or five minutes — with a new message including the prior exchange. Any server can pick up the new message. No held connections, no sticky routing, no shared memory.

MRTR moves features like elicitation, sampling, and long-running tasks from "impossible on serverless" to "just a normal email thread" (source: long-live-mcp-aqfer.md).

### Stateless Protocol Design

Replacing the `initialize` handshake with per-request/response shared information. A `discovery` mechanism lets clients query server capabilities when needed (source: mcp-http2-http3-reddit.md).

### Session Elevation

Moving sessions from an implicit side-effect of transport connection to the **data model layer** — explicit sessions, similar to how HTTP uses cookies and tokens for stateful semantics over a stateless protocol (source: mcp-http2-http3-reddit.md).

### Server Cards

Structured metadata documents exposed at `/.well-known/mcp.json`. Server Cards enable clients to discover server capabilities, authentication requirements, and available primitives *before* establishing a connection — reducing the cost of discovery (source: mcp-http2-http3-reddit.md).

### Subscription Streams

Replacing the general-purpose `GET` stream with explicit subscription streams. Clients open dedicated streams for specific items they want to monitor. TTL values and ETags enable intelligent client-side caching (source: mcp-http2-http3-reddit.md).

### JSON-RPC Envelope Improvements

Exposing routing-critical information (RPC method, tool name) via standard HTTP paths or headers — allowing load balancers and API gateways to route traffic without parsing JSON bodies (source: mcp-http2-http3-reddit.md).

## SDK V2: Dispatcher Pattern

The [[mcp-typescript-sdk]] introduces a **dispatcher pattern** that cleanly separates MCP semantics from wire format and transport, making pluggable transports practical for the first time. TypeScript V2 runs natively on Cloudflare Workers (source: long-live-mcp-aqfer.md).

## HTTP/3 Status

HTTP/3 support is being actively explored but is not yet part of the official specification. No mainstream MCP servers or clients rely on HTTP/3 yet, but several vendors are experimenting. Custom transport implementations (including HTTP/3) are supported by the SDK architecture (source: mcp-http2-http3-reddit.md).

## Developer Guidance by Scenario

| Scenario | Recommendation |
|----------|---------------|
| Local prototyping | STDIO — simple, no HTTP requirements |
| Remote (current) | Streamable HTTP with HTTP/2 enabled |
| Serverless (current) | Wait for June 2026 MRTR spec release |
| Serverless (after June 2026) | Streamable HTTP with MRTR support |
| Custom transport (e.g., HTTP/3) | Use SDK's pluggable transport API |

(source: mcp-http2-http3-reddit.md)

## Related pages

- [[mcp-specification]]
- [[mcp-typescript-sdk]]
- [[mcp-dev-summit]]
- [[mcp-servers]]
- [[mcp-programmatic-tool-calling]]
- [[agent-workflows]]
