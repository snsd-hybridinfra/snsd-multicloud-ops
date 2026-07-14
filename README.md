# SNSD Multi-Cloud Secure Operations Validation Platform

**한국어 제목:** SNSD 시나리오 기반 멀티클라우드 보안 운영 검증 플랫폼

Scenario-based multi-cloud secure operations validation platform for portfolio and non-production use. The repository demonstrates repeatable operational, security, recovery, governance, and intelligent-operations checks through documented criteria and traceable evidence; it does not represent a production deployment or formal compliance certification.

## Validation Model

`Scenario → Validation Criteria → Evidence Output → Runbook/Rollback where applicable`

The locked model contains exactly 50 scenarios across five levels:

- **L1 Foundation Validation** — control-plane, network, inventory, and repository foundations
- **L2 Security Baseline Validation** — access, least privilege, service, and platform baselines
- **L3 Service Operations Validation** — Kubernetes, traffic, database, and observability operations
- **L4 Failure Recovery Validation** — controlled failure, rollback, backup, restore, and recovery evidence
- **L5 Governance Intelligent Ops** — drift, policy, cost, cleanup, ML-assisted metric analysis, and final reporting

The canonical scenario list is maintained in [docs/scenario-model.md](docs/scenario-model.md).

## Repository Layout

- `scenarios/` — scenario definitions grouped by validation level
- `evidence/` — matching commands, validation records, logs, screenshots, and configs
- `tools/` — local PowerShell generators and validators
- `runbooks/`, `policy/`, `security-baseline/`, `cost-governance/` — non-production operational references
- `terraform/`, `ansible/`, `kubernetes/`, `eve-ng/`, `observability/`, `ml-security/` — locked platform implementation and example areas
- `docs/` — scope, naming, tracking, risk, and architecture records

## Run Local Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-repo-structure.ps1
powershell -ExecutionPolicy Bypass -File tools\validate-scenario-quality.ps1
powershell -ExecutionPolicy Bypass -File tools\validate-all-scenarios.ps1
powershell -ExecutionPolicy Bypass -File tools\generate-final-evidence-report.ps1
powershell -ExecutionPolicy Bypass -File tools\validate-final-evidence-report.ps1
```

The repository-wide wrapper runs local PowerShell validators in static-only mode. It does not run Terraform, kubectl, cloud CLIs, or live infrastructure queries.

## Scope and Safety

This repository uses sanitized examples and placeholders. Do not add credentials, secrets, private keys, generated state, kubeconfig, cloud account values, production identifiers, packet captures, malware samples, or real billing/monitoring exports.

Major excluded capabilities include production-grade HA/DR, automatic cross-cloud failover, SIEM/Wazuh/EDR/SOAR, threat hunting, packet payload analysis, malware detection, real-time blocking, formal compliance certification, and unapproved platform integrations. See [docs/scope-lock.md](docs/scope-lock.md) and [docs/excluded-scope.md](docs/excluded-scope.md) for the authoritative boundaries.

Agent working rules are defined in [AGENTS.md](AGENTS.md).
