# Rollback Plan

## Stop Condition

Stop immediately if validation activity exposes passwords, credentials, private keys, public IPs, account-specific values, tfstate, kubeconfig content, or attempts to implement S011 or S012 controls.

## Rollback Steps

1. Stop validation activity.
2. Remove unsafe evidence content.
3. Replace sensitive values with placeholders such as `<bastion-host>`, `<target-node>`, and `<target-user>`.
4. Mark affected checks as `BLOCKED` or `FAIL` in `validation.md`.
5. Record the blocked condition in the implementation log if scenario progress is affected.

## Recovery Validation

Confirm S013 remains direct root login denial planning only, with no passwords, credentials, private keys, public IPs, account-specific values, SSH key authentication implementation, password login denial implementation, or sudo policy validation added.
