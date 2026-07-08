# Rollback Plan

## Stop Condition

Stop immediately if reachability validation exposes real IP addresses, credentials, SSH private keys, provider account values, kubeconfig content, tfstate, or attempts SSH hardening implementation.

## Rollback Steps

1. Stop validation activity.
2. Remove unsafe evidence content.
3. Replace sensitive values with placeholders such as `<bastion-ip>`, `<db-primary-ip>`, `<aws-app-node-ip>`, `<azure-app-node-ip>`, or `<openstack-app-node-ip>`.
4. Mark affected checks as `BLOCKED` or `FAIL` in `validation.md`.
5. Record the blocked condition in the implementation log if scenario progress is affected.

## Recovery Validation

Confirm S008 remains reachability design documentation only, with placeholder-only bastion paths and no real Ansible automation, SSH hardening, credentials, private keys, public IPs, or account-specific values added.
