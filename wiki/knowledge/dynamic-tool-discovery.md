# Dynamic Tool Discovery

**Summary**: How AI agents find the right tool at runtime using semantic search instead of static pre-loaded lists — the Tool Search pattern, its scalability advantages, and its relationship to context engineering.
**Sources**: `docs/tool-calling/tool-search-redefining-agent-tool-calling-epsilla.md`, `docs/tool-calling/programmatic-tool-calling-claude-api.md`, `docs/tool-calling/mcp-programmatic-tool-calling-opensandbox-dev.md`, `docs/tool-calling/README.md`
**Last updated**: 2026-04-21

---

## Static vs. Dynamic Tool Loading

### Static (traditional) approach

All tool definitions are injected into the model context before any conversation begins. For a 5-server MCP setup (source: mcp-programmatic-tool-calling-opensandbox-dev.md):

| Server | Tools | Tokens |
|--------|-------|--------|
| GitHub | 35 | ~26K |
| Slack | 11 | ~21K |
| Jira | 20 | ~17K |
| Sentry | 5 | ~3K |
| Grafana | 5 | ~3K |

Total: **~70–134K tokens** consumed before the first user message. This is *context bloat*.

### Dynamic (Tool Search) approach

The model starts with only a **lightweight search stub (~500 tokens)**. When a capability is needed, it queries the search tool and receives only the relevant schema just-in-time (source: tool-search-redefining-agent-tool-calling-epsilla.md):

```
Initial context:  System Prompt + tool_search stub  (~500 tokens)
    ↓
User: "Create a PR on GitHub"
    ↓
Model → tool_search("github pull request")
    ↓
Discovers github.createPullRequest
    ↓
Injects only that definition (~800 tokens)
    ↓
Invokes tool

Total: ~1.3K tokens (vs. ~72K traditional)
```

---

## Why This Is Like RAG

Tool Search applies the same principle as Retrieval-Augmented Generation, but to tool schemas instead of knowledge documents (source: tool-search-redefining-agent-tool-calling-epsilla.md):

- **RAG**: query → retrieve knowledge chunks → inject into context → answer
- **Tool Search**: query → retrieve tool definition → inject into context → invoke tool

Both are instances of **Just-in-Time Retrieval (JITR)** — a core context engineering principle: do not preemptively load all potentially useful information; retrieve and inject it precisely when required (source: tool-search-redefining-agent-tool-calling-epsilla.md).

See [[context-engineering]] for the broader JITR strategy in agentic systems.

---

## The MCP Code Mode Three-Tool Pattern

In MCP-based implementations, dynamic discovery uses three sequential tools rather than a single search stub (source: mcp-programmatic-tool-calling-opensandbox-dev.md):

1. **`search`** — discovers tools matching a query, returning names and brief descriptions.
2. **`get_schema`** — retrieves the full parameter schema for specific tool names.
3. **`execute`** — runs generated code in a sandbox that invokes the discovered tool.

This three-step pattern is the `.NET/C# MCP Code Mode` approach, as opposed to Anthropic's single `tool_search` server tool (source: mcp-programmatic-tool-calling-opensandbox-dev.md).

See [[mcp-programmatic-tool-calling]] for implementation details and [[tool-calling-patterns]] for a comparison of all approaches.

---

## Accuracy vs. Scale Trade-off

Static loading hurts tool-selection accuracy even when context limits aren't reached — information overload degrades reasoning (source: tool-search-redefining-agent-tool-calling-epsilla.md):

| Model | Accuracy (static) | Accuracy (Tool Search) |
|-------|-------------------|------------------------|
| Claude Opus 4 | 49% | 74% |
| Claude Opus 4.5 | 79.5% | 88.1% |

Dynamic discovery reduces the decision space presented to the model at any given moment, improving both accuracy and efficiency.

---

## Prompt Cache Implications

Static tool lists that change across requests destroy prompt cache hits. Dynamic Tool Search fixes this by (source: tool-search-redefining-agent-tool-calling-epsilla.md):

- Keeping the stable prefix (system prompt + search stub) **unchanged across turns**.
- Injecting discovered schemas only at the **end** of the context.

Result: dramatically lower TTFT (Time to First Token) and fewer cache misses. See [[context-engineering]] for full prompt cache strategy.

---

## When to Use Dynamic Discovery

Dynamic tool discovery is recommended when (source: tool-search-redefining-agent-tool-calling-epsilla.md, mcp-programmatic-tool-calling-opensandbox-dev.md):

- The agent has **10+ tools** available.
- Tool definitions span **multiple MCP servers**.
- Combined tool schemas exceed **10K tokens**.
- The application must scale to **hundreds of APIs** (enterprise environments).

For smaller tool sets (fewer than 10 tools, < 10K token schemas), static loading remains simpler and sufficient. See [[tool-calling-patterns]] for guidance on when each pattern applies.

---

## Implementations at a Glance

| Platform | Mechanism |
|----------|-----------|
| Anthropic Claude (Sonnet 4+) | `tool_search` server tool |
| OpenAI GPT-5.4 | `tool_search` (namespace-level) |
| Spring AI | `ToolSearchToolCallAdvisor` |
| .NET MCP (Code Mode) | `search` + `get_schema` + `execute` |
| Vercel AI SDK | `withProgrammaticCalling()` — injects `code_execution` meta-tool |

(sources: tool-search-redefining-agent-tool-calling-epsilla.md, mcp-programmatic-tool-calling-opensandbox-dev.md, cameronking4-programmatic-tool-calling-github.md)

---

## Related pages

- [[tool-search-epsilla]]
- [[programmatic-tool-calling]]
- [[programmatic-tool-calling-sdk]]
- [[mcp-programmatic-tool-calling]]
- [[tool-calling-patterns]]
- [[context-engineering]]
- [[agent-workflows]]
- [[anthropic-tool-use]]
- [[json-schema-for-ai]]
