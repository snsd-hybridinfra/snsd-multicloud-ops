# Rollback Plan

## Stop Condition

Stop if any command attempts authentication, remote connection, registry access, credential or kubeconfig access, tfstate access, or an infrastructure-changing action.

## Rollback Steps

1. Terminate the command.
2. Remove unsafe generated output from the two S001 evidence files.
3. Restore the last reviewed evidence version from Git if necessary.
4. Record the affected validation check as `FAIL` or `BLOCKED`.

## Recovery Validation

Confirm the script again contains only `Get-Command` and version-only invocations, then rerun it and review both generated evidence files.
