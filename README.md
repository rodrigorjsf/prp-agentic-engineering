# PRP Framework for Claude Code

**PRP** (Product Requirements + Plans) is an AI-powered workflow automation plugin for Claude Code. It turns vague feature requests into production-ready code through structured planning, autonomous execution, and multi-agent review — with every decision documented in version-controlled artifacts.

## What problem PRP solves

AI coding sessions often fail for a predictable reason: the model starts implementing before it understands the codebase, the requirements, or the constraints. The result is code that works in isolation but breaks existing patterns, misses edge cases, or requires a complete rewrite.

PRP solves this by enforcing a **plan-first, evidence-first discipline**:

1. **Research before building** — PRP reads your codebase, gathers context, and validates assumptions before writing a single line.
2. **Artifacts over chat** — every plan, spec, and review is saved as a markdown file. Work survives context resets, is reviewable by humans, and feeds the next AI session without re-explaining everything.
3. **Validation loops** — every implementation step runs linters, tests, and type checks before moving on. Broken state never accumulates.

The methodology: **PRP = PRD + curated codebase intelligence + agent runbook**. That combination enables one-pass implementation — no back-and-forth, no mid-implementation surprises.

---

## Installation

### Option 1: Install from the GitHub marketplace (recommended)

```bash
/plugin marketplace add rodrigorjsf/prp-agentic-engineering
/plugin install prp-core@prp-engineering-marketplace
```

### Option 2: Declare in `settings.json` for team or reproducible installs

Add to your project-level `.claude/settings.json` or global `~/.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "prp-engineering-marketplace": {
      "source": "rodrigorjsf/prp-agentic-engineering"
    }
  },
  "enabledPlugins": [
    "prp-core@prp-engineering-marketplace"
  ]
}
```

This path works for team bootstrap and managed installs, because the plugin activates automatically when Claude Code loads the settings file.

### Option 3: Install from a local checkout

```bash
git clone https://github.com/rodrigorjsf/prp-agentic-engineering.git
/plugin marketplace add /absolute/path/to/prp-agentic-engineering
/plugin install prp-core@prp-engineering-marketplace
```

Cloning the repository alone does **not** install the plugin. You must register the marketplace entry and run the install command.

---

## Skills

Skills are the primary interface. Invoke them by name in Claude Code: `run the prp-plan skill for "add pagination to the API"`.

### Planning and specification

#### `prp-prd` — Product Requirements Document generator

Runs an interactive, problem-first interview before writing any spec. Asks clarifying questions, gathers evidence, validates feasibility, and produces a structured `.prd.md` file.

**Use when**: you have an idea but not a spec. The skill prevents you from building the wrong thing by demanding evidence before committing to a solution.

```text
Run the prp-prd skill for "real-time notifications"
Run the prp-prd skill  # starts with open questions
```

**Output**: `.claude/PRPs/prds/<feature>.prd.md` — a structured spec with goals, user stories, constraints, and implementation phases.

---

#### `prp-plan` — Feature implementation planner

Reads the codebase first, researches gaps second, and produces a detailed `.plan.md` before any code changes. The plan includes a task breakdown, validation commands, file references, and implementation notes grounded in existing patterns.

**Use when**: you have a spec or a clear feature description and need a battle-tested plan. The skill writes no code — it only produces the plan document.

```text
Run the prp-plan skill for "add rate limiting to the API"
Run the prp-plan skill with .claude/PRPs/prds/notifications.prd.md
```

**Output**: `.claude/PRPs/plans/<feature>.plan.md` — a phased implementation plan with explicit tasks, test commands, and codebase references.

---

#### `prp-implement` — Plan executor with validation loops

Executes a `.plan.md` file end-to-end. After each change, it runs linters, tests, and type checks. When a check fails, it fixes the failure before proceeding. On completion, it generates a summary report and archives the plan.

**Use when**: you have a plan and want autonomous, validated execution with no accumulated broken state.

```text
Run the prp-implement skill with .claude/PRPs/plans/rate-limiting.plan.md
Run the prp-implement skill with .claude/PRPs/plans/auth.plan.md --base main
```

**Output**: code changes on a feature branch + `.claude/PRPs/reports/<feature>.report.md`.

---

### Autonomous execution

