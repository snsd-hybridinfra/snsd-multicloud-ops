# Prerequisites

## Required Repository Inputs

- PowerShell capable of running repository validators.
- `security-baseline/kubernetes-rbac-baseline.md` and its rule matrix.
- `kubernetes/security/rbac-baseline/` non-production examples.
- Writable S018 evidence `logs/` and `configs/` directories.

## Safety Preconditions

No kubeconfig, token, certificate, private key, endpoint, Secret resource, credentials, state, real tfvars, clouds.yaml, openrc, cloud identity values, or account-specific content may be introduced.
