# Harness Taxonomy

The PRP harness groups all shipped components into three classes. Every skill and agent belongs to exactly one class.

## Component Classes

### Sequential artifact skills

Create durable PRP artifacts that later phases consume. Each skill owns one phase of the research → plan → implement → validate lifecycle and hands forward a compact artifact, not raw exploration output.

- `prp-prd` — PRD from a feature request
- `prp-plan` — implementation plan from a PRD or brief
- `prp-implement` — execution from a plan
- `prp-issue-investigate` — investigation artifact from a GitHub issue
- `prp-issue-fix` — fix and PR from an investigation artifact
- `prp-research-team` — research plan from a question
- `prp-codebase-question` — scoped research answer

### Advisory components

Challenge, review, and refine decisions. Advisory components do not create primary workflow artifacts and do not modify files directly.

- `prp-advisor` — pre-work and mid-work critique gate
- `prp-review` — PR review artifact
- `prp-review-agents` — multi-aspect specialized review
- `prp-prd` — also acts as an advisory scope-clarifier before planning
- `plan-critic` agent — targeted plan critique
- `prp-advisor` agent — advisor subagent for the skill
- `codebase-analyst` agent — deep implementation analysis
- `codebase-explorer` agent — file and structure exploration
- `web-researcher` agent — external documentation research

### Utility components

Execute one narrow, repeatable job as the final step of a flow. Utilities should not contain research or planning logic.

- `prp-commit` — atomic commit from staged changes
- `prp-pr` — pull request from a branch
- `prp-verification-before-completion` — final validation gate before claiming done
- `prp-ralph` / `prp-ralph-cancel` / `prp-ralph-loop` — autonomous loop control
- `prp-debug` — root-cause analysis helper

## Design intent

- Each class has a different context profile. Artifact skills need bounded briefs and compaction checkpoints. Advisory components need read access and a fixed output shape. Utility components should keep their context footprint small.
- A skill that crosses two classes (for example, an artifact skill that also reviews) should be refactored or the review step should be delegated to an advisory agent.
- See `context-budget-policy.md` for compaction rules and brief size limits.
- See `execution-policy.md` for when to stay inline vs. delegate to a subagent.
