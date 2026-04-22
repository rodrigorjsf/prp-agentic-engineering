# Tool Use Patterns

**Summary**: Patterns for defining and using tools with LLMs, covering single-tool forced use, multi-tool selection, strict schema enforcement, namespacing, and response handling — grounded in the Claude API implementation.
**Sources**: `docs/structured-outputs/anthropic-implement-tool-use.md`, `docs/structured-outputs/anthropic-strict-tool-use.md`, `docs/structured-outputs/anthropic-structured-outputs.md`
**Last updated**: 2026-04-21

---

Tool use patterns bridge the gap between an LLM's language capabilities and deterministic function execution. The patterns below are grounded in the Claude API but apply conceptually to any LLM tool use system. For schema design specifics, see [[json-schema-for-ai]]. For schema compliance guarantees, see [[anthropic-strict-tool-use]].

## Pattern 1: Single-Tool Forced Use

Force Claude to always call a specific tool using `tool_choice: {"type": "tool", "name": "<tool_name>"}`. Useful for structured extraction tasks where you always want the same output shape. (source: anthropic-implement-tool-use.md)

```python
response = client.messages.create(
    model="claude-opus-4-5",
    tools=[get_stock_price_tool],
    tool_choice={"type": "tool", "name": "get_stock_price"},
    messages=[{"role": "user", "content": "What is Apple's stock price?"}]
)
```

**When to use**: Data extraction pipelines, structured report generation, any workflow where you unconditionally need a function call.

**Caveat**: Not supported on Claude Mythos Preview. Not compatible with extended thinking. (source: anthropic-implement-tool-use.md)

## Pattern 2: Any-Tool Forced Use

Force Claude to call *some* tool (model's choice) using `tool_choice: {"type": "any"}`. Useful when you have several valid output shapes and want the model to pick the right one. (source: anthropic-implement-tool-use.md)

```python
response = client.messages.create(
    model="claude-sonnet-4-5",
    tools=[search_tool, lookup_tool, calculate_tool],
    tool_choice={"type": "any"},
    messages=[{"role": "user", "content": "What's 15% of 340?"}]
)
```

**When to use**: Routing/dispatch patterns, agentic workflows where the model selects the appropriate action.

## Pattern 3: Strict Schema Enforcement

Add `"strict": true` to a tool definition to activate grammar-constrained sampling. Combine with `tool_choice: {"type": "any"}` for the strongest guarantee — a tool *will* be called, and its inputs *will* be schema-valid. (source: anthropic-strict-tool-use.md, anthropic-implement-tool-use.md)

```python
tools = [{
    "name": "book_flight",
    "description": "Book a flight for the given passenger count and route.",
    "strict": True,
    "input_schema": {
        "type": "object",
        "properties": {
            "origin": {"type": "string"},
            "destination": {"type": "string"},
            "passengers": {"type": "integer"}
        },
        "required": ["origin", "destination", "passengers"],
        "additionalProperties": False
    }
}]
response = client.messages.create(
    model="claude-opus-4-5",
    tools=tools,
    tool_choice={"type": "any"},
    messages=[...]
)
```

**When to use**: Production agentic systems, booking/reservation systems, API integrations, financial calculations, database query builders. See [[anthropic-strict-tool-use]] for complexity limits.

## Pattern 4: Auto Tool Selection (Multi-Tool)

Let Claude decide which tools to call (and whether to call any) using `tool_choice: {"type": "auto"}` (the default). Claude may call multiple tools in a single response turn. (source: anthropic-implement-tool-use.md)

```python
# Claude may call get_weather AND get_time in the same response
response = client.messages.create(
    model="claude-opus-4-5",
    tools=[get_weather_tool, get_time_tool, search_tool],
    messages=[{"role": "user", "content": "What's the weather and time in SF right now?"}]
)
```

**When to use**: Conversational agents, assistants with mixed natural-language and function-calling needs.

**Handling multi-tool responses**: Iterate over `response.content` blocks — some are `text` blocks, others are `tool_use` blocks. Execute all tool calls and return results in the next `user` turn with `tool_result` blocks.

## Pattern 5: Consolidated Action Tools

Rather than creating a separate tool for every action (`create_pr`, `update_pr`, `close_pr`), group related operations into a single tool with an `action` parameter. This reduces tool selection ambiguity: (source: anthropic-implement-tool-use.md)

```json
{
  "name": "manage_pull_request",
  "description": "Create, update, or close a pull request. Use 'create' when opening a new PR, 'update' to change its description or title, 'close' to close without merging.",
  "input_schema": {
    "type": "object",
    "properties": {
      "action": {"type": "string", "enum": ["create", "update", "close"]},
      "pr_number": {"type": "integer"},
      "title": {"type": "string"},
      "body": {"type": "string"}
    },
    "required": ["action"]
  }
}
```

**When to use**: Any domain with CRUD-like operations (PRs, tickets, records).

## Pattern 6: Namespaced Tool Names

When tools span multiple services, prefix names with the service to avoid ambiguity and support tool search indexing: (source: anthropic-implement-tool-use.md)

```
github_list_prs
github_create_issue
slack_send_message
slack_list_channels
```

**When to use**: Multi-service agents, [[mcp-programmatic-tool-calling]] scenarios, any system where >10 tools are available.

## Pattern 7: Input Examples for Complex Tools

For complex tools with nested or non-obvious schemas, provide `input_examples` to show Claude valid inputs concretely: (source: anthropic-implement-tool-use.md)

```python
"input_examples": [
    {"origin": "JFK", "destination": "LAX", "date": "2025-12-01", "passengers": 2},
    {"origin": "SFO", "destination": "ORD", "date": "2025-11-15", "passengers": 1}
]
```

Token cost: ~20–50 tokens for simple examples, ~100–200 for complex nested objects.

## Pattern 8: JSON Output + Tool Use Combined

Use both `output_config.format` (JSON output) and `strict: true` (strict tool use) together in the same request when you need: (source: anthropic-structured-outputs.md)
- Reliable tool calls with schema-valid inputs, AND
- A structured JSON final response (not just a tool call)

This is useful for agentic workflows that must both *act* (via tools) and *report* (via structured response).

## Handling Tool Responses in Agent Loops

A complete [[agent-workflows]] tool loop:

1. Send request with tools defined
2. Receive response — iterate over `content` blocks
3. For each `tool_use` block: execute the function, capture result
4. Append assistant turn (with tool calls) to `messages`
5. Append `user` turn with `tool_result` blocks for each call
6. Send next request — repeat until `stop_reason: "end_turn"`

**Design tool responses carefully**: Return only high-signal information. Use semantic, stable identifiers (slugs, UUIDs) rather than opaque internal references. Include only the fields Claude needs to reason about its next step. (source: anthropic-implement-tool-use.md)

---

## Related pages

- [[anthropic-tool-use]]
- [[anthropic-strict-tool-use]]
- [[structured-outputs-anthropic]]
- [[json-schema-for-ai]]
- [[agent-workflows]]
- [[agent-best-practices]]
- [[mcp-programmatic-tool-calling]]
- [[prompt-engineering]]
- [[context-engineering]]
