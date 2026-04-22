# Artifact Lifecycle

PRP artifacts are first-class outputs. Every artifact must declare where it lives, when it is archived, and who is responsible for it.

## Artifact locations

All PRP runtime artifacts live under `.claude/PRPs/` in the target project:

| Type | Path | Created by |
|------|------|------------|
| PRDs | `.claude/PRPs/prds/` | `prp-prd` |
| Plans | `.claude/PRPs/plans/` | `prp-plan` |
| Completed plans | `.claude/PRPs/plans/completed/` | `prp-implement` (archives after execution) |
| Reports | `.claude/PRPs/reports/` | `prp-implement` |
| Issues | `.claude/PRPs/issues/` | `prp-issue-investigate` |
| Completed issues | `.claude/PRPs/issues/completed/` | `prp-issue-fix` |
| Reviews | `.claude/PRPs/reviews/` | `prp-review` |
| Ralph archives | `.claude/PRPs/ralph-archives/` | `prp-ralph` (on completion) |

## Lifecycle rules

1. **Every artifact must declare its location before writing.** Skills should state the output path in the first step of their workflow, not after the artifact is written.

2. **Archive completed artifacts consistently.** A plan is not complete until it is moved to `plans/completed/`. An issue investigation is not resolved until the artifact is in `issues/completed/`. Archival is a workflow step, not optional cleanup.

3. **Durable artifacts carry the workflow forward; transcripts do not.** Only the compact artifact (PRD, plan, report, issue plan) should be passed between phases. Raw conversation history, exploration transcripts, and verbose tool outputs are temporary and must not be treated as the handoff artifact.

4. **Keep repo-only eval outputs outside the shipped plugin payload.** Prompt-evaluation fixtures, test case files, and CI scripts live in the repository's `tests/` and `scripts/` directories. They do not live in `plugins/prp-core/` and must not be referenced from shipped skills.

## Artifact naming

- PRDs: `<feature-slug>.prd.md`
- Plans: `<feature-slug>.plan.md`
- Reports: `<feature-slug>-report.md`
- Issues: `issue-<number>-<slug>.md`
- Reviews: `pr-<number>-review.md`

## Related references

- `harness-taxonomy.md` — which skills own which artifact class
- `context-budget-policy.md` — brief size limits that govern handoff artifacts
- `execution-policy.md` — delegation modes that determine which agent writes the artifact
