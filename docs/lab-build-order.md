# Lab Phase 1 Build Order

## Purpose and Rules

The build order converts the locked S001-S050 repository model into a controlled non-production evidence-collection sequence. Each phase must complete its local checks and sanitization review before the next phase begins. Commands listed below are references for later collection; they are not executed by this document.

## Phase 0: Repository Validator Baseline

- **Goal:** Establish a clean repository baseline before any VM is prepared.
- **Related scenarios:** S001, S006, S010, S041-S050.
- **Commands to collect later:** `tools\validate-repo-structure.ps1`, `tools\validate-scenario-quality.ps1`, `tools\validate-all-scenarios.ps1`.
- **Evidence output:** S001, S006, S010, and S050 matching `logs/` and `configs/` directories.
- **Completion criteria:** Base validators pass, scenario/evidence coverage is 50/50, and no unsafe file is present.

## Phase 1: Virtual Lab Architecture and VM Preparation

- **Goal:** Prepare the minimum bastion, k3s, database, and monitoring VM roles on `<lab-network-placeholder>`.
- **Related scenarios:** S002-S007 and S009.
- **Commands to collect later:** hypervisor inventory, VM state, sanitized interface summary, sanitized route summary, and local hostname mapping commands appropriate to the disposable lab.
- **Evidence output:** `evidence/L1-foundation/<scenario>/logs/`, `screenshots/`, and `configs/`.
- **Completion criteria:** Every planned role exists, role ownership is documented, and committed outputs use placeholders instead of real addresses or hostnames.

## Phase 2: Bastion Reachability

- **Goal:** Confirm the planned management path through `bastion-vm` and document least-privilege access boundaries.
- **Related scenarios:** S008, S011-S016, and S037.
- **Commands to collect later:** sanitized SSH verbose result, reachability result, route/path summary, and security-rule read-only output from the disposable lab.
- **Evidence output:** matching L1, L2, and S037 evidence directories.
- **Completion criteria:** Approved bastion path succeeds, prohibited direct paths are documented, and no key, username, real address, or provider identifier is committed.

## Phase 3: k3s and Sample Service

- **Goal:** Deploy a disposable sample service and collect Kubernetes readiness, workload, ingress, proxy, and health evidence.
- **Related scenarios:** S018, S021-S025, S031-S032, S035, and S044.
- **Commands to collect later:** `kubectl get nodes`, `kubectl get pods -A`, `kubectl get service -A`, `kubectl get ingress -A`, and sanitized application health output.
- **Evidence output:** matching L2, L3, L4, and L5 scenario evidence paths.
- **Completion criteria:** Sample workloads are replaceable, required states are captured, kubeconfig and tokens remain outside the repository, and outputs are sanitized.

## Phase 4: MariaDB Primary/Replica

- **Goal:** Configure a synthetic-data MariaDB primary/replica pair for access, replication, lag, backup, and recovery evidence.
- **Related scenarios:** S017, S026-S027, S033-S034, and S038-S040.
- **Commands to collect later:** sanitized service status, replication status, lag measurement, synthetic consistency query, backup metadata, and restore verification.
- **Evidence output:** matching L2, L3, and L4 scenario evidence paths.
- **Completion criteria:** Replication is observable, only synthetic data is used, credentials/dumps are excluded, and rollback/recovery steps are recorded.

## Phase 5: Prometheus/Grafana/Blackbox

- **Goal:** Observe lab-only nodes, services, endpoints, and database behavior through the approved monitoring stack.
- **Related scenarios:** S019-S020, S028-S030, S036, S040, and S047.
- **Commands to collect later:** sanitized target status, selected metric queries, Blackbox probe results, dashboard inventory, and exporter status.
- **Evidence output:** matching L2-L5 scenario evidence paths, with screenshots placed in each scenario's `screenshots/` directory.
- **Completion criteria:** Required targets are represented, screenshots are masked, authentication data is excluded, and raw production-style exports are not committed.

## Phase 6: Failure and Recovery Experiments

- **Goal:** Run controlled disposable failures and prove documented recovery without automatic production actions.
- **Related scenarios:** S031-S040.
- **Commands to collect later:** pre-check, manual failure action record, detection output, rollback/recovery action record, and post-recovery health checks.
- **Evidence output:** `evidence/L4-failure-recovery/<scenario>/`.
- **Completion criteria:** Preconditions and rollback are recorded, post-recovery state is safe, and experiments remain confined to the disposable lab.

## Phase 7: Governance Evidence

- **Goal:** Compare sanitized lab state with the existing drift, policy, cost, cleanup, and evidence-governance models.
- **Related scenarios:** S037 and S041-S046, with aggregation in S050.
- **Commands to collect later:** local plan/config comparison, policy checklist, ownership/tag review, cleanup candidate review, and repository evidence completeness checks.
- **Evidence output:** matching L4/L5 evidence directories.
- **Completion criteria:** Governance judgments reference sanitized inputs, remediation remains controlled, and no provider billing or live account data is committed.

## Phase 8: ML Metric Dataset Evidence

- **Goal:** Produce a sanitized or synthetic metric dataset and deterministic anomaly/report evidence.
- **Related scenarios:** S047-S049.
- **Commands to collect later:** bounded metric export, schema validation, deterministic anomaly detection, and report generation commands already documented by those scenarios.
- **Evidence output:** `evidence/L5-governance-intelligent-ops/S047-*`, `S048-*`, and `S049-*`.
- **Completion criteria:** Dataset fields follow the documented schema, labels and endpoints are masked, no logs/packets/security telemetry are introduced, and human review remains explicit.

## Phase 9: Final Evidence Report Regeneration

- **Goal:** Recalculate repository coverage after sanitized lab evidence is added.
- **Related scenarios:** S050, aggregating S001-S050.
- **Commands to collect later:** `tools\generate-final-evidence-report.ps1`, `tools\validate-final-evidence-report.ps1`, and `tools\validate-all-scenarios.ps1`.
- **Evidence output:** `evidence/L5-governance-intelligent-ops/S050-final-evidence-report-generation-validation/`.
- **Completion criteria:** Final local report is regenerated, repository validators pass, missing/live-unvalidated work remains visible, and no certification claim is made.
