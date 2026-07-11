# Architecture

## Relevant Components

- Local control plane workstation
- Repository-local validation script: `tools/validate-control-plane-toolchain.ps1`
- Core CLI tier: Git, PowerShell, SSH, Python
- Later-stage CLI tier: Terraform, Ansible, kubectl, Docker
- S001 evidence log and summary

## Logical Flow

1. The operator invokes the repository-local PowerShell script.
2. The script uses `Get-Command` to inspect local command availability.
3. Available commands receive a version-only invocation.
4. The script prints `PASS`, `WARN`, or `FAIL` and writes sanitized evidence.
5. The process exits non-zero only when a core tool fails readiness validation.

## Out-of-Scope Components

Cloud APIs, provider credentials, Terraform providers, Ansible inventories, Kubernetes clusters, Docker registries and daemons, Prometheus, and Grafana are not accessed.
