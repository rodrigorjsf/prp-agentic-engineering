# PRP Core Harness Evolution Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Evolve `plugins/prp-core/` into a clearer, lower-rot, better-tested PRP harness with explicit context-budget policy, stronger delegation rules, a repo-only prompt-evaluation routine, and updated documentation.

**Architecture:** Keep the shipped plugin lean and staged. Move cross-cutting workflow policy into a small shared reference layer, apply bounded-brief and delegation rules consistently to orchestration-heavy skills, selectively adapt HumanLayer's structured agent-prompt style for the plugin's highest-leverage agents, and add a repo-only evaluation harness that tests prompt contracts without shipping fixture noise in the plugin payload.

**Tech Stack:** Markdown skill/agent/rule files, shell hooks, Python stdlib via `uv run python`, GitHub Actions YAML, and repo documentation.

---

## File map

### New shipped-plugin files

- `plugins/prp-core/references/harness-taxonomy.md`
- `plugins/prp-core/references/context-budget-policy.md`
- `plugins/prp-core/references/execution-policy.md`
- `plugins/prp-core/references/artifact-lifecycle.md`
- `plugins/prp-core/references/agent-prompt-style.md`

### New mirror files

- `.claude/references/harness-taxonomy.md`
- `.claude/references/context-budget-policy.md`
- `.claude/references/execution-policy.md`
- `.claude/references/artifact-lifecycle.md`
- `.claude/references/agent-prompt-style.md`

### New repo-only evaluation files

- `scripts/prp_core_prompt_eval.py`
- `tests/prp-core/README.md`
- `tests/prp-core/prompt-cases.json`
- `tests/prp-core/fixtures/plan-request.txt`
- `tests/prp-core/fixtures/implement-request.txt`
- `tests/prp-core/fixtures/review-request.txt`
- `tests/prp-core/fixtures/issue-fix-request.txt`
- `.github/workflows/prp-core-prompt-evals.yml`

### New repo docs

- `docs/superpowers/specs/2026-04-21-prp-core-harness-evolution-design.md`
- `docs/prp-core-harness-architecture.md`
- `docs/prp-core-prompt-evals.md`

### Existing shipped files to modify

- `plugins/prp-core/README.md`
- `plugins/prp-core/CLAUDE.md`
- `plugins/prp-core/skills/prp-plan/SKILL.md`
- `plugins/prp-core/skills/prp-prd/SKILL.md`
- `plugins/prp-core/skills/prp-implement/SKILL.md`
- `plugins/prp-core/skills/prp-review/SKILL.md`
- `plugins/prp-core/skills/prp-review-agents/SKILL.md`
- `plugins/prp-core/skills/prp-issue-investigate/SKILL.md`
- `plugins/prp-core/skills/prp-issue-fix/SKILL.md`
- `plugins/prp-core/skills/prp-codebase-question/SKILL.md`
- `plugins/prp-core/skills/prp-research-team/SKILL.md`
- `plugins/prp-core/skills/prp-advisor/SKILL.md`
- `plugins/prp-core/skills/prp-commit/SKILL.md`
- `plugins/prp-core/skills/prp-verification-before-completion/SKILL.md`
- `plugins/prp-core/agents/codebase-analyst.md`
- `plugins/prp-core/agents/codebase-explorer.md`
- `plugins/prp-core/agents/plan-critic.md`
- `plugins/prp-core/agents/prp-advisor.md`
- `plugins/prp-core/agents/web-researcher.md`
- `plugins/prp-core/rules/prp-workflow.md`
- `plugins/prp-core/hooks/prp-ralph-stop.sh`
- `plugins/prp-core/hooks/prp-research-team-stop.sh`

### Existing mirror/docs files to modify

- `.claude/skills/prp-plan/SKILL.md`
- `.claude/skills/prp-prd/SKILL.md`
- `.claude/skills/prp-implement/SKILL.md`
- `.claude/skills/prp-review/SKILL.md`
- `.claude/skills/prp-review-agents/SKILL.md`
- `.claude/skills/prp-issue-investigate/SKILL.md`
- `.claude/skills/prp-issue-fix/SKILL.md`
- `.claude/skills/prp-codebase-question/SKILL.md`
- `.claude/skills/prp-research-team/SKILL.md`
- `.claude/skills/prp-advisor/SKILL.md`
- `.claude/skills/prp-commit/SKILL.md`
- `.claude/skills/prp-verification-before-completion/SKILL.md`
- `.claude/agents/codebase-analyst.md`
- `.claude/agents/codebase-explorer.md`
- `.claude/agents/plan-critic.md`
- `.claude/agents/prp-advisor.md`
- `.claude/agents/web-researcher.md`
- `.claude/rules/artifact-paths.md`
- `.claude/rules/agent-conventions.md`
- `.claude/hooks/README.md`
- `README.md`
- `README-for-DUMMIES.md`

