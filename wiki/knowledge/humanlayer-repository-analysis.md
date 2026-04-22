# HumanLayer Repository Analysis

**Summary**: A repository-level analysis of `humanlayer/`, showing that the codebase centers on a local agent runtime (`hlyr` + `hld`) and a primary desktop UI (`humanlayer-wui` / CodeLayer), with shared contracts, shared database layers, and several prototype or transitional surfaces.
**Sources**: `docs/human-layer-project/humanlayer-repository-analysis.md`
**Last updated**: 2026-04-22

---

The `humanlayer/` repository is best understood as **CodeLayer built on top of HumanLayer runtime infrastructure**. The root product story has shifted toward CodeLayer as an open-source IDE for orchestrating AI coding agents, while much of the runtime and package naming still reflects the earlier HumanLayer identity (source: `humanlayer-repository-analysis.md`).

## Core architecture

The center of gravity is the local runtime, not the docs site or the prototype apps. The key split is:

- `hlyr/` as the CLI entrypoint and the stdio approvals MCP server
- `hld/` as the daemon that launches Claude Code sessions, injects MCP configuration, persists session state, and manages approvals
- `humanlayer-wui/` as the main user-facing desktop/web UI, branded as CodeLayer

This makes the repo a practical example of [[agentic-engineering-workflow]] implemented as product infrastructure rather than as a loose collection of prompts and scripts (source: `humanlayer-repository-analysis.md`).

## Runtime model

The most important execution path is:

1. A user launches work from the CLI or the CodeLayer UI.
2. `hld` starts or manages a Claude Code session.
3. The daemon injects a session-scoped MCP subprocess that resolves back to `hlyr mcp claude_approvals`.
4. Approval requests are stored, correlated to tool calls, and surfaced back to the user through daemon-facing clients.

This is a concrete, productized form of local orchestration, session state management, and tool mediation. One detail matters: the stdio MCP path and the HTTP MCP path do not expose the same tool contract (`request_permission` vs `request_approval`). It overlaps with ideas in [[mcp-specification]], [[multi-agent-communication]], and [[claude-code-subagents]], but applies them as application architecture rather than as generic patterns (source: `humanlayer-repository-analysis.md`).

## Primary versus secondary surfaces

The repo has three visible maturity levels:

### Shipping path

- `humanlayer-wui/`
- `hlyr/`
- `hld/`
- `claudecode-go/`

These form the product path that matters most to a reader trying to understand what the project actually ships (source: `humanlayer-repository-analysis.md`).

### Shared layers

- `packages/contracts/`
- `packages/database/`

These packages support typed contracts, schema definition, and newer app surfaces. They are important, but they are not the repo's primary runtime center (source: `humanlayer-repository-analysis.md`).

### Prototype or scaffold areas

- `apps/react/`
- `apps/daemon/`

These read as exploratory or scaffold layers rather than as the main delivered product. The repo keeps them alongside the production path, which is useful for experimentation but adds interpretation overhead for first-time readers (source: `humanlayer-repository-analysis.md`).

## Tooling and operations

The repo uses a hybrid orchestration model:

- Bun + Turbo for top-level JS tasks
- Make as the real cross-project control plane
- Go for the daemon and Claude Code SDK
- Tauri/Rust for the desktop shell and packaging

This is a good example of [[context-engineering]] applied to repo operations: each subsystem keeps its native tooling, while the root `Makefile` acts as the unifying control surface instead of forcing one artificial monorepo abstraction over everything (source: `humanlayer-repository-analysis.md`).

The operational posture is strong:

- CI separates checks and tests
- release automation handles macOS artifacts and Homebrew updates
- local development supports nightly builds, ticket-scoped environments, and worktree helpers

That gives the repo unusually strong ergonomics for an agent product under active development (source: `humanlayer-repository-analysis.md`).

## Main tensions in the codebase

Three tensions define the repo's current shape:

### Branding transition

The project has clearly moved toward CodeLayer, but HumanLayer naming remains in packages, docs, and legacy material. This is the most visible sign of transition (source: `humanlayer-repository-analysis.md`).

### Uneven monorepo boundaries

Root JS workspaces cover only `apps/*` and `packages/*`, while major components like `humanlayer-wui/`, `hlyr/`, `hld/`, and `claudecode-go/` sit outside that workspace boundary and are orchestrated through Make. The repo is coherent, but not fully captured by the workspace model alone (source: `humanlayer-repository-analysis.md`).

### Documentation lag

The code and product direction are clearer than some documentation surfaces. Protocol docs, navigation, and older material do not always describe every active runtime surface or current product boundary (source: `humanlayer-repository-analysis.md`).

## Why this repo matters

This repository is a concrete example of how a local-first agent product can combine:

- a daemon-owned orchestration model
- session-scoped MCP injection
- approval-aware execution
- persistent event/state tracking
- a desktop UI over the same runtime

That makes it relevant to several existing wiki themes: [[agentic-engineering-workflow]], [[mcp-specification]], [[multi-agent-communication]], and [[context-engineering]]. It shows what those ideas look like when they are assembled into a working product repo instead of discussed as isolated concepts (source: `humanlayer-repository-analysis.md`).

## Related pages

- [[agentic-engineering-workflow]]
- [[context-engineering]]
- [[mcp-specification]]
- [[multi-agent-communication]]
- [[claude-code-subagents]]
