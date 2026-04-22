# Graph Report - /home/rodrigo/Workspace/prp-agentic-engineering  (2026-04-22)

## Corpus Check
- 1 files · ~358,074 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 339 nodes · 455 edges · 21 communities detected
- Extraction: 83% EXTRACTED · 17% INFERRED · 1% AMBIGUOUS · INFERRED: 76 edges (avg confidence: 0.77)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]

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
- `Context Engineering` --conceptually_related_to--> `Parahuman AI Behavior`  [INFERRED]
  docs/context-engineering/context-engineering-most-important-skill-dev.md → docs/general-llm/Call_Me_A_Jerk_Persuading_AI_to_Comply_with_Objectionable_Requests.pdf
- `Context Engineering` --conceptually_related_to--> `Effective Context Engineering for AI Agents`  [INFERRED]
  docs/general-llm/research-context-engineering-comprehensive.md → docs/general-llm/research-context-rot-and-management.md
- `Spec-Driven Development` --semantically_similar_to--> `Structured Outputs`  [INFERRED] [semantically similar]
  docs/spec-driven-development/spec-driven-development-main.md → docs/structured-outputs/anthropic-structured-outputs.md
- `Strict Tool Use` --references--> `Anthropic Claude tool_search`  [EXTRACTED]
  docs/structured-outputs/anthropic-strict-tool-use.md → docs/tool-calling/README.md
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

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (40): Copilot MCP Surfaces, GitHub MCP Server, Push Protection, GitHub MCP Toolsets, code_execution Meta-Tool, MCP Bridge, Programmatic Tool Calling, Progressive Tool Discovery (+32 more)

