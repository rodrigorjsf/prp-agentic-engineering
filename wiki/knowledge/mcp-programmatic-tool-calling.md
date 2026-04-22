# MCP Programmatic Tool Calling

**Summary**: MCP's programmatic (code-mode) tool calling allows a model to write a small program that chains multiple tool calls in sequence on the server side, reducing round-trips, improving efficiency, and fitting naturally with the stateless transport work described in [[mcp-transport]].
**Sources**: long-live-mcp-aqfer.md, mcp-typescript-sdk-github.md, mcp-specification.md
**Last updated**: 2026-04-22

---

## What Is Programmatic Tool Calling?

Programmatic tool calling (also called "composability through code") is a planned MCP capability where the model writes a small program that chains several tool calls in sequence **on the server side**, rather than making one tool call at a time over the network (source: long-live-mcp-aqfer.md).

MCP co-creator David Soria Parra flagged this at the [[mcp-dev-summit]] as part of the 2026 roadmap beyond the June spec release: "Composability through code — lets the model write a small program that chains several tool calls in sequence on the server side." (source: long-live-mcp-aqfer.md)

## Why It Matters

The current MCP tool-calling model is sequential and stateful: the client calls a tool, waits for a result, decides what to call next, and repeats. This creates several inefficiencies (source: mcp-http2-http3-reddit.md):

- **Round-trip latency**: Each tool call requires a network round-trip between the LLM client and the MCP server
- **Context window pressure**: Intermediate tool results must be returned to the LLM context, consuming tokens
- **Stateful connection requirement**: The server must hold the connection open across multiple exchanges

Programmatic tool calling addresses all three by moving the chaining logic to the server, executing multiple tools locally, and returning only the final result to the client.

## Relationship to Sampling

MCP already supports **sampling** — a server-initiated capability where the server can request the LLM to perform a completion mid-execution (source: mcp-specification.md):

```typescript
// Client-side: request LLM completion from the host
const result = await server.requestSampling({
  messages: [{ role: "user", content: { type: "text", text: "What is 2+2?" } }],
  maxTokens: 100,
});
```

Programmatic tool calling inverts this: instead of the server asking the LLM for a completion, the LLM gives the server a program to execute across multiple tools.

## Relationship to MRTR (Stateless Transport)

Programmatic tool calling complements [[mcp-transport]]. MRTR makes stateful interactions work on serverless infrastructure by turning "phone calls" into "email threads." Programmatic tool calling reduces the number of turns needed by batching tool invocations on the server side — together they enable powerful multi-step [[agent-workflows]] without holding connections open (source: long-live-mcp-aqfer.md).

## Context Window Management Connection

At the [[mcp-dev-summit]], DSP addressed context bloat — the problem that connecting an MCP server with thousands of tools blows out the context window. His answer: "that's a client problem, not a protocol problem." Claude Code already solved it with progressive tool discovery (loading tool definitions only when needed), achieving about 85% reduction in token usage on real workloads (source: long-live-mcp-aqfer.md).

Programmatic tool calling extends this: once the model has decided on a multi-step action, it can delegate the entire sequence to the server rather than pulling each intermediate result back into context. This is a direct application of [[context-engineering]] principles — only include in context what the model actually needs at each step.

## Skills Integration

Programmatic tool calling has a natural relationship with [[mcp-skills-vs-mcp]]. A skill can define a multi-step procedure, and the model can implement that procedure as a server-side program that chains the relevant tools. The skill provides the *what* and *how*; programmatic tool calling provides the *execution efficiency* (source: long-live-mcp-aqfer.md).

This is also related to the [[mcp-skills-interest-group]] discussions around "script-bearing skills" — skills with embedded code that needs to execute on the server:

```json
{
  "requires": {
    "language": "python3",
    "packages": ["requests"],
    "min_version": "3.11"
  }
}
```

## Current Status (April 2026)

Programmatic tool calling is a **planned feature** on the MCP roadmap beyond the June 2026 spec release. It is not yet available in production (source: long-live-mcp-aqfer.md).

The [[mcp-typescript-sdk]] already provides the foundation via the dispatcher pattern in V2, which cleanly separates MCP semantics from transport and makes server-side composition more tractable (source: long-live-mcp-aqfer.md).

For current multi-step tool orchestration, the standard approach is:
1. Use MCP's Sampling primitive for server-to-model interactions
2. Use [[agent-workflows]] patterns with multiple sequential tool calls
3. Structure [[subagents]] to each handle narrowly scoped tasks

## Security Considerations

Programmatic tool calling will require careful security design (source: mcp-specification.md):

- Server-side programs represent a form of code execution on behalf of the model
- Trust model must ensure the LLM-generated program cannot exceed the permissions of the tools it calls
- Users should retain visibility and control — similar to how [[mcp-specification]] requires explicit user consent before invoking any tool

## Related pages

- [[mcp-specification]]
- [[mcp-transport]]
- [[mcp-dev-summit]]
- [[mcp-skills-vs-mcp]]
- [[mcp-skills-interest-group]]
- [[mcp-typescript-sdk]]
- [[agent-workflows]]
- [[subagents]]
- [[context-engineering]]
