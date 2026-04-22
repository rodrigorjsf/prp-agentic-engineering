# MCP Skills Interest Group

**Summary**: The Skills Over MCP Interest Group (est. February 2025) is a cross-vendor working group formalizing standards for delivering skills (reusable agent instructions) over the MCP Prompts primitive, addressing agent ignoring of skills, discovery via `/.well-known/agent-skills/index.json`, lazy loading, and file-system dependencies.
**Sources**: skills-over-mcp-meeting-notes-2248.md, skills-over-mcp-office-hours-2460.md
**Last updated**: 2026-04-21

---

## Background and Mandate

Anthropic's MCP 1.0 specification defines "Prompts" as a primitive — but the name is misleading and the feature has been underexplored. In practice, MCP prompts are best understood as **Skills**: reusable, named, structured instructions for how an agent should perform specific tasks using one or more tools (source: skills-over-mcp-meeting-notes-2248.md).

The group's mandate (source: skills-over-mcp-meeting-notes-2248.md):
1. Define conventions, URI schemes, discovery mechanisms, lifecycle policies, and agent interaction patterns for skills over MCP
2. Address the cross-vendor interoperability gap for skill definitions
3. Solve the agent-ignoring-skills problem observed in production deployments

## Inaugural Meeting (February 13, 2025)

Attendees from Anthropic, AWS, Databricks, Stacklok, Astronomer, Vercel, Magic, and independent contributors (source: skills-over-mcp-meeting-notes-2248.md).

### Core Problem: Agents Ignore Skills

Production deployments show that when given both skill definitions and tools, most agents (LLMs) skip the skills and attempt to accomplish tasks by chaining raw tool calls directly. This produces three problems (source: skills-over-mcp-meeting-notes-2248.md):

- **Correctness**: Agents make tool-use mistakes that skills were designed to prevent
- **Efficiency**: Agents take more steps than necessary
- **Predictability**: Results vary across runs and models

Root causes identified:
1. No instruction to check skills before tool use in most system prompts
2. Skills appear as long text blobs with no structured metadata, making them "invisible" to attention mechanisms
3. No mechanism for agents to "discover" which skills apply to a given task

### Skills-as-Instructors vs. Skills-as-Helpers

The meeting's most substantive discussion produced two mental models (source: skills-over-mcp-meeting-notes-2248.md):

**Skills-as-Instructors**: A skill is a *standing instruction* the agent must follow. Skills define policies, guardrails, workflows, and standard operating procedures. The skill is "in charge."

**Skills-as-Helpers**: A skill is a *reference document* the agent can consult but is not required to follow. Skills provide context, tips, and best practices. The skill is "advisory."

Working group consensus: both models are valid. Skills over MCP should support both modes via metadata flags — e.g., `"enforcement": "required"` vs. `"enforcement": "advisory"` (source: skills-over-mcp-meeting-notes-2248.md).

This distinction maps to the broader [[agent-best-practices]] question of how much autonomy agents should have.

### Cross-Vendor Interoperability

Participants flagged the risk of skills becoming a "vendor moat" if each LLM vendor (Anthropic, AWS, Google) interprets skill definitions differently. The group agreed to draft an interoperability requirements document and a shared, vendor-neutral JSON schema (source: skills-over-mcp-meeting-notes-2248.md).

### Skill Versioning

Skills need version identifiers (semver preferred). Clients that cache old skill definitions must know when content is stale — ETag-style invalidation was proposed but not decided (source: skills-over-mcp-meeting-notes-2248.md).

### Extending Prompts vs. New Primitive

Working group leaning: extend the existing Prompts primitive via convention (metadata, naming, discovery) — *not* a new MCP primitive — to maintain spec compatibility without requiring server updates (source: skills-over-mcp-meeting-notes-2248.md).

## Office Hours (March 24, 2025)

Second meeting: open community office hours covering four agenda items (source: skills-over-mcp-office-hours-2460.md).

### Decision: URI Scheme for Discovery

The group adopted **`/.well-known/agent-skills/index.json`** as the primary discovery mechanism, following established HTTP well-known conventions (RFC 8615) (source: skills-over-mcp-office-hours-2460.md).

