# Prerequisites

## Required Repository Inputs

- PowerShell capable of running repository validators.
- `security-baseline/azure-nsg-least-privilege-baseline.md`.
- `security-baseline/azure-nsg-rule-matrix.example.md`.
- Existing `terraform/modules/azure-network/` structural placeholders.
- Writable S015 evidence `logs/` and `configs/` directories.

## Safety Preconditions

No Azure credentials, client values, tenant or subscription values, real public addresses, corporate ranges, private keys, secrets, state, real tfvars, kubeconfig, `clouds.yaml`, openrc, or account-specific values may be introduced.
