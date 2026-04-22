# Wiki Index

Total content pages: **71**

---

## Foundational Concepts

| Page                       | Summary                                                                   |
| -------------------------- | ------------------------------------------------------------------------- |
| [[context-engineering]]    | Token budget management, position effects, four context strategies        |
| [[context-rot]]            | Empirical degradation from 0.92→0.68 accuracy, three architectural causes |
| [[progressive-disclosure]] | Tiered loading (always/on-demand/invoked), ETH Zurich evidence            |
| [[prompt-engineering]]     | Paradigm inversion for reasoning models, CoT/ToT/ReAct techniques         |

## Agent Architecture

| Page                          | Summary                                                                |
| ----------------------------- | ---------------------------------------------------------------------- |
| [[evaluating-agents-paper]]   | ETH Zurich 2026 study: minimal configs outperform comprehensive ones   |
| [[agent-workflows]]           | Fundamental loop, five core patterns, orchestration strategies         |
| [[subagents]]                 | Isolated task specialists, tool restriction patterns, and prompt design |
| [[agent-configuration-files]] | AGENTS.md, CLAUDE.md, and path-scoped rule patterns for persistent instructions |
| [[agent-best-practices]]      | Plan-first workflow guidance, context discipline, and common anti-patterns |
| [[harness-engineering]]       | Control-layer view of autonomous agents: context, rails, state, and execution environments |

## Claude Code Platform

| Page                      | Summary                                                       |
| ------------------------- | ------------------------------------------------------------- |
| [[claude-code-skills]]    | SKILL.md format, frontmatter, string substitutions, locations |
| [[claude-code-hooks]]     | Lifecycle events, hook types, exit codes, matchers            |
| [[claude-code-plugins]]   | Plugin structure, manifest, distribution, namespacing         |
| [[claude-code-memory]]    | CLAUDE.md hierarchy, path-scoped rules, imports, auto memory  |
| [[claude-code-subagents]] | Definition format, frontmatter fields, agent teams            |


## Agent Skills Standard

| Page                      | Summary                                                          |
| ------------------------- | ---------------------------------------------------------------- |
| [[agent-skills-standard]] | Open specification, frontmatter, progressive disclosure loading  |
| [[skill-authoring]]       | Eval-driven iteration, description optimization, script bundling |

## Research

| Page                          | Summary                                                         |
| ----------------------------- | --------------------------------------------------------------- |
| [[persuasion-in-ai]]          | Seven persuasion principles with quantitative effect sizes      |
| [[multilingual-performance]]  | Tokenization disparities, English-thinking, Portuguese analysis |
| [[whitespace-and-formatting]] | Formatting costs (1 token), structural quality improvements     |

## MCP (Model Context Protocol)

| Page | Summary |
|------|---------|
| [[mcp-specification]] | The MCP open protocol: JSON-RPC 2.0 architecture with Hosts, Clients, and Servers exposing Resources, Prompts, and Tools. Includes security principles and governance under AAIF/Linux Foundation. |
| [[mcp-vs-a2a]] | Comparison of MCP (agent-to-tool) and A2A (agent-to-agent) protocols — key differences, when to use each, and the combined enterprise architecture using both layers. |
| [[mcp-dev-summit]] | Recap of MCP Dev Summit NA 2026 (April 2–3, New York): June 2026 roadmap, MRTR stateless transport, CIMD/XAA auth, SDK V2, and MCP Apps. |
| [[mcp-skills-vs-mcp]] | Skills (institutional knowledge, the *how*) vs. MCP (authenticated capability access, the *ability*) — complementary layers, not competing technologies. |
| [[mcp-typescript-sdk]] | Official TypeScript SDK (`@modelcontextprotocol/sdk`): client/server APIs, STDIO and Streamable HTTP transports, Zod validation, OAuth 2.1 auth helpers, Express/Hono middleware. |
| [[mcp-servers]] | Reference servers (Fetch, Filesystem, Git, Memory, etc.), multi-language frameworks, MCP-compatible clients, and community ecosystem patterns (security proxies, skill libraries, grounding frameworks). |
| [[mcp-skills-interest-group]] | Skills Over MCP working group (est. Feb 2025): `/.well-known/agent-skills/index.json` discovery, lazy loading, skill enforcement modes, file-system dependency solutions, and script-bearing skill trust model. |
| [[agent-to-agent-protocol]] | Google's A2A protocol: Agent Cards, Tasks, Artifacts, and Push Notifications for peer-to-peer agent coordination — complementing MCP's agent-to-tool layer. |
| [[mcp-transport]] | STDIO (local) and Streamable HTTP (remote) transports, HTTP/2 requirements, current stateful limitations, and the June 2026 MRTR roadmap for serverless compatibility. |
| [[mcp-programmatic-tool-calling]] | Code-mode tool calling: the model writes a server-side program chaining multiple tool calls in sequence — planned 2026 roadmap item reducing round-trips and context window pressure. |

