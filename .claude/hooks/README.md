# Repo-local PRP hooks

This directory documents the **manual, repo-local** hook setup. Use it only if you copy the root `.claude/` assets into a project instead of installing the `prp-core` plugin.

## If you installed the plugin

Do **not** configure these hooks by hand. The plugin already registers both Stop hooks from `plugins/prp-core/hooks/hooks.json`:

- `${CLAUDE_PLUGIN_ROOT}/hooks/prp-ralph-stop.sh`
- `${CLAUDE_PLUGIN_ROOT}/hooks/prp-research-team-stop.sh`

## What is in this repo-local folder

The root `.claude/hooks/` directory currently contains:

- `prp-ralph-stop.sh`
- `README.md`

The Research Team stop hook exists only in the plugin package at `plugins/prp-core/hooks/prp-research-team-stop.sh`.

## Manual setup for repo-local Ralph hook

### Project-level settings

Add this to `.claude/settings.local.json` in the target project:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/prp-ralph-stop.sh"
          }
        ]
      }
    ]
  }
}
```

### Global settings

Add this to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/project/.claude/hooks/prp-ralph-stop.sh"
          }
        ]
      }
    ]
  }
}
```

## How the Ralph hook works

1. `prp-ralph` creates `.claude/prp-ralph.state.md`.
2. `prp-ralph-stop.sh` checks that file whenever Claude tries to exit.
3. If the completion promise is missing, the hook loops the session back into the same task.
4. If `<promise>COMPLETE</promise>` is present, or max iterations are reached, the state file is removed and Claude exits normally.

## Troubleshooting

### Hook not triggering

1. Verify the hook exists in settings:

   ```bash
   cat .claude/settings.local.json | jq '.hooks'
   ```

2. Verify the script is executable:

   ```bash
   ls -la .claude/hooks/prp-ralph-stop.sh
   ```

3. Test it manually only when an active Ralph loop has already created `.claude/prp-ralph.state.md`. The transcript path below is a placeholder and must point to a real Claude transcript file:

   ```bash
   echo '{"transcript_path": "/tmp/test.jsonl"}' | .claude/hooks/prp-ralph-stop.sh
   ```

### Loop not stopping

1. Verify the completion marker is exact: `<promise>COMPLETE</promise>`
2. Check the state file: `cat .claude/prp-ralph.state.md`
3. Confirm the max iteration limit has not already been reached

### Manual cancellation

Use the `prp-ralph-cancel` skill, or remove the state file manually:

```bash
rm .claude/prp-ralph.state.md
```
