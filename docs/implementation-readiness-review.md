# Implementation Readiness Review

> Superseded status note (2026-07-15): no scenario is currently implemented or
> runtime-validated. Current authoritative status is maintained in
> `docs/scenario-status-matrix.md` and `docs/evidence-status-matrix.md`.

Readiness date: 2026-07-10

## Classification Basis

Every scenario passes local structure, metadata, Included/Excluded scope, validation-table, and evidence-map checks. Each scenario is conservatively classified `NEEDS_SCOPE_CLARIFICATION` because `docs/scenario-model.md` and `docs/naming-rules.md` define legacy IDs and scenario titles that conflict with the implemented retired numbered scenario framework repository.

| Scenario ID | Scenario Name | Level | Readiness Status | Reason | Recommended Next Action |
|---|---|---|---|---|---|
| retired-numbered-case | control-plane-toolchain-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate the local toolchain |
| retired-numbered-case | eve-ng-onprem-routing-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then implement after retired-numbered-case evidence |
| retired-numbered-case | aws-network-provisioning-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then implement approved AWS placeholders |
| retired-numbered-case | azure-network-provisioning-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then implement approved Azure placeholders |
| retired-numbered-case | openstack-network-provisioning-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then implement approved OpenStack placeholders |
| retired-numbered-case | terraform-provider-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate provider structure without credentials |
| retired-numbered-case | multi-cloud-inventory-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then implement sanitized inventory structure |
| retired-numbered-case | bastion-reachability-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate placeholder access paths |
| retired-numbered-case | dns-hostname-resolution-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate placeholder hostname mapping |
| retired-numbered-case | evidence-directory-structure-validation | L1 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then execute repository evidence checks |
| retired-numbered-case | ssh-key-authentication-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate key authentication safely |
| retired-numbered-case | password-login-denial-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate password denial |
| retired-numbered-case | root-login-denial-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate root login denial |
| retired-numbered-case | aws-security-group-least-privilege-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate AWS baseline rules |
| retired-numbered-case | azure-nsg-least-privilege-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate Azure baseline rules |
| retired-numbered-case | openstack-security-group-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate OpenStack baseline rules |
| retired-numbered-case | mariadb-access-control-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate access control only |
| retired-numbered-case | kubernetes-rbac-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate RBAC without secrets |
| retired-numbered-case | nginx-security-header-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate header baseline |
| retired-numbered-case | grafana-anonymous-access-denial-validation | L2 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate anonymous access denial |
| retired-numbered-case | kubernetes-node-readiness-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate node readiness |
| retired-numbered-case | kubernetes-workload-deployment-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate workload deployment |
| retired-numbered-case | ingress-routing-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate Ingress routing only |
| retired-numbered-case | nginx-reverse-proxy-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate proxy forwarding only |
| retired-numbered-case | load-balancing-health-check-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate backend health only |
| retired-numbered-case | mariadb-primary-replica-replication-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate replication function |
| retired-numbered-case | db-replication-lag-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate provisional lag thresholds |
| retired-numbered-case | prometheus-target-discovery-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate target discovery |
| retired-numbered-case | grafana-dashboard-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate dashboard rendering |
| retired-numbered-case | blackbox-endpoint-probe-validation | L3 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate endpoint probes |
| retired-numbered-case | web-pod-failure-recovery-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then run controlled pod recovery |
| retired-numbered-case | api-service-failure-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then run controlled API failure |
| retired-numbered-case | db-replica-failure-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then run controlled replica failure |
| retired-numbered-case | db-primary-stop-runbook-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate the manual stop runbook |
| retired-numbered-case | load-balancer-failure-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate manual entrypoint recovery |
| retired-numbered-case | prometheus-target-down-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate target-DOWN detection |
| retired-numbered-case | security-rule-misconfiguration-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate controlled rollback |
| retired-numbered-case | backup-creation-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate sanitized backup creation |
| retired-numbered-case | restore-execution-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate restore execution |
| retired-numbered-case | service-health-after-recovery-validation | L4 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate post-recovery health |
| retired-numbered-case | terraform-drift-detection-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate drift detection only |
| retired-numbered-case | terraform-drift-remediation-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate approved manual remediation |
| retired-numbered-case | policy-as-code-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate policy review without enforcement |
| retired-numbered-case | kubernetes-manifest-policy-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate static manifest policy |
| retired-numbered-case | cost-guardrail-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate placeholder cost guardrails |
| retired-numbered-case | resource-cleanup-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate approved cleanup planning |
| retired-numbered-case | ml-metric-dataset-collection-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate sanitized metric collection |
| retired-numbered-case | ml-anomaly-detection-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate bounded anomaly logic |
| retired-numbered-case | ml-anomaly-report-generation-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate human-reviewed reporting |
| retired-numbered-case | final-evidence-report-generation-validation | L5 | NEEDS_SCOPE_CLARIFICATION | Local QA passed; canonical model does not define retired-numbered-case | Align canonical model and naming, then validate aggregate reporting only |

## Summary

| Readiness Status | Count |
|---|---:|
| READY_FOR_IMPLEMENTATION | 0 |
| NEEDS_SCOPE_CLARIFICATION | 50 |
| NEEDS_EVIDENCE_MAPPING_FIX | 0 |
| NEEDS_BOUNDARY_FIX | 0 |
| BLOCKED | 0 |

After the canonical model, naming rule, and status vocabulary are aligned, re-run the quality validator. If it passes, retired-numbered-case is the recommended first implementation scenario.
