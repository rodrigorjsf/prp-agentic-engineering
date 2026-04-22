# Execution Policy

The PRP harness defines four delegation modes. Choose the right mode based on task size, isolation, and determinism.

## Delegation modes

### 1. Stay inline

Use for short, deterministic, single-scope work that does not generate noisy intermediate output.

Criteria:
- Task completes in a handful of tool calls
- Output is compact and directly consumed by the next step
- No heavy exploration or multi-file corpus search needed

Examples: reading a single file, writing a short commit message, running a schema check.

### 2. Use an isolated subagent

Use for noisy exploration, large-corpus research, or analysis that would pollute the main context.

Criteria:
- Task requires reading many files, searching broadly, or running iterative queries
- Output will be summarized into a compact brief before handoff
- The work is independent enough that the main context does not need to observe every step

Examples: codebase exploration, external documentation research, review analysis.

Return only the compact result (discovery brief, research summary, review report) to the main context. Discard the exploration transcript.

### 3. Parallelize

Use only when scopes are genuinely independent — no shared files, no shared state, no ordering dependency.

Criteria:
- Two or more subagents can run without reading each other's outputs
- Merging their results does not require re-running either agent
- Parallelism does not create conflicting writes

If in doubt, keep execution sequential.

### 4. Use a documented repo-local evaluation harness

Use for deterministic batch verification that would otherwise repeat the same manual checks in the main context.

Criteria:
- A documented evaluation script already exists for this check
- The check is repeatable, schema-bound, or file-comparison-based
- The result is pass/fail, not a reasoning judgment

Do not assume evaluation harness scripts ship in the plugin payload. They are repo-only tools. Do not name repo-only script paths inside shipped skills.

## Parallelism guard

Before parallelizing, answer: "Do these scopes share any file, state variable, or sequencing constraint?" If yes, keep them sequential.

## Research-team policy

When `prp-research-team` is used, the orchestrating agent must:
1. Decompose the question into genuinely independent sub-questions
2. Assign each sub-question to a specialist with a bounded scope
3. Collect compact summaries from each specialist
4. Synthesize into the required six-section research plan

## Related references

- `context-budget-policy.md` — brief size limits and compaction rules
- `harness-taxonomy.md` — which component class owns each decision
- `artifact-lifecycle.md` — where outputs land after delegation
