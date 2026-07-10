# Validation

Scenario: S036-prometheus-target-down-validation
Level: L4-failure-recovery
Capability: Prometheus Target DOWN Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Prometheus target state, query, or exporter output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Pre-failure Prometheus service status validation plan | Prometheus service is reachable before target failure. | TODO | NOT_RUN | `commands.md`; `logs/prometheus-target-down-validation.log` |
| V002 | Pre-failure target UP status validation plan | Selected target is UP before failure. | TODO | NOT_RUN | `commands.md`; `screenshots/prometheus-target-before-failure.png` |
| V003 | Target failure injection plan | Failure injection targets one monitored target only. | TODO | NOT_RUN | `commands.md`; `logs/prometheus-target-down-validation.log` |
| V004 | Prometheus `/targets` DOWN status validation plan | Selected target appears DOWN in Prometheus. | TODO | NOT_RUN | `commands.md`; `screenshots/prometheus-target-during-failure.png` |
| V005 | Prometheus `up{job="<target-job>"}` query validation plan | Query reflects target DOWN state. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-query-mapping.md` |
| V006 | Target failure timestamp capture plan | Failure detection time can be measured. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-target-down-summary.md` |
| V007 | Exporter or endpoint restoration validation plan | Restoration path is documented. | TODO | NOT_RUN | `commands.md`; `logs/prometheus-target-down-validation.log` |
| V008 | Post-recovery target UP status validation plan | Selected target returns to UP. | TODO | NOT_RUN | `commands.md`; `screenshots/prometheus-target-after-recovery.png` |
| V009 | Detection time measurement plan | Detection time is recorded and compared with thresholds. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-target-down-threshold.md` |
| V010 | Recovery time measurement plan | Recovery time is recorded and compared with thresholds. | TODO | NOT_RUN | `commands.md`; `configs/prometheus-target-down-threshold.md` |
| V011 | Failure condition for target DOWN not detected, invalid scrape config, missing target label, target remains DOWN after recovery, recovery threshold exceeded, or missing evidence | Target DOWN detection issues produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Prometheus target DOWN summary is captured: NOT_READY
- Prometheus target DOWN threshold summary is captured: NOT_READY
- Prometheus query mapping is captured: NOT_READY
- Prometheus target DOWN validation log is captured: NOT_READY
- Before, during, and after screenshots are captured: NOT_READY

## Provisional Detection and Recovery Thresholds

- DETECTED: target DOWN visible within `< 60 seconds`.
- WARNING: target recovery visible within `60-300 seconds`.
- CRITICAL: target remains DOWN or recovery exceeds `300 seconds`.

## Boundary Notes

This scenario validates target DOWN detection through Prometheus target state and query evidence only. It does not claim Alertmanager integration, automated alert notification, or SOAR-style response.
