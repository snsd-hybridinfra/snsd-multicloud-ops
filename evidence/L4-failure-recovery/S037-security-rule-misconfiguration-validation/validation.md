# Validation

Scenario: S037-security-rule-misconfiguration-validation
Level: L4-failure-recovery
Capability: Security Rule Misconfiguration Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real cloud firewall, security group, NSG, OpenStack security group, or On-Prem firewall output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Pre-change security rule baseline validation plan | Baseline rule state is documented before misconfiguration. | TODO | NOT_RUN | `commands.md`; `screenshots/security-rule-before-change.png` |
| V002 | Misconfiguration injection plan | Misconfiguration is controlled and scoped to the selected rule. | TODO | NOT_RUN | `commands.md`; `logs/security-rule-misconfiguration-validation.log` |
| V003 | Public SSH exposure detection validation plan | Public SSH exposure placeholder is detected. | TODO | NOT_RUN | `commands.md`; `configs/security-rule-misconfiguration-summary.md` |
| V004 | Public DB exposure detection validation plan | Public DB exposure placeholder is detected. | TODO | NOT_RUN | `commands.md`; `configs/security-rule-misconfiguration-summary.md` |
| V005 | Overly broad CIDR detection validation plan | Overly broad inbound CIDR placeholder is detected. | TODO | NOT_RUN | `commands.md`; `screenshots/security-rule-during-misconfiguration.png` |
| V006 | Required service access breakage detection validation plan | Required service access breakage is detected. | TODO | NOT_RUN | `commands.md`; `logs/security-rule-misconfiguration-validation.log` |
| V007 | Unauthorized source access test validation plan | Unauthorized source behavior is documented. | TODO | NOT_RUN | `commands.md`; `configs/security-rule-misconfiguration-summary.md` |
| V008 | Authorized source access test validation plan | Authorized source behavior is documented. | TODO | NOT_RUN | `commands.md`; `configs/security-rule-misconfiguration-summary.md` |
| V009 | Manual rollback decision point validation plan | Rollback decision points are explicit and manual. | TODO | NOT_RUN | `commands.md`; `configs/security-rule-rollback-decision-points.md` |
| V010 | Post-rollback security rule validation plan | Rule state returns to approved baseline. | TODO | NOT_RUN | `commands.md`; `screenshots/security-rule-after-rollback.png` |
| V011 | Post-rollback service reachability validation plan | Required service reachability is restored. | TODO | NOT_RUN | `commands.md`; `logs/security-rule-misconfiguration-validation.log` |
| V012 | Detection and recovery time measurement plan | Detection and rollback timing is recorded and compared with thresholds. | TODO | NOT_RUN | `commands.md`; `configs/security-rule-recovery-threshold.md` |
| V013 | Failure condition for misconfiguration not detected, unauthorized exposure remaining, required access not restored, rollback unclear, recovery threshold exceeded, or missing evidence | Misconfiguration recovery issues produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Security rule misconfiguration summary is captured: NOT_READY
- Security rule recovery threshold summary is captured: NOT_READY
- Security rule rollback decision points are captured: NOT_READY
- Security rule misconfiguration validation log is captured: NOT_READY
- Before, during, and after screenshots are captured: NOT_READY

## Provisional Detection and Recovery Thresholds

- DETECTED: misconfiguration identified within `< 60 seconds`.
- WARNING: rollback completed within `60-300 seconds`.
- CRITICAL: unauthorized exposure remains or rollback exceeds `300 seconds`.

## Boundary Notes

This scenario validates controlled detection, manual rollback, and evidence capture only. It does not claim real-time automated blocking, WAF, IDS/IPS, EDR, SOAR, or production-grade CSPM capability.
