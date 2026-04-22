# PRP Core Prompt Evaluations

This document describes the repo-local prompt evaluation harness at `scripts/prp_core_prompt_eval.py`.

## Purpose

The harness provides deterministic contract checks for the `prp-core` plugin. It verifies that:

1. Key skills contain required policy language (context-budget, bounded briefs, execution-policy references)
2. Shipped plugin skills are line-for-line identical to their `.claude/` mirror copies
3. The `prp-research-team-stop.sh` hook validates all six required research plan sections

The harness runs without any external dependencies — Python standard library only. All checks are deterministic substring or file equality tests.

## Usage

```bash
# List all defined test cases
uv run python scripts/prp_core_prompt_eval.py --list

# Run a single case
uv run python scripts/prp_core_prompt_eval.py --case plan

# Run all cases (exit 0 = all pass, exit 1 = any failure)
uv run python scripts/prp_core_prompt_eval.py --all
```

## Test cases

Cases are defined in `tests/prp-core/prompt-cases.json`.

| Case ID | Type | What it checks |
|---------|------|----------------|
| `plan` | `must_contain` | `prp-plan/SKILL.md` contains `bounded brief`, `context-budget-policy`, `execution-policy`, `artifact` |
| `implement` | `must_contain` | `prp-implement/SKILL.md` contains same contract strings |
| `review` | `must_contain` | `prp-review/SKILL.md` contains same contract strings |
| `issue-fix` | `must_contain` | `prp-issue-fix/SKILL.md` contains same contract strings |
| `mirror-parity` | `mirror_pairs` | 15 plugin/mirror skill pairs are byte-identical |
| `research-team-hook-schema` | `must_contain` | Hook validates all six required section headings |

## Adding a new case

Add a JSON object to `tests/prp-core/prompt-cases.json`:

```json
{
  "id": "my-case",
  "description": "What the check verifies",
  "type": "must_contain",
  "targets": ["plugins/prp-core/skills/my-skill/SKILL.md"],
  "must_contain": ["required phrase"]
}
```

For mirror parity cases, add a `mirror_pairs` entry with `[plugin_path, mirror_path]` pairs.

## CI integration

The workflow at `.github/workflows/prp-core-prompt-evals.yml` runs `--all` on every PR that touches:

- `plugins/prp-core/skills/**`
- `plugins/prp-core/agents/**`
- `plugins/prp-core/references/**`
- `.claude/skills/**`
- `.claude/agents/**`
- `.claude/references/**`
- `scripts/prp_core_prompt_eval.py`
- `tests/prp-core/**`

A failed eval blocks merge. The workflow requires Python 3.11+ and `uv`.

## Fixture files

`tests/prp-core/fixtures/` contains representative input prompts for each workflow case. These are not executed against a live model — they serve as documentation of the expected invocation shape for each skill.

| Fixture | Represents |
|---------|-----------|
| `plan-request.txt` | Typical `prp-plan` invocation |
| `implement-request.txt` | Typical `prp-implement` invocation |
| `review-request.txt` | Typical `prp-review` invocation |
| `issue-fix-request.txt` | Typical `prp-issue-fix` invocation |
