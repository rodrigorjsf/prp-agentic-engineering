# Graph Report - ./docs  (2026-04-22)

## Corpus Check
- 85 files · ~173,933 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 329 nodes · 442 edges · 21 communities detected
- Extraction: 82% EXTRACTED · 17% INFERRED · 1% AMBIGUOUS · INFERRED: 76 edges (avg confidence: 0.77)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Skill Standards|Skill Standards]]
- [[_COMMUNITY_MCP Tool Discovery|MCP Tool Discovery]]
- [[_COMMUNITY_Claude Memory and Rules|Claude Memory and Rules]]
- [[_COMMUNITY_Harness Smart Zone|Harness Smart Zone]]
- [[_COMMUNITY_Long Context Failures|Long Context Failures]]
- [[_COMMUNITY_Hooks and Subagents|Hooks and Subagents]]
- [[_COMMUNITY_Context Rot Mechanics|Context Rot Mechanics]]
- [[_COMMUNITY_Strict Tool Use|Strict Tool Use]]
- [[_COMMUNITY_Agent Protocols|Agent Protocols]]
- [[_COMMUNITY_Structured Prompting|Structured Prompting]]
- [[_COMMUNITY_HumanLayer Runtime|HumanLayer Runtime]]
- [[_COMMUNITY_Long Context Research|Long Context Research]]
- [[_COMMUNITY_Claude Code Plugins|Claude Code Plugins]]
- [[_COMMUNITY_Spec-Driven Practice|Spec-Driven Practice]]
- [[_COMMUNITY_MCP Ecosystem|MCP Ecosystem]]
- [[_COMMUNITY_AGENTS Context Files|AGENTS Context Files]]
- [[_COMMUNITY_Spec-Driven Research|Spec-Driven Research]]
- [[_COMMUNITY_Persuasion Patterns|Persuasion Patterns]]
- [[_COMMUNITY_Human-Agent Collaboration|Human-Agent Collaboration]]
- [[_COMMUNITY_CIMD and XAA|CIMD and XAA]]
- [[_COMMUNITY_Roundtrip Overhead|Roundtrip Overhead]]

