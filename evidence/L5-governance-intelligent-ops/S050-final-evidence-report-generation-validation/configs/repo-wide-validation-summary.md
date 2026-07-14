# Repository-Wide Validation Summary

- Generated: 2026-07-14T10:13:51+09:00
- Mode: **StaticOnly**
- Final result: **PASS**
- Integration failures: **0**
- Validator failures: **0**
- Non-blocking validator warnings: **32**

## Integration Checks

| Check | Status | Detail |
|---|---|---|
| ScenarioCoverage | PASS | Expected locked S001-S050 scenario paths exist exactly once. |
| EvidenceCoverage | PASS | Evidence paths mirror the locked scenario paths. |
| ScenarioRequiredDocs | PASS | All scenarios contain the 11 required documents. |
| EvidenceRequiredItems | PASS | All evidence directories contain commands, validation, logs, screenshots, and configs. |
| ScenarioStatusModel | PASS | Scenario matrix uses only canonical scenario statuses. |
| EvidenceStatusModel | PASS | Evidence matrix uses only canonical readiness statuses. |
| CrossScenarioReferences | PASS | Required ownership and hand-off references are present. |
| ValidatorCoverage | PASS | Discovered 50 scenario-specific local validators. |

## Validator Results

| Validator | Status | Exit Code | Warnings |
|---|---|---:|---:|
| validate-repo-structure.ps1 | PASS | 0 | 0 |
| validate-scenario-quality.ps1 | PASS | 0 | 0 |
| validate-api-service-failure.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-aws-network-provisioning.ps1 | PASS_WITH_WARNINGS | 0 | 2 |
| validate-aws-security-group-least-privilege.ps1 | PASS | 0 | 0 |
| validate-azure-network-provisioning.ps1 | PASS_WITH_WARNINGS | 0 | 2 |
| validate-azure-nsg-least-privilege.ps1 | PASS | 0 | 0 |
| validate-backup-creation.ps1 | PASS | 0 | 0 |
| validate-bastion-reachability-model.ps1 | PASS | 0 | 0 |
| validate-blackbox-endpoint-probe.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-control-plane-toolchain.ps1 | PASS_WITH_WARNINGS | 0 | 4 |
| validate-cost-guardrail.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-db-primary-stop-runbook.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-db-replica-failure.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-db-replication-lag.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-dns-hostname-resolution-model.ps1 | PASS | 0 | 0 |
| validate-eve-ng-routing-baseline.ps1 | PASS | 0 | 0 |
| validate-evidence-directory-structure.ps1 | PASS | 0 | 0 |
| validate-final-evidence-report.ps1 | PASS | 0 | 0 |
| validate-grafana-anonymous-access-denial.ps1 | PASS | 0 | 0 |
| validate-grafana-dashboard.ps1 | PASS | 0 | 0 |
| validate-ingress-routing.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-kubernetes-manifest-policy.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-kubernetes-node-readiness.ps1 | PASS | 0 | 0 |
| validate-kubernetes-rbac-baseline.ps1 | PASS | 0 | 0 |
| validate-kubernetes-workload-deployment.ps1 | PASS | 0 | 0 |
| validate-load-balancer-failure.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-load-balancing-health-check.ps1 | PASS | 0 | 0 |
| validate-mariadb-access-control-baseline.ps1 | PASS | 0 | 0 |
| validate-mariadb-primary-replica-replication.ps1 | PASS | 0 | 0 |
| validate-ml-anomaly-detection.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-ml-anomaly-report-generation.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-ml-metric-dataset-collection.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-multicloud-inventory.ps1 | PASS | 0 | 0 |
| validate-nginx-reverse-proxy.ps1 | PASS | 0 | 0 |
| validate-nginx-security-header-baseline.ps1 | PASS | 0 | 0 |
| validate-openstack-network-provisioning.ps1 | PASS_WITH_WARNINGS | 0 | 2 |
| validate-openstack-security-group-baseline.ps1 | PASS | 0 | 0 |
| validate-policy-as-code.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-prometheus-target-discovery.ps1 | PASS | 0 | 0 |
| validate-prometheus-target-down.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-resource-cleanup.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-restore-execution.ps1 | PASS | 0 | 0 |
| validate-security-rule-misconfiguration.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-service-health-after-recovery.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-ssh-key-authentication-baseline.ps1 | PASS | 0 | 0 |
| validate-ssh-password-login-denial-baseline.ps1 | PASS | 0 | 0 |
| validate-ssh-root-login-denial-baseline.ps1 | PASS | 0 | 0 |
| validate-terraform-drift-detection.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-terraform-drift-remediation.ps1 | PASS_WITH_WARNINGS | 0 | 1 |
| validate-terraform-provider-baseline.ps1 | PASS_WITH_WARNINGS | 0 | 2 |
| validate-web-pod-failure-recovery.ps1 | PASS_WITH_WARNINGS | 0 | 1 |

This wrapper runs local PowerShell validators in static-only mode. It does not run Terraform, kubectl, cloud CLIs, live monitoring queries, or external infrastructure checks.