### Validation commands this plan will introduce

- `uv run python scripts/prp_core_prompt_eval.py --list`
- `uv run python scripts/prp_core_prompt_eval.py --case plan`
- `uv run python scripts/prp_core_prompt_eval.py --case implement`
- `uv run python scripts/prp_core_prompt_eval.py --case review`
- `uv run python scripts/prp_core_prompt_eval.py --case issue-fix`

### Graphify grounding queries to use during implementation

- `/graphify query "What guidance in this repository graph is most relevant for keeping an agent harness in the smart zone while reducing context rot through progressive disclosure, bounded artifacts, subagent isolation, and staged research-plan-implement-validate workflows?"`
- `/graphify query "What guidance in this repository graph is most relevant for building a repo-only prompt evaluation harness around verification before completion, strict tool use, structured outputs, and deterministic prompt contracts?"`
- `/graphify query "What graph evidence connects smart zone context management, prompt evaluation or validation, HumanLayer Repository Analysis, and structured agent prompts or subagent delegation patterns?"`
- `/graphify path "Sub-Agents for Clean Context Forking" "Spec-Plan-Execute Workflow (Harper Reed)"`

**Rule for use:** If a graph query shows no direct path between concepts, do not force the connection in prompts or docs. Treat those ideas as separate evidence streams unless later graph updates create a justified bridge.
**Current graph note:** the refreshed docs-only graph now shows concrete smart-zone paths into staged workflow and subagent isolation via `Dumb Zone (40%+ Context Degradation)` and `Advanced Context Engineering for Coding Agents`. It still does not show a clean direct path from smart-zone thresholds to the broader `Context Engineering` / formal context-rot-definition nodes, so keep those as adjacent evidence streams rather than one forced proof chain.

### Evidence refresh (2026-04-22)

This plan was re-verified after the smart-zone and harness-engineering docs were added to the graphified corpus and the wiki was refreshed.

| Claim | Wiki support | Graph support | Status |
| --- | --- | --- | --- |
| Smart-zone framing should stay central to harness policy | `wiki/knowledge/harness-engineering.md` and `wiki/knowledge/context-engineering.md` both treat context controls and compaction as first-class harness concerns | BFS query surfaced `Smart/Warm/Dumb Zone Thresholds (0-40/40-70/70%+)`, `Dumb Zone (40%+ Context Degradation)`, `Intentional Compaction`, and related context-rot nodes in the same evidence cluster | Confirmed |
| Staged workflows should remain explicit in the plan | `wiki/knowledge/harness-engineering.md` defines the harness workflow as research -> plan -> implement -> review; `wiki/knowledge/context-engineering.md` documents the Research-Plan-Implement workflow as a compaction strategy | Shortest path: `Smart/Warm/Dumb Zone Thresholds (0-40/40-70/70%+)` -> `Dumb Zone (40%+ Context Degradation)` -> `Advanced Context Engineering for Coding Agents` -> `Research-Plan-Implement (RPI) Workflow` | Confirmed |
| Subagent isolation belongs in the shared execution policy | `wiki/knowledge/harness-engineering.md` describes subagents as context firewalls; `wiki/knowledge/context-engineering.md` lists subagents as a core context-management strategy | Shortest path: `Smart/Warm/Dumb Zone Thresholds (0-40/40-70/70%+)` -> `Dumb Zone (40%+ Context Degradation)` -> `Advanced Context Engineering for Coding Agents` -> `Sub-Agents for Clean Context Forking` | Confirmed |
| Progressive disclosure should still be mentioned, but as an indirect smart-zone link | `wiki/knowledge/context-engineering.md` names progressive disclosure as one of the core context strategies | Shortest path: `Smart/Warm/Dumb Zone Thresholds (0-40/40-70/70%+)` -> `Dumb Zone (40%+ Context Degradation)` -> `Advanced Context Engineering for Coding Agents` -> `Sub-Agents for Clean Context Forking` -> `Scout Pattern (Pre-Screening Context Needs)` -> `Progressive Disclosure in AI Agents (MindStudio)` | Confirmed, but indirect |
| Do not collapse every smart-zone rationale into one graph-backed proof chain | The wiki ties smart zone, context rot, and compaction together conceptually, but keeps them as distinct ideas with different mechanisms | Targeted shortest-path queries did not produce a clean direct path from smart-zone thresholds to the broader `Context Engineering` / formal `Context Rot` nodes | Provisional / wiki-backed |

