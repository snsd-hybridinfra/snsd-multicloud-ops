# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Pre-failure Prometheus service status validation plan | Plan status check for `<prometheus-endpoint>`. | Prometheus service is reachable before target failure. | `commands.md`, `logs/prometheus-target-down-validation.log`, `validation.md` |
| V002 | Pre-failure target UP status validation plan | Review `/targets` or query evidence for `<target-job>`. | Selected target is UP before failure. | `commands.md`, `screenshots/prometheus-target-before-failure.png`, `validation.md` |
| V003 | Target failure injection plan | Plan one exporter or endpoint outage using placeholder commands. | Failure injection targets one monitored target only. | `commands.md`, `logs/prometheus-target-down-validation.log`, `validation.md` |
| V004 | Prometheus `/targets` DOWN status validation plan | Review `/targets` state during failure. | Selected target appears DOWN in Prometheus. | `commands.md`, `screenshots/prometheus-target-during-failure.png`, `validation.md` |
| V005 | Prometheus `up{job="<target-job>"}` query validation plan | Plan query against `<target-job>` and `<target-instance>`. | Query reflects target DOWN state. | `commands.md`, `configs/prometheus-query-mapping.md`, `validation.md` |
| V006 | Target failure timestamp capture plan | Record timestamps for failure action and DOWN observation. | Failure detection time can be measured. | `commands.md`, `configs/prometheus-target-down-summary.md`, `validation.md` |
| V007 | Exporter or endpoint restoration validation plan | Plan restoration using placeholder action. | Restoration path is documented. | `commands.md`, `logs/prometheus-target-down-validation.log`, `validation.md` |
| V008 | Post-recovery target UP status validation plan | Review `/targets` state after restoration. | Selected target returns to UP. | `commands.md`, `screenshots/prometheus-target-after-recovery.png`, `validation.md` |
| V009 | Detection time measurement plan | Compare failure timestamp and DOWN observation timestamp. | Detection time is recorded and compared with thresholds. | `commands.md`, `configs/prometheus-target-down-threshold.md`, `validation.md` |
| V010 | Recovery time measurement plan | Compare restoration action and recovered UP observation timestamp. | Recovery time is recorded and compared with thresholds. | `commands.md`, `configs/prometheus-target-down-threshold.md`, `validation.md` |
| V011 | Failure condition for target DOWN not detected, invalid scrape config, missing target label, target remains DOWN after recovery, recovery threshold exceeded, or missing evidence | Evaluate findings against explicit failure conditions. | Target DOWN detection issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates Prometheus target DOWN detection only; target discovery is handled in S028, Grafana dashboard validation in S029, Blackbox endpoint probing in S030, and Alertmanager integration is excluded.