#### `prp-ralph` — Autonomous iteration loop

Starts a loop that executes a plan, validates results, and re-iterates until all checks pass or the iteration limit is reached. Each iteration is a separate Claude Code session invoked by a Stop hook — the loop persists even through context resets.

**Use when**: you want fully hands-off execution. Start the loop and check back when it completes.

```text
Run the prp-ralph skill with .claude/PRPs/plans/feature.plan.md
Run the prp-ralph skill with .claude/PRPs/plans/feature.plan.md --max-iterations 30
```

**Output**: committed code changes, per-iteration progress logs in `.claude/prp-ralph.state.md`.

---

#### `prp-ralph-cancel` — Loop cancellation

Stops an active Ralph loop gracefully. Reads the state file, reports the current iteration, removes the state file, and preserves all work-in-progress commits.

**Use when**: you need to interrupt an autonomous loop to redirect it or inspect its current state.

```text
Run the prp-ralph-cancel skill
```

---

### Issue workflow

#### `prp-issue-investigate` — Issue investigator

Fetches a GitHub issue, analyzes the codebase to understand the affected code paths, identifies the root cause, and produces a complete implementation plan artifact. Posts findings as a GitHub comment so the investigation is visible to the whole team.

**Use when**: a bug or feature request arrives as a GitHub issue and you want a structured investigation before writing any fix.

```text
Run the prp-issue-investigate skill for issue 456
Run the prp-issue-investigate skill for https://github.com/org/repo/issues/456
```

**Output**: `.claude/PRPs/issues/<issue>.issue.md` — an implementation plan ready for `prp-issue-fix`.

---

#### `prp-issue-fix` — Issue fixer

Loads an investigation artifact produced by `prp-issue-investigate`, implements the fix, runs validation, opens a PR linked to the issue, performs a self-review, and archives the artifact.

**Use when**: the investigation is complete and you want the fix implemented and the PR opened automatically.

```text
Run the prp-issue-fix skill for issue 456
Run the prp-issue-fix skill with .claude/PRPs/issues/456-auth-crash.issue.md
```

---

#### `prp-debug` — Root cause analyzer

Applies the 5 Whys technique to find the specific code or configuration that, if changed, would prevent the issue. Distinguishes root causes from symptoms. Supports `--quick` for a fast surface scan.

**Use when**: you have an error, a stack trace, or a failing test and need to understand why it happens before touching code.

```text
Run the prp-debug skill for "NullPointerException in UserService line 84"
Run the prp-debug skill for "tests pass locally but fail in CI" --quick
```

---

### Research

#### `prp-codebase-question` — Codebase research assistant

Spawns parallel specialized agents to answer questions about the codebase. Every finding includes a `file:line` reference. The skill documents what exists — it does not suggest improvements or propose changes.

**Use when**: you need to understand how something works before modifying it, or you want a documented answer to share with the team.

```text
Run the prp-codebase-question skill for "how does authentication work?"
Run the prp-codebase-question skill for "where is rate limiting enforced?" --web
```

**Output**: `.claude/PRPs/reports/<question>.research.md` — a factual, referenced research document.

---

#### `prp-research-team` — Research team planner

Designs a dynamic team of specialized research agents and a structured research plan. The team composition adapts to the research question. Produces an executable plan document — no research is executed, only planned.

**Use when**: the research question is complex enough to benefit from multiple specialized agents working in parallel, and you want a plan to review before committing to the full investigation.

```text
Run the prp-research-team skill for "how should we migrate from REST to GraphQL?"
Run the prp-research-team skill for "evaluate authentication libraries for our stack"
```

---

### Review

#### `prp-review` — Pull request reviewer

Fetches the PR, checks the code against project patterns, runs all validation locally, categorizes issues by severity (critical / major / minor / nitpick), and posts the review to GitHub. Supports `--approve` and `--request-changes` to close the review loop.

**Use when**: you want a senior-engineer-level review on a PR before merging.

```text
Run the prp-review skill for PR 123
Run the prp-review skill for PR 123 --approve
Run the prp-review skill for PR 123 --request-changes
```

**Output**: GitHub review comment + `.claude/PRPs/reviews/<pr>.review.md`.

---

#### `prp-review-agents` — Multi-agent PR review

