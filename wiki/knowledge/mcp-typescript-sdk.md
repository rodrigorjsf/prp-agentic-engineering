# MCP TypeScript SDK

**Summary**: The official TypeScript SDK for MCP (`@modelcontextprotocol/sdk`) provides complete client and server implementations with STDIO and Streamable HTTP transports, Zod-based validation, OAuth 2.1 auth helpers, and middleware for Express and Hono.
**Sources**: mcp-typescript-sdk-github.md
**Last updated**: 2026-04-22

---

## Overview

The TypeScript SDK is the official implementation of the [[mcp-specification]] for Node.js and TypeScript environments, maintained by Anthropic. It implements the full MCP specification, providing (source: mcp-typescript-sdk-github.md):

- Client and server implementations
- Protocol types and validation (with Zod)
- Transport implementations: STDIO and Streamable HTTP
- Middleware integrations for Express and Hono
- Full TypeScript type safety

## Version Status

> ⚠️ The `main` branch now tracks the pre-alpha **V2 SDK** which has breaking changes from V1. For stable production use, see the `v1` branch. The npm package currently ships V1. V2 pre-alpha is available as `@modelcontextprotocol/sdk@next`.

V2 was announced at the [[mcp-dev-summit]] by Max Isbey at Anthropic — TypeScript V2 alpha is available, stable release ships alongside the June 2026 spec (source: mcp-typescript-sdk-github.md).

## Installation

```bash
npm install @modelcontextprotocol/sdk
# V2 pre-alpha:
npm install @modelcontextprotocol/sdk@next
```

## Quick Start: Server

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "Demo", version: "1.0.0" });

server.tool("add", { a: z.number(), b: z.number() }, async ({ a, b }) => ({
  content: [{ type: "text", text: String(a + b) }],
}));

const transport = new StdioServerTransport();
await server.connect(transport);
```

(source: mcp-typescript-sdk-github.md)

## Quick Start: Client

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const client = new Client({ name: "example-client", version: "1.0.0" });
const transport = new StdioClientTransport({ command: "node", args: ["server.js"] });

await client.connect(transport);
const tools = await client.listTools();
const result = await client.callTool({ name: "add", arguments: { a: 1, b: 2 } });
await client.close();
```

(source: mcp-typescript-sdk-github.md)

## Server Primitives

### Tools

```typescript
server.tool("get-weather", { city: z.string() }, async ({ city }) => {
  const weather = await fetchWeather(city);
  return { content: [{ type: "text", text: `Weather in ${city}: ${weather}` }] };
});
```

### Resources

```typescript
// Static resource
server.resource("config", "config://app", async (uri) => ({
  contents: [{ uri: uri.href, text: "App configuration here" }],
}));

// Dynamic resource with template
server.resource(
  "user-profile",
  new ResourceTemplate("users://{userId}/profile", { list: undefined }),
  async (uri, { userId }) => ({
    contents: [{ uri: uri.href, text: `Profile for user ${userId}` }],
  })
);
```

### Prompts (Skills delivery)

```typescript
server.prompt("review-code", { code: z.string() }, ({ code }) => ({
  messages: [{ role: "user", content: { type: "text", text: `Please review this code:\n\n${code}` } }],
}));
```

The Prompts primitive is one delivery mechanism discussed in [[mcp-skills-vs-mcp]] (source: mcp-typescript-sdk-github.md).

## Transport Options

See [[mcp-transport]] for the full transport conceptual overview.

### STDIO Transport (local deployments)

```typescript
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
const transport = new StdioServerTransport();
await server.connect(transport);
```

### Streamable HTTP Transport (remote deployments)

```typescript
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";

app.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
  res.on("finish", () => server.close());
});
```

(source: mcp-typescript-sdk-github.md)

## Middleware Integrations

```typescript
// Express
import { createExpressMcpMiddleware } from "@modelcontextprotocol/sdk/middleware/express.js";
app.use("/mcp", createExpressMcpMiddleware(server));

// Hono (works natively on Cloudflare Workers)
import { createHonoMcpMiddleware } from "@modelcontextprotocol/sdk/middleware/hono.js";
app.use("/mcp/*", createHonoMcpMiddleware(server));
```

TypeScript V2 runs natively on Cloudflare Workers (source: mcp-typescript-sdk-github.md).

## Authentication

The SDK includes OAuth 2.1-compliant authentication helpers via `OAuthServerProvider`. This enables implementing CIMD (Client ID Metadata Documents) and XAA (Cross-App Access) — auth mechanisms announced at the [[mcp-dev-summit]] (source: mcp-typescript-sdk-github.md).

## Error Handling

```typescript
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";

server.tool("my-tool", { id: z.string() }, async ({ id }) => {
  const result = await fetchById(id);
  if (!result) throw new McpError(ErrorCode.InvalidRequest, `Item not found: ${id}`);
  return { content: [{ type: "text", text: JSON.stringify(result) }] };
});
```

(source: mcp-typescript-sdk-github.md)

## Testing

The SDK includes in-memory transport utilities for testing MCP servers without real transport:

```typescript
import { InMemoryTransport } from "@modelcontextprotocol/sdk/inMemory.js";

const [clientTransport, serverTransport] = InMemoryTransport.createLinkedPair();
await server.connect(serverTransport);
await client.connect(clientTransport);
```

(source: mcp-typescript-sdk-github.md)

## V2 Highlights

The V2 pre-alpha introduces (source: mcp-typescript-sdk-github.md):
- Simplified API surface for common patterns
- Improved TypeScript types
- Streamlined transport registration
- Built-in Express/Hono/Node.js middleware
- **Dispatcher pattern**: cleanly separates MCP semantics from wire format and transport, making pluggable transports practical for the first time (source: long-live-mcp-aqfer.md)

## Related pages

- [[mcp-specification]]
- [[mcp-transport]]
- [[mcp-servers]]
- [[mcp-skills-vs-mcp]]
- [[mcp-dev-summit]]
- [[mcp-programmatic-tool-calling]]