## God Nodes (most connected - your core abstractions)
1. `Claude Code subagent definition best practices` - 12 edges
2. `Spec-Driven Development` - 10 edges
3. `Strict Tool Use` - 9 edges
4. `Context Engineering` - 9 edges
5. `Structured Outputs` - 8 edges
6. `Create plugins` - 8 edges
7. `Skill authoring best practices` - 8 edges
8. `Model Context Protocol (MCP)` - 7 edges
9. `Agent Skills Standard — Official Documentation` - 7 edges
10. `Lost in the Middle (ACL/TACL)` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Parahuman AI Behavior` --conceptually_related_to--> `Context Engineering`  [INFERRED]
  docs/general-llm/Call_Me_A_Jerk_Persuading_AI_to_Comply_with_Objectionable_Requests.pdf → docs/context-engineering/context-engineering-most-important-skill-dev.md
- `Structured Outputs` --semantically_similar_to--> `Spec-Driven Development`  [INFERRED] [semantically similar]
  docs/structured-outputs/anthropic-structured-outputs.md → docs/spec-driven-development/spec-driven-development-main.md
- `Two-Agent Architecture` --conceptually_related_to--> `Layered Multi-Agent Stack`  [INFERRED]
  docs/general-llm/research-agent-workflows-and-patterns.md → docs/agent-protocols/ai-agent-protocols-2026-guide.md
- `Anthropic Claude tool_search` --references--> `Strict Tool Use`  [EXTRACTED]
  docs/tool-calling/README.md → docs/structured-outputs/anthropic-strict-tool-use.md
- `Anthropic Claude Cookbook` --references--> `Model Context Protocol (MCP)`  [INFERRED]
  docs/agentic-engineering/claude-cookbook-anthropic.md → docs/mcp/mcp-vs-a2a-dzone.md

## Hyperedges (group relationships)
- **Anthropic Reliability Stack** — anthropic_structured_outputs_structured_outputs, anthropic_structured_outputs_json_outputs, anthropic_strict_tool_use_strict_tool_use, anthropic_structured_outputs_constrained_decoding [EXTRACTED 1.00]
- **HumanLayer Runtime Stack** — humanlayer_repository_analysis_humanlayer_wui, humanlayer_repository_analysis_hlyr, humanlayer_repository_analysis_hld, humanlayer_repository_analysis_claudecode_go, humanlayer_repository_analysis_approval_loop [EXTRACTED 1.00]
- **RPI Workflow Implementations** — advanced-context-engineering_rpi_workflow, research-plan-implement_humanlayer_rpi, rpir-tyler-burleigh_rpir_workflow, building-agent-harness_atelier [EXTRACTED 0.95]
- **Context Degradation Phenomena** — advanced-context-engineering_dumb_zone, progressive-disclosure_context_rot, shedding-dead-context_dead_context, context-stops-being-scarce_compaction_problem [INFERRED 0.85]
- **MCP Ecosystem Components** — mcp-vs-a2a_mcp, mcp-typescript-sdk_typescript_sdk, mcp-servers_reference_servers, mcp-transport_mrtr_stateless, mcp-transport_server_cards, anthropic-mcp-topics_mcp_ecosystem [EXTRACTED 0.90]
- **Long-Context Mitigation Experiments** — lost_in_the_middle_and_in_between_multi_hop_qa, lost_in_the_middle_and_in_between_chain_of_thought_prompting, lost_in_the_middle_and_in_between_knowledge_graph_triple_extraction, lost_in_the_middle_and_in_between_document_summarization [EXTRACTED 1.00]
- **Context Engineering Scoped File Set** — research_context_engineering_comprehensive_doc, research_context_rot_and_management_doc, research_whitespace_and_formatting_doc, research_multilingual_performance_doc, research_agent_workflows_and_patterns_doc [EXTRACTED 1.00]
- **Agent Skills Standard Document Set** — agentskills_readme_doc, agentskills_what_are_skills_doc, agentskills_specification_doc, agentskills_best_practices_doc, agentskills_using_scripts_doc, agentskills_optimizing_descriptions_doc, agentskills_evaluating_skills_doc [EXTRACTED 1.00]
- **Spec-Driven Development Tool Landscape** — spec_driven_development_readme_doc, spec_driven_development_variant_kiro, spec_driven_development_variant_spec_kit, spec_driven_development_variant_tessl [EXTRACTED 1.00]
- **Skills over MCP Discovery Stack** — skills_over_mcp_meeting_notes_2248_prompts_as_skills, skills_over_mcp_office_hours_2460_well_known_skill_index, skills_over_mcp_office_hours_2460_lazy_loading_pattern, mcp_specification_prompts_primitive, skills_vs_mcp_speakeasy_server_prompt_bridge [INFERRED 0.86]
- **Programmatic Tool Calling Stack** — long_live_mcp_aqfer_progressive_tool_discovery, tool_search_redefining_agent_tool_calling_epsilla_tool_search, programmatic_tool_calling_claude_api_tool_search, mcp_programmatic_tool_calling_opensandbox_code_mode, cameronking4_programmatic_tool_calling_programmatic_tool_calling [INFERRED 0.88]
- **Claude Extensibility Stack** — claude_hook_reference_doc_hook_lifecycle, extend_claude_with_skills_context_fork, creating_custom_subagents_custom_subagents, claude_orchestrate_of_claude_code_sessions_agent_teams, research_claude_code_skills_format_marketplace_format [INFERRED 0.82]
- **Project memory stack** — how_claude_remembers_a_project_claude_md_files, how_claude_remembers_a_project_auto_memory, how_claude_remembers_a_project_memory_command [EXTRACTED 0.95]
- **Plugin package layout** — claude_create_plugin_doc_plugin_manifest, claude_create_plugin_doc_plugin_skills_directory, claude_create_plugin_doc_plugin_root_structure, claude_create_plugin_doc_plugin_settings_json [EXTRACTED 0.96]
- **Subagent guardrail bundle** — research_subagent_best_practices_tool_restrictions, research_subagent_best_practices_pretooluse_hooks, research_subagent_best_practices_worktree_isolation [INFERRED 0.84]

## Communities

### Community 0 - "Skill Standards"
Cohesion: 0.07
Nodes (40): Best practices for skill creators, Gotchas Pattern, Validation Loop, Evaluating skill output quality, Eval-Driven Iteration, Optimizing skill descriptions, Skill Triggering via Description, Agent Skills Standard (+32 more)

### Community 1 - "MCP Tool Discovery"
Cohesion: 0.08
Nodes (40): Copilot MCP Surfaces, GitHub MCP Server, Push Protection, GitHub MCP Toolsets, code_execution Meta-Tool, MCP Bridge, Programmatic Tool Calling, Progressive Tool Discovery (+32 more)

### Community 2 - "Claude Memory and Rules"
Cohesion: 0.08
Nodes (38): Plugin skills directory, Auto memory, claudeMdExcludes, CLAUDE.md files, .claude/rules, Concise specific instructions, Context noise reduction, How Claude remembers your project (+30 more)

### Community 3 - "Harness Smart Zone"
Cohesion: 0.07
Nodes (34): Dumb Zone, Intentional Compaction, Research-Plan-Implement (RPI) Workflow, Critic Agent Pattern, Atelier, Harness Concept, Mitchell Hashimoto, Parahuman AI Behavior (+26 more)

### Community 4 - "Long Context Failures"
Cohesion: 0.12
Nodes (20): Chain-of-Thought Prompting, Why Re-ranking Becomes Impractical, Document Summarization, Why Context Reduction Remains Fragile, In-Between Effect, Knowledge Graph Triple Extraction, Levy et al. 2024, Liu et al. 2024 (+12 more)

### Community 5 - "Hooks and Subagents"
Cohesion: 0.2
Nodes (18): Deterministic Hook Automation, Hook Type Selection, Hook Decision Control, Hook Lifecycle, Subagent and Team Hooks, Agent Teams, Subagents vs Agent Teams, Custom Subagents (+10 more)

### Community 6 - "Context Rot Mechanics"
Cohesion: 0.14
Nodes (14): Entropy in Legacy Codebases, 500 Instruction Ceiling, Attention Dilution, Attention Sinks, IFScale Benchmark, Prompt Repetition Hack, Context Selection, Context Structuring (+6 more)

### Community 7 - "Strict Tool Use"
Cohesion: 0.19
Nodes (14): Why Strict Tool Use Matters for Agents, Strict Tool PHI Schema Exclusion, Strict Tool Schema Complexity Limits, Strict Tool Use, tool_choice any, Validated Tool Inputs, Constrained Decoding, Grammar Compilation Cache (+6 more)

### Community 8 - "Agent Protocols"
Cohesion: 0.18
Nodes (14): A2A Protocol, Agent Card, A2aprotocol — a Hugging Face Space by a2aprotocol, Agent Network Protocol (ANP), Advancing Agentic AI through Communication Protocols, Using scripts in skills, Self-Contained Skill Scripts, AI Agent Protocols 2026: The Complete Guide to Standardizing AI Communication (+6 more)

### Community 9 - "Structured Prompting"
Cohesion: 0.18
Nodes (14): Input Examples, Strict Tool Choice, Tool Definition Quality, Prompt Chaining, Prompt Consistency Techniques, Retrieval Grounding, Structured Outputs for Guarantees, Long Context Prompting (+6 more)

### Community 10 - "HumanLayer Runtime"
Cohesion: 0.25
Nodes (11): Approval Loop, claudecode-go, CodeLayer, Why hld Owns Orchestration, hld Daemon, hlyr CLI, HumanLayer Local Runtime, humanlayer-wui (+3 more)

### Community 11 - "Long Context Research"
Cohesion: 0.25
Nodes (11): Long Context Paper Collection, Knowledge Graph Extraction Fragility, Multi-Hop Follow-up Paper, Long-Context Evaluation Protocols, Lost in the Middle (ACL/TACL), Positional Bias, U-Shaped Performance Curve, Lost in the Middle (arXiv Preprint) (+3 more)

### Community 12 - "Claude Code Plugins"
Cohesion: 0.27
Nodes (11): Conflict prevention, Create plugins, --plugin-dir flag, Plugin manifest, Standalone-to-plugin migration, Plugin root structure, Plugin settings.json, /reload-plugins command (+3 more)

### Community 13 - "Spec-Driven Practice"
Cohesion: 0.27
Nodes (10): Why Specs Reduce AI Guesswork, AWS Kiro, GitHub Spec Kit, Why SDD Breaks Down for Some Work, Spec-Anchored Adoption, Spec-as-Source Adoption, Spec-Driven Development, Spec-First Adoption (+2 more)

### Community 14 - "MCP Ecosystem"
Cohesion: 0.22
Nodes (10): Agent Cards, MCP Ecosystem Projects, Anthropic Claude Cookbook, AWS MCP Adoption, MCP Reference Servers, MRTR Stateless Transport, MCP Server Cards, MCP TypeScript SDK (+2 more)

### Community 15 - "AGENTS Context Files"
Cohesion: 0.27
Nodes (10): AGENTS.md, A Complete Guide To AGENTS.md, Instruction Budget, Path-Scoped Rules, Stale Documentation Poisons Context, AGENTBENCH, Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?, Minimal Context Files (+2 more)

### Community 16 - "Spec-Driven Research"
Cohesion: 0.38
Nodes (10): Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants, Spec-Anchored, Spec-as-Source, Spec-First, Spec-Driven Development — Research Overview, Spec-Driven Development, Spec-Driven Development: Exploring Three SDD Tools, Kiro (+2 more)

### Community 17 - "Persuasion Patterns"
Cohesion: 0.5
Nodes (4): Call Me A Jerk, Commitment Principle, Persuasion Principles for Agent Skill Engineering, Parahuman Effect

### Community 18 - "Human-Agent Collaboration"
Cohesion: 1.0
Nodes (3): Towards Fluid Human-Agent Collaboration, Dynamic Mentalizing, Fluid Collaboration

### Community 19 - "CIMD and XAA"
Cohesion: 1.0
Nodes (2): CIMD, XAA

### Community 20 - "Roundtrip Overhead"
Cohesion: 1.0
Nodes (1): Multi Round-Trip Requests

## Ambiguous Edges - Review These
- `Spec-Anchored` → `Spec Kit`  [AMBIGUOUS]
  docs/spec-driven-development/spec-driven-development-variant.md · relation: conceptually_related_to
- `Resource URIs` → `GitHub MCP Toolsets`  [AMBIGUOUS]
  docs/mcp/skills-over-mcp-office-hours-2460.md · relation: conceptually_related_to
- `Evaluation-driven development` → `Confidence-based filtering`  [AMBIGUOUS]
  docs/shared/skill-authoring-best-practices.md · relation: conceptually_related_to

## Knowledge Gaps
- **81 isolated node(s):** `AWS Kiro`, `Spec-Anchored Adoption`, `Why Specs Reduce AI Guesswork`, `Why SDD Breaks Down for Some Work`, `Why Structured Outputs Improve Reliability` (+76 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `CIMD and XAA`** (2 nodes): `CIMD`, `XAA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Roundtrip Overhead`** (1 nodes): `Multi Round-Trip Requests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Spec-Anchored` and `Spec Kit`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Resource URIs` and `GitHub MCP Toolsets`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Evaluation-driven development` and `Confidence-based filtering`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Context Engineering` connect `Harness Smart Zone` to `Context Rot Mechanics`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **What connects `AWS Kiro`, `Spec-Anchored Adoption`, `Why Specs Reduce AI Guesswork` to the rest of the system?**
  _81 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Skill Standards` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `MCP Tool Discovery` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._