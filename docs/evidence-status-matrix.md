# Evidence Status Matrix

Evidence status values: `NOT_READY`, `PARTIAL`, `READY`, `REVIEWED`

| ID | Scenario | commands.md | validation.md | logs | screenshots | configs | Evidence Status |
|---|---|---|---|---|---|---|---|
| S001 | control-plane-toolchain-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S002 | eve-ng-onprem-routing-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S003 | aws-network-provisioning-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S004 | azure-network-provisioning-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S005 | openstack-network-provisioning-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S006 | terraform-provider-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S007 | multi-cloud-inventory-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S008 | bastion-reachability-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S009 | dns-hostname-resolution-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S010 | evidence-directory-structure-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S011 | ssh-key-authentication-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S012 | password-login-denial-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S013 | root-login-denial-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S014 | aws-security-group-least-privilege-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S015 | azure-nsg-least-privilege-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S016 | openstack-security-group-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S017 | mariadb-access-control-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S018 | kubernetes-rbac-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S019 | nginx-security-header-validation | PARTIAL | PARTIAL | NOT_READY | NOT_READY | NOT_READY | PARTIAL |
| S020 | grafana-anonymous-access-denial-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S021 | kubernetes-node-readiness-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S022 | kubernetes-workload-deployment-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S023 | ingress-routing-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S024 | nginx-reverse-proxy-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S025 | load-balancing-health-check-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S026 | mariadb-primary-replica-replication-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S027 | db-replication-lag-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S028 | prometheus-target-discovery-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S029 | grafana-dashboard-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S030 | blackbox-endpoint-probe-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S031 | web-pod-failure-recovery-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S032 | api-service-failure-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S033 | db-replica-failure-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S034 | db-primary-stop-runbook-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S035 | load-balancer-failure-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S036 | prometheus-target-down-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S037 | security-rule-misconfiguration-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S038 | backup-creation-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S039 | restore-execution-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S040 | service-health-after-recovery-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S041 | terraform-drift-detection-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S042 | terraform-drift-remediation-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S043 | policy-as-code-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S044 | kubernetes-manifest-policy-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S045 | cost-guardrail-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S046 | resource-cleanup-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S047 | ml-metric-dataset-collection-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S048 | ml-anomaly-detection-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S049 | ml-anomaly-report-generation-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
| S050 | final-evidence-report-generation-validation | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY | NOT_READY |
