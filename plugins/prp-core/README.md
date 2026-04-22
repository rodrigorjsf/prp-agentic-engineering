# PRP Core Plugin

`prp-core` is the installable Claude Code plugin in this repository. It packages the PRP (Product Requirements → Plan → Implement → Validate) workflow as skills, agents, rules, hooks, and reference files.

## What ships in the plugin

| Artifact type | Count | Location |
| --- | --- | --- |
| Skills | 17 | `skills/` |
| Agents | 12 | `agents/` |
| Rules | 2 | `rules/` |
| Stop hooks | 2 | `hooks/` (registered via `hooks/hooks.json`) |
| References | 5 | `references/` |

## Workflow overview

The PRP pipeline runs in four phases. Each phase requires a durable artifact before the next begins.

```
Feature idea / Issue / Question
        ↓
[Research]   prp-prd / prp-codebase-question / prp-research-team / prp-debug
        ↓ .prd.md / .issues/*.md
[Plan]       prp-plan / prp-issue-investigate  →  prp-advisor (gate)
        ↓ .plan.md
[Implement]  prp-implement / prp-ralph / prp-issue-fix  →  prp-verification-before-completion (gate)
        ↓ reports/*.md
[Ship]       prp-commit  →  prp-pr
```

Parallel review runs independently: `prp-review` / `prp-review-agents` → `.claude/PRPs/reviews/*.md`.

## Skills

### Planning and execution

**`prp-prd`** — Research and produce a PRD from a feature idea.
- **Why**: Establishes goal, business value, user-visible behavior, and technical context before any planning or code begins.
- **Produces**: `.claude/PRPs/prds/<feature>.prd.md`
- **Connects to**: → `prp-plan` (next phase), ← `prp-advisor` (pre-work gate)

**`prp-plan`** — Create an implementation plan from a PRD or direct request.
- **Why**: Turns research findings into actionable phases, task lists, and executable validation commands. Separates planning context from implementation context.
- **Produces**: `.claude/PRPs/plans/<feature>.plan.md`
- **Connects to**: ← `prp-prd` (upstream artifact), → `prp-implement` (next phase), → `plan-critic` agent (review gate)

**`prp-implement`** — Execute a `.plan.md` file with per-step validation.
- **Why**: Mechanical execution in a clean, plan-scoped context. Delegates noisy work to subagents. Archives the plan on completion.
- **Produces**: `.claude/PRPs/reports/<feature>-report.md`; moves plan to `plans/completed/`
- **Connects to**: ← `prp-plan` (upstream artifact), → `prp-verification-before-completion` (gate), → `prp-commit`, → `prp-pr`

**`prp-ralph`** — Start an autonomous iterative loop over a plan.
- **Why**: Enables fully autonomous multi-iteration execution. The stop hook is the control boundary — Ralph keeps running until all validations pass or the iteration limit is hit.
- **Produces**: `.claude/prp-ralph.state.md` (active loop state)
- **Connects to**: → `prp-ralph-stop.sh` hook (control boundary), ↔ `prp-ralph-loop` (iteration logic), → `prp-ralph-cancel`

**`prp-ralph-cancel`** — Cancel an active Ralph loop.
- **Why**: Safety escape hatch when you need to interrupt an autonomous loop without losing partial work.
- **Produces**: Removes `.claude/prp-ralph.state.md`; preserves modified files and existing commits
- **Connects to**: ↔ `prp-ralph` (active loop state)

**`prp-ralph-loop`** — Internal iteration logic for active Ralph loops.
- **Why**: Activated automatically when `.claude/prp-ralph.state.md` exists. Executes the next plan iteration and applies the completion protocol.
- **Produces**: Updated state file per iteration
- **Connects to**: ← `prp-ralph-stop.sh` hook (guards each iteration), ↔ `prp-ralph` (state file)

### Issues and debugging

**`prp-issue-investigate`** — Investigate a GitHub issue and produce an implementation plan artifact.
- **Why**: Structures analysis into a durable, reviewable artifact before any code changes. Separates investigation context from implementation context.
- **Produces**: `.claude/PRPs/issues/issue-<number>-<slug>.md`
- **Connects to**: ← GitHub issue (input), → `prp-issue-fix` (downstream executor), ← `prp-advisor` (pre-work gate)

