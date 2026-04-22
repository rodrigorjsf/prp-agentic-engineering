# Anthropic Strict Tool Use

**Summary**: Setting `strict: true` on a Claude tool definition activates grammar-constrained sampling, guaranteeing tool inputs exactly match the provided JSON Schema — eliminating type mismatches and missing fields in agentic systems.
**Sources**: `docs/structured-outputs/anthropic-strict-tool-use.md`, `docs/structured-outputs/anthropic-implement-tool-use.md`
**Last updated**: 2026-04-21

---

Strict tool use is the tool-input counterpart to JSON outputs. Where [[structured-outputs-anthropic]] controls *what Claude says*, strict tool use controls *how Claude calls your functions*. (source: anthropic-strict-tool-use.md)

## Why It Matters for Agents

Without strict mode, Claude may provide `passengers: "two"` or `passengers: "2"` when your booking function expects `passengers: 2`. This causes runtime errors and requires defensive validation and retry logic throughout the pipeline. (source: anthropic-strict-tool-use.md)

**With `strict: true`:**
- Functions always receive correctly-typed arguments
- No validation/retry loops for tool calls
- Production agents that work consistently at scale

## Enabling Strict Mode

Add `"strict": true` as a top-level property alongside `name`, `description`, and `input_schema`. Also add `"additionalProperties": false` to your schema objects — this is required for the grammar compiler. (source: anthropic-strict-tool-use.md)

```json
{
  "name": "book_flight",
  "description": "Book a flight for the given passenger count and route.",
  "strict": true,
  "input_schema": {
    "type": "object",
    "properties": {
      "origin": {
        "type": "string",
        "description": "IATA airport code for the departure airport"
      },
      "destination": {
        "type": "string",
        "description": "IATA airport code for the arrival airport"
      },
      "passengers": {
        "type": "integer",
        "description": "Number of passengers"
      }
    },
    "required": ["origin", "destination", "passengers"],
    "additionalProperties": false
  }
}
```

**What is guaranteed:**
- The tool `input` block strictly follows `input_schema`
- The tool `name` is always valid (from the provided tool set) (source: anthropic-strict-tool-use.md)

## Combining with `tool_choice`

Pair `strict: true` with `tool_choice: {"type": "any"}` for the strongest guarantee: Claude *will* call a tool *and* its inputs will be schema-valid. (source: anthropic-strict-tool-use.md, anthropic-implement-tool-use.md)

```python
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    tools=[{"name": "book_flight", "strict": True, "input_schema": { ... }}],
    tool_choice={"type": "any"},
    messages=[{"role": "user", "content": "Book a flight from JFK to LAX for 2 passengers"}]
)
```

See [[anthropic-tool-use]] for the full `tool_choice` options and compatibility constraints.

## Common Use Cases

| Use case | Why strict mode helps |
|----------|-----------------------|
| **Booking systems** | Guarantees integer passenger counts, valid enum seat classes, required date fields |
| **Database queries** | Ensures filter parameters have correct types, preventing malformed queries |
| **API integrations** | Guarantees function calls match the expected API contract exactly |
| **Multi-agent pipelines** | Ensures upstream Claude calls pass correctly-typed inputs to downstream agents |
| **Financial calculations** | Prevents string-typed amounts where integers or floats are required |

(source: anthropic-strict-tool-use.md)

## Schema Complexity Limits

The same limits from [[structured-outputs-anthropic]] apply to strict tools (combined across all strict schemas in a request): (source: anthropic-strict-tool-use.md)

| Limit | Value |
|-------|-------|
| Strict tools per request | **20** |
| Total optional parameters across all strict tool schemas | **24** |
| Total parameters with union types across all strict schemas | **16** |

Exceeding these returns `400 "Schema is too complex for compilation"`. See [[json-schema-for-ai]] for tips on reducing complexity.

## JSON Schema Limitations

Strict tool use uses the same constrained JSON Schema subset as structured outputs. Some features (e.g., `minimum`, `maximum`, `minLength`, `maxLength`) are not supported. See the [Structured Outputs guide](./structured-outputs-anthropic.md) for the complete list. (source: anthropic-strict-tool-use.md)

## Data Retention

Tool `input_schema` definitions are compiled into grammars and **cached for up to 24 hours**. Prompts and responses qualify for Zero Data Retention (ZDR). (source: anthropic-strict-tool-use.md)

**HIPAA eligible** — but **PHI must not appear in schema definitions**:
- Property names
- `enum` values
- `const` values
- `pattern` regular expressions

PHI should only appear in message content (prompts and responses). (source: anthropic-strict-tool-use.md)

---

## Related pages

- [[structured-outputs-anthropic]]
- [[anthropic-tool-use]]
- [[json-schema-for-ai]]
- [[tool-use-patterns]]
- [[agent-workflows]]
- [[agent-best-practices]]
- [[mcp-programmatic-tool-calling]]
