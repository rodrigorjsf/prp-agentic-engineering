# Anthropic 2026 Full Connectivity Forecast

**Summary**: Anthropic engineer David Soria Parra's forecast that 2026 will be the year of AI agent "full connectivity," combining computer use, CLI tools, and MCP — and his critique of naive REST-to-MCP wrapping in favor of programmatic, agent-native interface design.
**Sources**: `docs/agent-protocols/anthropic-engineer-2026-forecast-full-connectivity-mcp.md`
**Last updated**: 2026-04-21

---

## The 2026 Full Connectivity Vision

David Soria Parra of Anthropic, speaking on the AI Engineer podcast, forecasts that 2026 will be defined by "full connectivity" for AI agents (source: anthropic-engineer-2026-forecast-full-connectivity-mcp.md):

> "2026 I think is all about connectivity and the best agents use every available method."

The future stack is a pragmatic combination of:

- **Computer use** (GUI automation — direct screen control and visual understanding)
- **Command-line interfaces (CLIs)** — script execution and system-level access
- **[[mcp-specification]]** — agent-native design, programmatic calling, server discovery, and skills over MCP
- **Packaged Skills** — domain knowledge bundles with continuous updates

The key shift is moving away from single-method dogma toward whichever connectivity method best fits each task (source: anthropic-engineer-2026-forecast-full-connectivity-mcp.md).

## The "Cringe" Critique: Why REST Wrapping Fails

A central theme is a blunt critique of a common industry practice: mechanically converting existing REST APIs into MCP servers (source: anthropic-engineer-2026-forecast-full-connectivity-mcp.md):

> "We all need to stop taking REST APIs and put them one to one into an MCP server. Every time I see someone building another REST to MCP server conversion tool, I'm… it's a bit cringe because I think it just results in horrible things."

**The problem**: REST APIs are designed for deterministic, step-by-step human orchestration. They often require multiple sequential calls to complete a single logical task. Forcing an agent to navigate this ignores the agent's unique strength: reasoning about an entire workflow at once.

| Paradigm | How It Works | Agent Experience |
|----------|-------------|-----------------|
| Sequential REST Wrapping | Agent calls API A, waits, calls API B, waits, calls API C | Cumbersome, slow, prone to error |
| Programmatic Tool Calling | Agent writes a script composing A, B, C in one optimized operation | Fast, efficient, feels "intelligent" |

(source: anthropic-engineer-2026-forecast-full-connectivity-mcp.md)

This connects to the broader [[agentic-systems-architectural-paradigms]] shift from sequential tool-calling to programmatic execution.

## Programmatic Orchestration: Agents as Micro-Programmers

The alternative is programmatic tool calling — enabling the model to write a small script or program that composes multiple tools in a single operation (source: anthropic-engineer-2026-forecast-full-connectivity-mcp.md):

> "You don't want the model to go call a tool, take the result, then go and call another tool… what you're effectively doing is you're letting the model orchestrate things together."

This shift represents a move from agents as simple tool-users to agents as **micro-programmers**, capable of crafting bespoke solutions on the fly. It requires backend services designed to accept and safely execute agent-generated programs — a significant architectural departure from traditional API design.

This is directly relevant to [[context-engineering]]: the quality of the agent's execution depends heavily on how context is structured to support programmatic reasoning.

## MCP's New Infrastructure Features

Two key innovations coming to the MCP ecosystem (source: anthropic-engineer-2026-forecast-full-connectivity-mcp.md):

### Server Discovery

Allows AI agents and crawlers to automatically detect MCP servers running on websites or local networks. This removes the need for manual configuration and registry listings, making tool discovery as easy as browsing to a webpage.

### Skills over MCP

Allows server authors to bundle updated domain knowledge, prompts, and capabilities directly within the MCP server itself:

> "It allows you as a server author to continuously ship updated skills without having to rely on plug-in mechanisms and registries."

This creates a **decentralized and dynamic update model** — an agent connecting to a server immediately gains access to its latest capabilities without any central approval process (source: anthropic-engineer-2026-forecast-full-connectivity-mcp.md).

## MCP Adoption Metrics (as of 2026)

(source: anthropic-engineer-2026-forecast-full-connectivity-mcp.md)

- **97 million** monthly MCP SDK downloads
- All major cloud and AI vendors (OpenAI, Google, Microsoft, AWS) now ship MCP-compatible solutions
- **10,000+** active MCP servers in production
- SDKs available in Python, TypeScript, C#, and Java
- Registry-free skills and server discovery now standard features

## Industry Implications

The companies and developers who move beyond the "cringe" phase of simple API wrapping and invest in designing interfaces specifically for AI interaction will build the platforms for the first generation of truly useful general knowledge worker agents (source: anthropic-engineer-2026-forecast-full-connectivity-mcp.md).

> "This transition marks the moment AI stops adapting to our digital world and begins forcing our digital world to adapt to it."

See [[agent-best-practices]] for concrete recommendations derived from this philosophy, and [[multi-agent-communication]] for how A2A complements MCP in the full connectivity stack.

## Related pages

- [[mcp-specification]]
- [[mcp-vs-a2a]]
- [[agent-protocol-standards]]
- [[agentic-systems-architectural-paradigms]]
- [[context-engineering]]
- [[agent-workflows]]
- [[agent-best-practices]]
- [[subagents]]
