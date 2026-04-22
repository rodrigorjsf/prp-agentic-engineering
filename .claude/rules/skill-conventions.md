---
paths:
  - "plugins/prp-core/skills/*/SKILL.md"
  - ".claude/skills/*/SKILL.md"
---
<!-- Dev-only — not shipped in plugin -->
<!-- Migrated from CLAUDE.md — skill-specific conventions extracted to on-demand rule -->

# Skill File Conventions

- SKILL.md uses YAML frontmatter with `name` and `description` fields only
- SKILL.md body ≤ 400 lines; overflow content goes to `references/` subdirectory
- Load reference files with `${CLAUDE_SKILL_DIR}/references/filename.md`
- Cross-reference other skills as "run the `prp-X` skill" (never `/prp-X` command syntax)
- Agent references in skills must use plugin-qualified names: `prp-core:agent-name`
