# Copilot Instructions

- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Use the `graphify` MCP tools or  Trigger: `/graphify`
When the user types `/graphify`, invoke the Skill tool with `skill: "graphify"` before doing anything else.

## Build, test, and lint

- Use `uv` for repo-level Python tasks.
- No repo-wide build, lint, or test commands are declared in `pyproject.toml` or other top-level manifests. Do not assume `pytest`, `ruff`, `npm`, `make`, or single-test targets exist for this repository itself.

## High-level architecture

- This repository publishes a Claude Code marketplace. `.claude-plugin/marketplace.json` exposes the installable plugin `prp-core` from `plugins/prp-core/`.
- `plugins/prp-core/` is the shipped plugin payload. It contains the plugin manifest, skill definitions, agent definitions, and hook scripts that users install.
- Root `.claude/` is a development mirror of shared plugin artifacts, plus repo-only extras such as `prp-core-runner`, `update-review-instructions`, and `gpui-researcher`. If you change a shared skill, agent, or hook, check whether the mirrored file also needs the same update.
- Plugin hooks live under `plugins/prp-core/hooks/`. Root `.claude/hooks/` documents repo-local/manual hook setup and does not mirror every plugin hook.
- `.github/instructions/` contains Copilot code review instructions. Those files guide review behavior, not plugin runtime behavior.
- PRP artifacts such as PRDs, plans, reports, issues, and reviews are runtime outputs written by skills into the target project's `.claude/PRPs/`; they are not committed source directories in this repo.

## Key conventions

- Skills are the primary interface. In docs and config, prefer skill wording such as `run the prp-plan skill`; do not reintroduce legacy `/prp-*` command framing unless you are editing historical examples on purpose.
- Keep the packaged plugin and the repo-local mirror distinct. Root-only extras must not be documented as shipped plugin payload.
- Keep manifest and install naming aligned across docs and config: the marketplace publishes `prp-core` from `./plugins/prp-core`, and install examples should use `prp-core@prp-engineering-marketplace`.
- Keep `CLAUDE.md` minimal. Project-wide essentials belong there; file-pattern-specific rules belong in `.claude/rules/*.md`.
- Keep `.claude/rules/` narrowly scoped and one-topic-per-file. For example, SKILL.md conventions should target `**/skills/*/SKILL.md`, and hook-script conventions should target shell hooks rather than README or JSON files.
- When editing `.github/instructions/*.instructions.md`, include YAML frontmatter with `applyTo`, keep each file under 4,000 characters, and write concrete review checks rather than generic quality guidance.