Runs the same PR through a panel of specialized review agents, each focused on a distinct quality dimension. Always runs the code quality check; activates additional agents based on what the PR changes.

| Aspect flag | Agent activated | Focus |
|-------------|----------------|-------|
| `comments` | `comment-analyzer` | Comment accuracy and rot |
| `tests` | `pr-test-analyzer` | Behavioral test coverage |
| `errors` | `silent-failure-hunter` | Swallowed errors and bad fallbacks |
| `types` | `type-design-analyzer` | Type invariants and encapsulation |
| `docs` | `docs-impact-agent` | Stale or missing documentation |
| `simplify` | `code-simplifier` | Clarity and maintainability |
| `all` | All of the above | Full panel review |

**Use when**: you want comprehensive coverage across multiple quality dimensions, especially before merging significant changes.

```text
Run the prp-review-agents skill for PR 123 with all aspects
Run the prp-review-agents skill for PR 123 with tests errors
```

---

### Advisor

#### `prp-advisor` — Pre-work advisor gate

Checks whether the native `advisor` tool is available and routes to it; falls back to the `prp-core:prp-advisor` subagent when the native tool is not configured. Either way, it delivers a concise, enumerated review of your current approach before substantive work begins.

**Use when**: before writing any spec, plan, or code — before committing to an interpretation, and before declaring a task complete. The prp-workflow rule enforces this gate automatically for PRD and plan artifacts.

```text
Run the prp-advisor skill
```

---

### Validation

#### `prp-verification-before-completion` — Completion gate

Verifies that all validation criteria from the plan pass before the plan is archived. Called automatically by `prp-implement` as Phase 4.6, immediately after all technical checks and before any report is written or the plan is moved to `completed/`.

**Use when**: before declaring any implementation phase done. If this gate fails, fix the failures before proceeding.

```text
Run the prp-verification-before-completion skill
```

---

### Git workflow

#### `prp-commit` — Atomic commit builder

