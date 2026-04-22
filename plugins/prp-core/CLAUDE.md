# PRP Core Plugin — Claude Code plugin providing PRP workflow automation.

## Scope

- This directory is the installable plugin payload: `skills/`, `agents/`, `hooks/`, `rules/`, `references/`, and `.claude-plugin/plugin.json`.
- Root `.claude/` is a development mirror, not the package itself.
- Keep shared plugin artifacts aligned between this directory and the root `.claude/` mirror.
- Root-only extras such as `prp-core-runner`, `update-review-instructions`, and `gpui-researcher` do not ship in the plugin.
- Cross-cutting policy lives in `references/`. Skills and agents link to those files instead of duplicating policy inline.
