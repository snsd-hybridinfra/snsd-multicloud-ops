# Prerequisites

## Required Repository Inputs

- PowerShell capable of running repository validators.
- `security-baseline/openstack-security-group-baseline.md`.
- `security-baseline/openstack-security-group-rule-matrix.example.md`.
- Existing `terraform/modules/openstack-network/` Security Group placeholders.
- Writable S016 evidence `logs/` and `configs/` directories.

## Safety Preconditions

No credentials, `clouds.yaml`, openrc, auth URLs, project or tenant values, usernames, passwords, tokens, real public addresses, corporate ranges, private keys, secrets, state, real tfvars, kubeconfig, or account-specific values may be introduced.
