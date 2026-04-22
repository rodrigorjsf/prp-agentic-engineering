# Agent Communication Protocols

**Summary**: A structured academic overview of the four emerging communication standards for AI agents — MCP, ACP, A2A, and ANP — arguing that standardized protocols are essential for interoperability, tool discovery, and coordinated task execution across LLM-powered agents.
**Sources**: `docs/agent-protocols/advancing-agentic-ai-communication-protocols.md`
**Last updated**: 2026-04-21

---

## Overview

Autonomous agents powered by Large Language Models require reliable and standardized frameworks to connect tools, exchange contextual information, and synchronize tasks across diverse systems (source: advancing-agentic-ai-communication-protocols.md). Without such standards, developers must manually create interfaces, handle authentication protocols, and navigate incompatible function-calling standards across platforms.

This paper from the International Journal of Scientific Research in Science and Technology (IJSRST) explores four protocols that address this problem: [[mcp-specification]], A2A, ACP, and ANP (source: advancing-agentic-ai-communication-protocols.md).

## The Four Protocols

### Model Context Protocol (MCP)

- **Architecture**: JSON-RPC based client-server (source: advancing-agentic-ai-communication-protocols.md)
- **Primary use**: Connecting agents to external tools, databases, and APIs
- **Key feature**: Secure tool execution with well-typed data transfer
- **Created by**: Anthropic (November 2024), donated to the Linux Foundation

MCP solves the agent-to-tool connectivity problem. See [[mcp-specification]] for full detail and [[mcp-vs-a2a]] for a comparison.

### Agent-to-Agent Protocol (A2A)

- **Architecture**: HTTP-based, JSON-RPC with SSE streaming (source: advancing-agentic-ai-communication-protocols.md)
- **Primary use**: Peer-to-peer task delegation between agents
- **Key feature**: Capability-rich Agent Cards for agent discovery
- **Created by**: Google (April 2025), donated to the Linux Foundation

A2A enables [[multi-agent-communication]] without requiring shared internal logic. See [[agent-to-agent-protocol]] for full detail.

### Agent Communication Protocol (ACP)

- **Architecture**: REST-compliant (source: advancing-agentic-ai-communication-protocols.md)
- **Primary use**: Asynchronous streaming, multimodal agent outputs
- **Key feature**: Support for multipart message formats
- **Created by**: IBM Research; merged into A2A in September 2025

ACP is now deprecated. Its capabilities have been absorbed into A2A under the Linux Foundation (source: advancing-agentic-ai-communication-protocols.md).

### Agent Network Protocol (ANP)

- **Architecture**: Decentralized, using Decentralized Identifiers (DIDs) and JSON-LD semantic graphs (source: advancing-agentic-ai-communication-protocols.md)
- **Primary use**: Agent discovery in open networks and secure collaboration
- **Key feature**: DIDs for decentralized identity
- **Created by**: Agent Network Protocol Contributors

ANP addresses open-network discovery scenarios where agents from unknown organizations must find and authenticate each other without a central registry.

## Why Standardization Matters

Without standardized protocols, the integration surface between agents and tools grows as N×M — every agent must implement a custom connector for every tool. Standardization collapses this to M+N (source: advancing-agentic-ai-communication-protocols.md). This applies equally to [[multi-agent-communication]], where each agent pair would otherwise require bespoke negotiation logic.

Standardized protocols also enable:
- **Interoperability**: Agents from different vendors can discover and communicate with each other
- **Tool discovery**: Agents can find and invoke tools without hard-coded connectors
- **Coordinated task execution**: Distributed workflows become composable rather than monolithic

See [[agent-protocol-standards]] for a synthesized comparison across all four protocols and guidance on when to use each.

## Historical Context

Earlier multi-agent communication standards include KQML (1993) and FIPA (2000), which defined communicative act libraries for agent coordination (source: advancing-agentic-ai-communication-protocols.md). The current wave of protocols builds on those foundations but is designed for LLM-native, HTTP-first environments.

## Related pages

- [[agent-protocol-standards]]
- [[mcp-specification]]
- [[agent-to-agent-protocol]]
- [[mcp-vs-a2a]]
- [[multi-agent-communication]]
- [[context-engineering]]
- [[agent-workflows]]
