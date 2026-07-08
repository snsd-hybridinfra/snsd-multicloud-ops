# Rollback Plan

## Stop Condition

Stop immediately if validation activity exposes real SSH private keys, credentials, public IPs, account-specific usernames, tfstate, kubeconfig content, or attempts password/root login controls.

## Rollback Steps

1. Stop validation activity.
2. Remove unsafe evidence content.
3. Replace sensitive values with placeholders such as `<ssh-private-key-path>`, `<bastion-host>`, `<target-node>`, and `<target-user>`.
4. Mark affected checks as `BLOCKED` or `FAIL` in `validation.md`.
5. Record the blocked condition in the implementation log if scenario progress is affected.

## Recovery Validation

Confirm S011 remains SSH key authentication planning only, with no real keys, credentials, public IPs, account-specific values, password-login denial, or root-login denial implementation added.
