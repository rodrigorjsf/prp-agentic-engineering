# Anthropic Tool Use — Implementation Guide

**Summary**: How to implement tool use with the Claude API, covering tool definition best practices, `input_examples`, `tool_choice` control options, and how Claude responds when tools are available.
**Sources**: `docs/structured-outputs/anthropic-implement-tool-use.md`
**Last updated**: 2026-04-21

---

Tool use lets Claude call external functions. Tools are defined in the `tools` top-level parameter of the API request. Strict schema validation is layered on top via `strict: true` — see [[anthropic-strict-tool-use]]. (source: anthropic-implement-tool-use.md)

## Choosing a Model

- **Claude Opus 4.7**: Best for complex tools and ambiguous queries; handles multiple tools well and seeks clarification when needed.
- **Claude Haiku models**: Suitable for straightforward tools; may infer missing parameters.

When using tool use with extended thinking, consult the extended thinking compatibility notes. (source: anthropic-implement-tool-use.md)

## Tool Definition Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `name` | Yes | Must match `^[a-zA-Z0-9_-]{1,64}$` |
| `description` | Yes | Detailed description of what the tool does, when to use it, and its limitations |
| `input_schema` | Yes | JSON Schema object defining expected parameters |
| `input_examples` | No | Array of example input objects |
| `strict` | No | Set `true` to enable grammar-constrained schema validation |
| `cache_control` | No | Prompt caching configuration |

When you call the API with `tools`, Claude automatically receives a constructed system prompt explaining the available tools. (source: anthropic-implement-tool-use.md)

## Best Practices for Tool Definitions

**Provide extremely detailed descriptions** — this is the most important factor in tool performance. A good description covers: (source: anthropic-implement-tool-use.md)
- What the tool does
- When it should (and should not) be used
- What each parameter means and how it affects behavior
- Important caveats and limitations (aim for 3–4+ sentences per tool)

**Consolidate related operations** — rather than `create_pr`, `update_pr`, `close_pr`, use a single tool with an `action` parameter. Fewer, more capable tools reduce selection ambiguity. (source: anthropic-implement-tool-use.md)

**Good vs. poor description example:**

```python
# Good
{
    "name": "get_stock_price",
    "description": (
        "Retrieves the current stock price for a given ticker symbol. "
        "The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. "
        "The tool will return the closing price and is updated at the end of each trading day. "
        "It does not provide real-time prices or data for OTC markets."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "ticker": {"type": "string", "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."}
        },
        "required": ["ticker"]
    }
}

# Poor
{
    "name": "get_stock_price",
    "description": "Gets the stock price for a ticker.",
    "input_schema": {"type": "object", "properties": {"ticker": {"type": "string"}}, "required": ["ticker"]}
}
```

See [[json-schema-for-ai]] for guidance on writing effective `input_schema` definitions.

## Providing Tool Use Examples (`input_examples`)

Concrete input examples help Claude understand how to use a tool, especially for complex schemas. (source: anthropic-implement-tool-use.md)

```python
{
    "name": "book_flight",
    "input_examples": [
        {"origin": "JFK", "destination": "LAX", "date": "2025-12-01", "passengers": 2},
        {"origin": "SFO", "destination": "ORD", "date": "2025-11-15", "passengers": 1}
    ]
}
```

**Requirements and limitations:**
- Each example must be valid according to the tool's `input_schema` (invalid examples return `400`)
- Not supported for server-side tools
- Token cost: ~20–50 tokens for simple examples, ~100–200 for complex nested objects

## Controlling Output with `tool_choice`

| Value | Behavior |
|-------|----------|
| `auto` | Claude decides whether to call any tool (default when tools are provided) |
| `any` | Claude must use one of the provided tools (model's choice) |
| `tool` | Forces use of a specific named tool |
| `none` | Prevents tool use (default when no tools provided) |

When `tool_choice` is `any` or `tool`, the API prefills the assistant message — Claude will not emit a natural language explanation before `tool_use` blocks. (source: anthropic-implement-tool-use.md)

**Extended thinking compatibility**: only `auto` and `none` are compatible with extended thinking. **Claude Mythos Preview** does not support forced tool use — use `auto` and rely on prompting. (source: anthropic-implement-tool-use.md)

### Combining `tool_choice` with `strict: true`

Use `tool_choice: {"type": "any"}` + `strict: true` to guarantee both that a tool is called AND that its inputs conform to your schema: (source: anthropic-implement-tool-use.md)

```python
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=[{
        "name": "save_contact",
        "description": "Save a contact record.",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "email": {"type": "string"}
            },
            "required": ["name", "email"],
            "additionalProperties": False
        }
    }],
    tool_choice={"type": "any"},
    messages=[{"role": "user", "content": "Save Alice Smith, alice@example.com"}]
)
```

## Model Responses with Tools

Claude often comments on what it's doing before invoking tools. Your code should treat these as normal assistant text and not rely on specific phrasing conventions. (source: anthropic-implement-tool-use.md)

Example for "What's the weather in San Francisco right now, and what time is it there?":
```
Claude: "I'll check the current weather and time in San Francisco for you!"
[tool_use: get_weather {"location": "San Francisco, CA"}]
[tool_use: get_time {"location": "San Francisco, CA"}]
```

## Production Recommendations

- **Use meaningful namespacing** in tool names when spanning multiple services (e.g., `github_list_prs`, `slack_send_message`)
- **Return only high-signal information** from tool responses — semantic identifiers (slugs, UUIDs) rather than opaque references
- **Enable `strict: true`** for production agentic workflows — see [[anthropic-strict-tool-use]]

---

## Related pages

- [[anthropic-strict-tool-use]]
- [[structured-outputs-anthropic]]
- [[json-schema-for-ai]]
- [[tool-use-patterns]]
- [[agent-workflows]]
- [[agent-best-practices]]
- [[mcp-programmatic-tool-calling]]
- [[prompt-engineering]]
