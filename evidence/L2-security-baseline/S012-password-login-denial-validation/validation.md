# Validation

Scenario: S012-password-login-denial-validation
Level: L2-security-baseline
Capability: Password Login Denial Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real password-login denial output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | sshd_config PasswordAuthentication setting validation plan | PasswordAuthentication is planned to be disabled. | TODO | NOT_RUN | `commands.md`; `configs/sshd-password-authentication-summary.md` |
| V002 | sshd effective configuration validation plan using sshd -T | Effective config reports password authentication disabled. | TODO | NOT_RUN | `commands.md`; `configs/sshd-effective-config-summary.md` |
| V003 | Bastion password login denial validation plan | Bastion denies password-based SSH login. | TODO | NOT_RUN | `commands.md`; `logs/password-login-denial-validation.log` |
| V004 | On-Prem DB node password login denial validation plan | On-Prem DB node denies password-based SSH login. | TODO | NOT_RUN | `commands.md`; `logs/password-login-denial-validation.log` |
| V005 | On-Prem Monitoring node password login denial validation plan | Monitoring node denies password-based SSH login. | TODO | NOT_RUN | `commands.md`; `logs/password-login-denial-validation.log` |
| V006 | AWS service node password login denial validation plan | AWS service node denies password-based SSH login. | TODO | NOT_RUN | `commands.md`; `logs/password-login-denial-validation.log` |
| V007 | Azure service node password login denial validation plan | Azure service node denies password-based SSH login. | TODO | NOT_RUN | `commands.md`; `logs/password-login-denial-validation.log` |
| V008 | OpenStack service node password login denial validation plan | OpenStack service node denies password-based SSH login. | TODO | NOT_RUN | `commands.md`; `logs/password-login-denial-validation.log` |
| V009 | Authentication failure log capture plan | Failed password login evidence can be captured and sanitized. | TODO | NOT_RUN | `logs/password-login-denial-validation.log`; `screenshots/password-login-denial-test.png` |
| V010 | PasswordAuthentication enabled, password login success, missing sshd config, or missing failure evidence failure condition | Password-auth failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- sshd PasswordAuthentication summary is captured: NOT_READY
- sshd effective config summary is captured: NOT_READY
- Password login denial validation log is captured: NOT_READY
- Password login denial screenshot is captured: NOT_READY

## Notes

This scenario validates password login denial only. SSH key authentication success is handled in S011, and root login denial is handled in S013.
