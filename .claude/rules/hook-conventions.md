---
paths:
  - "plugins/prp-core/hooks/*.sh"
  - ".claude/hooks/*.sh"
---
<!-- Migrated from codebase analysis — hook protocol rules extracted to on-demand rule -->

# Hook Script Conventions

- Scripts read JSON from stdin (Claude Code hook protocol)
- Output JSON with `{"decision": "block"|"allow", "reason": "..."}` to stdout
- Informational messages go to stderr (never stdout — stdout is parsed as JSON)
- Use `jq` for JSON construction; validate input with `2>/dev/null` guards
- Use `set -euo pipefail` at script top
- The `<promise>COMPLETE</promise>` sentinel in Ralph hooks is a critical contract — the stop hook parses it to decide loop continuation
