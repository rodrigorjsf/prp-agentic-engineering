# Context Budget Policy

The PRP harness treats context as a budget. Every token must earn its place. Noise in the context window degrades reasoning quality measurably — 3,000 filler tokens drop simple math accuracy from 0.92 to 0.68 (Levy et al., ACL 2024).

## Core rules

1. **Keep orchestration in the smart zone by default.** Run the primary workflow in a context window that stays under 40% capacity. Above that threshold, compaction or a subagent handoff is required before the next phase starts.

2. **Compact noisy outputs into bounded briefs before handoff.** Raw exploration transcripts, verbose tool outputs, and multi-file search dumps must be summarized before they pass to the next skill or phase. Brief size limits:
   - Discovery brief: ≤ 50 lines
   - Execution brief: ≤ 30 lines
   - Validation brief: ≤ 20 lines

3. **Prefer references over repeated inline policy text.** Cross-cutting policy belongs in shared reference files, not duplicated in each skill. Skills should link to the relevant reference instead of restating the same guidance.

4. **Treat raw agent transcripts as temporary context.** Subagent work products belong in compact artifacts (plan files, reports, brief sections), not in the main conversation thread. Discard exploration transcripts once the artifact is written.

5. **Progressive disclosure for instructions.** Load skill context, agents, and path-scoped rules on demand. Do not front-load all workflow instructions into every session. Always-loaded instructions must stay under 200 lines total.

## Compaction checkpoints

Each orchestration-heavy skill must define at least one compaction checkpoint — a point where noisy intermediate outputs are summarized before the next step proceeds. Typical checkpoints:

- After initial codebase exploration → summarize into a discovery brief
- After running all review agents → summarize findings into a combined report
- After investigation → summarize into an issue plan before implementation

## When to start a fresh context

Start a fresh context or subagent when:
- The current context is over 40% capacity and more noisy work remains
- The next task is genuinely independent of the current exploration
- The task is a large-corpus search, multi-file read, or iterative test loop

## Related references

- `harness-taxonomy.md` — component classes and their context profiles
- `execution-policy.md` — when to delegate to a subagent vs. stay inline
- `artifact-lifecycle.md` — where durable outputs live
