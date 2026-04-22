# Programmatic Tool Calling — AI SDK Implementation

**Summary**: cameronking4's open-source proof-of-concept implementing Programmatic Tool Calling on Vercel AI SDK 5.0 and Next.js 16 — replacing multi-round-trip tool calling with sandboxed code execution across 100+ LLM providers.
**Sources**: `docs/tool-calling/cameronking4-programmatic-tool-calling-github.md`, `docs/tool-calling/README.md`
**Last updated**: 2026-04-21

---

## The Problem: N Round-Trips

Traditional LLM tool calling is inherently sequential and expensive. Each tool call is a separate LLM round-trip; intermediate results accumulate in the context window (source: cameronking4-programmatic-tool-calling-github.md):

```
User: "Get data for users 1-5 and find the highest scorer"

Round 1: LLM → getUser(1) → result → LLM (context grows)
Round 2: LLM → getUser(2) → result → LLM (context grows)
...
Round 6: LLM → final answer

6 LLM calls × full context each = high latency + high token cost
```

This is the core inefficiency that Programmatic Tool Calling (PTC) solves. See [[tool-calling-patterns]] for a taxonomy of all approaches.

---

## The Solution: Code Generation + Sandbox Execution

PTC collapses N round-trips into **2 fixed LLM calls** (source: cameronking4-programmatic-tool-calling-github.md):

```
Round 1: LLM generates JavaScript:
  const users = await Promise.all([
    getUser({ id: '1' }), getUser({ id: '2' }),
    getUser({ id: '3' }), getUser({ id: '4' }),
    getUser({ id: '5' })
  ]);
  return users.sort((a,b) => b.score - a.score)[0];

→ Execute in Vercel Sandbox → Return final result only

Round 2: LLM receives final answer, responds to user
```

Intermediate results **never enter the LLM context**, preventing context pollution (source: cameronking4-programmatic-tool-calling-github.md).

See [[programmatic-tool-calling]] for Anthropic's native `code_execution` server tool implementing the same concept.

---

## Efficiency Metrics

| Metric | Traditional | PTC | Improvement |
|--------|-------------|-----|-------------|
| LLM Round-trips | N (per tool) | 2 (fixed) | 90% reduction |
| Context Growth | Exponential | Constant | 85% efficiency |
| Token Usage (10 tools) | ~70,000 | ~14,000 | **80% savings** |
| Latency | Sequential | Parallel | **3–5× faster** |
| MCP Tool Calls | N round-trips | 1 code_execution | 60–80% savings |

(source: cameronking4-programmatic-tool-calling-github.md)

---

## Architecture

```
User Request
    ↓
Vercel AI SDK 5.0 + withProgrammaticCalling(tools)
  ├── Wraps local tools (Zod schemas)
  ├── Wraps MCP tools (JSON Schema)
  └── Injects code_execution meta-tool
    ↓
LLM (Any Provider via AI Gateway — 100+ models)
  Generates JavaScript orchestrating N tool calls
    ↓
Vercel Sandbox (Isolated Cloud Execution)
  ├── Local Tools: getUser(), calculate()
  └── MCP Bridge (File-based IPC):
      ├── mcp_firecrawl_scrape()
      └── mcp_github_search()
    ↓
Main Process (MCP Tool Bridge Monitor)
  Routes sandbox MCP requests to real MCP servers
    ↓
Final Result Only → Back to LLM → User Response
```

(source: cameronking4-programmatic-tool-calling-github.md)

For MCP integration details, see [[mcp-programmatic-tool-calling]].

---

## Usage Example

```typescript
import { withProgrammaticCalling } from 'programmatic-tool-calling-ai-sdk';
import { tool } from 'ai';
import { z } from 'zod';

const myTools = {
  getUser: tool({
    description: 'Get user by ID',
    inputSchema: z.object({ id: z.string() }),
    execute: async ({ id }) => ({ id, name: 'Alice', score: 95 }),
  }),
};

const { tools } = withProgrammaticCalling(myTools);
// LLM now has access to code_execution meta-tool
// Can call getUser() in parallel for multiple IDs
// Executes in Vercel Sandbox; returns only final result
```

(source: cameronking4-programmatic-tool-calling-github.md)

See [[json-schema-for-ai]] for schema design within these tool definitions.

---

## Token Savings Tracking

PTC tracks four saving categories (source: cameronking4-programmatic-tool-calling-github.md):

```json
{
  "intermediateResultTokens": 12500,
  "roundTripContextTokens":   35000,
  "toolCallOverheadTokens":     400,
  "llmDecisionTokens":          720,
  "totalSaved":               48620
}
```

---

## Cost Analysis

### Vercel Sandbox Pricing

| Metric | Rate | Free Tier (Hobby) |
|--------|------|-------------------|
| Active CPU Time | $0.128/hour | 5 hours/month |
| Provisioned Memory | $0.0106/GB-hour | 420 GB-hours |
| Network Bandwidth | $0.15/GB | 20 GB |
| Sandbox Creations | $0.60/million | 5,000 |

### ROI Per Complex Workflow (10 tools)

| Metric | Traditional | PTC |
|--------|-------------|-----|
| LLM Round-trips | 10 | 2 |
| Context tokens | ~70,000 | ~14,000 |
| LLM cost (GPT-4) | $0.70–$2.10 | $0.14–$0.42 |
| Sandbox cost | $0 | ~$0.002 |
| **Net Savings** | — | **$0.50–$1.70** |

(source: cameronking4-programmatic-tool-calling-github.md)

---

## Key Features

- **Universal model support** — Anthropic Claude, OpenAI GPT, and 100+ models via Vercel AI Gateway (source: cameronking4-programmatic-tool-calling-github.md).
- **Vercel Sandbox** — isolated Node.js 22 cloud environment with automatic syntax validation (source: cameronking4-programmatic-tool-calling-github.md).
- **MCP integration** — file-based IPC bridge supporting HTTP, SSE, and Stdio MCP transports (source: cameronking4-programmatic-tool-calling-github.md).
- **Defensive helpers** — `toArray`, `safeGet`, `isSuccess` injected into generated code to prevent runtime errors (source: cameronking4-programmatic-tool-calling-github.md).

---

## Related pages

- [[programmatic-tool-calling]]
- [[mcp-programmatic-tool-calling]]
- [[tool-calling-patterns]]
- [[dynamic-tool-discovery]]
- [[tool-search-epsilla]]
- [[agent-workflows]]
- [[context-engineering]]
- [[json-schema-for-ai]]
- [[structured-outputs-anthropic]]
