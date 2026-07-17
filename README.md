# SNSD Multi-Cloud Secure Operations Validation Platform

## Current Repository Truth State

- Status: **EVE-NG NETWORK FOUNDATION AND OPENSTACK AIO NETWORK PATH VALIDATED**
- The EVE-NG host, one router, one Layer-2 switch, six VLAN gateways,
  Router-on-a-Stick, NAT/PAT, and a temporary directional ACL test are
  operator-confirmed implemented.
- A non-production Kolla-Ansible OpenStack AIO control plane and one
  provider/tenant/Floating-IP path are operator-validated under S005.
- S002 and S005 have `READY` sanitized evidence; Kubernetes, MariaDB,
  monitoring, backup, AWS, Azure, Terraform reproduction, HA, and persistent
  storage remain unvalidated.
- Local repository/document validators check structure and safety only. Their
  success is not infrastructure or scenario validation.

**한국어 제목:** SNSD 시나리오 기반 멀티클라우드 보안 운영 검증 플랫폼

Scenario-based portfolio repository for a non-production multi-cloud secure
operations validation platform. It records planned criteria and sanitized
operator-executed lab evidence without storing credentials or raw runtime data.

## Zero Trust Guideline 2.0 Positioning

This repository is designed to align hybrid and multicloud operational
capabilities with the Korean Zero Trust Guideline 2.0. Capability alignment,
implementation status, runtime validation, evidence level, and maturity
assessment are tracked separately. This is not a claim of full compliance,
complete implementation, certification, or organization-wide maturity.

See the [Zero Trust Guideline 2.0 framework](docs/zero-trust/README.md).

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

These local PowerShell commands validate repository/document structure only.
They do not produce authoritative scenario evidence and do not run Terraform,
kubectl, cloud CLIs, or live infrastructure queries.

## Current OpenStack Result

- Kolla-Ansible single-node AIO deployment: operator-validated.
- Core services, Nova compute, hypervisor, and Neutron agents: healthy in the supplied results.
- EVE-NG VLAN 70 -> `physnet1` -> `br-ex` -> Neutron router -> Floating IP -> tenant instance: validated.
- Tenant instance gateway and outbound public IPv4 reachability: validated.
- Scope: disposable non-production single-node lab; no HA, persistent storage, production hardening, Terraform reproduction, or automated cleanup claim.

See [S005](scenarios/L1-foundation/S005-openstack-network-provisioning-validation/README.md)
and its [validation record](evidence/L1-foundation/S005-openstack-network-provisioning-validation/validation.md).

## Authoritative Lab Architecture References

The non-production multi-cloud lab baseline is defined in:

- [Multi-cloud architecture baseline](docs/lab-reference-architecture.md)
- [Authoritative phase plan](docs/lab-build-order.md)
- [IP address and reservation plan](docs/lab-ip-plan.md)
- [Network zone plan](docs/lab-network-zone-plan.md)
- [Platform responsibility matrix](docs/platform-responsibility-matrix.md)
- [Cloud cost guardrails](docs/cloud-cost-guardrails.md)
- [Resource lifecycle policy](docs/resource-lifecycle-policy.md)
- [External address policy](docs/external-address-policy.md)
- [Host capacity baseline](docs/host-capacity-baseline.md)
- [VM resource allocation plan](docs/vm-resource-allocation-plan.md)
- [Lab execution profiles](docs/lab-execution-profiles.md)
- [Storage and snapshot policy](docs/storage-and-snapshot-policy.md)
- [ADR-0001](docs/adr/ADR-0001-multicloud-network-and-platform-baseline.md)
- [ADR-0002 runtime evidence boundary](docs/adr/0002-non-production-runtime-evidence-boundary.md)
- [Evidence collection guide](docs/lab-evidence-collection-guide.md)
- [Evidence sanitization rules](docs/lab-sanitization-rules.md)

These documents prepare later sanitized evidence collection; they do not provision or query live infrastructure, authorize cloud spend, or change scenario status.

## Scope and Safety

This repository uses sanitized examples and placeholders. Do not add credentials, secrets, private keys, generated state, kubeconfig, cloud account values, production identifiers, packet captures, malware samples, or real billing/monitoring exports.

Major excluded capabilities include production-grade HA/DR, automatic cross-cloud failover, SIEM/Wazuh/EDR/SOAR, threat hunting, packet payload analysis, malware detection, real-time blocking, formal compliance certification, and unapproved platform integrations. See [docs/scope-lock.md](docs/scope-lock.md) and [docs/excluded-scope.md](docs/excluded-scope.md) for the authoritative boundaries.

Agent working rules are defined in [AGENTS.md](AGENTS.md).
