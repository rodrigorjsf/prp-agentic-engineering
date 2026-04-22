---
paths:
  - "plugins/prp-core/agents/*.md"
  - ".claude/agents/*.md"
---
<!-- Dev-only — not shipped in plugin -->
<!-- Migrated from plugin conventions — agent-specific rules extracted to on-demand rule -->

# Agent File Conventions

> **Authoritative prompt structure**: `plugins/prp-core/references/agent-prompt-style.md`  
> **Component class definitions**: `plugins/prp-core/references/harness-taxonomy.md`

- YAML frontmatter requires: `name`, `description`, `model`, `color`
- Model selection: `haiku` for structured/fast tasks (explorer, comment-analyzer, docs-impact), `sonnet` for reasoning-heavy tasks (analyst, reviewer, type-design)
- Include `tools` and `maxTurns` in frontmatter: advisory agents get `maxTurns: 10`, exploration agents get `maxTurns: 15`
- Agents are read-only advisors — they must NOT modify files or create commits
