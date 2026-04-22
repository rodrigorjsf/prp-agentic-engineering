# Anthropic Output Consistency Techniques

**Summary**: Prompt engineering and workflow techniques for increasing Claude output consistency, with clear guidance on when to use these versus the guaranteed-compliance approach of Structured Outputs.
**Sources**: `docs/structured-outputs/anthropic-increase-consistency.md`
**Last updated**: 2026-04-21

---

> **For guaranteed JSON schema conformance**, use [[structured-outputs-anthropic]] (`output_config.format`) instead of the techniques below. The techniques on this page are useful for general output consistency or when you need flexibility beyond strict JSON schemas. (source: anthropic-increase-consistency.md)

## When to Use Each Approach

| Situation | Recommended Approach |
|-----------|---------------------|
| Guaranteed JSON schema compliance | **[[structured-outputs-anthropic]]** (`output_config.format`) |
| Guaranteed schema-valid tool inputs | **[[anthropic-strict-tool-use]]** (`strict: true`) |
| General JSON-like output with flexibility | Prompt engineering + prefilling |
| Consistent tone or character | Role system prompts + examples |
| Contextual consistency across a session | Retrieval-augmented prompting |
| Complex multi-step workflow | Prompt chaining |

(source: anthropic-increase-consistency.md)

## Technique 1: Specify the Desired Output Format

Precisely define your desired output format in your system prompt or user message. Include: (source: anthropic-increase-consistency.md)
- The exact format (JSON, XML, Markdown, plain text)
- Required fields and their types
- Any ordering or nesting requirements
- An example output structure

This is the baseline for all consistency work and pairs naturally with [[prompt-engineering]] patterns.

## Technique 2: Prefill Claude's Response

> **Not supported** on Claude Mythos Preview, Opus 4.7, Opus 4.6, and Sonnet 4.6. Use [[structured-outputs-anthropic]] or system prompt instructions instead. (source: anthropic-increase-consistency.md)

Prefill the `Assistant` turn with the start of your desired format to bypass friendly preambles and lock in structure:

```python
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Extract the name and email from: Alice Smith, alice@example.com"},
        {"role": "assistant", "content": '{"name": "'}  # prefill starts the JSON
    ]
)
```

By starting Claude's response with `{"name": "`, Claude is constrained to continue in JSON format. (source: anthropic-increase-consistency.md)

## Technique 3: Constrain with Examples (Few-Shot Prompting)

Provide concrete examples of your desired output. This trains Claude's understanding better than abstract instructions: (source: anthropic-increase-consistency.md)

```
System: You extract contact information and return it in this exact format:
Name: [full name]
Email: [email address]
Phone: [phone number or "N/A"]

Example output:
Name: Jane Doe
Email: jane@example.com
Phone: 555-9876

User: Here is an email from Bob Jones at bob@acme.com, phone 555-1234.
```

Few-shot examples prime Claude to follow the same format reliably across varied inputs.

## Technique 4: Use Retrieval for Contextual Consistency

For tasks requiring consistent context (chatbots, knowledge bases), use retrieval to ground Claude's responses in a fixed information set. This prevents hallucination and drift from source material — especially important when output format must reference specific entities or values from a corpus. (source: anthropic-increase-consistency.md)

This technique pairs naturally with [[context-engineering]] patterns.

## Technique 5: Chain Prompts for Complex Tasks

Break complex tasks into smaller, consistent subtasks. Each subtask gets Claude's full attention, reducing inconsistency errors at scale. (source: anthropic-increase-consistency.md)

**Example pipeline:**
1. **Extract**: Raw data from the input document → unstructured text
2. **Parse**: Extracted text into a structured schema → JSON
3. **Validate**: Enrich the JSON with business logic → final output

Chaining lets each step have its own clear format constraint, making failures easier to detect and handle per stage. This is a core pattern in [[agent-workflows]].

## Technique 6: Keep Claude in Character

For role-based applications, consistent character requires deliberate prompting: (source: anthropic-increase-consistency.md)

- **System prompts to set the role**: Define Claude's role, personality, background, and specific traits in detail.
- **Prepare for possible scenarios**: List common scenarios and expected responses to "train" Claude to handle diverse situations without breaking character.

**Example system prompt:**
```
You are Aria, a friendly customer support assistant for Acme Inc.
You always respond in English, use a warm and professional tone,
and never discuss competitors. If you don't know the answer,
say: "I'll need to check on that for you — let me get back to you shortly."
```

---

## Related pages

- [[structured-outputs-anthropic]]
- [[anthropic-strict-tool-use]]
- [[prompt-engineering]]
- [[context-engineering]]
- [[agent-workflows]]
- [[agent-best-practices]]
- [[json-schema-for-ai]]
