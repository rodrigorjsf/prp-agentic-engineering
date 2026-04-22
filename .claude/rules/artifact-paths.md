---
paths:
  - "plugins/prp-core/skills/*/SKILL.md"
  - ".claude/skills/*/SKILL.md"
---
<!-- Dev-only — not shipped in plugin -->
<!-- Migrated from codebase analysis — artifact path contracts extracted to on-demand rule -->

# PRP Artifact Path Contracts

> **Authoritative policy**: `plugins/prp-core/references/artifact-lifecycle.md` — this rule is a scoped quick-reference for skill authors.

All PRP artifacts go under `.claude/PRPs/` with this structure:

| Type | Path | Created by |
|------|------|-----------|
| PRDs | `.claude/PRPs/prds/` | `prp-prd` |
| Plans | `.claude/PRPs/plans/` | `prp-plan` |
| Completed plans | `.claude/PRPs/plans/completed/` | `prp-implement` (archives after execution) |
| Reports | `.claude/PRPs/reports/` | `prp-implement` |
| Issues | `.claude/PRPs/issues/` | `prp-issue-investigate` |
| Completed issues | `.claude/PRPs/issues/completed/` | `prp-issue-fix` |
| Reviews | `.claude/PRPs/reviews/` | `prp-review` |
| Ralph archives | `.claude/PRPs/ralph-archives/` | `prp-ralph` (on completion) |
