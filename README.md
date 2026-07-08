# SNSD Multi-Cloud Secure Operations Validation Platform

This repository is the scenario-based validation foundation for a multi-cloud secure operations platform. It is designed to prove operational, security, recovery, governance, and intelligent-operations behaviors through repeatable scenarios and evidence, before any production cloud implementation is introduced.

## Repository Method

The primary unit of work is a validation scenario. Each scenario defines:

- objective and acceptance criteria
- allowed scope and dependencies
- execution steps
- expected evidence
- pass, partial, and fail conditions

Evidence is stored separately from scenario definitions so implementation work, observations, and review artifacts stay traceable.

## Validation Levels

- `L1-foundation`: repository, platform structure, lab readiness, and baseline operating conventions
- `L2-security-baseline`: identity, network, host, Kubernetes, and policy security baselines
- `L3-service-operations`: deployment, traffic, observability, and routine service operations
- `L4-failure-recovery`: failure injection, backup, restore, failover, and recovery validation
- `L5-governance-intelligent-ops`: cost, compliance, reporting, anomaly detection, and ML-assisted operations

See [docs/scenario-model.md](docs/scenario-model.md) for the 50 core scenarios.

## Scope Guardrails

This foundation does not create real cloud resources, credentials, secrets, private keys, tfstate, kubeconfig files, or account-specific configuration. The locked scope and excluded scope are documented in:

- [docs/scope-lock.md](docs/scope-lock.md)
- [docs/excluded-scope.md](docs/excluded-scope.md)

## Key Directories

- `scenarios/`: scenario definitions grouped by validation level
- `evidence/`: captured results grouped by validation level
- `terraform/`: future IaC modules and environment layouts, without providers or credentials
- `ansible/`: future automation inventory, playbooks, and roles
- `kubernetes/`: future namespace, workload, ingress, and security manifests
- `eve-ng/`: topology and network device configuration references
- `observability/`: Prometheus, Grafana, and exporter configuration references
- `ml-security/`: datasets, scripts, models, and reports for security analytics
- `docs/adr/`: architecture decision records

## Working Rules

Use concise scenario-first changes, document assumptions, and store validation outputs under the matching evidence level. Codex-specific working rules are in [AGENTS.md](AGENTS.md).
