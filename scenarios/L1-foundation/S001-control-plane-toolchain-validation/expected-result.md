# Expected Result

## Success Conditions

- All ten required tool version checks are documented.
- Each tool returns version information when executed on `<target-node>`.
- Evidence records command purpose, TODO output location, and validation status.
- No cloud authentication, infrastructure change, or sensitive file access occurs.

## Required Evidence

- `commands.md`: planned commands, purpose, timestamp placeholder, target placeholder, and TODO output placeholder.
- `validation.md`: validation table with expected result, actual result placeholder, status, and evidence reference.

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after actual sanitized command outputs are collected and every validation item has a final status.
