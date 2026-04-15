---
name: prp-core-runner
description: Orchestrate complete PRP workflow from feature request to pull request. Run create branch, create PRP, execute implementation, commit changes, and create PR in sequence. Use when implementing features using PRP methodology or when user requests full PRP workflow.
---

# PRP Core Workflow Runner

Run the 5 PRP skills in sequence. Stop on first failure.

## Pipeline

### Step 1: Create Branch
Run the `prp-commit` skill to create a conventional branch name from the feature description.
- Branch format: `feat/short-description` or `fix/short-description`
- Must be on a clean working tree

### Step 2: Create Plan
Run the `prp-plan` skill with the feature description.
- Produces `.plan.md` in the PRPs directory
- Includes codebase exploration, gap analysis, and implementation steps

### Step 3: Execute Implementation
Run the `prp-implement` skill pointing to the plan from Step 2.
- Implements each task from the plan
- Runs validation after every change
- Fixes failures immediately before moving on

### Step 4: Commit Changes
Run the `prp-commit` skill to create an atomic commit.
- Stages files by logical context
- Writes conventional commit message (type/scope/description)

### Step 5: Create PR
Run the `prp-pr` skill to push and open a pull request.
- Auto-detects base branch
- Uses repository PR template if available
- Writes summary from committed changes

## Error Handling

- **Stop immediately** if any step fails — do NOT proceed to the next step
- Report which step failed, the error, and actionable guidance
- Do not attempt to auto-fix complex validation failures

## When to Use

- User requests "implement a feature using PRP" or "run the full PRP workflow"
- User wants end-to-end automation from feature idea to pull request
- User mentions both "PRP" and a feature to implement

Do NOT use when the user only wants a single step (plan, implement, commit, or PR individually).
