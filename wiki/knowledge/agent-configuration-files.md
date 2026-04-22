# Agent Configuration Files

**Summary**: Repository-level context files such as AGENTS.md, CLAUDE.md, and Claude Code path-scoped rules provide persistent project instructions to coding agents — and work best when they stay minimal, specific, and non-redundant.
**Sources**: a-guide-to-agents.md, how-claude-remembers-a-project.md, Evaluating-AGENTS-paper.md
**Last updated**: 2026-04-22

---

## File Types by Platform

| File                    | Platform       | Purpose                              | Loaded                               |
| ----------------------- | -------------- | ------------------------------------ | ------------------------------------ |
| **CLAUDE.md**           | Claude Code    | Project-specific instructions        | Every request (directory hierarchy)  |
| **AGENTS.md**           | Cross-platform | Portable agent instructions          | Every request                        |
| **.claude/rules/*.md**  | Claude Code    | Path-scoped rules with glob patterns | When matching files touched          |

## CLAUDE.md Hierarchy

Claude Code discovers CLAUDE.md files via directory traversal:

1. **Managed policy** — `/etc/claude-code/CLAUDE.md` (Linux), `C:\Program Files\ClaudeCode\CLAUDE.md` (Windows)
2. **User** — `~/.claude/CLAUDE.md`
3. **Project** — `./CLAUDE.md` or `./.claude/CLAUDE.md`
4. **Subdirectory** — Nested CLAUDE.md files (lazy loading)

**Load precedence**: Enterprise > Personal > Project

### Import Syntax

- `@README` — Import file content
- `@package.json` — Import project files
- `@~/.claude/my-instructions.md` — Cross-project imports
- Import depth limit: **5 hops maximum**

## Line Budgets

| Config File      | Target          | Maximum   |
| ---------------- | --------------- | --------- |
| Root CLAUDE.md   | 15–40 lines     | 200 lines |
| Plugin CLAUDE.md | 10–30 lines     | 200 lines |
| Rule files       | 10–30 lines     | 200 lines |

## What Belongs in Config Files

**Include** (unique value):

- Build and test commands
- Project-specific conventions not inferable from code
- Non-obvious patterns and gotchas
- Package manager preferences

**Exclude** (redundant or harmful):

- Standard language conventions (agents already know these)
- Information inferable from the codebase
- Dense paragraphs (use headers and bullets)
- Personal preferences in project files
- Conflicting rules (model picks one arbitrarily)

## Related pages

- [[progressive-disclosure]]
- [[evaluating-agents-paper]]
- [[claude-code-memory]]
- [[context-engineering]]
