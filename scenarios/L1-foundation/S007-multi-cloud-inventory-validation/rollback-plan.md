# Rollback Plan

## Stop Condition

Stop immediately if inventory validation exposes real IP addresses, credentials, SSH private keys, kubeconfig content, tfstate, or account-specific values.

## Rollback Steps

1. Stop validation activity.
2. Remove unsafe evidence content.
3. Replace sensitive values with placeholders such as `<aws-app-node-ip>`, `<azure-app-node-ip>`, `<openstack-app-node-ip>`, or `<db-primary-ip>`.
4. Mark affected checks as `BLOCKED` or `FAIL` in `validation.md`.
5. Record the blocked condition in the implementation log if scenario progress is affected.

## Recovery Validation

Confirm S007 remains documentation and evidence planning only, with placeholder-only inventory values and no real Ansible automation or sensitive files added.
