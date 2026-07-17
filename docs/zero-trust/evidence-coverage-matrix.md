# Evidence Coverage Matrix

Evidence quality and execution authority are separate. Allowed authority values are `USER_EXECUTED_RUNTIME`, `CODEX_EXECUTED_LOCAL`, `CODEX_EXECUTED_LIVE_RUNTIME`, `DESIGN_ONLY`, `CONFIGURATION_ONLY`, and `MISSING`. OpenStack or EVE-NG runtime is never attributed to Codex unless Codex actually executed the live read-only check.

| Scenario | Capability IDs | Validation method | Evidence artifact | Quality | Validation authority |
|---|---|---|---|---|---|
| S001 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L1-foundation/S001-control-plane-toolchain-validation/` | DESIGN | DESIGN_ONLY |
| S002 | ZT-3.1.1, ZT-3.4.1, ZT-4.3.1 | Sanitized routing, NAT/PAT, allow/deny, reverse-direction, and cleanup checks | `evidence/L1-foundation/S002-eve-ng-on-prem-routing-validation/` | RUNTIME | USER_EXECUTED_RUNTIME |
| S003 | ZT-3.1.1, ZT-3.4.1, ZT-4.3.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L1-foundation/S003-aws-network-provisioning-validation/` | DESIGN | DESIGN_ONLY |
| S004 | ZT-3.1.1, ZT-3.4.1, ZT-4.3.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L1-foundation/S004-azure-network-provisioning-validation/` | DESIGN | DESIGN_ONLY |
| S005 | ZT-3.1.1, ZT-3.4.1, ZT-4.1.1, ZT-7.1, ZT-8.2 | Sanitized AIO provider/tenant path plus restricted read-only 50-check validation | `evidence/L1-foundation/S005-openstack-network-provisioning-validation/` | RUNTIME | USER_EXECUTED_RUNTIME; CODEX_EXECUTED_LIVE_RUNTIME |
| S006 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L1-foundation/S006-terraform-provider-validation/` | DESIGN | DESIGN_ONLY |
| S007 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L1-foundation/S007-multi-cloud-inventory-validation/` | DESIGN | DESIGN_ONLY |
| S008 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L1-foundation/S008-bastion-reachability-validation/` | DESIGN | DESIGN_ONLY |
| S009 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L1-foundation/S009-dns-hostname-resolution-validation/` | DESIGN | DESIGN_ONLY |
| S010 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L1-foundation/S010-evidence-directory-structure-validation/` | DESIGN | DESIGN_ONLY |
| S011 | ZT-4.1.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L2-security-baseline/S011-ssh-key-authentication-validation/` | DESIGN | DESIGN_ONLY |
| S012 | ZT-4.1.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L2-security-baseline/S012-password-login-denial-validation/` | DESIGN | DESIGN_ONLY |
| S013 | ZT-4.1.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L2-security-baseline/S013-root-login-denial-validation/` | DESIGN | DESIGN_ONLY |
| S014 | ZT-3.1.1, ZT-4.1.1, ZT-4.3.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L2-security-baseline/S014-aws-security-group-least-privilege-validation/` | DESIGN | DESIGN_ONLY |
| S015 | ZT-3.1.1, ZT-4.1.1, ZT-4.3.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L2-security-baseline/S015-azure-nsg-least-privilege-validation/` | DESIGN | DESIGN_ONLY |
| S016 | ZT-3.1.1, ZT-4.1.1, ZT-4.3.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L2-security-baseline/S016-openstack-security-group-validation/` | DESIGN | DESIGN_ONLY |
| S017 | ZT-6.2.1, ZT-4.1.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L2-security-baseline/S017-mariadb-access-control-validation/` | DESIGN | DESIGN_ONLY |
| S018 | ZT-5.1.1, ZT-4.1.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L2-security-baseline/S018-kubernetes-rbac-validation/` | DESIGN | DESIGN_ONLY |
| S019 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L2-security-baseline/S019-nginx-security-header-validation/` | DESIGN | DESIGN_ONLY |
| S020 | ZT-4.1.1, ZT-5.1.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L2-security-baseline/S020-grafana-anonymous-access-denial-validation/` | DESIGN | DESIGN_ONLY |
| S021 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L3-service-operations/S021-kubernetes-node-readiness-validation/` | DESIGN | DESIGN_ONLY |
| S022 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L3-service-operations/S022-kubernetes-workload-deployment-validation/` | DESIGN | DESIGN_ONLY |
| S023 | ZT-3.4.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L3-service-operations/S023-ingress-routing-validation/` | DESIGN | DESIGN_ONLY |
| S024 | ZT-3.4.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L3-service-operations/S024-nginx-reverse-proxy-validation/` | DESIGN | DESIGN_ONLY |
| S025 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L3-service-operations/S025-load-balancing-health-check-validation/` | DESIGN | DESIGN_ONLY |
| S026 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L3-service-operations/S026-mariadb-primary-replica-replication-validation/` | DESIGN | DESIGN_ONLY |
| S027 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L3-service-operations/S027-db-replication-lag-validation/` | DESIGN | DESIGN_ONLY |
| S028 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L3-service-operations/S028-prometheus-target-discovery-validation/` | DESIGN | DESIGN_ONLY |
| S029 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L3-service-operations/S029-grafana-dashboard-validation/` | DESIGN | DESIGN_ONLY |
| S030 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L3-service-operations/S030-blackbox-endpoint-probe-validation/` | DESIGN | DESIGN_ONLY |
| S031 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L4-failure-recovery/S031-web-pod-failure-recovery-validation/` | DESIGN | DESIGN_ONLY |
| S032 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L4-failure-recovery/S032-api-service-failure-validation/` | DESIGN | DESIGN_ONLY |
| S033 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L4-failure-recovery/S033-db-replica-failure-validation/` | DESIGN | DESIGN_ONLY |
| S034 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L4-failure-recovery/S034-db-primary-stop-runbook-validation/` | DESIGN | DESIGN_ONLY |
| S035 | ZT-3.5.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L4-failure-recovery/S035-load-balancer-failure-validation/` | DESIGN | DESIGN_ONLY |
| S036 | ZT-7.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L4-failure-recovery/S036-prometheus-target-down-validation/` | DESIGN | DESIGN_ONLY |
| S037 | ZT-3.2.1, ZT-4.4.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L4-failure-recovery/S037-security-rule-misconfiguration-validation/` | DESIGN | DESIGN_ONLY |
| S038 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L4-failure-recovery/S038-backup-creation-validation/` | DESIGN | DESIGN_ONLY |
| S039 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L4-failure-recovery/S039-restore-execution-validation/` | DESIGN | DESIGN_ONLY |
| S040 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L4-failure-recovery/S040-service-health-after-recovery-validation/` | DESIGN | DESIGN_ONLY |
| S041 | ZT-4.4.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L5-governance-intelligent-ops/S041-terraform-drift-detection-validation/` | DESIGN | DESIGN_ONLY |
| S042 | ZT-4.4.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L5-governance-intelligent-ops/S042-terraform-drift-remediation-validation/` | DESIGN | DESIGN_ONLY |
| S043 | ZT-8.1, ZT-4.4.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L5-governance-intelligent-ops/S043-policy-as-code-validation/` | DESIGN | DESIGN_ONLY |
| S044 | ZT-5.4.1, ZT-8.1, ZT-4.4.1 | Scenario definition reviewed; implementation evidence is absent | `scenarios/L5-governance-intelligent-ops/S044-kubernetes-manifest-policy-validation/` | DESIGN | DESIGN_ONLY |
| S045 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L5-governance-intelligent-ops/S045-cost-guardrail-validation/` | DESIGN | DESIGN_ONLY |
| S046 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L5-governance-intelligent-ops/S046-resource-cleanup-validation/` | DESIGN | DESIGN_ONLY |
| S047 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L5-governance-intelligent-ops/S047-ml-metric-dataset-collection-validation/` | DESIGN | DESIGN_ONLY |
| S048 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L5-governance-intelligent-ops/S048-ml-anomaly-detection-validation/` | DESIGN | DESIGN_ONLY |
| S049 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L5-governance-intelligent-ops/S049-ml-anomaly-report-generation-validation/` | DESIGN | DESIGN_ONLY |
| S050 | NOT_MAPPED | Scenario reviewed; no direct source-capability mapping established | `scenarios/L5-governance-intelligent-ops/S050-final-evidence-report-generation-validation/` | DESIGN | DESIGN_ONLY |

Package-level evidence is tracked separately from the locked S001-S050 rows.
ZT-NET-001 contributes Codex-executed sanitized router runtime evidence for
ZT-3.1.1, ZT-3.4.1, ZT-4.1.1, ZT-4.3.1, ZT-7.1, and ZT-8.2 through
`docs/evidence/zero-trust/zt-net-001-validation.yaml`. It is
PARTIALLY_VALIDATED because no persistent interface ACL binding exists.
