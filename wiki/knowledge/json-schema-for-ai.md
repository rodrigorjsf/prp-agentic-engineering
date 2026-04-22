# JSON Schema for AI — Constraining LLM Outputs

**Summary**: Patterns, validation best practices, and limitations for using JSON Schema to constrain LLM outputs, focused on the Anthropic/Claude structured outputs and strict tool use implementations.
**Sources**: `docs/structured-outputs/anthropic-structured-outputs.md`, `docs/structured-outputs/anthropic-strict-tool-use.md`, `docs/structured-outputs/anthropic-implement-tool-use.md`
**Last updated**: 2026-04-21

---

JSON Schema is the foundation of [[structured-outputs-anthropic]] and [[anthropic-strict-tool-use]]. Both features compile your schema into a grammar that drives constrained sampling — meaning the model's token probabilities are filtered to only produce tokens that can lead to a valid schema-conformant output. (source: anthropic-structured-outputs.md)

## Why Schema Quality Matters

A poorly designed schema can:
- Exceed complexity limits and trigger `400` errors
- Slow down first-request latency due to grammar compilation time
- Produce semantically correct but practically useless outputs (e.g., wrong property ordering)
- Make it impossible to mark critical fields as required

A well-designed schema acts as a contract between your application and the model, enabling reliable downstream parsing without defensive error handling. (source: anthropic-structured-outputs.md)

## Supported JSON Schema Features

Both JSON outputs and strict tool use support standard JSON Schema with some limitations. The Python, TypeScript, Ruby, and PHP SDKs **automatically transform** schemas with unsupported features before sending them to the API. (source: anthropic-structured-outputs.md)

### Unsupported Constraints (auto-handled by SDKs)

The following constraints are removed from the schema sent to Claude (SDKs inject them into field descriptions instead):
- `minimum` / `maximum`
- `minLength` / `maxLength`
- `minItems` / `maxItems`
- Non-supported string `format` values

### Always Required for Strict Mode

When using `strict: true` on a tool, add `"additionalProperties": false` to every object in your schema. This is required for the grammar compiler. (source: anthropic-strict-tool-use.md)

## Schema Complexity Limits

Schemas compile into grammars. The combined cost of all strict schemas in a single request must stay within: (source: anthropic-structured-outputs.md)

| Limit | Value | Why it matters |
|-------|-------|----------------|
| Strict tools per request | **20** | Each tool adds to grammar size |
| Optional parameters (total) | **24** | Each optional parameter roughly doubles grammar state space |
| Parameters with union types (total) | **16** | `anyOf` / type arrays create exponential compilation cost |

Exceeding these returns `400 "Schema is too complex for compilation"`. A 180-second compilation timeout applies as a final hard stop.

## Best Practices

### 1. Mark Required Fields Explicitly

Always use the `required` array. Every field not in `required` counts toward the 24-optional-parameter limit and roughly doubles a portion of the grammar state space: (source: anthropic-structured-outputs.md)

```json
{
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "email": {"type": "string"}
  },
  "required": ["name", "email"],
  "additionalProperties": false
}
```

### 2. Avoid Union Types Where Possible

Union types (`anyOf`, `"type": ["string", "null"]`) each count toward the 16-union-parameter limit and create exponential grammar size. Prefer explicit types with clear semantics: (source: anthropic-structured-outputs.md)

```json
// Prefer this (explicit required field)
"status": {"type": "string", "enum": ["active", "inactive"]}

// Over this (nullable union — counts toward union limit)
"status": {"type": ["string", "null"]}
```

### 3. Write Descriptive Property Descriptions

Since constraints like `minimum` are removed from the schema and injected into descriptions by the SDK, write clear human-readable descriptions that also inform Claude of constraints: (source: anthropic-structured-outputs.md)

```json
"passengers": {
  "type": "integer",
  "description": "Number of passengers. Must be between 1 and 9."
}
```

### 4. Flatten Nested Structures

Deeply nested objects with optional fields compound complexity multiplicatively. Flatten where semantically reasonable: (source: anthropic-structured-outputs.md)

```json
// Flatter (preferred for strict schemas)
{
  "billing_street": {"type": "string"},
  "billing_city": {"type": "string"}
}

// Nested (avoid in strict schemas with many optional fields)
{
  "billing": {
    "type": "object",
    "properties": {
      "street": {"type": "string"},
      "city": {"type": "string"}
    }
  }
}
```

### 5. Use Enums for Constrained Values

Enums are fully supported and help Claude pick valid values without guessing: (source: anthropic-strict-tool-use.md)

```json
"seat_class": {
  "type": "string",
  "enum": ["economy", "business", "first"]
}
```

### 6. Property Ordering Behavior

When using structured outputs, **required properties appear first in Claude's output**, followed by optional properties. Schema order is preserved within each group. If property order matters to your application, mark all properties as required. (source: anthropic-structured-outputs.md)

## Grammar Caching

The compiled grammar is cached for **24 hours** from last use. Cache invalidation is triggered by:
- Changing schema structure
- Changing the tool set in a request

Changing only `name` or `description` fields does **not** invalidate the cache — this is important for prompt iteration without latency penalties. (source: anthropic-structured-outputs.md)

## HIPAA Considerations

JSON schemas are cached separately from message content. **PHI must not appear in schema definitions**: (source: anthropic-strict-tool-use.md)
- Property names
- `enum` values
- `const` values
- `pattern` regular expressions

PHI should only appear in message content (prompts and responses).

## SDK Transformation Pipeline

For Python, TypeScript, Ruby, and PHP, the SDK transformation pipeline is: (source: anthropic-structured-outputs.md)
1. Remove unsupported constraints
2. Update field descriptions with constraint info
3. Add `additionalProperties: false` to all objects
4. Filter string formats to supported list only
5. Validate the API response against your **original** schema (with all constraints)

This means Claude receives a simplified schema, but your code still enforces all constraints through post-response validation.

---

## Related pages

- [[structured-outputs-anthropic]]
- [[anthropic-strict-tool-use]]
- [[anthropic-tool-use]]
- [[tool-use-patterns]]
- [[prompt-engineering]]
- [[context-engineering]]
- [[agent-best-practices]]