### Community 1 - "Community 1"
Cohesion: 0.08
Nodes (38): Plugin skills directory, Auto memory, claudeMdExcludes, CLAUDE.md files, .claude/rules, Concise specific instructions, Context noise reduction, How Claude remembers your project (+30 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (34): Dumb Zone, Intentional Compaction, Research-Plan-Implement (RPI) Workflow, Critic Agent Pattern, Atelier, Harness Concept, Mitchell Hashimoto, Parahuman AI Behavior (+26 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (32): A2A Protocol, Agent Card, A2aprotocol — a Hugging Face Space by a2aprotocol, Agent Network Protocol (ANP), Advancing Agentic AI through Communication Protocols, Best practices for skill creators, Gotchas Pattern, Validation Loop (+24 more)

### Community 4 - "Community 4"
Cohesion: 0.11
Nodes (24): Why Strict Tool Use Matters for Agents, Strict Tool PHI Schema Exclusion, Strict Tool Schema Complexity Limits, Strict Tool Use, tool_choice any, Validated Tool Inputs, Constrained Decoding, Grammar Compilation Cache (+16 more)

### Community 5 - "Community 5"
Cohesion: 0.12
Nodes (20): Chain-of-Thought Prompting, Why Re-ranking Becomes Impractical, Document Summarization, Why Context Reduction Remains Fragile, In-Between Effect, Knowledge Graph Triple Extraction, Levy et al. 2024, Liu et al. 2024 (+12 more)

### Community 6 - "Community 6"
Cohesion: 0.15
Nodes (18): AGENTS.md, A Complete Guide To AGENTS.md, Instruction Budget, Path-Scoped Rules, Stale Documentation Poisons Context, What are skills?, Progressive Skill Discovery, Skill Directory Structure (+10 more)

### Community 7 - "Community 7"
Cohesion: 0.2
Nodes (18): Deterministic Hook Automation, Hook Type Selection, Hook Decision Control, Hook Lifecycle, Subagent and Team Hooks, Agent Teams, Subagents vs Agent Teams, Custom Subagents (+10 more)

### Community 8 - "Community 8"
Cohesion: 0.14
Nodes (14): Entropy in Legacy Codebases, 500 Instruction Ceiling, Attention Dilution, Attention Sinks, IFScale Benchmark, Prompt Repetition Hack, Context Selection, Context Structuring (+6 more)

### Community 9 - "Community 9"
Cohesion: 0.23
Nodes (14): Agentic Context Engineering (ACE), Architectural Paradigms of Advanced Agentic Systems, The Prompt Report, Context Engineering, LLM Context Engineering: Comprehensive Research Synthesis, Smallest Set of High-Signal Tokens, LLM Multilingual Performance & Language Overhead, Tokenization Unfairness Between Languages (+6 more)

### Community 10 - "Community 10"
Cohesion: 0.18
Nodes (14): Input Examples, Strict Tool Choice, Tool Definition Quality, Prompt Chaining, Prompt Consistency Techniques, Retrieval Grounding, Structured Outputs for Guarantees, Long Context Prompting (+6 more)

### Community 11 - "Community 11"
Cohesion: 0.25
Nodes (11): Approval Loop, claudecode-go, CodeLayer, Why hld Owns Orchestration, hld Daemon, hlyr CLI, HumanLayer Local Runtime, humanlayer-wui (+3 more)

### Community 12 - "Community 12"
Cohesion: 0.25
Nodes (11): Long Context Paper Collection, Knowledge Graph Extraction Fragility, Multi-Hop Follow-up Paper, Long-Context Evaluation Protocols, Lost in the Middle (ACL/TACL), Positional Bias, U-Shaped Performance Curve, Lost in the Middle (arXiv Preprint) (+3 more)

### Community 13 - "Community 13"
Cohesion: 0.27
Nodes (11): Conflict prevention, Create plugins, --plugin-dir flag, Plugin manifest, Standalone-to-plugin migration, Plugin root structure, Plugin settings.json, /reload-plugins command (+3 more)

### Community 14 - "Community 14"
Cohesion: 0.29
Nodes (9): evaluate_mirror_parity(), evaluate_must_contain(), load_cases(), main(), Deterministic prompt-contract evaluator for prp-core.  Checks shipped skills, ag, Check that each target file contains all required strings., Check that each (shipped, mirror) pair is identical., Run one case. Returns (pass_count, fail_count). (+1 more)

### Community 15 - "Community 15"
Cohesion: 0.22
Nodes (10): Agent Cards, MCP Ecosystem Projects, Anthropic Claude Cookbook, AWS MCP Adoption, MCP Reference Servers, MRTR Stateless Transport, MCP Server Cards, MCP TypeScript SDK (+2 more)

### Community 16 - "Community 16"
Cohesion: 0.38
Nodes (10): Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants, Spec-Anchored, Spec-as-Source, Spec-First, Spec-Driven Development — Research Overview, Spec-Driven Development, Spec-Driven Development: Exploring Three SDD Tools, Kiro (+2 more)

### Community 17 - "Community 17"
Cohesion: 0.5
Nodes (4): Call Me A Jerk, Commitment Principle, Persuasion Principles for Agent Skill Engineering, Parahuman Effect

### Community 18 - "Community 18"
Cohesion: 1.0
Nodes (3): Towards Fluid Human-Agent Collaboration, Dynamic Mentalizing, Fluid Collaboration

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (2): CIMD, XAA

### Community 20 - "Community 20"
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
- **85 isolated node(s):** `Deterministic prompt-contract evaluator for prp-core.  Checks shipped skills, ag`, `Check that each target file contains all required strings.`, `Check that each (shipped, mirror) pair is identical.`, `Run one case. Returns (pass_count, fail_count).`, `AWS Kiro` (+80 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 19`** (2 nodes): `CIMD`, `XAA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `Multi Round-Trip Requests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Spec-Anchored` and `Spec Kit`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Resource URIs` and `GitHub MCP Toolsets`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Evaluation-driven development` and `Confidence-based filtering`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Practical Agent Workflows and Patterns` connect `Community 3` to `Community 9`, `Community 6`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `LLM Context Engineering: Comprehensive Research Synthesis` connect `Community 9` to `Community 3`, `Community 6`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **Why does `Context Engineering` connect `Community 2` to `Community 8`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **What connects `Deterministic prompt-contract evaluator for prp-core.  Checks shipped skills, ag`, `Check that each target file contains all required strings.`, `Check that each (shipped, mirror) pair is identical.` to the rest of the system?**
  _85 weakly-connected nodes found - possible documentation gaps or missing edges._