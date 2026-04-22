# Tool Calling Patterns

**Summary**: A synthesis of all major tool calling patterns — static vs. dynamic loading, forced/auto/parallel calling, programmatic code-execution, and MCP Code Mode — with guidance on when to use each.
**Sources**: `docs/tool-calling/programmatic-tool-calling-claude-api.md`, `docs/tool-calling/tool-search-redefining-agent-tool-calling-epsilla.md`, `docs/tool-calling/cameronking4-programmatic-tool-calling-github.md`, `docs/tool-calling/mcp-programmatic-tool-calling-opensandbox-dev.md`, `docs/tool-calling/README.md`
**Last updated**: 2026-04-21

---

## Pattern Overview

| Pattern | Round-trips | Token cost | Best for |
|---------|-------------|------------|----------|
| Static tool list + auto | N | High (all schemas loaded) | < 10 tools, simple workflows |
| Static tool list + forced | 1+ | High | Guaranteed tool invocation |
| Parallel tool calling | 1 per batch | High (all schemas) | Independent simultaneous calls |
| Dynamic Tool Search | N (reduced) | Low (lazy schema load) | 10+ tools, MCP servers |
| Programmatic (code execution) | 2 (fixed) | Very low | Complex multi-tool orchestration |
| MCP Code Mode | 2–3 | Very low | Enterprise APIs, .NET/Java environments |

---

## 1. Static Tool List — Auto Mode

The model decides whether and which tool to call. All tool definitions are pre-loaded in the `tools` parameter (source: programmatic-tool-calling-claude-api.md).

```
tools: [tool_a, tool_b, tool_c, ...]
tool_choice: "auto"
```

**When to use**: Fewer than 10 tools, straightforward tasks, simple agentic loops.
**Limitation**: Every tool schema consumes input tokens on every request, even unused tools.

See [[anthropic-tool-use]] for API implementation details and [[json-schema-for-ai]] for schema design.

---

## 2. Forced Tool Use

`tool_choice: "any"` forces the model to call at least one tool. `tool_choice: {"type": "tool", "name": "X"}` forces a specific function (source: programmatic-tool-calling-claude-api.md).

Adding `strict: true` to a tool definition ensures Claude's output always matches the schema exactly (source: programmatic-tool-calling-claude-api.md).

**When to use**: Workflows that must collect structured data before responding; validation steps; guaranteed extraction.

---

## 3. Parallel Tool Calling

The model emits multiple `tool_use` blocks in a single response. Your application executes them concurrently, then returns all `tool_result` blocks together (source: programmatic-tool-calling-claude-api.md).

**When to use**: Multiple independent operations that can run simultaneously — e.g., fetching data from several APIs at once.
**Limitation**: Still one LLM round-trip per batch; intermediate results still enter the context.

---

## 4. Dynamic Tool Search (Lazy Loading)

Instead of pre-loading all schemas, the model starts with a single lightweight `tool_search` stub and discovers definitions on demand (source: tool-search-redefining-agent-tool-calling-epsilla.md):

```
Initial: System Prompt + tool_search stub (~500 tokens)
  ↓
Model calls tool_search("query")
  ↓
Relevant schema injected just-in-time
  ↓
Tool invoked
```

**Token savings**: 85%+ vs. static loading for large tool sets (source: tool-search-redefining-agent-tool-calling-epsilla.md).
**Accuracy gains**: Claude Opus 4: 49% → 74%; Claude Opus 4.5: 79.5% → 88.1% (source: tool-search-redefining-agent-tool-calling-epsilla.md).
**When to use**: 10+ tools, multiple MCP servers, schemas > 10K tokens, enterprise scale.

See [[tool-search-epsilla]] and [[dynamic-tool-discovery]] for full detail.

---

## 5. Programmatic Tool Calling (Code Execution)

Inspired by Anthropic's November 2025 advanced tool use announcement (source: cameronking4-programmatic-tool-calling-github.md). The LLM generates executable code that orchestrates all tool calls, runs once in a sandbox, and returns only the final result.

```
Round 1: LLM generates JavaScript/Python
  → parallel calls, conditionals, aggregations

Sandbox executes code
  → intermediate results NEVER enter LLM context

Round 2: LLM receives final result → responds to user
```

**LLM round-trips**: Always 2, regardless of how many tools are called (source: programmatic-tool-calling-claude-api.md).
**Token savings**: 80%+ on complex workflows (source: cameronking4-programmatic-tool-calling-github.md).
**Latency**: 3–5× faster than sequential calling (source: cameronking4-programmatic-tool-calling-github.md).
**When to use**: Complex multi-tool workflows; data aggregation across many calls; MCP-heavy agents.

See [[programmatic-tool-calling]] (Anthropic native) and [[programmatic-tool-calling-sdk]] (Vercel AI SDK implementation).

---

## 6. MCP Code Mode (Three-Tool Pattern)

The .NET/C# MCP Code Mode variant uses three distinct tools instead of a single `code_execution` server (source: mcp-programmatic-tool-calling-opensandbox-dev.md):

1. **`search`** — semantic discovery of relevant tools.
2. **`get_schema`** — retrieves full schema for chosen tool.
3. **`execute`** — runs LLM-generated Python code in an isolated sandbox.

Benefits include 50%+ token reduction, batch execution, and full sandbox isolation for security (source: mcp-programmatic-tool-calling-opensandbox-dev.md).

See [[mcp-programmatic-tool-calling]] for implementation details.

---

## Choosing a Pattern

```
< 10 tools, simple workflow?
  → Static list + auto mode

Need guaranteed tool invocation or strict schema?
  → Forced tool use + strict: true

Multiple independent calls in one step?
  → Parallel tool calling

10+ tools or MCP servers (token cost priority)?
  → Dynamic Tool Search

Complex orchestration, many sequential/parallel calls?
  → Programmatic tool calling (code execution)

Enterprise scale in .NET/Java with hundreds of APIs?
  → MCP Code Mode (search + get_schema + execute)
```

---

## Combining Patterns

Patterns compose. A common production configuration (source: tool-search-redefining-agent-tool-calling-epsilla.md, programmatic-tool-calling-claude-api.md):

- **Tool Search** reduces the schema loading overhead.
- **Programmatic calling** collapses orchestration round-trips.
- **Prompt caching** on the stable prefix maximizes cache hits.

See [[context-engineering]] for how to sequence these for maximum efficiency and [[agent-workflows]] for how they fit into the full agent loop.

---

## Related pages

- [[programmatic-tool-calling]]
- [[programmatic-tool-calling-sdk]]
- [[tool-search-epsilla]]
- [[dynamic-tool-discovery]]
- [[mcp-programmatic-tool-calling]]
- [[anthropic-tool-use]]
- [[agent-workflows]]
- [[context-engineering]]
- [[json-schema-for-ai]]
- [[structured-outputs-anthropic]]
- [[tool-use-patterns]]
