# Rollback Plan

Static S031 changes repository evidence only; no live cluster rollback applies.

1. Stop if sensitive/real cluster content or destructive automation is found.
2. Remove unsafe artifacts and restore placeholders/read-only logic.
3. Correct samples/parser locally and rerun Static validation.
4. Investigate lab recovery failures under a separate authorized runbook.
5. Revert invalid repository changes through version control.

Never delete/restart/apply/patch/edit/scale/cordon/drain/taint resources from this validator.
