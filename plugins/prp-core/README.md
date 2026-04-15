# PRP Core Plugin

Complete PRP (Product Requirement Prompt) workflow automation for Claude Code.

## Overview

This plugin provides a comprehensive workflow for creating, executing, and shipping features using the PRP methodology - where **PRP = PRD + curated codebase intelligence + agent/runbook** designed to enable AI agents to ship production-ready code on the first pass.

## Skills

### Core Workflow

| Skill | Description |
|-------|-------------|
| `prp-core-runner` | Orchestrate full workflow: plan → implement → commit → PR |
| `prp-plan` | Create implementation plan from PRD or free-form input |
| `prp-implement` | Execute a `.plan.md` with validation after every change |
| `prp-prd` | Interactive PRD generator with implementation phases |

### Issue Workflow

| Skill | Description |
|-------|-------------|
| `prp-issue-investigate` | Analyze GitHub issue, create implementation plan |
| `prp-issue-fix` | Execute fix from investigation artifact |

### Research & Analysis

| Skill | Description |
|-------|-------------|
| `prp-research-team` | Multi-agent parallel research for complex topics |
| `prp-codebase-question` | Answer codebase questions with file:line references |
| `prp-debug` | Root cause analysis using 5 Whys technique |

### Git & Review

| Skill | Description |
|-------|-------------|
| `prp-commit` | Smart commit with natural language file targeting |
| `prp-pr` | Create PR with template support |
| `prp-review` | Comprehensive PR code review |
| `prp-review-agents` | Multi-agent PR review (comments, tests, errors, types, code, docs) |

### Autonomous Loops

| Skill | Description |
|-------|-------------|
| `prp-ralph` | Start autonomous iteration loop with validation gates |
| `prp-ralph-cancel` | Cancel active Ralph loop |

## Agents

Specialized agents for code analysis and review workflows.

### Codebase Analysis

| Agent | Description |
|-------|-------------|
| `codebase-analyst` | Documents HOW code works with file:line references |
| `codebase-explorer` | Finds WHERE code lives AND extracts patterns |
| `web-researcher` | Researches web for docs, APIs, best practices |

### Review Workflow

| Agent | Description |
|-------|-------------|
| `code-reviewer` | Project guidelines, bugs, type/module checks |
| `comment-analyzer` | Comment accuracy and maintainability |
| `pr-test-analyzer` | Test coverage quality and gaps |
| `silent-failure-hunter` | Error handling and silent failures |
| `type-design-analyzer` | Type encapsulation and invariants |
| `code-simplifier` | Clarity and maintainability improvements |
| `docs-impact-agent` | Updates stale documentation |

### Using Agents

Agents are invoked automatically by the `prp-review-agents` skill or manually via Task tool:

```
# Run the prp-review-agents skill for PR #123
"run prp-review-agents for PR 123"

# Specific aspects only
"run prp-review-agents for PR 123 - focus on tests and errors"
```

## Workflow

### Large Features: PRD → Plan → Implement

```
Run the prp-prd skill for "user authentication system"
    ↓
Creates PRD with Implementation Phases table
    ↓
Run the prp-plan skill with .claude/PRPs/prds/user-auth.prd.md
    ↓
Auto-selects next pending phase, creates plan
    ↓
Run the prp-implement skill with .claude/PRPs/plans/user-auth-phase-1.plan.md
    ↓
Executes plan, updates PRD progress, archives plan
    ↓
Repeat prp-plan for next phase
```

### Medium Features: Direct to Plan

```
Run the prp-plan skill for "add pagination to the API"
    ↓
Run the prp-implement skill with .claude/PRPs/plans/add-pagination.plan.md
```

### Bug Fixes: Issue Workflow

```
Run the prp-issue-investigate skill for issue #123
    ↓
Run the prp-issue-fix skill for issue #123
```

## Installation

### Option 1: From GitHub (Recommended)

```bash
# Add marketplace from GitHub
/plugin marketplace add Wirasm/PRPs-agentic-eng

# Install plugin
/plugin install prp-core@prp-marketplace
```

### Option 2: Local Development/Testing

```bash
# Navigate to the repository root
cd /path/to/PRPs-agentic-eng

# Start Claude Code
claude

# Add local marketplace (use absolute path)
/plugin marketplace add /absolute/path/to/PRPs-agentic-eng

# Install plugin
/plugin install prp-core@prp-marketplace

# Restart Claude Code (required)
```

### Option 3: Team Automatic Installation

Add to your project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "prp-marketplace": {
      "source": "Wirasm/PRPs-agentic-eng"
    }
  },
  "enabledPlugins": [
    "prp-core@prp-marketplace"
  ]
}
```

## Artifacts Structure

All artifacts are stored in `.claude/PRPs/`:

```
.claude/PRPs/
├── prds/              # Product requirement documents
├── plans/             # Implementation plans
│   └── completed/     # Archived completed plans
├── reports/           # Implementation reports
├── issues/            # Issue investigation artifacts
│   └── completed/     # Archived completed investigations
└── reviews/           # PR review reports
```

## PRD Phases

PRDs include an Implementation Phases table:

```markdown
| # | Phase | Description | Status | Parallel | Depends | PRP Plan |
|---|-------|-------------|--------|----------|---------|----------|
| 1 | Auth  | User login  | complete | -      | -       | [link]   |
| 2 | API   | Endpoints   | in-progress | -   | 1       | [link]   |
| 3 | UI    | Frontend    | pending | with 4  | 2       | -        |
```

- **Status**: `pending` → `in-progress` → `complete`
- **Parallel**: Phases that can run concurrently
- **Depends**: Phases that must complete first

## PRP Methodology

### What is a PRP?

**PRP = PRD + curated codebase intelligence + agent/runbook**

A PRP is a comprehensive implementation document containing:
1. **Context** - All necessary patterns, documentation, and examples
2. **Plan** - Step-by-step tasks with validation gates
3. **Validation** - Executable commands to verify correctness

### Core Principles

1. **Context is King** - Include ALL necessary information
2. **Validation Loops** - Provide executable tests the AI can run and fix
3. **Information Dense** - Use keywords and patterns from codebase
4. **Bounded Scope** - Each plan completable by AI in one loop

## Requirements

- Claude Code installed
- Git configured
- GitHub CLI (`gh`) for PR creation

## Troubleshooting

### Plugin Not Loading

```bash
/plugin
/plugin uninstall prp-core@marketplace
/plugin install prp-core@marketplace
# Restart Claude Code
```

### Skills Not Found

Ensure Claude Code restarted after installation. Skills are loaded from the plugin's `skills/` directory.

## License

MIT License

## Support

- **Issues**: https://github.com/Wirasm/PRPs-agentic-eng/issues
- **Documentation**: https://github.com/Wirasm/PRPs-agentic-eng