## Task 1: Add the shared harness contract layer

**Files:**
- Create: `plugins/prp-core/references/harness-taxonomy.md`
- Create: `plugins/prp-core/references/context-budget-policy.md`
- Create: `plugins/prp-core/references/execution-policy.md`
- Create: `plugins/prp-core/references/artifact-lifecycle.md`
- Create: `plugins/prp-core/references/agent-prompt-style.md`
- Create: `.claude/references/harness-taxonomy.md`
- Create: `.claude/references/context-budget-policy.md`
- Create: `.claude/references/execution-policy.md`
- Create: `.claude/references/artifact-lifecycle.md`
- Create: `.claude/references/agent-prompt-style.md`
- Test: `plugins/prp-core/README.md`

- [ ] **Step 0: Run the smart-zone grounding query**

Run: `/graphify query "What guidance in this repository graph is most relevant for keeping an agent harness in the smart zone while reducing context rot through progressive disclosure, bounded artifacts, subagent isolation, and staged research-plan-implement-validate workflows?"`  
Expected: confirm the graph-backed path from smart-zone thresholds into `Dumb Zone`, `Advanced Context Engineering`, `Research-Plan-Implement (RPI) Workflow`, and `Sub-Agents for Clean Context Forking`; treat progressive disclosure as adjacent but indirect evidence; cross-check `wiki/knowledge/harness-engineering.md` and `wiki/knowledge/context-engineering.md` before turning the findings into shared references

- [ ] **Step 1: Write the contract skeletons in the shipped plugin**

```md
# Harness Taxonomy

- Sequential artifact skills: create durable PRP artifacts.
- Advisory components: review, critique, and refine decisions.
- Utility components: commit, PR, verification, and narrow helpers.
```

- [ ] **Step 2: Mirror the same contract files into `.claude/references/`**

```md
# Execution Policy

1. Stay inline for short, deterministic work.
2. Use isolated subagents for noisy exploration.
3. Parallelize only independent scopes.
4. Use documented repo-local evaluation harnesses when they exist, but do not assume they ship in the plugin payload.
```

- [ ] **Step 3: Add the context-budget policy**

```md
# Context Budget Policy

- Keep orchestration in the smart zone by default.
- Compact noisy outputs into bounded briefs before handoff.
- Prefer references over repeated inline policy text.
- Treat raw agent transcripts as temporary, not durable context.
```

- [ ] **Step 4: Add the artifact-lifecycle policy**

```md
# Artifact Lifecycle

- PRDs, plans, reports, issues, and reviews must declare where they live.
- Archive completed plan artifacts consistently.
- Keep repo-only eval outputs outside the shipped plugin payload.
```

- [ ] **Step 5: Add the selective agent-prompt style contract**

```md
# Agent Prompt Style

- One explicit job per agent.
- Hard "do not" boundaries.
- Minimal tool surface.
- Named responsibilities and strategy.
- Fixed output format when the task shape is repeatable.
```

- [ ] **Step 6: Verify the new references are present in both shipped and mirror trees**

Run: `git --no-pager diff -- plugins/prp-core/references .claude/references`  
Expected: new reference files exist, and shipped/mirror copies match line-for-line

- [ ] **Step 7: Commit**

```bash
git add plugins/prp-core/references .claude/references
git commit -m "feat(prp-core): add shared harness reference layer"
```

## Task 2: Build the repo-only prompt evaluation harness

**Files:**
- Create: `scripts/prp_core_prompt_eval.py`
- Create: `tests/prp-core/README.md`
- Create: `tests/prp-core/prompt-cases.json`
- Create: `tests/prp-core/fixtures/plan-request.txt`
- Create: `tests/prp-core/fixtures/implement-request.txt`
- Create: `tests/prp-core/fixtures/review-request.txt`
- Create: `tests/prp-core/fixtures/issue-fix-request.txt`
- Create: `.github/workflows/prp-core-prompt-evals.yml`
- Test: `scripts/prp_core_prompt_eval.py`

