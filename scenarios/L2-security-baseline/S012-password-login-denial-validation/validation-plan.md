# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | sshd_config PasswordAuthentication setting validation plan | Document planned review of `PasswordAuthentication` in sshd config. | PasswordAuthentication is planned to be disabled. | `commands.md`, `configs/sshd-password-authentication-summary.md`, `validation.md` |
| V002 | sshd effective configuration validation plan using sshd -T | Document planned `sshd -T` effective config check. | Effective config reports password authentication disabled. | `commands.md`, `configs/sshd-effective-config-summary.md`, `validation.md` |
| V003 | Bastion password login denial validation plan | Document password login denial test to `<bastion-host>`. | Bastion denies password-based SSH login. | `commands.md`, `logs/password-login-denial-validation.log`, `validation.md` |
| V004 | On-Prem DB node password login denial validation plan | Document password login denial test to `<db-primary-node>`. | On-Prem DB node denies password-based SSH login. | `commands.md`, `logs/password-login-denial-validation.log`, `validation.md` |
| V005 | On-Prem Monitoring node password login denial validation plan | Document password login denial test to `<monitoring-node>`. | Monitoring node denies password-based SSH login. | `commands.md`, `logs/password-login-denial-validation.log`, `validation.md` |
| V006 | AWS service node password login denial validation plan | Document password login denial test to `<aws-service-node>`. | AWS service node denies password-based SSH login. | `commands.md`, `logs/password-login-denial-validation.log`, `validation.md` |
| V007 | Azure service node password login denial validation plan | Document password login denial test to `<azure-service-node>`. | Azure service node denies password-based SSH login. | `commands.md`, `logs/password-login-denial-validation.log`, `validation.md` |
| V008 | OpenStack service node password login denial validation plan | Document password login denial test to `<openstack-service-node>`. | OpenStack service node denies password-based SSH login. | `commands.md`, `logs/password-login-denial-validation.log`, `validation.md` |
| V009 | Authentication failure log capture plan | Document capture of failed password-auth events. | Failed password login evidence can be captured and sanitized. | `logs/password-login-denial-validation.log`, `screenshots/password-login-denial-test.png`, `validation.md` |
| V010 | PasswordAuthentication enabled, password login success, missing sshd config, or missing failure evidence failure condition | Define explicit failure criteria. | Password-auth failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. SSH key authentication success is handled in S011, and root login denial is handled in S013.
