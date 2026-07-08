# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| grafana.ini anonymous access setting validation plan | `commands.md`; `configs/grafana-anonymous-access-summary.md`; `validation.md` | command plan, access summary, validation record | yes |
| Grafana effective configuration validation plan | `commands.md`; `configs/grafana-security-policy.md`; `validation.md` | command plan, security policy, validation record | yes |
| Unauthenticated dashboard access denial validation plan | `commands.md`; `logs/grafana-access-validation.log`; `screenshots/grafana-anonymous-access-denied.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Login page requirement validation plan | `commands.md`; `screenshots/grafana-login-required.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Anonymous API access denial validation plan | `commands.md`; `logs/grafana-access-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Grafana admin password not stored in repository validation plan | `commands.md`; `configs/grafana-security-policy.md`; `validation.md` | command plan, security policy, validation record | yes |
| Monitoring Zone access boundary validation plan | `commands.md`; `configs/grafana-anonymous-access-summary.md`; `validation.md` | command plan, access summary, validation record | yes |
| Grafana access log capture plan | `commands.md`; `logs/grafana-access-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Failure condition for anonymous access enabled, dashboard public exposure, stored admin password, or unexplained access success | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Grafana output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
