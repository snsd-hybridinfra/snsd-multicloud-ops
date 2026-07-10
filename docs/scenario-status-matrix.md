# Scenario Status Matrix

Scenario status values: `NOT_STARTED`, `PLANNED`, `IN_PROGRESS`, `IMPLEMENTED`, `VALIDATED`, `PARTIAL`, `BLOCKED`, `DEPRECATED`

| ID | Scenario | Level | Category | Status | Last Updated | Notes |
|---|---|---|---|---|---|---|
| S001 | control-plane-toolchain-validation | L1 | Foundation | PLANNED | 2026-07-08 | Control plane toolchain validation documentation completed; command output not collected yet |
| S002 | eve-ng-onprem-routing-validation | L1 | Foundation | PLANNED | 2026-07-08 | EVE-NG on-prem routing validation documentation completed; routing output not collected yet |
| S003 | aws-network-provisioning-validation | L1 | Foundation | PLANNED | 2026-07-08 | AWS network provisioning validation documentation completed; Terraform and AWS output not collected yet |
| S004 | azure-network-provisioning-validation | L1 | Foundation | PLANNED | 2026-07-08 | Azure network provisioning validation documentation completed; Terraform and Azure output not collected yet |
| S005 | openstack-network-provisioning-validation | L1 | Foundation | PLANNED | 2026-07-08 | OpenStack network provisioning validation documentation completed; Terraform and OpenStack output not collected yet |
| S006 | terraform-provider-validation | L1 | Foundation | PLANNED | 2026-07-08 | Terraform provider validation documentation completed; provider command output not collected yet |
| S007 | multi-cloud-inventory-validation | L1 | Foundation | PLANNED | 2026-07-08 | Multi-cloud inventory validation documentation completed; inventory output not collected yet |
| S008 | bastion-reachability-validation | L1 | Foundation | PLANNED | 2026-07-08 | Bastion reachability validation documentation completed; reachability output not collected yet |
| S009 | dns-hostname-resolution-validation | L1 | Foundation | PLANNED | 2026-07-08 | Hostname resolution validation documentation completed; DNS lookup output not collected yet |
| S010 | evidence-directory-structure-validation | L1 | Foundation | PLANNED | 2026-07-08 | Evidence directory structure validation documentation completed; structure command output not collected yet |
| S011 | ssh-key-authentication-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | SSH key authentication validation documentation completed; SSH output not collected yet |
| S012 | password-login-denial-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | Password login denial validation documentation completed; denial output not collected yet |
| S013 | root-login-denial-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | Root login denial validation documentation completed; denial output not collected yet |
| S014 | aws-security-group-least-privilege-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | AWS Security Group least privilege validation documentation completed; rule output not collected yet |
| S015 | azure-nsg-least-privilege-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | Azure NSG least privilege validation documentation completed; rule output not collected yet |
| S016 | openstack-security-group-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | OpenStack Security Group least privilege validation documentation completed; rule output not collected yet |
| S017 | mariadb-access-control-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | MariaDB access control validation documentation completed; database output not collected yet |
| S018 | kubernetes-rbac-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | Kubernetes RBAC least privilege validation documentation completed; kubectl output not collected yet |
| S019 | nginx-security-header-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | Nginx security header validation documentation completed; response output not collected yet |
| S020 | grafana-anonymous-access-denial-validation | L2 | Security Baseline | PLANNED | 2026-07-08 | Grafana anonymous access denial validation documentation completed; Grafana output not collected yet |
| S021 | kubernetes-node-readiness-validation | L3 | Service Operations | PLANNED | 2026-07-08 | Kubernetes node readiness validation documentation completed; kubectl output not collected yet |
| S022 | kubernetes-workload-deployment-validation | L3 | Service Operations | PLANNED | 2026-07-08 | Kubernetes workload deployment validation documentation completed; kubectl output not collected yet |
| S023 | ingress-routing-validation | L3 | Service Operations | PLANNED | 2026-07-08 | Ingress routing validation documentation completed; routing output not collected yet |
| S024 | nginx-reverse-proxy-validation | L3 | Service Operations | PLANNED | 2026-07-10 | Nginx Reverse Proxy validation documentation completed; proxy output not collected yet |
| S025 | load-balancing-health-check-validation | L3 | Service Operations | PLANNED | 2026-07-10 | Load balancing health check validation documentation completed; health output not collected yet |
| S026 | mariadb-primary-replica-replication-validation | L3 | Service Operations | PLANNED | 2026-07-10 | MariaDB Primary-Replica replication validation documentation completed; replication output not collected yet |
| S027 | db-replication-lag-validation | L3 | Service Operations | PLANNED | 2026-07-10 | MariaDB replication lag validation documentation completed; lag output not collected yet |
| S028 | prometheus-target-discovery-validation | L3 | Service Operations | PLANNED | 2026-07-10 | Prometheus target discovery validation documentation completed; target output not collected yet |
| S029 | grafana-dashboard-validation | L3 | Service Operations | PLANNED | 2026-07-10 | Grafana dashboard validation documentation completed; dashboard output not collected yet |
| S030 | blackbox-endpoint-probe-validation | L3 | Service Operations | PLANNED | 2026-07-10 | Blackbox endpoint probe validation documentation completed; probe output not collected yet |
| S031 | web-pod-failure-recovery-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | Web Pod failure recovery validation documentation completed; recovery output not collected yet |
| S032 | api-service-failure-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | API service failure validation documentation completed; failure and recovery output not collected yet |
| S033 | db-replica-failure-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | DB Replica failure validation documentation completed; failure and recovery output not collected yet |
| S034 | db-primary-stop-runbook-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | DB Primary stop runbook validation documentation completed; manual outage response output not collected yet |
| S035 | load-balancer-failure-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | Load balancer failure validation documentation completed; failure and recovery output not collected yet |
| S036 | prometheus-target-down-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | Prometheus target DOWN detection validation documentation completed; target state output not collected yet |
| S037 | security-rule-misconfiguration-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | Security rule misconfiguration validation documentation completed; rule output not collected yet |
| S038 | backup-creation-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | Backup creation validation documentation completed; backup output not collected yet |
| S039 | restore-execution-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | Restore execution validation documentation completed; restore output not collected yet |
| S040 | service-health-after-recovery-validation | L4 | Failure Recovery | PLANNED | 2026-07-10 | Service health after recovery validation documentation completed; post-recovery output not collected yet |
| S041 | terraform-drift-detection-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
| S042 | terraform-drift-remediation-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
| S043 | policy-as-code-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
| S044 | kubernetes-manifest-policy-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
| S045 | cost-guardrail-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
| S046 | resource-cleanup-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
| S047 | ml-metric-dataset-collection-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
| S048 | ml-anomaly-detection-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
| S049 | ml-anomaly-report-generation-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
| S050 | final-evidence-report-generation-validation | L5 | Governance Intelligent Ops | NOT_STARTED | TBD | Initial tracking state |
