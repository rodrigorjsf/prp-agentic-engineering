# PRP Core Prompt Evaluation Harness

This directory contains the repo-only prompt-contract evaluation harness for `prp-core`. It is not part of the shipped plugin payload.

## Purpose

The harness runs deterministic checks against shipped skill files, agents, and hooks to catch:

- Missing contract language (bounded brief sizes, context-budget-policy references, execution-policy references)
- Mirror drift (shipped `plugins/prp-core/` files diverging from `.claude/` mirror copies)
- Hook schema alignment (required research plan sections present in the stop hook)

## Structure

```
tests/prp-core/
├── README.md               # This file
├── prompt-cases.json       # Test case definitions
└── fixtures/
    ├── plan-request.txt         # Example prp-plan invocation
    ├── implement-request.txt    # Example prp-implement invocation
    ├── review-request.txt       # Example prp-review invocation
    └── issue-fix-request.txt    # Example prp-issue-fix invocation
```

## Running the harness

```bash
# List available cases
uv run python scripts/prp_core_prompt_eval.py --list

# Run a specific case
uv run python scripts/prp_core_prompt_eval.py --case plan
uv run python scripts/prp_core_prompt_eval.py --case implement
uv run python scripts/prp_core_prompt_eval.py --case review
uv run python scripts/prp_core_prompt_eval.py --case issue-fix
uv run python scripts/prp_core_prompt_eval.py --case mirror-parity
uv run python scripts/prp_core_prompt_eval.py --case research-team-hook-schema

# Run all cases
uv run python scripts/prp_core_prompt_eval.py --all
```

Exit code 0 = all checks pass. Exit code 1 = one or more checks failed.

## Case types

### Contract checks (`must_contain`)

Check that target skill or hook files contain specific required strings. These catch when a skill is updated but the shared contract language is removed or never added.

### Mirror parity (`mirror-parity`)

Check that shipped plugin files in `plugins/prp-core/` match their `.claude/` mirror copies line-for-line. Both trees must stay in sync after every skill or agent update.

### Hook schema alignment (`research-team-hook-schema`)

Check that `prp-research-team-stop.sh` validates all six required research plan sections. This ensures the hook, skill, and documentation stay aligned.

## CI

The harness runs on pull requests that touch `plugins/prp-core/`, `.claude/`, `scripts/prp_core_prompt_eval.py`, or `tests/prp-core/`. See `.github/workflows/prp-core-prompt-evals.yml`.

## Adding a new case

Add a new entry to `prompt-cases.json`:

```json
{
  "id": "my-case",
  "description": "What this case checks",
  "must_contain": ["required string 1", "required string 2"],
  "targets": ["plugins/prp-core/skills/my-skill/SKILL.md"]
}
```

For mirror parity cases, use `mirror_pairs` instead of `targets` + `must_contain`. See existing cases for the format.

## See also

- `docs/prp-core-prompt-evals.md` — full evaluation model rationale
- `plugins/prp-core/references/context-budget-policy.md` — contract strings being tested
- `plugins/prp-core/references/execution-policy.md` — delegation contract being tested
