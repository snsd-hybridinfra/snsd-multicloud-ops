# Validation

Scenario: S013-root-login-denial-validation
Level: L2-security-baseline
Capability: Root Login Denial Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real root-login denial output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | sshd_config PermitRootLogin setting validation plan | PermitRootLogin is planned to be disabled. | TODO | NOT_RUN | `commands.md`; `configs/sshd-root-login-summary.md` |
| V002 | sshd effective configuration validation plan using sshd -T | Effective config reports direct root login disabled. | TODO | NOT_RUN | `commands.md`; `configs/sshd-effective-config-summary.md` |
| V003 | Bastion root login denial validation plan | Bastion denies direct root SSH login. | TODO | NOT_RUN | `commands.md`; `logs/root-login-denial-validation.log` |
| V004 | On-Prem DB node root login denial validation plan | On-Prem DB node denies direct root SSH login. | TODO | NOT_RUN | `commands.md`; `logs/root-login-denial-validation.log` |
| V005 | On-Prem Monitoring node root login denial validation plan | Monitoring node denies direct root SSH login. | TODO | NOT_RUN | `commands.md`; `logs/root-login-denial-validation.log` |
| V006 | AWS service node root login denial validation plan | AWS service node denies direct root SSH login. | TODO | NOT_RUN | `commands.md`; `logs/root-login-denial-validation.log` |
| V007 | Azure service node root login denial validation plan | Azure service node denies direct root SSH login. | TODO | NOT_RUN | `commands.md`; `logs/root-login-denial-validation.log` |
| V008 | OpenStack service node root login denial validation plan | OpenStack service node denies direct root SSH login. | TODO | NOT_RUN | `commands.md`; `logs/root-login-denial-validation.log` |
| V009 | Authentication failure log capture plan | Failed direct root login evidence can be captured and sanitized. | TODO | NOT_RUN | `logs/root-login-denial-validation.log`; `screenshots/root-login-denial-test.png` |
| V010 | PermitRootLogin enabled, root login success, missing sshd config, or missing failure evidence failure condition | Root-login failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- sshd root login summary is captured: NOT_READY
- sshd effective config summary is captured: NOT_READY
- Root login denial validation log is captured: NOT_READY
- Root login denial screenshot is captured: NOT_READY

## Notes

This scenario validates direct root login denial only. SSH key authentication is handled in S011, password login denial is handled in S012, and sudo policy validation is excluded.
