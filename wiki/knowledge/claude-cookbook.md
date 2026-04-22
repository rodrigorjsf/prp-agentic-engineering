# Claude Cookbook

**Summary**: The Anthropic Claude Cookbook is an official, community-driven collection of copy-paste code examples and guides covering core Claude capabilities, tool use, multimodal input, third-party integrations, and advanced agentic techniques including sub-agents and automated evaluations.
**Sources**: `docs/agentic-engineering/claude-cookbook-anthropic.md`
**Last updated**: 2026-04-21

---

## Overview

The Claude Cookbook provides code and guides designed to help developers build with Claude. All examples are designed as copy-paste snippets adaptable to any project. While examples are primarily written in Python, the concepts can be adapted to any language that supports the Claude API (source: claude-cookbook-anthropic.md).

**Prerequisites**: A Claude API key (sign up at anthropic.com). New to the Claude API? The [Claude API Fundamentals course](https://github.com/anthropics/courses/tree/master/anthropic_api_fundamentals) provides a solid foundation.

The cookbook is hosted at: https://github.com/anthropics/anthropic-cookbook

## Recipe Categories

### Core Capabilities

These examples cover foundational Claude abilities relevant to building any agentic system (source: claude-cookbook-anthropic.md):

- **Classification** — Techniques for text and data classification using Claude. Relevant to [[agent-best-practices]] routing patterns.
- **Retrieval Augmented Generation (RAG)** — Enhancing Claude's responses with external knowledge sources. A key pattern for [[context-engineering]] when codebase knowledge exceeds the context window.
- **Summarization** — Techniques for effective text summarization. Directly applicable to [[rpi-workflow]] artifact compaction.

### Tool Use and Integration

- **Tool use** — Integrating Claude with external tools and functions to extend its capabilities (source: claude-cookbook-anthropic.md):
  - Customer service agent patterns
  - Calculator integration
  - SQL query generation

This maps to [[mcp-specification]] patterns and [[agent-workflows]] for structured tool invocation.

### Third-Party Integrations

- **RAG with vector databases** — Pinecone integration for semantic search
- **Wikipedia search** — Web knowledge retrieval
- **Web page reading** — Processing live web content
- **Embeddings with Voyage AI** — Creating vector embeddings

(source: claude-cookbook-anthropic.md)

### Multimodal Capabilities

- **Vision** — Getting started with images, best practices for vision, interpreting charts and graphs, extracting content from forms
- **Image generation** — Using Claude with Stable Diffusion for image generation

(source: claude-cookbook-anthropic.md)

### Advanced Techniques

These are the most relevant to [[agentic-engineering-workflow]] patterns (source: claude-cookbook-anthropic.md):

- **[[subagents]]** — Using Haiku as a sub-agent in combination with Opus. Demonstrates the model-specialization pattern where cheaper/faster models handle mechanical subtasks while stronger models handle judgment-intensive phases — the same pattern used in [[rpir-workflow]] multi-agent scaling.
- **PDF upload and summarization** — Parsing and passing PDFs as text to Claude
- **Automated evaluations** — Using Claude to automate the prompt evaluation process (a form of Critic Agent, as described in [[agentic-software-modernization]])
- **JSON mode** — Ensuring consistent JSON output from Claude
- **Content moderation** — Building a moderation filter
- **Prompt caching** — Efficient prompt caching techniques

## Connection to Agentic Engineering Patterns

The cookbook's advanced techniques section directly supports the agentic engineering patterns documented across this wiki:

| Cookbook Recipe | Agentic Engineering Application |
|-----------------|----------------------------------|
| Sub-agents (Haiku + Opus) | [[rpi-workflow]] subagent isolation for research phase |
| RAG patterns | [[context-engineering]] for large codebases |
| Automated evaluations | Critic agent loop in [[agentic-software-modernization]] |
| Prompt caching | Cost reduction in multi-phase [[rpir-workflow]] |
| JSON mode | Structured plan artifacts in [[agent-harness]] workflows |

## Additional Resources

- [Anthropic developer documentation](https://docs.claude.com/claude/docs/guide-to-anthropics-prompt-engineering-resources)
- [Anthropic support docs](https://support.anthropic.com)
- [Anthropic Discord community](https://www.anthropic.com/discord)
- [Anthropic on AWS](https://github.com/aws-samples/anthropic-on-aws) — examples for Claude on AWS infrastructure

(source: claude-cookbook-anthropic.md)

## Contributing

The Claude Cookbook thrives on community contributions. Review existing issues and pull requests before contributing. Share ideas for new examples on the [issues page](https://github.com/anthropics/anthropic-cookbook/issues) (source: claude-cookbook-anthropic.md).

## Related pages

- [[agent-workflows]]
- [[subagents]]
- [[context-engineering]]
- [[mcp-specification]]
- [[agent-best-practices]]
- [[rpi-workflow]]
- [[rpir-workflow]]
- [[agentic-software-modernization]]