- [ ] **Step 0: Run the prompt-contract grounding query**

Run: `/graphify query "What guidance in this repository graph is most relevant for building a repo-only prompt evaluation harness around verification before completion, strict tool use, structured outputs, and deterministic prompt contracts?"`  
Expected: evidence for strict tool use, structured outputs, spec-anchored validation, and agent-friendly script interfaces

- [ ] **Step 1: Write failing prompt cases before the runner**

```json
[
  {
    "id": "plan",
    "input_file": "tests/prp-core/fixtures/plan-request.txt",
    "must_contain": ["bounded brief", "parallel", "artifact"],
    "targets": ["plugins/prp-core/skills/prp-plan/SKILL.md"]
  }
]
```

- [ ] **Step 2: Run the missing runner to confirm the harness is not implemented yet**

Run: `uv run python scripts/prp_core_prompt_eval.py --list`  
Expected: FAIL with "No such file or directory" or equivalent missing-runner error

- [ ] **Step 3: Implement the minimal runner**

```python
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_cases(path: Path) -> list[dict]:
    return json.loads(path.read_text())
```

- [ ] **Step 4: Add deterministic checks for required substrings, mirror parity, and hook schema alignment**

```python
def evaluate_case(case: dict) -> list[str]:
    failures: list[str] = []
    for target in case["targets"]:
        text = Path(target).read_text()
        for needle in case["must_contain"]:
            if needle not in text:
                failures.append(f"{case['id']}: missing '{needle}' in {target}")
    return failures
```

```python
def assert_equal_text(left: Path, right: Path) -> list[str]:
    return [] if left.read_text() == right.read_text() else [f"mirror drift: {left} != {right}"]
```

- [ ] **Step 5: Add fixture docs and a CI workflow**

```yaml
name: prp-core-prompt-evals
on:
  pull_request:
    paths:
      - "plugins/prp-core/**"
      - ".claude/**"
      - "scripts/prp_core_prompt_eval.py"
      - "tests/prp-core/**"
jobs:
  prompt-evals:
    runs-on: ubuntu-latest
```

- [ ] **Step 6: Run the harness on all cases**

Run: `uv run python scripts/prp_core_prompt_eval.py --list`  
Expected: PASS and prints the available case IDs

- [ ] **Step 7: Run one concrete case**

Run: `uv run python scripts/prp_core_prompt_eval.py --case plan`  
Expected: FAIL at first, because the current plan skill does not yet contain the new shared-contract language

- [ ] **Step 8: Commit**

```bash
git add scripts/prp_core_prompt_eval.py tests/prp-core .github/workflows/prp-core-prompt-evals.yml
git commit -m "feat(repo): add prp-core prompt evaluation harness"
```

## Task 3: Apply the context-budget, delegation, and agent-prompt contract

**Files:**
- Modify: `plugins/prp-core/skills/prp-plan/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-prd/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-implement/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-review/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-review-agents/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-issue-investigate/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-issue-fix/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-codebase-question/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-research-team/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-advisor/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-commit/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-verification-before-completion/SKILL.md`
- Modify: `plugins/prp-core/agents/codebase-analyst.md`
- Modify: `plugins/prp-core/agents/codebase-explorer.md`
- Modify: `plugins/prp-core/agents/plan-critic.md`
- Modify: `plugins/prp-core/agents/prp-advisor.md`
- Modify: `plugins/prp-core/agents/web-researcher.md`
- Modify mirror copies under `.claude/skills/...`
- Modify mirror copies under `.claude/agents/...`
- Test: `scripts/prp_core_prompt_eval.py`

- [ ] **Step 0: Run the structured-agent grounding query**

Run: `/graphify query "What graph evidence connects smart zone context management, prompt evaluation or validation, HumanLayer Repository Analysis, and structured agent prompts or subagent delegation patterns?"`  
Expected: evidence for subagent isolation, progressive disclosure, intentional compaction, and structured prompts; if HumanLayer is not directly connected to smart-zone concepts, keep it as a prompt-structure comparator only

- [ ] **Step 1: Update one orchestration-heavy skill with the shared contract language**

