# Validation

Scenario: S040-service-health-after-recovery-validation
Level: L4-failure-recovery
Capability: Service Health After Recovery Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real post-recovery service output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Web service HTTP response post-recovery validation plan | Web service is reachable after recovery. | TODO | NOT_RUN | `commands.md`; `screenshots/service-health-after-recovery-web-api.png` |
| V002 | API service HTTP response post-recovery validation plan | API service is reachable after recovery. | TODO | NOT_RUN | `commands.md`; `screenshots/service-health-after-recovery-web-api.png` |
| V003 | Ingress route post-recovery validation plan | Ingress route resolves to expected service path. | TODO | NOT_RUN | `commands.md`; `logs/service-health-after-recovery-validation.log` |
| V004 | Nginx Reverse Proxy post-recovery validation plan | Reverse proxy returns expected response after recovery. | TODO | NOT_RUN | `commands.md`; `logs/service-health-after-recovery-validation.log` |
| V005 | Load balancing health endpoint post-recovery validation plan | Health endpoint reports healthy state. | TODO | NOT_RUN | `commands.md`; `configs/post-recovery-checklist.md` |
| V006 | MariaDB Primary availability reference validation plan | DB Primary dependency is available or explicitly marked degraded. | TODO | NOT_RUN | `commands.md`; `configs/service-health-after-recovery-summary.md` |
| V007 | MariaDB Replica state reference validation plan | DB Replica state is reviewable or explicitly marked degraded. | TODO | NOT_RUN | `commands.md`; `configs/service-health-after-recovery-summary.md` |
| V008 | Prometheus target UP post-recovery validation plan | Required targets are UP or missing evidence is marked. | TODO | NOT_RUN | `commands.md`; `screenshots/service-health-after-recovery-monitoring.png` |
| V009 | Grafana dashboard visibility post-recovery validation plan | Required dashboards are visible or issue is documented. | TODO | NOT_RUN | `commands.md`; `screenshots/service-health-after-recovery-monitoring.png` |
| V010 | Blackbox `probe_success` post-recovery validation plan | Recovered endpoints pass Blackbox probe checks. | TODO | NOT_RUN | `commands.md`; `configs/post-recovery-checklist.md` |
| V011 | Final service recovery judgment validation plan | Final judgment is `RECOVERED`, `DEGRADED`, `FAILED`, or `INCONCLUSIVE`. | TODO | NOT_RUN | `commands.md`; `configs/post-recovery-judgment-model.md`; `screenshots/service-health-after-recovery-final-judgment.png` |
| V012 | Failure condition for Web/API unavailable, DB dependency unavailable, monitoring visibility missing, Blackbox probe failed, inconsistent recovery evidence, degraded state not documented, or missing final judgment | Final recovery issues produce `FAILED`, `DEGRADED`, or `INCONCLUSIVE` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Service health after recovery summary is captured: NOT_READY
- Post-recovery judgment model is captured: NOT_READY
- Post-recovery checklist is captured: NOT_READY
- Service health after recovery validation log is captured: NOT_READY
- Web/API, monitoring, and final judgment screenshots are captured: NOT_READY

## Judgment States

- `RECOVERED`: all required service checks pass.
- `DEGRADED`: core service is reachable but one or more non-critical checks fail.
- `FAILED`: core service, DB dependency, or monitoring visibility remains unavailable.
- `INCONCLUSIVE`: required evidence is missing.

## Boundary Notes

This scenario validates post-recovery service health only. It does not claim automatic DR, production-grade HA, automatic cross-cloud failover, or enterprise recovery orchestration.
