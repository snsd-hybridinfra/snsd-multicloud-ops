# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Pre-failure Prometheus service status validation plan | `commands.md`; `logs/prometheus-target-down-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Pre-failure target UP status validation plan | `commands.md`; `screenshots/prometheus-target-before-failure.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Target failure injection plan | `commands.md`; `logs/prometheus-target-down-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Prometheus `/targets` DOWN status validation plan | `commands.md`; `screenshots/prometheus-target-during-failure.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Prometheus `up{job="<target-job>"}` query validation plan | `commands.md`; `configs/prometheus-query-mapping.md`; `validation.md` | command plan, query mapping, validation record | yes |
| Target failure timestamp capture plan | `commands.md`; `configs/prometheus-target-down-summary.md`; `validation.md` | command plan, target summary, validation record | yes |
| Exporter or endpoint restoration validation plan | `commands.md`; `logs/prometheus-target-down-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Post-recovery target UP status validation plan | `commands.md`; `screenshots/prometheus-target-after-recovery.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Detection time measurement plan | `commands.md`; `configs/prometheus-target-down-threshold.md`; `validation.md` | command plan, threshold summary, validation record | yes |
| Recovery time measurement plan | `commands.md`; `configs/prometheus-target-down-threshold.md`; `validation.md` | command plan, threshold summary, validation record | yes |
| Failure condition for target DOWN not detected, invalid scrape config, missing target label, target remains DOWN after recovery, recovery threshold exceeded, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Prometheus target state, query, or exporter output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
