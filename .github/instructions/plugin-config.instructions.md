---
applyTo: ".claude-plugin/**/*.json,plugins/*/.claude-plugin/**/*.json,**/CLAUDE.md"
---
# Plugin Config Review Guidelines

## Distribution boundaries
- Flag any change that treats the installable plugin under `plugins/prp-core/` and the root `.claude/` mirror as the same distribution.
- Verify project-only extras such as `prp-core-runner`, `update-review-instructions`, and `gpui-researcher` are not documented as shipped plugin payload.

## Manifest alignment
- Check that `.claude-plugin/marketplace.json` still publishes `prp-core` from `./plugins/prp-core`.
- Check that `plugins/*/.claude-plugin/plugin.json` keeps the package identity aligned with the shipped plugin.
- Flag install or troubleshooting examples that use the wrong plugin identifier; this repo installs as `prp-core@prp-marketplace`.

## CLAUDE hierarchy
- Keep root `CLAUDE.md` minimal: project description, non-standard tooling, and high-signal pointers only.
- Flag inventory-style path, count, or version listings in root `CLAUDE.md`; they are high-churn and belong in scoped files or docs.
- Verify package-specific guidance stays in `plugins/prp-core/CLAUDE.md`, not duplicated in the root file.

## Common Issues to Flag
- Plugin and repo-local assets described as the same thing
- Marketplace `source` or plugin `name` drift
- Root `CLAUDE.md` repeating plugin inventory counts
- Legacy `/prp-*` command wording in configuration guidance
