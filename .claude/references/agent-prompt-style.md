# Agent Prompt Style

PRP agents follow a structured prompt style that keeps each agent's job explicit, its boundaries clear, and its output predictable. The pattern is: one declared job, explicit DO NOT boundaries, a short strategy, and a fixed output shape.

## Required structure

Every agent prompt must include these sections in this order:

### 1. Critical role declaration

State the agent's single job in the opening line. Use this form:

```
## CRITICAL: Your only job is to [specific role]
```

Follow with explicit `DO NOT` boundaries for the two or three most common scope violations.

### 2. Core Responsibilities

A numbered list of the concrete actions the agent takes. Keep it to five or fewer items. Each item should be specific enough that another agent could audit whether it was followed.

### 3. Strategy

A numbered stepwise approach the agent should follow. This is not a restatement of responsibilities — it is the execution order and any key decision rules.

### 4. Output Format

Define the required output shape. For agents with a repeatable task, the output format should be explicit: section names, order, and any required fields.

## Hard boundaries

- One job per agent. An agent that reviews code must not also modify files. An agent that explores must not also commit.
- Minimal tool surface. Grant only the tools the agent genuinely needs. Advisory agents typically need read-only access (grep, glob, view, bash). No file modification tools.
- `maxTurns` must be declared. Advisory agents: `maxTurns: 10`. Exploration agents: `maxTurns: 15`.

## PRP-specific frontmatter

Retain all PRP-specific frontmatter fields (`name`, `description`, `model`, `color`, `tools`, `maxTurns`, `skills`) unless a change is explicitly justified by the plugin's actual runtime needs. Do not silently drop fields when adapting prompt structure.

Model selection:
- `haiku` — structured, fast tasks (explorer, comment-analyzer, docs-impact)
- `sonnet` — reasoning-heavy tasks (analyst, reviewer, type-design, advisor)

## Adaptation guidance

When normalizing an existing agent against this style:

1. Add the critical role declaration if it is missing.
2. Add hard `DO NOT` boundaries if implicit.
3. Consolidate scattered responsibilities into numbered Core Responsibilities.
4. Add a Strategy section if the agent's approach is not stated.
5. Make the output format explicit if it is currently open-ended.
6. Do not remove PRP-specific frontmatter or behavioral capabilities without reviewing the plugin's runtime contract.

## Related references

- `harness-taxonomy.md` — advisory vs. utility component classification
- `execution-policy.md` — when an agent receives a subagent delegation
- `context-budget-policy.md` — brief size limits for agent output