**`prp-issue-fix`** — Implement a fix from an issue investigation artifact.
- **Why**: Clean implementation context after investigation is complete and documented. Ensures changes are grounded in the investigation artifact.
- **Produces**: Code changes; moves issue artifact to `issues/completed/`
- **Connects to**: ← `prp-issue-investigate` (upstream artifact), → `prp-verification-before-completion` (gate), → `prp-commit`, → `prp-pr`

**`prp-debug`** — Root-cause analysis using the 5 Whys technique.
- **Why**: Prevents surface-level fixes by identifying the specific code or config that, if changed, prevents the issue from recurring.
- **Produces**: Analysis report with root cause and fix recommendation
- **Connects to**: → feeds findings into `prp-issue-investigate` or `prp-plan`

### Research

**`prp-codebase-question`** — Answer codebase questions through systematic parallel exploration.
- **Why**: Runs exploration in isolated subagent contexts to prevent research noise from polluting the parent agent's context. Returns only a compact, structured answer.
- **Produces**: Condensed research summary (in-context; no artifact file)
- **Connects to**: → feeds into `prp-plan` or user decision points

**`prp-research-team`** — Design a dynamic research team and plan.
- **Why**: Orchestrates multiple parallel specialist agents for complex cross-cutting research. The stop hook validates output structure so it is always complete.
- **Produces**: Structured research plan with 6 required sections
- **Connects to**: → `prp-research-team-stop.sh` hook (output validator), → feeds into `prp-prd` or `prp-plan`

### Review

**`prp-review`** — Comprehensive PR code review.
- **Why**: Validates changes against project patterns locally before posting. Documents findings in a durable artifact for audit and iteration.
- **Produces**: `.claude/PRPs/reviews/pr-<number>-review.md`
- **Connects to**: ← open PR (input), → `code-reviewer`, `silent-failure-hunter` agents

**`prp-review-agents`** — Multi-aspect PR review using parallel specialized agents.
- **Why**: Runs independent specialist agents (tests, errors, types, docs, security) in isolated contexts and surfaces only high-signal findings.
- **Produces**: Structured findings per aspect
- **Connects to**: ← open PR (input), → `code-reviewer`, `pr-test-analyzer`, `silent-failure-hunter`, `type-design-analyzer`, `docs-impact-agent`, `comment-analyzer`

**`prp-verification-before-completion`** — Final validation gate before claiming work is complete.
- **Why**: Required back-pressure mechanism. Forces deterministic proof (test output, build output) before any completion claim. Enforced by the `prp-workflow` rule.
- **Produces**: No artifact; blocks phase completion until validation evidence is produced
- **Connects to**: → required before `prp-commit` at each phase; enforced by `prp-workflow` rule

### Advisor

**`prp-advisor`** — Call the advisor before substantive work.
- **Why**: Catches design flaws at the highest-leverage moment — before code is written. Detects the native advisor tool if available; falls back to the `prp-advisor` subagent.
- **Produces**: Advisory critique (in-context; no artifact file)
- **Connects to**: → called before any `*.prd.md` or `*.plan.md` is created; ↔ `prp-advisor` agent (fallback backend)

### Git workflow

**`prp-commit`** — Create atomic commits by logical scope following Conventional Commits.
- **Why**: Keeps git history tied to plan phases. Groups changes by logical scope rather than bulk-staging everything at once.
- **Produces**: One commit per logical scope in the diff
- **Connects to**: ← `prp-implement`, `prp-issue-fix` (trigger points), → `prp-pr`

**`prp-pr`** — Create a pull request from the current branch.
- **Why**: Standardizes PR creation with template usage, auto-detects base branch, and validates git state before pushing.
- **Produces**: GitHub pull request
- **Connects to**: ← `prp-commit` (must precede); hard gate enforced by `prp-workflow` rule: plan must be archived first

## Agents

Agents are spawned by skills in isolated subagent contexts. Each receives a condensed brief, completes one job, and returns compact output. Every agent belongs to one component class defined in `references/harness-taxonomy.md`.

