---
paths:
  - "plugins/prp-core/references/*.md"
  - ".claude/references/*.md"
---
# Reference File Conventions

Reference files in `references/` are the authoritative source of truth for cross-cutting policy. Skills and agents link to these files; they never duplicate policy inline.

## Required Structure

- `# [Title]` — one-line title
- Brief purpose sentence (what this file governs)
- Main content with clear headings
- `## Evidence` or inline citation where the policy is research-backed

## Authoring Rules

- Line budget: ≤ 100 lines per file.
- No external product names or attributions — describe patterns self-containedly.
- Link to other references with bare filenames: `context-budget-policy.md`, not absolute paths.
- Mirror parity: every change to `plugins/prp-core/references/` must be mirrored to `.claude/references/` byte-for-byte.
- Apply the deletion test: "Would removing this cause an agent to make mistakes?" If not, cut it.
