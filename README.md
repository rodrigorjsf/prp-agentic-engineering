# PRP Framework for Claude Code

This repository is a Claude Code plugin marketplace for PRP workflow automation. It contains the published `prp-core` plugin, a repo-local `.claude/` mirror used during development, and a small set of project-only extras that are not shipped in the plugin package.

## Current repository state

| Path | Purpose | Current state |
| --- | --- | --- |
| `.claude-plugin/marketplace.json` | Marketplace manifest | Publishes `prp-core` from `./plugins/prp-core` as `prp-marketplace` |
| `plugins/prp-core/` | Installable Claude Code plugin | v3.0.0 with **15 skills**, **10 agents**, and **2 Stop hooks** |
| `.claude/skills/` | Repo-local mirror | **17 skills**: the plugin's 15 plus `prp-core-runner` and `update-review-instructions` |
| `.claude/agents/` | Repo-local mirror | **11 agents**: the plugin's 10 plus `gpui-researcher` |
| `.claude/hooks/` | Repo-local manual hook setup | Ralph hook only; the Research Team stop hook exists only inside the plugin package |

## What the `prp-core` plugin ships

### Skills

**Planning and execution**

- `prp-prd`
- `prp-plan`
- `prp-implement`
- `prp-ralph`
- `prp-ralph-cancel`
- `prp-ralph-loop`

**Issues and debugging**

- `prp-issue-investigate`
- `prp-issue-fix`
- `prp-debug`

**Research and review**

- `prp-codebase-question`
- `prp-research-team`
- `prp-review`
- `prp-review-agents`

**Git workflow**

- `prp-commit`
- `prp-pr`

### Agents

- `code-reviewer`
- `code-simplifier`
- `codebase-analyst`
- `codebase-explorer`
- `comment-analyzer`
- `docs-impact-agent`
- `pr-test-analyzer`
- `silent-failure-hunter`
- `type-design-analyzer`
- `web-researcher`

### Hooks

When you install the plugin, Claude Code loads these Stop hooks from `plugins/prp-core/hooks/hooks.json` automatically:

- `prp-ralph-stop.sh`
- `prp-research-team-stop.sh`

`prp-ralph-stop.sh` keeps active Ralph loops running until they complete or hit the iteration limit. `prp-research-team-stop.sh` validates the generated research plan through `.claude/prp-research-team.state` and blocks exit until the required sections are present.

Manual hook configuration is only needed when you copy the repo-local `.claude/` assets instead of installing the plugin.

## Installation

### Option 1: Install from the GitHub marketplace repo

```bash
/plugin marketplace add rodrigorjsf/prp-agentic-engineering
/plugin install prp-core@prp-marketplace
```

This is the normal install path.

### Option 2: Install through the Claude Code plugin API

Add the marketplace and plugin to either your project-level `.claude/settings.json` or your global `~/.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "prp-marketplace": {
      "source": "rodrigorjsf/prp-agentic-engineering"
    }
  },
  "enabledPlugins": [
    "prp-core@prp-marketplace"
  ]
}
```

Use this path for team bootstrap, managed installs, or reproducible local setup.

### Option 3: Install from a local checkout of this repo

```bash
git clone https://github.com/rodrigorjsf/prp-agentic-engineering.git
cd prp-agentic-engineering

/plugin marketplace add /absolute/path/to/prp-agentic-engineering
/plugin install prp-core@prp-marketplace
```

Downloading or cloning the repository by itself does **not** install the plugin. You still need to install it through a marketplace entry or through the Claude Code plugin settings API.

### Repo-local mirror, not plugin install

If you want the root `.claude/` mirror, including the repo-only extras, you must copy or sync those files into your own project manually. That path is meant for development and customization, not as the primary installation method.

## How to use it

In Claude Code, use the skill names directly in your request.

### Large features

```text
Run the prp-prd skill for "user authentication system"
Run the prp-plan skill with .claude/PRPs/prds/user-auth.prd.md
Run the prp-implement skill with .claude/PRPs/plans/user-auth-phase-1.plan.md
```

### Autonomous execution

```text
Run the prp-ralph skill with .claude/PRPs/plans/my-feature.plan.md --max-iterations 20
```

### Bug workflow

```text
Run the prp-issue-investigate skill for issue 123
Run the prp-issue-fix skill for issue 123
```

### Review workflow

```text
Run the prp-review skill for PR 123
Run the prp-review-agents skill for PR 123 with all aspects
```

## Artifacts created by the workflow

The skills write their working artifacts to `.claude/PRPs/` inside the target project:

```text
.claude/PRPs/
├── prds/
├── plans/
│   └── completed/
├── reports/
├── issues/
│   └── completed/
└── reviews/
```

## Repository layout

```text
.
├── .claude-plugin/marketplace.json   # Marketplace manifest for this repo
├── .claude/                          # Repo-local mirror and project-only extras
│   ├── agents/
│   ├── hooks/
│   └── skills/
├── plugins/
│   └── prp-core/
│       ├── .claude-plugin/plugin.json
│       ├── agents/
│       ├── hooks/
│       └── skills/
├── README.md
└── README-for-DUMMIES.md
```

## Repo-local extras that are not in the plugin

These assets exist in the root `.claude/` mirror but are not installed by `prp-core`:

- `.claude/skills/prp-core-runner/`
- `.claude/skills/update-review-instructions/`
- `.claude/agents/gpui-researcher.md`

## Requirements

- Claude Code with plugin support
- Git
- GitHub CLI (`gh`) if you want the PR-oriented skills to open pull requests

## License

MIT
