# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Pre-change security rule baseline validation plan | Review placeholder rule baseline. | Baseline rule state is documented before misconfiguration. | `commands.md`, `screenshots/security-rule-before-change.png`, `validation.md` |
| V002 | Misconfiguration injection plan | Plan one placeholder rule misconfiguration. | Misconfiguration is controlled and scoped to the selected rule. | `commands.md`, `logs/security-rule-misconfiguration-validation.log`, `validation.md` |
| V003 | Public SSH exposure detection validation plan | Review rule pattern for broad SSH exposure. | Public SSH exposure placeholder is detected. | `commands.md`, `configs/security-rule-misconfiguration-summary.md`, `validation.md` |
| V004 | Public DB exposure detection validation plan | Review rule pattern for broad DB exposure. | Public DB exposure placeholder is detected. | `commands.md`, `configs/security-rule-misconfiguration-summary.md`, `validation.md` |
| V005 | Overly broad CIDR detection validation plan | Review `<unauthorized-cidr>` and inbound scope. | Overly broad inbound CIDR placeholder is detected. | `commands.md`, `screenshots/security-rule-during-misconfiguration.png`, `validation.md` |
| V006 | Required service access breakage detection validation plan | Review missing or incorrect required service rule. | Required service access breakage is detected. | `commands.md`, `logs/security-rule-misconfiguration-validation.log`, `validation.md` |
| V007 | Unauthorized source access test validation plan | Plan access check from `<unauthorized-cidr>`. | Unauthorized source behavior is documented. | `commands.md`, `configs/security-rule-misconfiguration-summary.md`, `validation.md` |
| V008 | Authorized source access test validation plan | Plan access check from `<allowed-cidr>`. | Authorized source behavior is documented. | `commands.md`, `configs/security-rule-misconfiguration-summary.md`, `validation.md` |
| V009 | Manual rollback decision point validation plan | Review rollback decision point checklist. | Rollback decision points are explicit and manual. | `commands.md`, `configs/security-rule-rollback-decision-points.md`, `validation.md` |
| V010 | Post-rollback security rule validation plan | Review rule state after rollback. | Rule state returns to approved baseline. | `commands.md`, `screenshots/security-rule-after-rollback.png`, `validation.md` |
| V011 | Post-rollback service reachability validation plan | Review required service access after rollback. | Required service reachability is restored. | `commands.md`, `logs/security-rule-misconfiguration-validation.log`, `validation.md` |
| V012 | Detection and recovery time measurement plan | Compare misconfiguration, detection, rollback, and restored-state timestamps. | Detection and rollback timing is recorded and compared with thresholds. | `commands.md`, `configs/security-rule-recovery-threshold.md`, `validation.md` |
| V013 | Failure condition for misconfiguration not detected, unauthorized exposure remaining, required access not restored, rollback unclear, recovery threshold exceeded, or missing evidence | Evaluate findings against explicit failure conditions. | Misconfiguration recovery issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates controlled misconfiguration detection and manual rollback only; it does not provide real-time blocking, WAF, IDS/IPS, EDR, SOAR, or CSPM capability.
