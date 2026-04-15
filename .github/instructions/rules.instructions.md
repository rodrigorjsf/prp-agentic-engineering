---
applyTo: ".claude/rules/**/*.md"
---
# Claude Rules Review Guidelines

## Frontmatter and scope
- Verify every rule file has YAML frontmatter with `paths:`.
- Flag any `paths:` glob broader than the rule body. SKILL.md conventions must not match `references/**/*.md`; hook script rules must not match README or JSON files.
- Prefer narrow, file-type-aware globs such as `**/skills/*/SKILL.md` and `**/hooks/*.sh`.

## Content placement
- Check that rule files contain only non-obvious, file-pattern-specific conventions.
- Flag project-wide guidance that belongs in root `CLAUDE.md`, or scope-wide guidance that belongs in a subdirectory `CLAUDE.md`.
- Flag duplicated guidance already covered by another rule file or the relevant scoped `CLAUDE.md`.

## Rule quality
- Keep one topic per file.
- Use concrete, reviewable directives rather than vague advice.
- Flag high-churn inventory data, directory listings, or references to files that do not exist.

## Common Issues to Flag
- Missing or overbroad `paths:`
- Rule body applies to one file type but the glob matches many
- Duplicate guidance across multiple rules
- Root-level guidance stuffed into a path-scoped rule
