# PRP Plugin — Getting Started

**PRP** automates the hardest part of AI-assisted coding: knowing what to do before writing code. Install the plugin once, then use plain-English skill commands in Claude Code to plan features, fix bugs, review PRs, and ship clean commits — with every decision saved as a file your whole team can read.

---

## The core idea in one sentence

You describe what you want; PRP researches your codebase, makes a plan, implements it, validates it, and opens the PR — without you babysitting each step.

---

## Install in 30 seconds

Open Claude Code and run:

```bash
/plugin marketplace add rodrigorjsf/prp-agentic-engineering
/plugin install prp-core@prp-engineering-marketplace
```

That's it. The skills activate immediately.

---

## The mental model

PRP follows a linear pipeline. Each step produces a file. The next step reads that file.

```
Idea → PRD spec → Plan → Implementation → Commit → PR → Review
```

You can enter the pipeline at any step. Already have a spec? Skip to `prp-plan`. Already have a plan? Skip to `prp-implement`. Already have code ready to ship? Jump to `prp-commit`.

---

## What each skill does

### When you have an idea but no spec

**`prp-prd`** interviews you about your idea before writing anything. It asks what problem you're solving, who needs it, and what success looks like. Then it writes a structured spec file.

```text
Run the prp-prd skill for "let users export their data as CSV"
```

Produces: `.claude/PRPs/prds/csv-export.prd.md`

---

### When you have a spec and need a plan

**`prp-plan`** reads your codebase, finds where the relevant code lives, and writes a step-by-step implementation plan grounded in your existing patterns. It writes no code — only the plan.

```text
Run the prp-plan skill with .claude/PRPs/prds/csv-export.prd.md
```

Or skip the PRD entirely if the feature is clear:

```text
Run the prp-plan skill for "add CSV export to the user dashboard"
```

Produces: `.claude/PRPs/plans/csv-export.plan.md`

---

### When you have a plan and want to build

**`prp-implement`** executes the plan file. After each change, it runs your tests, linter, and type checker. If something breaks, it fixes it before moving on. When done, it archives the plan and writes a summary report.

```text
Run the prp-implement skill with .claude/PRPs/plans/csv-export.plan.md
```

---

### When you want fully hands-off execution

**`prp-ralph`** runs `prp-implement` in a loop. It keeps iterating — implement, validate, fix, repeat — until all checks pass or it hits the iteration limit. You start it and check back when it finishes.

```text
Run the prp-ralph skill with .claude/PRPs/plans/csv-export.plan.md --max-iterations 20
```

Stop it anytime:

```text
Run the prp-ralph-cancel skill
```

---

### When a bug arrives as a GitHub issue

**`prp-issue-investigate`** fetches the issue, traces the affected code, finds the root cause, and writes an investigation plan. It also posts a comment on the issue so your team sees the findings.

```text
Run the prp-issue-investigate skill for issue 234
```

Then fix it:

**`prp-issue-fix`** reads the investigation plan, implements the fix, opens a PR linked to the issue, and posts a self-review.

```text
Run the prp-issue-fix skill for issue 234
```

---

### When you have an error and don't know why

**`prp-debug`** applies root-cause analysis to find the specific code that causes the problem. It asks "why?" five times before proposing a fix, so it addresses the cause — not the symptom.

```text
Run the prp-debug skill for "TypeError: Cannot read property 'id' of undefined in checkout.js:42"
Run the prp-debug skill for "flaky test: UserService.create fails intermittently" --quick
```

---

### When you need to understand your codebase

**`prp-codebase-question`** answers questions about how your code works, with every answer backed by file and line references. It never suggests changes — it only documents what exists.

```text
Run the prp-codebase-question skill for "how does our payment retry logic work?"
Run the prp-codebase-question skill for "where is user input sanitized?"
```

---

### When you're ready to commit

**`prp-commit`** looks at your changes, groups related files into logical units, and creates one conventional commit per group. No `git add .`, no mixed concerns in a single commit.

```text
Run the prp-commit skill
```

---

### When you're ready to open a PR

**`prp-pr`** detects the base branch, writes a PR description summarizing your changes, and opens the PR on GitHub.

```text
Run the prp-pr skill
```

---

### When you want a code review

**`prp-review`** reviews the PR like a senior engineer: checks code against project patterns, runs validation, categorizes issues by severity, and posts the review on GitHub.

```text
Run the prp-review skill for PR 123
Run the prp-review skill for PR 123 --approve
```

For deeper coverage, use the multi-agent review:

```text
Run the prp-review-agents skill for PR 123 with all aspects
```

This runs specialized agents for test coverage, error handling, type design, documentation impact, and code simplification — all in parallel.

---

## Common workflows

### Build a new feature from scratch

```text
Run the prp-prd skill for "real-time notifications"
Run the prp-plan skill with .claude/PRPs/prds/real-time-notifications.prd.md
Run the prp-implement skill with .claude/PRPs/plans/real-time-notifications-phase-1.plan.md
Run the prp-commit skill
Run the prp-pr skill
```

### Fix a reported bug

```text
Run the prp-issue-investigate skill for issue 789
Run the prp-issue-fix skill for issue 789
```

### Ship a quick change

```text
Run the prp-plan skill for "rename the config file from .env to .env.local"
Run the prp-implement skill with .claude/PRPs/plans/rename-config.plan.md
Run the prp-commit skill
Run the prp-pr skill
```

### Review a teammate's PR

```text
Run the prp-review-agents skill for PR 42 with tests errors docs
```

---

## Where files get saved

Every skill saves its output to `.claude/PRPs/` inside your project:

```text
.claude/PRPs/
├── prds/          ← specs from prp-prd
├── plans/         ← plans from prp-plan
│   └── completed/ ← archived after prp-implement finishes
├── reports/       ← implementation summaries and research
├── issues/        ← investigation plans from prp-issue-investigate
│   └── completed/ ← archived after prp-issue-fix finishes
└── reviews/       ← review reports from prp-review
```

These files are plain markdown. Commit them. Future AI sessions read them directly, so you never re-explain your decisions.

---

## Quick reference

| I want to… | Skill to use |
|-----------|-------------|
| Turn an idea into a spec | `prp-prd` |
| Plan a feature | `prp-plan` |
| Implement a plan | `prp-implement` |
| Run autonomously until done | `prp-ralph` |
| Stop an autonomous loop | `prp-ralph-cancel` |
| Investigate a GitHub issue | `prp-issue-investigate` |
| Fix an investigated issue | `prp-issue-fix` |
| Understand a bug's root cause | `prp-debug` |
| Understand how my code works | `prp-codebase-question` |
| Create clean commits | `prp-commit` |
| Open a PR with a description | `prp-pr` |
| Review a PR | `prp-review` |
| Deep multi-agent PR review | `prp-review-agents` |
