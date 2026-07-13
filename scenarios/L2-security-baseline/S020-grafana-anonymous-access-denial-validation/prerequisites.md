# Prerequisites

## Required Repository Inputs

- PowerShell capable of running repository validators.
- `security-baseline/grafana-anonymous-access-denial-baseline.md` and its matrix.
- `observability/grafana/grafana.ini.anonymous-denial.example`.
- Writable S020 evidence `logs/` and `configs/` directories.

## Safety Preconditions

No real Grafana passwords, API tokens, dashboard or datasource credentials, URLs, public addresses, private keys, secrets, state, real tfvars, kubeconfig, clouds.yaml, openrc, cloud identity values, or account-specific content may be introduced.