```md
Before continuing:
1. Read `plugins/prp-core/references/context-budget-policy.md`.
2. Compact noisy findings into a bounded brief before handoff.
3. Parallelize only independent scopes.
4. Use repo-only scripts only for deterministic batch checks.
```

- [ ] **Step 2: Add the same contract shape to the remaining shipped skills**

```md
Required intermediate artifact:
- Discovery Brief: <= 50 lines
- Execution Brief: <= 30 lines
- Validation Brief: <= 20 lines
```

- [ ] **Step 3: Mirror the same edits into `.claude/skills/...`**

```md
Keep shared plugin artifacts aligned with the shipped plugin.
Do not copy repo-only eval instructions into the shipped payload.
```

- [ ] **Step 4: Standardize parallelism wording**

```md
Use parallel agents only when scopes are independent.
If scopes share files or state, keep execution sequential.
```

- [ ] **Step 5: Add explicit fallback language for deterministic batch verification without naming repo-only script paths inside shipped skills**

```md
If the task needs deterministic batch verification, use the documented repo-local
evaluation harness instead of repeating manual checks in the main context.
```

- [ ] **Step 6: Normalize the selected PRP agents with the HumanLayer-inspired structure**

```md
## CRITICAL: Your only job is to [specific role]
- DO NOT ...
- DO NOT ...
- ONLY ...

## Core Responsibilities
1. ...
2. ...

## Strategy
1. ...
2. ...

## Output Format
Define a stable section layout for repeated task shapes.
```

```md
Retain existing PRP-specific frontmatter and capabilities unless a change is
explicitly justified by the plugin's actual runtime/tooling needs.
```

- [ ] **Step 7: Run the prompt-eval harness on all affected cases**

Run: `uv run python scripts/prp_core_prompt_eval.py --case plan && uv run python scripts/prp_core_prompt_eval.py --case implement && uv run python scripts/prp_core_prompt_eval.py --case review && uv run python scripts/prp_core_prompt_eval.py --case issue-fix`  
Expected: PASS for each updated case

- [ ] **Step 8: Commit**

```bash
git add plugins/prp-core/skills plugins/prp-core/agents .claude/skills .claude/agents
git commit -m "feat(prp-core): standardize context and agent contracts"
```

## Task 4: Consolidate shared orchestration behavior and tighten guardrails

**Files:**
- Modify: `plugins/prp-core/skills/prp-implement/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-pr/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-issue-investigate/SKILL.md`
- Modify: `plugins/prp-core/skills/prp-issue-fix/SKILL.md`
- Modify: `plugins/prp-core/rules/prp-workflow.md`
- Modify: `plugins/prp-core/hooks/prp-ralph-stop.sh`
- Modify: `plugins/prp-core/hooks/prp-research-team-stop.sh`
- Modify: `.claude/rules/artifact-paths.md`
- Modify: `.claude/rules/agent-conventions.md`
- Modify: `.claude/hooks/README.md`
- Modify mirror copies when applicable
- Test: `scripts/prp_core_prompt_eval.py`, hook shell scripts

- [ ] **Step 0: Run the workflow-bridge path query**

Run: `/graphify path "Sub-Agents for Clean Context Forking" "Spec-Plan-Execute Workflow (Harper Reed)"`  
Expected: a short path showing subagent isolation feeding the staged spec/plan/execute workflow; use that bridge to keep guardrails aligned with staged execution rather than ad hoc orchestration

- [ ] **Step 1: Move repeated branch/artifact language behind the new shared references**

```md
Base-branch selection and artifact archival must follow the shared lifecycle policy.
Do not redefine the same policy block in each skill.
```

- [ ] **Step 2: Tighten the workflow rule without broadening it carelessly**

```md
paths:
  - .claude/PRPs/prds/**/*.prd.md
  - .claude/PRPs/plans/**/*.plan.md

Require:
- advisor before approach lock-in
- verification before completion claims
- archived plan before PR creation
```

- [ ] **Step 3: Reconcile overlapping mirror rules with the new shared references**

```md
This rule should keep only path-scoped, auto-loaded guidance.
Move reusable policy text into shared references, or link to those references.
```

- [ ] **Step 4: Keep the research-team six-section schema aligned across skill, hook, and docs**

```bash
required_sections=(
  "## Research Question"
  "## Research Question Decomposition"
  "## Team Composition"
  "## Research Tasks"
  "## Team Orchestration Guide"
  "## Acceptance Criteria"
)
for section in "${required_sections[@]}"; do
  grep -qF "$section" "$OUTPUT_PATH" || missing+=("$section")
done
```

