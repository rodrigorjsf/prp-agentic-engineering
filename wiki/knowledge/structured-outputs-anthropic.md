# Structured Outputs — Anthropic

**Summary**: Anthropic's constrained-decoding feature that guarantees Claude returns valid, schema-compliant JSON via two complementary mechanisms: JSON outputs and strict tool use.
**Sources**: `docs/structured-outputs/anthropic-structured-outputs.md`
**Last updated**: 2026-04-21

---

Structured outputs constrain Claude's responses to follow a specific schema, eliminating parse errors and schema violations for downstream processing. (source: anthropic-structured-outputs.md)

## Two Complementary Features

| Feature | Parameter | Purpose |
|---------|-----------|---------|
| JSON outputs | `output_config.format` | Controls Claude's response format — what Claude says |
| Strict tool use | `strict: true` on a tool definition | Validates tool parameters — how Claude calls your functions |

Both features can be used independently or together in the same request. (source: anthropic-structured-outputs.md)

## Supported Models

Structured outputs are **generally available** on the Claude API for Claude Mythos Preview, Opus 4.7, Opus 4.6, Sonnet 4.6, Sonnet 4.5, Opus 4.5, and Haiku 4.5. Available on Amazon Bedrock for the same range (excluding Mythos Preview on Vertex AI). In beta on Microsoft Foundry. (source: anthropic-structured-outputs.md)

## Why Use Structured Outputs

Without structured outputs, careful prompting alone may still produce:
- `JSON.parse()` errors from invalid syntax
- Missing required fields
- Inconsistent data types
- Schema violations requiring retries

Constrained decoding via **compiled grammars** guarantees responses that are always valid, type-safe, and reliable. (source: anthropic-structured-outputs.md)

## JSON Outputs

JSON outputs return valid JSON matching your schema in `response.content[0].text`. Use them when you need to:
- Control Claude's response format
- Extract structured data from images or text
- Generate structured reports or API responses

**How it works:**
1. Define a JSON schema (`type: "json_schema"`)
2. Pass it in `output_config.format`
3. Parse the guaranteed-valid JSON from `response.content[0].text`

See [[anthropic-tool-use]] for the parallel mechanism that validates tool inputs rather than response text.

### SDK Helpers

| Language | Tool |
|----------|------|
| Python | Pydantic models via `client.messages.parse()` |
| TypeScript | Zod schemas via `zodOutputFormat()` or `jsonSchemaOutputFormat()` |
| Java | Plain Java classes via `outputConfig(Class<T>)` |
| Ruby | `Anthropic::BaseModel` classes |
| PHP | Classes implementing `StructuredOutputModel` |
| CLI, C#, Go | Raw JSON schemas via `output_config` |

The Python, TypeScript, Ruby, and PHP SDKs **automatically transform** unsupported schema features: removing unsupported constraints, injecting those constraints into `description` strings, adding `additionalProperties: false`, filtering string formats, and validating the final response against the original schema. (source: anthropic-structured-outputs.md)

## Schema Complexity Limits

Schemas are compiled into grammars. More complex schemas mean longer compile times and larger grammar sizes. (source: anthropic-structured-outputs.md)

| Limit | Value |
|-------|-------|
| Strict tools per request | **20** |
| Total optional parameters across all strict schemas | **24** |
| Total parameters with union types across all strict schemas | **16** |

Exceeding these triggers a `400 "Schema is too complex for compilation"` error. A 180-second compilation timeout applies as a final stop-gap.

**Tips to reduce complexity:**
- Mark only critical tools as strict
- Reduce optional parameters (each one roughly doubles grammar state space)
- Flatten deeply nested objects
- Split large tool sets across multiple requests or sub-agents

## Grammar Caching and Latency

- **First request**: additional latency while the grammar compiles
- **Subsequent requests**: served from cache within **24 hours** of last use
- Cache invalidation triggers: changing schema structure, changing the tool set. Changing only `name` or `description` does **not** invalidate the cache.
- Using `output_config.format` also injects a system prompt and invalidates any existing prompt cache for that thread. (source: anthropic-structured-outputs.md)

## Property Ordering

Required properties appear first, followed by optional properties. If order matters to your application, mark all properties as required. (source: anthropic-structured-outputs.md)

## Invalid-Output Edge Cases

| Stop reason | Behavior |
|-------------|----------|
| `refusal` | Claude refuses for safety — 200 status, tokens billed, output may not match schema |
| `max_tokens` | Output may be incomplete — retry with higher `max_tokens` |

## Feature Compatibility

**Works with**: batch processing (50% discount), token counting, streaming, combining JSON outputs + strict tool use in same request.

**Incompatible with**: Citations (returns `400`), message prefilling. (source: anthropic-structured-outputs.md)

## Data Retention

JSON schemas are cached up to 24 hours. Prompts and responses qualify for Zero Data Retention (ZDR). Structured outputs are **HIPAA eligible** — but **PHI must not appear in schema definitions** (property names, `enum`/`const` values, `pattern` regex). (source: anthropic-structured-outputs.md)

---

## Related pages

- [[anthropic-tool-use]]
- [[anthropic-strict-tool-use]]
- [[anthropic-output-consistency]]
- [[json-schema-for-ai]]
- [[tool-use-patterns]]
- [[context-engineering]]
- [[agent-workflows]]
- [[prompt-engineering]]
