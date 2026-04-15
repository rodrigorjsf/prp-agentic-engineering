# PRP Plugin for Humans

This repo is not just a folder of prompts anymore. It is a **Claude Code plugin marketplace repo** that publishes the `prp-core` plugin.

## What you actually get

- **Plugin package**: `prp-core`
- **15 plugin skills** for planning, implementation, debugging, review, and Git workflow
- **10 plugin agents** for analysis and review
- **2 automatic Stop hooks** for Ralph and Research Team workflows
- **Repo-only extras** in the root `.claude/` mirror:
  - `prp-core-runner`
  - `update-review-instructions`
  - `gpui-researcher`

## Fastest install

```bash
/plugin marketplace add rodrigorjsf/prp-agentic-engineering
/plugin install prp-core@prp-marketplace
```

That installs the actual plugin.

## Install with the Claude Code plugin API

If you want Claude Code to enable the plugin from config, add this to `.claude/settings.json` or `~/.claude/settings.json`:

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

## Install from a local checkout

```bash
git clone https://github.com/rodrigorjsf/prp-agentic-engineering.git
cd prp-agentic-engineering

/plugin marketplace add /absolute/path/to/prp-agentic-engineering
/plugin install prp-core@prp-marketplace
```

Cloning the repo alone is **not** enough. Claude still needs the marketplace entry or the plugin settings config.

## How to use it

Use the skill names in Claude Code.

### Big feature

```text
Run the prp-prd skill for "user authentication"
Run the prp-plan skill with .claude/PRPs/prds/user-auth.prd.md
Run the prp-implement skill with .claude/PRPs/plans/user-auth-phase-1.plan.md
```

### Medium feature

```text
Run the prp-plan skill for "add pagination to the API"
Run the prp-implement skill with .claude/PRPs/plans/add-pagination.plan.md
```

### Fully autonomous mode

```text
Run the prp-ralph skill with .claude/PRPs/plans/my-feature.plan.md --max-iterations 20
```

### Bug fix

```text
Run the prp-issue-investigate skill for issue 456
Run the prp-issue-fix skill for issue 456
```

### Review and ship

```text
Run the prp-commit skill
Run the prp-pr skill
Run the prp-review skill for PR 123
```

## Where files get saved

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

## The only thing to remember

1. Need a spec first? Use `prp-prd`.
2. Ready to plan? Use `prp-plan`.
3. Ready to build? Use `prp-implement` or `prp-ralph`.
4. Fixing a bug? Use `prp-issue-investigate` and `prp-issue-fix`.
5. Done? Use `prp-commit`, then `prp-pr`.