- [ ] **Step 5: Re-run the prompt harness and shell syntax checks**

Run: `uv run python scripts/prp_core_prompt_eval.py --list && bash -n plugins/prp-core/hooks/prp-ralph-stop.sh && bash -n plugins/prp-core/hooks/prp-research-team-stop.sh`  
Expected: PASS from the eval runner, and no shell syntax output

- [ ] **Step 6: Commit**

```bash
git add plugins/prp-core/skills/prp-implement/SKILL.md plugins/prp-core/skills/prp-pr/SKILL.md plugins/prp-core/skills/prp-issue-investigate/SKILL.md plugins/prp-core/skills/prp-issue-fix/SKILL.md plugins/prp-core/rules/prp-workflow.md plugins/prp-core/hooks/prp-ralph-stop.sh plugins/prp-core/hooks/prp-research-team-stop.sh .claude/rules/artifact-paths.md .claude/rules/agent-conventions.md .claude/hooks/README.md
git commit -m "refactor(prp-core): consolidate orchestration guardrails"
```

## Task 5: Refresh shipped and repo-local documentation

**Files:**
- Create: `docs/prp-core-harness-architecture.md`
- Create: `docs/prp-core-prompt-evals.md`
- Modify: `plugins/prp-core/README.md`
- Modify: `plugins/prp-core/CLAUDE.md`
- Modify: `README.md`
- Modify: `README-for-DUMMIES.md`
- Test: rendered markdown review and prompt-eval docs commands

- [ ] **Step 0: Re-run the HumanLayer comparator query before writing docs**

Run: `/graphify query "What graph evidence connects smart zone context management, prompt evaluation or validation, HumanLayer Repository Analysis, and structured agent prompts or subagent delegation patterns?"`  
Expected: enough evidence to document HumanLayer as a structural prompt comparator, but no forced claim that it is the proof source for smart-zone policy unless the graph shows a direct bridge

- [ ] **Step 1: Write the architecture explainer**

```md
# PRP Core Harness Architecture

This document explains the shipped harness taxonomy, context-budget rules,
delegation policy, prompt-eval routine, and why the plugin stays lean.
```

- [ ] **Step 2: Rewrite the plugin README around progressive disclosure**

```md
## What ships

`prp-core` ships the workflow surface.
Use this README for install and usage.
Use `docs/prp-core-harness-architecture.md` for the why.
```

- [ ] **Step 3: Keep `plugins/prp-core/CLAUDE.md` short and package-scoped**

```md
- This directory is the installable plugin payload.
- Shared references live in `references/`.
- Repo-only eval tooling lives outside `plugins/prp-core/`.
```

- [ ] **Step 4: Update the root READMEs to explain plugin vs mirror vs repo-only eval tooling**

```md
- `plugins/prp-core/` is shipped.
- `.claude/` mirrors shared plugin artifacts for development.
- `scripts/` and `tests/prp-core/` are repo-only harness maintenance tools.
```

- [ ] **Step 5: Document how to run prompt evaluations**

Run: `uv run python scripts/prp_core_prompt_eval.py --list`  
Expected: lists cases and points to `docs/prp-core-prompt-evals.md`

- [ ] **Step 6: Commit**

```bash
git add docs/prp-core-harness-architecture.md docs/prp-core-prompt-evals.md plugins/prp-core/README.md plugins/prp-core/CLAUDE.md README.md README-for-DUMMIES.md
git commit -m "docs: document prp-core harness architecture and eval flow"
```

## Self-review checklist

- [ ] Every cross-cutting policy moved into a shared reference has at least one skill that links to it.
- [ ] No repo-only eval instructions leaked into the shipped plugin payload.
- [ ] Every shipped skill updated in `plugins/prp-core/` has the matching mirror update in `.claude/`.
- [ ] Mirror rules and hook docs no longer duplicate the new shared references.
- [ ] The selected agents follow the same one-job, hard-boundary, fixed-output structure where it improves clarity.
- [ ] The prompt-eval harness has at least four cases that match the main workflow families.
- [ ] The docs explain both the current state and the research-driven why.

## Suggested implementation order

1. Task 1
2. Task 2
3. Task 3
4. Task 4
5. Task 5
