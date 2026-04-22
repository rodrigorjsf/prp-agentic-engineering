# Agent Best Practices

**Summary**: Practical guidance for agent-assisted development from the current workflow and configuration docs — covering the harness model (instructions + tools + model), context management, plan-first execution, rule/skill differentiation, and code review rigor.
**Sources**: research-agent-workflows-and-patterns.md, a-guide-to-agents.md, `docs/harness-engineering/harness-engineering.md`, `docs/harness-engineering/harnessengineering-building-the-operating-system-for-autonomous-agents.md`
**Last updated**: 2026-04-22

---

## Agent Harness Model

Every coding agent = **Instructions** + **Tools** + **Model**

| Component    | Purpose             | Examples                               |
| ------------ | ------------------- | -------------------------------------- |
| Instructions | Guide behavior      | CLAUDE.md, AGENTS.md, path-scoped rules |
| Tools        | Extend capabilities | Terminal, browser, search, MCP servers |
| Model        | Core reasoning      | Claude, GPT, etc.                      |

## Workflow Principles

### 1. Plan Before Implementing

- Start with an explicit planning phase before coding
- **Spec → Plan → Execute** separates thinking from doing
- Discrete loops prevent "getting over your skis"

### 2. Context Management

- Let the agent find files on demand — don't manually tag everything
- Fresh conversations when switching tasks (stale context poisons reasoning)
- After 2 failed corrections, `/clear` and restart
- Failed approaches accumulate and degrade performance

### 3. Rules vs Skills

| Aspect      | Rules                       | Skills                              |
| ----------- | --------------------------- | ----------------------------------- |
| Loading     | Always or glob-matched      | On relevance or manual              |
| Content     | Static context, conventions | Dynamic workflows, domain knowledge |
| Size        | Short, focused              | Multi-phase, can reference files    |
| When to add | Agent repeats same mistake  | Reusable multi-step workflow        |

### 4. Specific Prompts

"Write a test for auth.ts covering the logout edge case" beats "Write tests."

### 5. Code Review Rigor

Treat AI output like a junior developer's code review — verify, don't trust blindly.

## Anti-Patterns

| Anti-Pattern                           | Why It Fails                                     |
| -------------------------------------- | ------------------------------------------------ |
| Copying entire style guides into rules | Bloats context; agent already knows conventions  |
| Documenting every command              | Agent knows npm, git, pytest                     |
| Adding rules for rare edge cases       | Low signal-to-noise ratio                        |
| One-shotting complex projects          | Models perform poorly without verification loops |
| Duplicating codebase knowledge         | Agent can read the code itself                   |

## Context Budget Rules

- Keep config files under **200 lines** (~2,000–4,000 tokens)
- **~150–200 instructions** is the consistency limit for frontier LLMs
- Every token in always-loaded files loads on **every request**
- Test: "Would removing this cause mistakes?" If not, cut it

## Parallel Execution

- Route research and noisy verification to [[subagents]]
- Use isolated workspaces or worktrees when parallel tasks should not share file state
- Separate research, implementation, and review roles so each context stays narrow

## Two-Agent Architecture (Long-Running Tasks)

1. **Initializer** (first session) — creates structured artifacts (feature list, progress file)
2. **Coding Agent** (incremental) — picks up from artifacts, makes progress, updates state
3. Use **JSON for state** (model less likely to corrupt vs. Markdown)
4. Use **git history as state tracking** mechanism

## Related pages

- [[agent-workflows]]
- [[context-engineering]]
- [[progressive-disclosure]]
- [[agent-configuration-files]]
- [[evaluating-agents-paper]]
