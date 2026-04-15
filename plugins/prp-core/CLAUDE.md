# PRP Core Plugin — Claude Code plugin providing PRP workflow automation (v3.0.0).

## Architecture

- **Skills** (`skills/`): 15 SKILL.md files with `references/` for templates. Primary interface.
- **Agents** (`agents/`): 10 specialized subagents for code review, exploration, and analysis.
- **Hooks** (`hooks/`): Stop hooks for Ralph loop and research-team sentinel validation.

## Dual-Layer Sync

Skills and agents are mirrored to `.claude/` at project level. Edits must be applied to both locations or drift will cause inconsistent behavior. Project-level has two extras not in the plugin:
- `.claude/skills/prp-core-runner/` — orchestration skill
- `.claude/agents/gpui-researcher.md` — project-specific agent
