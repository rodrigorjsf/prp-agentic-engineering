# PRP Core Plugin — Claude Code plugin providing PRP workflow automation (v3.0.0).

## Scope

- This directory is the installable plugin payload: `skills/`, `agents/`, `hooks/`, and `.claude-plugin/plugin.json`.
- Root `.claude/` is a development mirror, not the package itself.
- Keep shared plugin artifacts aligned between this directory and the root `.claude/` mirror.
- Root-only extras such as `prp-core-runner`, `update-review-instructions`, and `gpui-researcher` do not ship in the plugin.
