# Subagents

**Summary**: Specialized assistants running in isolated context windows with custom system prompts and restricted tool sets — a core pattern for keeping the main agent context clean during research, planning, review, and other noisy work.
**Sources**: creating-custom-subagents.md, claude-orchestrate-of-claude-code-sessions.md, research-subagent-best-practices.md
**Last updated**: 2026-04-22

---

Subagents are the workhorse of [[agent-workflows]]. They receive only their system prompt plus basic environment details — **not** parent conversation history. This isolation is a feature: it keeps the main context clean and lets subagents focus on their specific task.

## Core Properties

| Feature | Current docs say |
|---------|------------------|
| Format | Markdown file with YAML frontmatter |
| Required fields | `name` and `description` |
| Tool control | Restrict aggressively; read-only by default for exploration/review |
| Context model | Isolated window with its own prompt and environment |
| Cost control | Use `maxTurns`, narrower tools, and cheaper models where appropriate |
| Typical locations | Session, project, user, or plugin scope |
| Team role | Best for research, review, planning, and other high-noise tasks |

## Common Tool Profiles

| Agent Role         | Tools                        | Model              | Notes                                            |
| ------------------ | ---------------------------- | ------------------ | ------------------------------------------------ |
| Code reviewer      | Read, Grep, Glob, Bash       | Haiku (fast/cheap) | ~97% of community agents use this read-only core |
| Explorer           | Read, Grep, Glob             | Haiku              | Minimal set for fast codebase search             |
| Code modifier      | Read, Grep, Glob, Edit, Bash | Sonnet             | Standard work requiring writes                   |
| Architect/Reasoner | Read, Grep, Glob, Bash       | Opus               | Complex reasoning and planning                   |
| Security auditor   | Read, Grep, Glob             | Sonnet             | Read-only with stronger model for nuance         |

## Built-in Subagents

Both platforms provide built-in subagents:

- **Explore** — Fast, read-only codebase search (Haiku model in Claude Code)
- **Bash/Terminal** — Shell command execution with output isolation
- **Plan** — Research-focused read-only agent (Claude Code)
- **general-purpose** — Full tool access (Claude Code)

## System Prompt Structure

Effective subagent prompts follow a five-part structure:

1. **Role** — Who the agent is and its expertise area
2. **Process** — Step-by-step procedure to follow
3. **Checklist** — Specific items to verify or produce
4. **Output Format** — Exact structure of the response (field names, grouping, format)
5. **Success Criteria** — What constitutes a complete, useful result

Keep prompts focused and under 2000 words. Longer prompts are slower to process and harder to maintain.

## Design Principles

1. **Restrict tools to minimum necessary** — Read-only agents get Read+Grep+Glob; prevents accidental modifications
2. **Use Haiku for fast, cheap exploration** — Sonnet for standard work, Opus for complex reasoning
3. **Set `maxTurns`** to prevent runaway agents (15 for exploration, 20 for evaluation) — missing `maxTurns` is a common source of unexpected token consumption
4. **Implement confidence-based filtering** — Report only >80% confidence issues. This threshold significantly reduces noise while preserving actionable findings. The agent prompt must explicitly instruct: "Report only issues where you are at least 80% confident"
5. **Specify exact output structure** — Field names, format, grouping in the system prompt. Without this, output varies between invocations and is hard to parse programmatically
6. **Use normal guidance language** — Replace "CRITICAL: You MUST" with "Use when...". Natural phrasing performs equivalently without wasting tokens on emphasis markers
7. **Restrict spawnable agents** — Use `Agent(worker, researcher)` syntax to limit which agents a parent can spawn

## Effort Levels (Claude Code Only)

| Level    | Behavior                             | Availability  |
| -------- | ------------------------------------ | ------------- |
| `low`    | Quick, shallow analysis              | All models    |
| `medium` | Standard depth                       | All models    |
| `high`   | Thorough analysis                    | All models    |
| `max`    | Deepest reasoning, extended thinking | Opus 4.6 only |

## Plugin Security (Claude Code)

Agents bundled in [[claude-code-plugins]] have restricted capabilities — the `hooks`, `mcpServers`, and `permissionMode` frontmatter fields are **silently ignored** when the agent is loaded from a plugin context. To use these fields, copy the agent file to `.claude/agents/` or `~/.claude/agents/`.

## Anti-Patterns

Ten common mistakes when building and deploying subagents:

1. **Giving all tools to read-only agents** → Risk of accidental file modifications; restrict to Read+Grep+Glob
2. **Using subagents for simple, single-purpose tasks** → Use [[claude-code-skills]] instead; subagents add context-switching overhead
3. **Generic or vague subagent descriptions** → The description determines when the orchestrator delegates; unclear descriptions mean missed or wrong invocations
4. **Over-delegation by larger models** → Opus may delegate when a simpler direct approach suffices; not every task needs a subagent
5. **Overly long prompts (2000+ words)** → Slower processing, harder maintenance, diminishing returns on quality
6. **Too many subagents (50+)** → Agent confusion during selection, increased maintenance burden; consolidate or use skill-based dispatch
7. **Duplicating slash commands as subagents** → If the task is single-purpose, a skill or command is more appropriate
8. **Missing `maxTurns`** → Runaway agents consuming tokens with no bound; always set a turn limit
9. **Not restricting tool access** → Security risk and unfocused behavior; every agent should have the minimum tools it needs
10. **Not checking into version control** → Team members can't benefit; `.claude/agents/` should be committed

## Related pages

- [[claude-code-subagents]]
- [[agent-workflows]]
- [[progressive-disclosure]]
- [[claude-code-plugins]]
