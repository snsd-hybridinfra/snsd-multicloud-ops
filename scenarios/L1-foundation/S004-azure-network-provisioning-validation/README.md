# S004-azure-network-provisioning-validation

## Summary

Azure Network Provisioning Validation validates one operational capability in the L1 Foundation scenario set.

## Objective

Define how Azure Network Provisioning Validation will be validated before any implementation code or real environment changes are introduced.

## Scope

This skeleton covers scenario planning, validation criteria, rollback thinking, and evidence mapping only. It does not implement Terraform, Ansible, Kubernetes, cloud, monitoring, ML, or backup code.

## Validation Criteria

- Objective, scope, prerequisites, execution flow, validation checks, expected results, failure conditions, rollback, and evidence mapping are documented.
- Evidence output locations are defined under $evidencePath.
- No secrets, credentials, tfstate, kubeconfig files, private keys, or account-specific values are introduced.

## Evidence Output

Evidence is collected in $evidencePath using commands.md, alidation.md, logs/, screenshots/, and configs/.