## Context Engineering (New Sources)

| Page | Summary |
|------|---------|
| [[million-token-context-window]] | What large context windows actually mean in practice — benchmark degradation curves, the compaction problem, and why discipline outperforms capacity |
| [[agents-md-liability]] | Why growing AGENTS.md files beyond a certain size actively harm AI agent performance through attention dilution, primacy bias, and the dumb zone |
| [[context-scarcity-end]] | How flat-rate 1M context pricing changes workflows, removes economic pressure for discipline, and shifts the bottleneck from capacity to relevance |
| [[dead-context]] | Instructions, tool definitions, and metadata occupying the context window without contributing to the current task — how it accumulates and strategies to shed it |
| [[commercial-agent-context]] | Context engineering as infrastructure for multi-tenant production agent systems — memory taxonomy, truth vs. acceleration layers, and the full context engine loop |

## Agent Protocols & Communication

| Page | Summary |
|------|---------|
| [[agent-communication-protocols]] | Academic overview of MCP, ACP, A2A, and ANP — four emerging communication standards for AI agents (IJSRST paper) |
| [[ai-agent-protocols-2026]] | Complete 2026 guide to the consolidated two-protocol world (MCP + A2A), with decision framework and production architecture |
| [[agentic-systems-architectural-paradigms]] | Dual symbolic/neural paradigm framework, context engineering as the primary quality lever, and programmatic execution patterns |
| [[anthropic-2026-full-connectivity]] | Anthropic engineer's forecast for 2026 "full connectivity" and critique of REST-wrapping anti-pattern |
| [[a2a-protocol]] | Google's Agent-to-Agent protocol: Agent Cards, task lifecycle, streaming, and Python SDK quick start |
| [[human-agent-collaboration]] | Fluid collaboration theory and Theory of Mind reasoning requirements for AI agents collaborating with humans in real-time |
| [[agent-protocol-standards]] | Synthesized overview of MCP, A2A, ACP, and ANP: differences, complementarity, governance, and decision guidance |
| [[multi-agent-communication]] | How agents communicate: message-passing patterns, orchestration models, task lifecycle, discovery, and authentication |

## Structured Outputs (Anthropic)

| Page | Summary |
|------|---------|
| [[structured-outputs-anthropic]] | Anthropic's constrained-decoding feature guaranteeing schema-compliant JSON via JSON outputs and strict tool use |
| [[anthropic-tool-use]] | Implementing tool use with the Claude API: definitions, best practices, input_examples, tool_choice |
| [[anthropic-strict-tool-use]] | Setting strict: true for grammar-constrained tool inputs, guaranteeing type-safe function calls |
| [[anthropic-output-consistency]] | Prompt engineering techniques for output consistency, with guidance on when to use structured outputs instead |
| [[json-schema-for-ai]] | Using JSON Schema to constrain LLM outputs: supported features, complexity limits, best practices |
| [[tool-use-patterns]] | Patterns for defining and using tools with LLMs: forced use, multi-tool, strict mode, namespacing |

## Agentic Engineering

