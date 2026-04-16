# PRP Core Plugin

`prp-core` is the installable Claude Code plugin in this repository. It packages the PRP workflow as skills, agents, and hooks.

## What ships in the plugin

| Artifact | Count | Notes |
| --- | --- | --- |
| Skills | 15 | The installable workflow surface in `skills/` |
| Agents | 11 | Specialized review and analysis agents in `agents/` |
| Stop hooks | 2 | Registered from `hooks/hooks.json` |

## Skills

### Planning and execution

- `prp-prd`
- `prp-plan`
- `prp-implement`
- `prp-ralph`
- `prp-ralph-cancel`
- `prp-ralph-loop`

### Issues and debugging

- `prp-issue-investigate`
- `prp-issue-fix`
- `prp-debug`

### Research and review

- `prp-codebase-question`
- `prp-research-team`
- `prp-review`
- `prp-review-agents`

### Git workflow

- `prp-commit`
- `prp-pr`

## Agents

- `code-reviewer`
- `code-simplifier`
- `codebase-analyst`
- `codebase-explorer`
- `comment-analyzer`
- `docs-impact-agent`
- `plan-critic`
- `pr-test-analyzer`
- `silent-failure-hunter`
- `type-design-analyzer`
- `web-researcher`

## Hooks

Plugin installs register both Stop hooks automatically through `hooks/hooks.json`:

- `${CLAUDE_PLUGIN_ROOT}/hooks/prp-ralph-stop.sh`
- `${CLAUDE_PLUGIN_ROOT}/hooks/prp-research-team-stop.sh`

`prp-ralph-stop.sh` keeps active Ralph loops running until they complete or hit the iteration limit. `prp-research-team-stop.sh` validates the generated research plan through `.claude/prp-research-team.state` and blocks exit until the required sections are present.

If you install the plugin, you do **not** need to add those hooks manually to your settings. Manual hook setup only applies when you copy the repo-local `.claude/` mirror yourself.

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

## Artifacts written by the skills

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