| Agent | Class | Role | Invoked by |
| --- | --- | --- | --- |
| `code-reviewer` | Advisory | Reviews code for guideline compliance, bugs, and quality. High-confidence issues only. | `prp-review`, `prp-review-agents` |
| `code-simplifier` | Advisory | Identifies simplification opportunities in recently changed code. Advisory only. | `prp-review-agents` |
| `codebase-analyst` | Advisory | Traces implementation details and data flow with `file:line` references. | `prp-plan`, `prp-implement` |
| `codebase-explorer` | Advisory | Finds where code lives and shows how it is implemented. Combines search with pattern extraction. | `prp-plan`, `prp-codebase-question` |
| `comment-analyzer` | Advisory | Verifies that code comments match actual code behavior. Advisory only. | `prp-review-agents` |
| `docs-impact-agent` | Advisory | Identifies stale docs and missing entries for new user-facing features. Advisory only. | `prp-review-agents` |
| `plan-critic` | Advisory | Reviews PRP plans for completeness, coherence, and blind spots before generation. | `prp-plan`, `prp-implement` |
| `pr-test-analyzer` | Advisory | Analyzes PR test coverage for behavioral completeness, not line metrics. | `prp-review-agents` |
| `prp-advisor` | Advisory | Advisory subagent backing the `prp-advisor` skill when the native advisor tool is unavailable. | `prp-advisor` skill |
| `silent-failure-hunter` | Advisory | Hunts for swallowed errors, inadequate error handling, and inappropriate fallbacks. | `prp-review`, `prp-review-agents` |
| `type-design-analyzer` | Advisory | Analyzes type design for encapsulation, invariant expression, and enforcement quality. | `prp-review-agents` |
| `web-researcher` | Advisory | Searches for current documentation, APIs, and best practices beyond training data. | `prp-plan`, `prp-codebase-question`, `prp-research-team` |

## Rules

The plugin ships two path-scoped execution rules in `rules/`.

**`prp-workflow`** — Enforces the full PRP lifecycle for `*.prd.md` and `*.plan.md` files.
- Fires when a PRD or plan file is open.
- Enforces: GitHub issue creation after PRD/plan creation, `prp-verification-before-completion` at each phase, `prp-commit` after each phase, and `prp-pr` only after plan is archived.
- **Why it ships**: End users executing PRP workflows need this lifecycle enforcement. Without it, phases get skipped and artifacts drift.

**`harness-engineering`** — Enforces harness engineering principles during PRP execution.
- Fires when `.claude/**/*.md`, `*.prd.md`, or `*.plan.md` files are open.
- Enforces: Smart Zone context budget (three tiers), subagent isolation, artifact discipline, and progressive disclosure.
- **Why it ships**: Plugin users need the same smart-zone and compaction discipline as contributors. Context budget violations degrade reasoning quality for all users.

## Hooks

Plugin installs register both Stop hooks automatically through `hooks/hooks.json`. They fire when Claude Code attempts to stop or exit.

**`prp-ralph-stop.sh`** — Controls Ralph loop continuation.
- Checks `.claude/prp-ralph.state.md` on each Stop event.
- Blocks exit while an active Ralph loop is running and has remaining iterations.
- **Why it ships**: Without this hook, Ralph cannot maintain autonomous execution across Stop events. The hook is the control boundary that keeps the loop alive.

**`prp-research-team-stop.sh`** — Validates generated research plans.
- Checks `.claude/prp-research-team.state` on each Stop event.
- Blocks exit unless the research plan contains all 6 required sections: `Research Question`, `Research Question Decomposition`, `Team Composition`, `Research Tasks`, `Team Orchestration Guide`, `Acceptance Criteria`.
- **Why it ships**: Without this gate, the `prp-research-team` skill can silently produce incomplete plans. The hook is the structural completeness contract.

If you install the plugin, you do **not** need to add those hooks manually to your settings. Manual hook setup only applies when you copy the repo-local `.claude/` mirror yourself.

## References

The `references/` directory contains authoritative policy documents. Skills and agents link to these instead of duplicating policy inline. When two components disagree about a policy, the reference file wins.

**`harness-taxonomy.md`** — Component class definitions: artifact / advisory / utility.
- **Why**: Every skill and agent belongs to exactly one class. Class membership determines context profile, brief size limits, and whether the component can modify files.
- **Used by**: All skills and agents to understand their execution contract.

**`context-budget-policy.md`** — Smart-zone thresholds, brief size limits, and compaction rules.
- **Why**: Context bloat degrades reasoning quality. This policy is the single source of truth for when to compact, when to delegate, and what the brief size limits are.
- **Used by**: All skills at each phase handoff; governs when to fork a subagent.

