# MCP Servers

**Summary**: The MCP servers ecosystem includes official reference implementations maintained by Anthropic, a rich set of community frameworks and clients across multiple languages, and growing enterprise tooling for governance, security, and developer experience.
**Sources**: modelcontextprotocol-servers-github.md, anthropic-mcp-github-topics.md
**Last updated**: 2026-04-22

---

## Reference Servers

The `modelcontextprotocol/servers` GitHub repository houses reference MCP server implementations maintained by Anthropic. These demonstrate canonical patterns and serve as the test bed for the [[mcp-specification]] (source: modelcontextprotocol-servers-github.md):

| Server | Package | Purpose |
|--------|---------|---------|
| **Everything** | `@modelcontextprotocol/server-everything` | Exercises all MCP features — intended for client testing, not production |
| **Fetch** | `@modelcontextprotocol/server-fetch` | Web content fetching via headless Chrome; enables LLMs to retrieve and process web content |
| **Filesystem** | `@modelcontextprotocol/server-filesystem` | Secure file operations with configurable access controls (read/write, create/list/delete directories, search, metadata) |
| **Git** | `@modelcontextprotocol/server-git` | Git repository interaction and automation (file contents, branches, commits) |
| **Memory** | `@modelcontextprotocol/server-memory` | Local knowledge graph backed by a JSON file; stores memories as entities and relations |
| **Sequential Thinking** | `@modelcontextprotocol/server-sequential-thinking` | Dynamic, reflective problem-solving through structured step-by-step thinking |
| **Time** | `@modelcontextprotocol/server-time` | Time and timezone conversions |

Each reference server follows MCP's core security principle: servers should request only the permissions they need (source: modelcontextprotocol-servers-github.md).

## Server Frameworks

Build your own MCP server using these community-maintained frameworks (source: modelcontextprotocol-servers-github.md):

| Name | Language | Description |
|------|----------|-------------|
| FastMCP | Python | Fast, Pythonic MCP server building with simple API |
| FastMCP | TypeScript | High-level TypeScript framework |
| Foxy Contexts | Golang | Declarative MCP servers in Go |
| Genkit MCP | TypeScript | Genkit ↔ MCP integration |
| LiteMCP | TypeScript | Lightweight MCP server framework |
| mark3labs/mcp-go | Golang | Golang MCP implementation |
| mcp-framework | TypeScript | MCP framework for building servers |
| mcp-proxy | TypeScript | Wraps stdio servers with an SSE server |
| mcp-rs-template | Rust | MCP CLI server template for Rust |
| Quarkus MCP Server | Java | Quarkus framework integration |
| Spring AI MCP | Java | Java+Spring AI MCP client and server |

## Client Frameworks

Frameworks that consume MCP servers as clients (source: modelcontextprotocol-servers-github.md):

| Name | Language | Description |
|------|----------|-------------|
| LangChain MCP | Python | LangChain MCP adapters |
| LangChain.js MCP | TypeScript | LangChain MCP adapters for JavaScript |
| mastra | TypeScript | TypeScript agent framework with MCP support |
| mcp-agent | Python | Framework to build AI agents |
| Semantic Kernel MCP | C# | Semantic Kernel integration |
| smolagents | Python | HuggingFace smolagents with MCP tooling |
| strands | Python | AWS Strands agent framework |
| vercel-ai-sdk | TypeScript | Vercel AI SDK with MCP toolset support |

## MCP Clients (Applications)

Applications with native MCP support (source: modelcontextprotocol-servers-github.md):

- **Claude Desktop** — Anthropic's desktop client
- **Claude.ai** — Web interface with remote MCP server support
- **Cline** — Open source AI coding assistant (VS Code extension)
- **Continue** — Open-source AI code assistant
- **Cursor** — AI-powered code editor
- **Windsurf** — AI coding environment by Codeium
- **Zed** — Code editor with built-in MCP support
- **GitHub Copilot** — with MCP extension points

## SDKs Across Languages

The MCP ecosystem provides official SDKs in multiple languages (source: modelcontextprotocol-servers-github.md):

TypeScript, Python, Java, Kotlin, C#, **Go** (added to tier-1 at [[mcp-dev-summit]]), Rust, Swift.

See [[mcp-typescript-sdk]] for the TypeScript SDK reference.

## Community Projects: Patterns and Innovation

The `anthropic-mcp` GitHub topic surfaces notable community projects that illustrate how the ecosystem is extending beyond the official reference implementations (source: anthropic-mcp-github-topics.md):

| Project | Pattern |
|---------|---------|
| **McpVanguard** | Security proxy: policy enforcement, rate limiting, audit logging sitting between MCP clients and servers |
| **mcpruntime** | Runtime framework: process manager for multiple MCP servers with health checks and restart policies |
| **dexterity** | Skill composition layer: DSL for composing multi-step skills from MCP tools with versioning |
| **mcp-explorer** | Interactive browser: connect to any MCP server, browse tools/resources/prompts visually, test in real time |
| **grounding-ai** | Grounding framework: uses MCP resource access to inject authoritative data into LLM context, reducing hallucination |
| **paki-curator** | Full agentic workflow: scheduled curation using MCP for both tool access and skill delivery |
| **claudeskills** | Community skills library: 50+ curated skills implemented as MCP prompts, installable via a companion server |

(source: anthropic-mcp-github-topics.md)

## Emerging Ecosystem Patterns

Observations from the community (source: anthropic-mcp-github-topics.md):

1. **Security is a top concern** — proxies, audit logs, and policy enforcement are being built independently because they're not yet standard in the spec
2. **Skills are gaining traction** — multiple repos use the ideas discussed in [[mcp-skills-vs-mcp]] as a first-class concept beyond MCP's "prompts" primitive
3. **Developer tooling is maturing** — the ecosystem has moved from "how do I build an MCP server?" to "how do I operate, debug, and govern multiple MCP servers in production?"
4. **Grounding as a pattern** — using MCP resource access for factual grounding is being pioneered by the community

## Utilities

| Tool | Description |
|------|-------------|
| MCP Inspector | Interactive debugging tool for MCP servers |
| mcptools | CLI for MCP server management |
| mcp-get | CLI for installing and managing MCP servers |
| mcp-manager | CLI for managing MCP server configurations |

(source: modelcontextprotocol-servers-github.md)

## Related pages

- [[mcp-specification]]
- [[mcp-typescript-sdk]]
- [[mcp-transport]]
- [[mcp-skills-vs-mcp]]
- [[mcp-skills-interest-group]]
- [[mcp-dev-summit]]
- [[agent-best-practices]]
- [[claude-code-skills]]
