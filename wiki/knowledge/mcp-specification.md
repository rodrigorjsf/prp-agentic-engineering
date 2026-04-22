# MCP Specification

**Summary**: The Model Context Protocol (MCP) is an open protocol standardizing how LLM applications integrate with external data sources and tools via JSON-RPC 2.0, inspired by the Language Server Protocol.
**Sources**: mcp-specification.md, about-mcp-github-docs.md
**Last updated**: 2026-04-21

---

## Overview

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools (source: mcp-specification.md). It is designed for building AI-powered IDEs, chat interfaces, and custom AI workflows — providing a standardized way to connect LLMs with the [[context-engineering]] they need.

MCP takes inspiration from the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/), which standardized how to add programming language support across a development tooling ecosystem. In a similar way, MCP standardizes how to integrate additional context and tools into the AI application ecosystem (source: mcp-specification.md).

The authoritative protocol definition is based on the TypeScript schema at `schema.ts` in the official specification repository (source: mcp-specification.md).

## Architecture: Hosts, Clients, and Servers

MCP uses JSON-RPC 2.0 messages to establish communication between three roles (source: mcp-specification.md):

- **Hosts**: LLM applications that initiate connections (e.g., Claude Desktop, Cursor, GitHub Copilot CLI)
- **Clients**: Connectors within the host application that speak the MCP protocol
- **Servers**: Services that provide context and capabilities to the host

This client-server architecture means one agent can connect to many MCP servers, each exposing different tools and data sources (source: mcp-vs-a2a-dzone.md).

## Server-Side Primitives

Servers offer three categories of features to clients (source: mcp-specification.md):

- **Resources**: Context and data — for the user or the AI model to use as background knowledge
- **Prompts**: Templated messages and workflows for users (also called [[claude-code-skills]] in the skills layer)
- **Tools**: Functions the AI model can call to execute actions

## Client-Side Primitives

Clients may offer the following features to servers (source: mcp-specification.md):

- **Sampling**: Server-initiated agentic behaviors and recursive LLM interactions
- **Roots**: Server-initiated inquiries into URI or filesystem boundaries
- **Elicitation**: Server-initiated requests for additional information from users

Additional utilities include configuration, progress tracking, cancellation, error reporting, and logging (source: mcp-specification.md).

## Protocol Characteristics

- **Message format**: JSON-RPC 2.0 (source: mcp-specification.md)
- **Connection model**: Stateful connections (evolving toward stateless — see [[mcp-transport]])
- **Capability negotiation**: Server and client negotiate capabilities at connection time
- **Governance**: Donated to the Linux Foundation's Agentic AI Foundation (AAIF) in December 2025 (source: long-live-mcp-aqfer.md)

## Security and Trust

MCP enables arbitrary data access and code execution paths. The specification defines four key principles (source: mcp-specification.md):

1. **User Consent and Control** — users must explicitly consent to data access and operations
2. **Data Privacy** — hosts must obtain user consent before exposing data to servers
3. **Tool Safety** — tools represent arbitrary code execution; hosts must obtain explicit user consent before invoking any tool
4. **LLM Sampling Controls** — users must explicitly approve sampling requests

Implementors are recommended to build robust consent flows, provide clear security documentation, and implement appropriate access controls (source: mcp-specification.md).

## Availability and Adoption

MCP is supported across (source: about-mcp-github-docs.md):

- **IDEs**: VS Code, JetBrains, Xcode, Cursor, Windsurf — supporting local and increasingly remote MCP servers
- **Copilot CLI**: Both local and remote MCP servers, with the GitHub MCP server built in
- **Copilot cloud agent**: Repository-level MCP server configuration

As of April 2026, MCP exceeds 97 million SDK downloads per month with 170+ AAIF member organizations (source: long-live-mcp-aws.md).

## GitHub MCP Server

GitHub provides and maintains its own MCP server that can (source: about-mcp-github-docs.md):

- Automate and streamline code-related tasks
- Connect third-party tools to GitHub's context and AI capabilities
- Enable cloud-based workflows without local setup
- Invoke GitHub tools such as Copilot cloud agent and code scanning

The GitHub MCP server supports **toolsets**: groups of functionalities that can be enabled or disabled to improve tool selection accuracy and reduce context window usage (source: about-mcp-github-docs.md).

## Related pages

- [[mcp-transport]]
- [[mcp-servers]]
- [[mcp-typescript-sdk]]
- [[mcp-skills-vs-mcp]]
- [[mcp-skills-interest-group]]
- [[mcp-vs-a2a]]
- [[agent-to-agent-protocol]]
- [[mcp-programmatic-tool-calling]]
- [[claude-code-skills]]
- [[context-engineering]]
