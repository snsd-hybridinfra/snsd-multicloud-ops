# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Pre-change security rule baseline validation plan | `commands.md`; `screenshots/security-rule-before-change.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Misconfiguration injection plan | `commands.md`; `logs/security-rule-misconfiguration-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Public SSH exposure detection validation plan | `commands.md`; `configs/security-rule-misconfiguration-summary.md`; `validation.md` | command plan, misconfiguration summary, validation record | yes |
| Public DB exposure detection validation plan | `commands.md`; `configs/security-rule-misconfiguration-summary.md`; `validation.md` | command plan, misconfiguration summary, validation record | yes |
| Overly broad CIDR detection validation plan | `commands.md`; `screenshots/security-rule-during-misconfiguration.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Required service access breakage detection validation plan | `commands.md`; `logs/security-rule-misconfiguration-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Unauthorized source access test validation plan | `commands.md`; `configs/security-rule-misconfiguration-summary.md`; `validation.md` | command plan, misconfiguration summary, validation record | yes |
| Authorized source access test validation plan | `commands.md`; `configs/security-rule-misconfiguration-summary.md`; `validation.md` | command plan, misconfiguration summary, validation record | yes |
| Manual rollback decision point validation plan | `commands.md`; `configs/security-rule-rollback-decision-points.md`; `validation.md` | command plan, rollback decision summary, validation record | yes |
| Post-rollback security rule validation plan | `commands.md`; `screenshots/security-rule-after-rollback.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Post-rollback service reachability validation plan | `commands.md`; `logs/security-rule-misconfiguration-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Detection and recovery time measurement plan | `commands.md`; `configs/security-rule-recovery-threshold.md`; `validation.md` | command plan, threshold summary, validation record | yes |
| Failure condition for misconfiguration not detected, unauthorized exposure remaining, required access not restored, rollback unclear, recovery threshold exceeded, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real cloud firewall, security group, NSG, OpenStack security group, or On-Prem firewall output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