| Page | Summary |
|------|---------|
| [[rpi-workflow]] | Three-phase Research → Plan → Implement workflow by Dex Horthy / HumanLayer; each phase produces a compacted artifact and starts with a fresh context window to maximize LLM output quality. |
| [[rpir-workflow]] | Tyler Burleigh's Research → Plan → Implement → Review extension; adds explicit review sessions after every phase, written artifact persistence, and a multi-model scaling model. |
| [[agent-harness]] | Martin C. Richards' case for building an agent harness — a set of skills, workflows, and methodology encoding how your agent thinks and builds — and why harness quality outweighs model choice. |
| [[claude-cookbook]] | Anthropic's official collection of copy-paste Claude code examples covering classification, RAG, tool use, multimodal capabilities, sub-agents, automated evaluations, and prompt caching. |
| [[agentic-software-modernization]] | Markus Harrer's analysis of using agentic AI for legacy software (COBOL, RPG) modernization: RPI workflow, critic-agent loops, codebase hygiene, context compaction, and traceability links. |
| [[agentic-engineering-workflow]] | Synthesized overview of the RPI/RPIR agentic engineering workflow pattern — how it independently emerged across multiple practitioners and why it is the reliable answer to vibe coding. |
| [[agent-harness-design]] | Design patterns for building agent harnesses: component taxonomy (sequential/advisory/utility), context isolation, artifact design, skill routing, backflow support, and multi-model specialization. |

## Repository Analyses

| Page | Summary |
|------|---------|
| [[humanlayer-repository-analysis]] | Analysis of the `humanlayer/` repo: CodeLayer product positioning, `hlyr` + `hld` local runtime architecture, primary WUI surface, shared packages, tooling model, and consolidation risks. |

## Spec-Driven Development

| Page | Summary |
|------|---------|
| [[spec-driven-development]] | Academic overview of SDD — treating specifications as the primary artifact of software development, with three rigor levels, four-phase workflow, AI error reduction evidence, tool survey, and case studies. |
| [[spec-driven-development-practice]] | Practitioner guide contrasting vibe coding with spec-first; step-by-step Spec Kit walkthrough, real prompting examples, and honest assessment of where SDD breaks down. |
| [[spec-driven-development-critique]] | Critical hands-on analysis of Kiro, Spec Kit, and Tessl from the Martin Fowler team; surfaces concrete failure modes: review overhead, false control, one-size-fits-all workflows, and AI non-determinism. |
| [[spec-first-ai-development]] | The spec-first paradigm — why writing specs before code matters for AI-assisted development, and how it shifts the developer's role to spec author and AI orchestrator. |
| [[code-to-contract]] | Contract-based thinking in AI-assisted development — how specifications become executable contracts enforced through CI/CD, BDD frameworks, and API contract testing tools. |

## Long Context Research

| Page | Summary |
|------|---------|
| [[lost-in-the-middle-paper]] | Full summary of Liu et al. (2024, TACL) — U-shaped performance curve, multi-doc QA and key-value retrieval experiments, 20%+ accuracy drop at center position, mitigation strategies. |
| [[lost-in-the-middle-in-between]] | Baker et al. (2024, arXiv) follow-up — multi-hop QA over long contexts, the "in-between" effect (relative distance between evidence documents), combinatorial explosion of position permutations. |
| [[u-shaped-attention-curve]] | Concept page — primacy effect, recency effect, middle neglect, quantitative evidence, practical placement guidelines for any LLM context window. |
| [[long-context-mitigation]] | Strategies for mitigating positional bias — position-aware placement, reranking, permutation self-consistency, CoT, knowledge graph extraction, summarization, progressive disclosure. |

## Tool Calling

| Page | Summary |
|------|---------|
| [[programmatic-tool-calling]] | Claude API programmatic tool calling: client vs. server tools, agentic loop, forced tool use, pricing, and the advanced code-execution pattern that collapses N round-trips into 2. |
| [[tool-search-epsilla]] | Epsilla's analysis of Tool Search as the most significant AI agent infrastructure shift of 2025-2026: semantic discovery, 85%+ token savings, accuracy benchmarks, prompt cache protection, and FAQ. |
| [[programmatic-tool-calling-sdk]] | cameronking4's Vercel AI SDK implementation of Programmatic Tool Calling: architecture, efficiency tables, cost analysis, and real usage examples across 100+ LLM providers. |
| [[dynamic-tool-discovery]] | Dynamic/semantic tool search vs. static tool lists: how agents find the right tool at runtime, the Tool Search pattern, JITR principle, and scalability guidance. |
| [[tool-calling-patterns]] | Synthesis of all tool calling patterns — forced, auto, parallel, programmatic, code-mode, MCP-based — with a decision guide for when to use each. |
