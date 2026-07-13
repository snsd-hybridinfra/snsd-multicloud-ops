# Rollback Plan

## Stop Condition

Stop if any action attempts AWS authentication, provider initialization, plan/apply/destroy, state creation, credential access, or cloud resource changes.

## Rollback Steps

1. Terminate the command.
2. Remove unsafe generated output or non-example variable/state files.
3. Restore the module or environment from the last reviewed Git version.
4. Reapply only non-production example values.
5. Rerun the repository validator.

## Recovery Validation

Confirm V001-V008 pass and generated evidence contains repository review results only.
