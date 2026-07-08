# Commands

Scenario: S012-password-login-denial-validation
Level: L2-security-baseline
Capability: Password Login Denial Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include passwords, credentials, SSH private keys, real public IPs, account-specific usernames, tfstate, kubeconfig content, cloud account IDs, subscription IDs, tenant IDs, or provider-specific secrets.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | sshd_config PasswordAuthentication setting validation plan | Review `/etc/ssh/sshd_config` or approved equivalent for `PasswordAuthentication no`. | Confirm planned static configuration check. | TODO: record sanitized output after approved execution. |
| V002 | sshd effective configuration validation plan using sshd -T | `sshd -T | Select-String passwordauthentication` or approved equivalent. | Confirm planned effective configuration check. | TODO: record sanitized output after approved execution. |
| V003 | Bastion password login denial validation plan | Attempt approved password-auth denial test to `<bastion-host>` without recording passwords. | Confirm Bastion denies password login. | TODO: record sanitized output after approved execution. |
| V004 | On-Prem DB node password login denial validation plan | Attempt approved password-auth denial test to `<db-primary-node>` without recording passwords. | Confirm DB node denies password login. | TODO: record sanitized output after approved execution. |
| V005 | On-Prem Monitoring node password login denial validation plan | Attempt approved password-auth denial test to `<monitoring-node>` without recording passwords. | Confirm monitoring node denies password login. | TODO: record sanitized output after approved execution. |
| V006 | AWS service node password login denial validation plan | Attempt approved password-auth denial test to `<aws-service-node>` without recording passwords. | Confirm AWS node denies password login. | TODO: record sanitized output after approved execution. |
| V007 | Azure service node password login denial validation plan | Attempt approved password-auth denial test to `<azure-service-node>` without recording passwords. | Confirm Azure node denies password login. | TODO: record sanitized output after approved execution. |
| V008 | OpenStack service node password login denial validation plan | Attempt approved password-auth denial test to `<openstack-service-node>` without recording passwords. | Confirm OpenStack node denies password login. | TODO: record sanitized output after approved execution. |
| V009 | Authentication failure log capture plan | Review approved SSH authentication failure logs. | Confirm denied password login evidence can be captured and sanitized. | TODO: record sanitized output after approved execution. |
| V010 | PasswordAuthentication enabled, password login success, missing sshd config, or missing failure evidence failure condition | Review failed password-denial findings. | Confirm failure criteria produce `FAIL` or `BLOCKED` status. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/sshd-password-authentication-summary.md`
- `configs/sshd-effective-config-summary.md`
- `logs/password-login-denial-validation.log`
- `screenshots/password-login-denial-test.png`
