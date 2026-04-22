# Tool Search — Epsilla Analysis

**Summary**: Epsilla's deep analysis of Tool Search as the most significant AI agent infrastructure shift of 2025-2026 — covering semantic tool discovery, accuracy benchmarks, prompt cache protection, and a full FAQ.
**Sources**: `docs/tool-calling/tool-search-redefining-agent-tool-calling-epsilla.md`, `docs/tool-calling/README.md`
**Last updated**: 2026-04-21

---

## What Is Tool Search?

Tool Search is a **lazy-loading mechanism for tool definitions**. Instead of pre-loading every available tool schema at startup, an AI model holds only a lightweight search stub. When a specific capability is required, it calls the search tool to find and inject the relevant definition just-in-time (source: tool-search-redefining-agent-tool-calling-epsilla.md).

> Conceptually, Tool Search is RAG applied to tool schemas rather than knowledge documents. It indexes tool names, descriptions, and parameters and retrieves them on demand.

See [[dynamic-tool-discovery]] for a cross-implementation view of this pattern.

---

## The Context Bloat Problem

Traditional tool calling pre-loads all definitions upfront. A typical enterprise setup (source: tool-search-redefining-agent-tool-calling-epsilla.md):

```
GitHub:  35 tools → ~26K tokens
Slack:   11 tools → ~21K tokens
Jira:    20 tools → ~17K tokens
Sentry:   5 tools →  ~3K tokens

Total: ~72K tokens consumed BEFORE conversation starts
```

Anthropic has observed tool definitions consuming **134K tokens** before any task begins. Even with 200K+ context windows, pre-loading this many schemas degrades tool-selection accuracy due to information overload and destroys prompt caching efficiency (source: tool-search-redefining-agent-tool-calling-epsilla.md).

---

## Tool Search vs. Traditional Calling

**Traditional approach** — all schemas loaded before the first user message:

```json
{
  "model": "claude-3-sonnet-20240229",
  "tools": [
    { "name": "get_weather", ... },
    { "name": "search_restaurants", ... },   // irrelevant
    { "name": "book_reservation", ... }      // irrelevant
  ]
}
```

**Tool Search approach** — start with a single stub, discover on demand:

```json
{
  "model": "claude-sonnet-4",
  "tools": [{ "type": "tool_search", "name": "tool_search" }]
}
// → Model calls tool_search("weather")
// → Discovers get_weather
// → Loads only that definition (~800 tokens)
// Total: ~1.3K tokens vs. ~72K
```

(source: tool-search-redefining-agent-tool-calling-epsilla.md)

---

## Benchmarks and Accuracy Improvements

| Dimension | Key Information |
|-----------|-----------------|
| **Essence** | Lazy loading — loads only tools required for the current task |
| **Token savings** | 85%+ (Anthropic); 34–64% (Spring AI cross-platform benchmark) |
| **Claude Opus 4 accuracy** | 49% → 74% with Tool Search enabled |
| **Claude Opus 4.5 accuracy** | 79.5% → 88.1% with Tool Search enabled |
| **Applicable scenarios** | 10+ tools; multiple MCP servers; definitions exceeding 10K tokens |

(source: tool-search-redefining-agent-tool-calling-epsilla.md)

---

## Implementations

| Platform | Implementation |
|----------|----------------|
| Anthropic Claude | `tool_search_tool` server tool (Claude Sonnet 4+) |
| OpenAI GPT-5.4 | `tool_search` (namespace-level) |
| Spring AI | `ToolSearchToolCallAdvisor` |

(source: tool-search-redefining-agent-tool-calling-epsilla.md)

See [[anthropic-tool-use]] for Claude-specific API details and [[programmatic-tool-calling]] for the broader Anthropic implementation.

---

## Prompt Cache Protection

Tool Search keeps the initial context prefix (system prompt + lightweight search stub) extremely stable. Full tool schemas are injected at the **end** of the context, not the beginning. This ensures (source: tool-search-redefining-agent-tool-calling-epsilla.md):

- The static prefix remains cacheable across turns and sessions.
- **TTFT (Time to First Token)** is reduced.
- Computational overhead drops significantly.

For context management strategy, see [[context-engineering]].

---

## Key Definitions

- **Tool Search** — dynamic tool discovery mechanism; model loads only needed schemas just-in-time (source: tool-search-redefining-agent-tool-calling-epsilla.md).
- **Context Bloat** — degradation caused by pre-loading massive JSON schemas of unused tools (source: tool-search-redefining-agent-tool-calling-epsilla.md).
- **Just-in-Time Retrieval (JITR)** — retrieve and inject information only at the exact moment the execution trajectory requires it (source: tool-search-redefining-agent-tool-calling-epsilla.md).
- **Prompt Caching Stability** — isolating dynamic elements (discovered schemas) to end of context so the static prefix stays cacheable (source: tool-search-redefining-agent-tool-calling-epsilla.md).

---

## FAQs

**Q: Why is Tool Search necessary when models have 200K+ context windows?**
Even with massive windows, pre-loading hundreds of schemas degrades accuracy due to information overload, inflates token costs per request, and destroys prompt cache efficiency (source: tool-search-redefining-agent-tool-calling-epsilla.md).

**Q: Does Tool Search increase overall system latency?**
While an additional search-and-load step is added, overall execution latency often *decreases* because the lighter initial context maximizes prompt cache hits and minimizes payload size sent to the LLM (source: tool-search-redefining-agent-tool-calling-epsilla.md).

**Q: How does Tool Search differ from RAG?**
Tool Search applies RAG principles specifically to tool schemas and function signatures rather than knowledge documents (source: tool-search-redefining-agent-tool-calling-epsilla.md).

---

## Related pages

- [[dynamic-tool-discovery]]
- [[programmatic-tool-calling]]
- [[programmatic-tool-calling-sdk]]
- [[mcp-programmatic-tool-calling]]
- [[tool-calling-patterns]]
- [[context-engineering]]
- [[anthropic-tool-use]]
- [[json-schema-for-ai]]
