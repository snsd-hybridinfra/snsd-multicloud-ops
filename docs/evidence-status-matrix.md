# Evidence Status Matrix

Evidence Readiness Status values: `NOT_READY`, `PARTIAL`, `READY`, `REVIEWED`

| ID | Scenario | commands.md | validation.md | logs | screenshots | configs | Evidence Status |
|---|---|---|---|---|---|---|---|
| S001 | control-plane-toolchain-validation | READY | READY | READY | READY | READY | READY |
| S002 | eve-ng-on-prem-routing-validation | READY | READY | READY | READY | READY | READY |
| S003 | aws-network-provisioning-validation | READY | READY | READY | READY | READY | READY |
| S004 | azure-network-provisioning-validation | READY | READY | READY | READY | READY | READY |
| S005 | openstack-network-provisioning-validation | READY | READY | READY | READY | READY | READY |
| S006 | terraform-provider-validation | READY | READY | READY | READY | READY | READY |
| S007 | multi-cloud-inventory-validation | READY | READY | READY | READY | READY | READY |
| S008 | bastion-reachability-validation | READY | READY | READY | READY | READY | READY |
| S009 | dns-hostname-resolution-validation | READY | READY | READY | READY | READY | READY |
| S010 | evidence-directory-structure-validation | READY | READY | READY | READY | READY | READY |
| S011 | ssh-key-authentication-validation | READY | READY | READY | READY | READY | READY |
| S012 | password-login-denial-validation | READY | READY | READY | READY | READY | READY |
| S013 | root-login-denial-validation | READY | READY | READY | READY | READY | READY |
| S014 | aws-security-group-least-privilege-validation | READY | READY | READY | READY | READY | READY |
| S015 | azure-nsg-least-privilege-validation | READY | READY | READY | READY | READY | READY |
| S016 | openstack-security-group-validation | READY | READY | READY | READY | READY | READY |
| S017 | mariadb-access-control-validation | READY | READY | READY | READY | READY | READY |
| S018 | kubernetes-rbac-validation | READY | READY | READY | READY | READY | READY |
| S019 | nginx-security-header-validation | READY | READY | READY | READY | READY | READY |
| S020 | grafana-anonymous-access-denial-validation | READY | READY | READY | READY | READY | READY |
| S021 | kubernetes-node-readiness-validation | READY | READY | READY | READY | READY | READY |
| S022 | kubernetes-workload-deployment-validation | READY | READY | READY | READY | READY | READY |
| S023 | ingress-routing-validation | READY | READY | READY | READY | READY | READY |
| S024 | nginx-reverse-proxy-validation | READY | READY | READY | READY | READY | READY |
| S025 | load-balancing-health-check-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S026 | mariadb-primary-replica-replication-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S027 | db-replication-lag-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S028 | prometheus-target-discovery-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S029 | grafana-dashboard-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S030 | blackbox-endpoint-probe-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S031 | web-pod-failure-recovery-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S032 | api-service-failure-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S033 | db-replica-failure-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S034 | db-primary-stop-runbook-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S035 | load-balancer-failure-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S036 | prometheus-target-down-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S037 | security-rule-misconfiguration-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S038 | backup-creation-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S039 | restore-execution-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S040 | service-health-after-recovery-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S041 | terraform-drift-detection-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S042 | terraform-drift-remediation-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S043 | policy-as-code-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S044 | kubernetes-manifest-policy-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S045 | cost-guardrail-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S046 | resource-cleanup-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S047 | ml-metric-dataset-collection-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S048 | ml-anomaly-detection-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S049 | ml-anomaly-report-generation-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S050 | final-evidence-report-generation-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
