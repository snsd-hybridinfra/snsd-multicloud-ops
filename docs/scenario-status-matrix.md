# Scenario Status Matrix

Current environment truth: the EVE-NG network foundation is implemented and
the complete E001-E014 sanitized evidence chain is represented. S002 is
`VALIDATED`; all other scenarios remain unchanged.

Scenario Lifecycle Status values: `NOT_STARTED`, `PLANNED`, `IN_PROGRESS`, `IMPLEMENTED`, `VALIDATED`, `PARTIAL`, `BLOCKED`, `DEPRECATED`

| ID | Scenario | Level | Category | Status | Last Updated | Notes |
|---|---|---|---|---|---|---|
| S001 | control-plane-toolchain-validation | L1 | Foundation | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S002 | eve-ng-on-prem-routing-validation | L1 | Foundation | VALIDATED | 2026-07-16 | E001-E014 complete: host/KVM, devices, VLAN/routing, NAT/PAT, persistence, directional traffic, cleanup, host-only ping, SSH/22, and HTTP/80; HTTPS/443 accurately recorded unavailable |
| S003 | aws-network-provisioning-validation | L1 | Foundation | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S004 | azure-network-provisioning-validation | L1 | Foundation | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S005 | openstack-network-provisioning-validation | L1 | Foundation | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S006 | terraform-provider-validation | L1 | Foundation | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S007 | multi-cloud-inventory-validation | L1 | Foundation | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S008 | bastion-reachability-validation | L1 | Foundation | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S009 | dns-hostname-resolution-validation | L1 | Foundation | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S010 | evidence-directory-structure-validation | L1 | Foundation | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S011 | ssh-key-authentication-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S012 | password-login-denial-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S013 | root-login-denial-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S014 | aws-security-group-least-privilege-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S015 | azure-nsg-least-privilege-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S016 | openstack-security-group-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S017 | mariadb-access-control-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S018 | kubernetes-rbac-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S019 | nginx-security-header-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S020 | grafana-anonymous-access-denial-validation | L2 | Security Baseline | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S021 | kubernetes-node-readiness-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S022 | kubernetes-workload-deployment-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S023 | ingress-routing-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S024 | nginx-reverse-proxy-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S025 | load-balancing-health-check-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S026 | mariadb-primary-replica-replication-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S027 | db-replication-lag-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S028 | prometheus-target-discovery-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S029 | grafana-dashboard-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S030 | blackbox-endpoint-probe-validation | L3 | Service Operations | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S031 | web-pod-failure-recovery-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S032 | api-service-failure-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S033 | db-replica-failure-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S034 | db-primary-stop-runbook-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S035 | load-balancer-failure-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S036 | prometheus-target-down-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S037 | security-rule-misconfiguration-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S038 | backup-creation-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S039 | restore-execution-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S040 | service-health-after-recovery-validation | L4 | Failure Recovery | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S041 | terraform-drift-detection-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S042 | terraform-drift-remediation-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S043 | policy-as-code-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S044 | kubernetes-manifest-policy-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S045 | cost-guardrail-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S046 | resource-cleanup-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S047 | ml-metric-dataset-collection-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S048 | ml-anomaly-detection-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S049 | ml-anomaly-report-generation-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
| S050 | final-evidence-report-generation-validation | L5 | Governance Intelligent Ops | NOT_STARTED | 2026-07-15 | Planned definition only; no runtime implementation, target execution, or authoritative scenario evidence exists |
