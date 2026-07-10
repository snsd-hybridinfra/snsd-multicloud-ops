# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Web service HTTP response post-recovery validation plan | Plan HTTP response check for `<web-endpoint>`. | Web service is reachable after recovery. | `commands.md`, `screenshots/service-health-after-recovery-web-api.png`, `validation.md` |
| V002 | API service HTTP response post-recovery validation plan | Plan HTTP response check for `<api-endpoint>`. | API service is reachable after recovery. | `commands.md`, `screenshots/service-health-after-recovery-web-api.png`, `validation.md` |
| V003 | Ingress route post-recovery validation plan | Plan route check for `<ingress-host>`. | Ingress route resolves to expected service path. | `commands.md`, `logs/service-health-after-recovery-validation.log`, `validation.md` |
| V004 | Nginx Reverse Proxy post-recovery validation plan | Plan response check for `<reverse-proxy-host>`. | Reverse proxy returns expected response after recovery. | `commands.md`, `logs/service-health-after-recovery-validation.log`, `validation.md` |
| V005 | Load balancing health endpoint post-recovery validation plan | Plan health check for `<health-endpoint>`. | Health endpoint reports healthy state. | `commands.md`, `configs/post-recovery-checklist.md`, `validation.md` |
| V006 | MariaDB Primary availability reference validation plan | Reference `<db-primary-host>` availability evidence. | DB Primary dependency is available or explicitly marked degraded. | `commands.md`, `configs/service-health-after-recovery-summary.md`, `validation.md` |
| V007 | MariaDB Replica state reference validation plan | Reference `<db-replica-host>` state evidence. | DB Replica state is reviewable or explicitly marked degraded. | `commands.md`, `configs/service-health-after-recovery-summary.md`, `validation.md` |
| V008 | Prometheus target UP post-recovery validation plan | Review Prometheus target state for recovered components. | Required targets are UP or missing evidence is marked. | `commands.md`, `screenshots/service-health-after-recovery-monitoring.png`, `validation.md` |
| V009 | Grafana dashboard visibility post-recovery validation plan | Review dashboard visibility at `<grafana-endpoint>`. | Required dashboards are visible or issue is documented. | `commands.md`, `screenshots/service-health-after-recovery-monitoring.png`, `validation.md` |
| V010 | Blackbox `probe_success` post-recovery validation plan | Review probe success for service endpoints. | Recovered endpoints pass Blackbox probe checks. | `commands.md`, `configs/post-recovery-checklist.md`, `validation.md` |
| V011 | Final service recovery judgment validation plan | Compare evidence with judgment states. | Final judgment is `RECOVERED`, `DEGRADED`, `FAILED`, or `INCONCLUSIVE`. | `commands.md`, `configs/post-recovery-judgment-model.md`, `screenshots/service-health-after-recovery-final-judgment.png`, `validation.md` |
| V012 | Failure condition for Web/API unavailable, DB dependency unavailable, monitoring visibility missing, Blackbox probe failed, inconsistent recovery evidence, degraded state not documented, or missing final judgment | Evaluate findings against explicit failure conditions. | Final recovery issues produce `FAILED`, `DEGRADED`, or `INCONCLUSIVE` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates post-recovery service health only; backup creation, restore execution, and individual failure scenarios are handled separately.