Analyzes all staged and unstaged changes, groups them into independent logical units, and creates one conventional commit per group. Never uses `git add -A`. Commit messages conform to [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

**Use when**: you have changes across multiple files and want clean, atomic commits that reviewers and `git log` readers can understand.

```text
Run the prp-commit skill
Run the prp-commit skill for src/auth/
```

---

#### `prp-pr` — Pull request creator

Detects the base branch, validates git state, checks for a PR template, writes a summary of changes, and opens the PR. Pushes the branch if needed.

**Use when**: your feature branch is ready and you want the PR opened with a proper description.

```text
Run the prp-pr skill
Run the prp-pr skill --base develop
```

---

## Agents

Agents are specialized subprocesses invoked by skills during research, review, and implementation. You can also invoke them directly.

| Agent | Responsibility | Use directly when |
|-------|---------------|-------------------|
| `code-reviewer` | Reviews code against project guidelines; reports high-confidence issues only (80+) | After writing code, before committing |
| `code-simplifier` | Identifies simplification opportunities while preserving functionality; advisory only | After implementing a feature |
| `codebase-analyst` | Traces data flow and documents technical workings with `file:line` references | Before modifying unfamiliar code |
| `codebase-explorer` | Locates files, extracts code patterns, and shows concrete examples in one pass | When exploring a new area of the codebase |
| `comment-analyzer` | Verifies comments match actual code behavior; flags outdated or misleading comments | Before PRs that change documented code |
| `docs-impact-agent` | Identifies stale docs and missing entries for new features; advisory only | After adding user-facing features |
| `plan-critic` | Reviews PRP artifacts for completeness, coherence, and blind spots before implementation | Before executing a plan |
| `pr-test-analyzer` | Evaluates behavioral test coverage quality; rates gaps by criticality (1–10) | After creating a PR |
| `prp-advisor` | Delivers a concise enumerated review of your approach; backed by a stronger reviewer model | Before substantive work and before declaring done |
| `silent-failure-hunter` | Hunts swallowed errors, inadequate error handling, and inappropriate fallbacks | After implementing error handling |
| `type-design-analyzer` | Rates type design on encapsulation, invariant expression, and enforcement quality | When introducing or refactoring types |
| `web-researcher` | Searches the web for current docs, APIs, and best practices; returns cited findings | When your knowledge cutoff matters |

---

## Hooks

The plugin installs two Stop hooks automatically from `plugins/prp-core/hooks/hooks.json`:

- **`prp-ralph-stop.sh`** — keeps an active Ralph loop running when Claude Code would otherwise exit. The hook reads `.claude/prp-ralph.state.md` and re-invokes the loop until it completes or hits the iteration limit.
- **`prp-research-team-stop.sh`** — validates the generated research plan against `.claude/prp-research-team.state` before allowing exit. Blocks premature termination when required sections are missing.

Manual hook configuration is only necessary when you copy the repo-local `.claude/` assets instead of installing the plugin.

---

## Workflow examples

### Build a large feature from scratch

```text
# 1. Define requirements
Run the prp-prd skill for "user authentication system"

# 2. Create implementation plan
Run the prp-plan skill with .claude/PRPs/prds/user-auth.prd.md

# 3. Execute each phase
Run the prp-implement skill with .claude/PRPs/plans/user-auth-phase-1.plan.md
Run the prp-implement skill with .claude/PRPs/plans/user-auth-phase-2.plan.md

# 4. Review and ship
Run the prp-commit skill
Run the prp-pr skill
Run the prp-review skill for PR 123
```

### Autonomous execution of a clear plan

```text
Run the prp-ralph skill with .claude/PRPs/plans/add-pagination.plan.md --max-iterations 20
```

Ralph iterates until all tests pass, then stops. Check the report in `.claude/PRPs/reports/`.

### Investigate and fix a GitHub issue

```text
Run the prp-issue-investigate skill for issue 789
# Review the investigation artifact
Run the prp-issue-fix skill for issue 789
```

### Deep-dive code review before merging

```text
Run the prp-review-agents skill for PR 456 with all aspects
```

---

## Artifacts

The skills write all working artifacts to `.claude/PRPs/` inside your project:

```text
.claude/PRPs/
├── prds/                  # Product requirements documents (.prd.md)
├── plans/                 # Implementation plans (.plan.md)
│   └── completed/         # Archived plans after prp-implement finishes
├── reports/               # Implementation and research reports
├── issues/                # Issue investigation artifacts (.issue.md)
│   └── completed/         # Archived after prp-issue-fix finishes
└── reviews/               # PR review reports (.review.md)
```

Artifacts are plain markdown files. They accumulate over time, forming a project-specific knowledge base that future AI sessions can read directly.

---

## Repository layout

```text
.
├── .claude-plugin/marketplace.json   # Marketplace manifest
├── .claude/                          # Repo-local mirror + project-only extras
│   ├── agents/                       # 14 agents (12 plugin + gpui-researcher + rubber-duck)
│   ├── hooks/                        # Manual Ralph hook setup
│   ├── rules/                        # Path-scoped execution rules (e.g. prp-workflow)
│   └── skills/                       # 19 skills (17 plugin + prp-core-runner, update-review-instructions)
├── plugins/
│   └── prp-core/                     # Installable plugin package (v3.1.2)
│       ├── .claude-plugin/plugin.json
│       ├── agents/                   # 12 agents
│       ├── hooks/                    # 2 Stop hooks
│       ├── rules/                    # 1 path-scoped rule (prp-workflow)
│       └── skills/                   # 17 skills
├── README.md
└── README-for-DUMMIES.md
```

### Repo-local extras not shipped in the plugin

| Asset | Purpose |
|-------|---------|
| `.claude/skills/prp-core-runner/` | Orchestrates the full plan → implement → commit → PR pipeline in one command |
| `.claude/skills/update-review-instructions/` | Generates scoped Copilot review instruction files for `.github/instructions/` |
| `.claude/agents/gpui-researcher.md` | Researches GPUI APIs and validates usage patterns against real-world examples |
| `.claude/agents/rubber-duck.md` | General-purpose critical thinking agent for challenging assumptions and unblocking |

To use these extras, copy or symlink the root `.claude/` directory into your project.

---

## Requirements

- Claude Code with plugin support
- Git
- GitHub CLI (`gh`) — required for PR-oriented skills (`prp-pr`, `prp-review`, `prp-issue-investigate`, `prp-issue-fix`)

## License

MIT