**`execution-policy.md`** — Four delegation modes: inline / subagent / parallel / harness.
- **Why**: Without clear delegation rules, skills do too much work inline and pollute context with exploration noise. This policy defines when work stays inline vs. goes to a subagent.
- **Used by**: Any skill or agent deciding whether to fork a subagent or stay inline.

**`artifact-lifecycle.md`** — PRP artifact locations, naming conventions, and archival rules.
- **Why**: Artifact paths must be consistent across skills so downstream skills can find upstream artifacts. This is the authoritative path table.
- **Used by**: All artifact-producing skills (`prp-prd`, `prp-plan`, `prp-implement`, `prp-issue-investigate`, `prp-review`).

**`agent-prompt-style.md`** — One-job CRITICAL declaration, DO NOT boundaries, output format contract.
- **Why**: Agents without explicit one-job boundaries expand scope and waste context. This style guide makes agent contracts testable and repeatable.
- **Used by**: Any new or modified agent prompt; enforced by the `harness-engineering` rule.

## Artifacts written by the skills

```text
.claude/PRPs/
├── prds/                    ← PRDs created by prp-prd
├── plans/                   ← Plans created by prp-plan
│   └── completed/           ← Archived by prp-implement after execution
├── reports/                 ← Execution reports from prp-implement
├── issues/                  ← Investigation artifacts from prp-issue-investigate
│   └── completed/           ← Archived by prp-issue-fix after fix
└── reviews/                 ← Review artifacts from prp-review
```

Runtime loop state (active only; not archived):

```text
.claude/
├── prp-ralph.state.md           ← Active Ralph loop state (removed by prp-ralph-cancel)
└── prp-research-team.state      ← Active research-team validation state
```

## Plugin vs. repo-local extras

The root repository also contains a `.claude/` mirror for development. These assets are **not** part of the `prp-core` plugin package:

- `.claude/skills/prp-core-runner/`
- `.claude/skills/update-review-instructions/`
- `.claude/agents/gpui-researcher.md`

If you need those extras, use the repo-local mirror intentionally. Do not assume they are included in plugin installs.

## Installation

### Option 1: Install from GitHub marketplace source

```bash
/plugin marketplace add rodrigorjsf/prp-agentic-engineering
/plugin install prp-core@prp-engineering-marketplace
```

### Option 2: Install through the Claude Code plugin API

Add this to project-level `.claude/settings.json` or global `~/.claude/settings.json`:

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

This is the right option for shared setup and automatic enablement.

### Option 3: Install from a local checkout

```bash
git clone https://github.com/rodrigorjsf/prp-agentic-engineering.git
cd prp-agentic-engineering

/plugin marketplace add /absolute/path/to/prp-agentic-engineering
/plugin install prp-core@prp-engineering-marketplace
```

Cloning the repository alone does not activate the plugin.

## Using the plugin

In Claude Code, use the skill names directly in your request.

### Large feature flow

```text
Run the prp-prd skill for "user authentication system"
Run the prp-plan skill with .claude/PRPs/prds/user-auth.prd.md
Run the prp-implement skill with .claude/PRPs/plans/user-auth-phase-1.plan.md
```

### Direct plan flow

```text
Run the prp-plan skill for "add pagination to the API"
Run the prp-implement skill with .claude/PRPs/plans/add-pagination.plan.md
```

### Issue flow

```text
Run the prp-issue-investigate skill for issue 123
Run the prp-issue-fix skill for issue 123
```

### Review flow

```text
Run the prp-review skill for PR 123
Run the prp-review-agents skill for PR 123 with all aspects
```

## Requirements

- Claude Code with plugin support
- Git
- GitHub CLI (`gh`) for PR creation workflows

## Troubleshooting

### Plugin not loading

```bash
/plugin uninstall prp-core@prp-engineering-marketplace
/plugin install prp-core@prp-engineering-marketplace
```

### Skills not found

Make sure Claude Code has reloaded the plugin after installation or after a settings change.

## Support

- **Repository**: https://github.com/rodrigorjsf/prp-agentic-engineering
- **Issues**: https://github.com/rodrigorjsf/prp-agentic-engineering/issues

## License

MIT
