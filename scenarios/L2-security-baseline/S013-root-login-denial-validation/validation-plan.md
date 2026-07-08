# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | sshd_config PermitRootLogin setting validation plan | Document planned review of `PermitRootLogin` in sshd config. | PermitRootLogin is planned to be disabled. | `commands.md`, `configs/sshd-root-login-summary.md`, `validation.md` |
| V002 | sshd effective configuration validation plan using sshd -T | Document planned `sshd -T` effective config check. | Effective config reports direct root login disabled. | `commands.md`, `configs/sshd-effective-config-summary.md`, `validation.md` |
| V003 | Bastion root login denial validation plan | Document direct root login denial test to `<bastion-host>`. | Bastion denies direct root SSH login. | `commands.md`, `logs/root-login-denial-validation.log`, `validation.md` |
| V004 | On-Prem DB node root login denial validation plan | Document direct root login denial test to `<db-primary-node>`. | On-Prem DB node denies direct root SSH login. | `commands.md`, `logs/root-login-denial-validation.log`, `validation.md` |
| V005 | On-Prem Monitoring node root login denial validation plan | Document direct root login denial test to `<monitoring-node>`. | Monitoring node denies direct root SSH login. | `commands.md`, `logs/root-login-denial-validation.log`, `validation.md` |
| V006 | AWS service node root login denial validation plan | Document direct root login denial test to `<aws-service-node>`. | AWS service node denies direct root SSH login. | `commands.md`, `logs/root-login-denial-validation.log`, `validation.md` |
| V007 | Azure service node root login denial validation plan | Document direct root login denial test to `<azure-service-node>`. | Azure service node denies direct root SSH login. | `commands.md`, `logs/root-login-denial-validation.log`, `validation.md` |
| V008 | OpenStack service node root login denial validation plan | Document direct root login denial test to `<openstack-service-node>`. | OpenStack service node denies direct root SSH login. | `commands.md`, `logs/root-login-denial-validation.log`, `validation.md` |
| V009 | Authentication failure log capture plan | Document capture of failed direct root login events. | Failed root login evidence can be captured and sanitized. | `logs/root-login-denial-validation.log`, `screenshots/root-login-denial-test.png`, `validation.md` |
| V010 | PermitRootLogin enabled, root login success, missing sshd config, or missing failure evidence failure condition | Define explicit failure criteria. | Root-login failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. SSH key authentication success is handled in S011, password login denial is handled in S012, and sudo policy validation is excluded.