**Index format** — a lightweight array of objects:
```json
[
  {
    "id": "deploy-to-staging",
    "name": "Deploy Service to Staging",
    "description": "Deploy any microservice to the staging environment",
    "version": "1.2.0",
    "href": "/skills/deploy-to-staging.md",
    "ttl": 300
  }
]
```

**Why not `skill://` custom URIs?** Requires all clients to implement custom resolution logic, raising the adoption barrier (source: skills-over-mcp-office-hours-2460.md).

**For STDIO servers**: expose skills via `prompts/list` RPC with a convention that entries may include `"uri"` metadata pointing to a local file path (source: skills-over-mcp-office-hours-2460.md).

### Lazy Loading Pattern

Large MCP deployments may expose 100+ skills. The adopted lazy loading pattern (source: skills-over-mcp-office-hours-2460.md):

```
Client connects to MCP server
       ↓
Fetch /.well-known/agent-skills/index.json (lightweight: id + name + description)
       ↓
Agent reads task / user intent
       ↓
Agent searches index to identify relevant skills
       ↓
Agent fetches full skill documents for top candidates (on demand)
       ↓
Agent follows skill instructions when executing task
```

Key design decisions:
- **Index TTL**: include a `"ttl"` field (seconds); default suggested 300 seconds
- **Full skill caching**: use ETag headers (HTTP) or version identifiers (MCP RPC)
- **Search**: keyword/substring matching initially; vector/semantic search is out of scope for v1
- **Limitation**: lazy loading does not automatically solve agents ignoring skills — system prompt instructions to check skills are still required (source: skills-over-mcp-office-hours-2460.md)

This addresses [[context-engineering]] concerns: loading all skills at once is expensive in tokens, latency, and context window pressure.

### Script-Bearing Skills and Trust

Skills with embedded code (bash, Python, etc.) must declare a `"requires"` block (source: skills-over-mcp-office-hours-2460.md):

```json
{
  "requires": {
    "language": "python3",
    "packages": ["requests", "pydantic"],
    "min_version": "3.11"
  }
}
```

Trust model decisions:
1. **Pure text skills** are the default and most common case
2. **Script-bearing skills** from untrusted servers must not execute without explicit user confirmation
3. **Sandboxing** is required — containers or virtual environments; the agent framework is responsible (source: skills-over-mcp-office-hours-2460.md)

### File System Dependency Problem

Many skills reference local files (e.g., `./docs/conventions.md`). When served remotely, these break. Three failure modes identified (source: skills-over-mcp-office-hours-2460.md):

1. **Absolute paths**: hardcoded paths like `/Users/jack/project/README.md` fail for every other user
2. **Relative paths**: ambiguous — relative to the server? the client? the agent's working directory?
3. **Silent degradation**: skills designed for local context fail silently when run from a cloud MCP server

**Adopted approach** (source: skills-over-mcp-office-hours-2460.md):
- **Long-term**: use MCP Resource URIs (e.g., `mcp://server-name/resources/schema.json`) instead of file system paths — servers expose files as resources, making them accessible remotely
- **Short-term**: skill scope declaration — `"local-only"`, `"remote-safe"`, or `"conditional"` — so clients can filter appropriately

See [[mcp-specification]] for the Resources primitive that enables this pattern.

## Open Questions Carried Forward

- Should skill enforcement be opt-in or opt-out?
- How to handle skill conflicts when two MCP servers provide skills with the same name?
- Are skills "owned" by a server, or can they be user-level (stored in client)?
- Should skill index search be standardized (query language, filters)?
- How does skill enforcement interact with multi-agent setups and [[subagents]]? (source: skills-over-mcp-meeting-notes-2248.md, skills-over-mcp-office-hours-2460.md)

## Connection to the MCP 2026 Roadmap

At the [[mcp-dev-summit]], MCP co-creator David Soria Parra flagged "Skills over MCP" as a planned roadmap item beyond the June 2026 spec release — giving a way to ship skill libraries alongside MCP servers (source: long-live-mcp-aqfer.md).

## Related pages

- [[mcp-skills-vs-mcp]]
- [[claude-code-skills]]
- [[mcp-specification]]
- [[mcp-servers]]
- [[mcp-dev-summit]]
- [[context-engineering]]
- [[agent-best-practices]]
- [[subagents]]
