# Scenario Model

## Current Repository State

The canonical S001-S050 set is defined. S002 and S005 are `VALIDATED` with
`READY` sanitized evidence. S005 combines operator-executed deployment and
data-plane evidence with later Codex-executed forced-command read-only
corroboration. It covers the non-production OpenStack AIO control plane and one
end-to-end provider/tenant/Floating-IP network path; all unrelated scenario
statuses remain unchanged.
Repository/document validation is tracked separately and cannot advance a
scenario lifecycle state.

Scenario-based validation is the main repository method. Each scenario is a controlled test of one operational capability and must produce reviewable evidence.

## Scenario Format

Each scenario should include:

- `id`: stable scenario ID
- `title`: short descriptive name
- `level`: one of the five validation levels
- `objective`: behavior being validated
- `scope`: allowed systems and files
- `prerequisites`: required setup
- `steps`: validation procedure
- `evidence`: required artifacts
- `pass_criteria`: measurable pass conditions

## Canonical Scenario Set

The following IDs and titles are the canonical v1 set. Directory names append the
kebab-case title to the ID as defined in `docs/naming-rules.md`.

### L1 Foundation Validation

- `S001` Control Plane Toolchain Validation
- `S002` EVE-NG On-Prem Routing Validation
- `S003` AWS Network Provisioning Validation
- `S004` Azure Network Provisioning Validation
- `S005` OpenStack Network Provisioning Validation
- `S006` Terraform Provider Validation
- `S007` Multi-Cloud Inventory Validation
- `S008` Bastion Reachability Validation
- `S009` DNS / Hostname Resolution Validation
- `S010` Evidence Directory Structure Validation

### L2 Security Baseline Validation

- `S011` SSH Key Authentication Validation
- `S012` Password Login Denial Validation
- `S013` Root Login Denial Validation
- `S014` AWS Security Group Least Privilege Validation
- `S015` Azure NSG Least Privilege Validation
- `S016` OpenStack Security Group Validation
- `S017` MariaDB Access Control Validation
- `S018` Kubernetes RBAC Validation
- `S019` Nginx Security Header Validation
- `S020` Grafana Anonymous Access Denial Validation

### L3 Service Operations Validation

- `S021` Kubernetes Node Readiness Validation
- `S022` Kubernetes Workload Deployment Validation
- `S023` Ingress Routing Validation
- `S024` Nginx Reverse Proxy Validation
- `S025` Load Balancing Health Check Validation
- `S026` MariaDB Primary-Replica Replication Validation
- `S027` DB Replication Lag Validation
- `S028` Prometheus Target Discovery Validation
- `S029` Grafana Dashboard Validation
- `S030` Blackbox Endpoint Probe Validation

### L4 Failure & Recovery Validation

- `S031` Web Pod Failure Recovery Validation
- `S032` API Service Failure Validation
- `S033` DB Replica Failure Validation
- `S034` DB Primary Stop Runbook Validation
- `S035` Load Balancer Failure Validation
- `S036` Prometheus Target Down Validation
- `S037` Security Rule Misconfiguration Validation
- `S038` Backup Creation Validation
- `S039` Restore Execution Validation
- `S040` Service Health After Recovery Validation

### L5 Governance & Intelligent Operations Validation

- `S041` Terraform Drift Detection Validation
- `S042` Terraform Drift Remediation Validation
- `S043` Policy as Code Validation
- `S044` Kubernetes Manifest Policy Validation
- `S045` Cost Guardrail Validation
- `S046` Resource Cleanup Validation
- `S047` ML Metric Dataset Collection Validation
- `S048` ML Anomaly Detection Validation
- `S049` ML Anomaly Report Generation Validation
- `S050` Final Evidence Report Generation Validation

## Scenario Lifecycle Status Model

- `NOT_STARTED`: no planning or implementation work has begun.
- `PLANNED`: documentation and intended validation are defined.
- `IN_PROGRESS`: implementation or evidence collection is active.
- `IMPLEMENTED`: the required implementation exists but validation is incomplete.
- `VALIDATED`: every required check has supporting evidence.
- `PARTIAL`: only part of the scenario is implemented or validated.
- `BLOCKED`: an explicit dependency prevents progress.
- `DEPRECATED`: the scenario is retained for history but is no longer active.
