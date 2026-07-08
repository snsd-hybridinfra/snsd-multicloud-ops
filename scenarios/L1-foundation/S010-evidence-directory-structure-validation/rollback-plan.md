# Rollback Plan

## Stop Condition

Stop immediately if evidence validation exposes real credentials, private keys, public IPs, tfstate, kubeconfig files, account-specific values, or unapproved binary artifacts.

## Rollback Steps

1. Stop validation activity.
2. Remove unsafe evidence content.
3. Replace sensitive values with placeholders such as `<redacted-path>` or `<redacted-value>`.
4. Mark affected checks as `BLOCKED` or `FAIL` in `validation.md`.
5. Record the blocked condition in the implementation log if scenario progress is affected.

## Recovery Validation

Confirm S010 remains repository structure and evidence policy validation only, with no implementation logic or sensitive files added.
