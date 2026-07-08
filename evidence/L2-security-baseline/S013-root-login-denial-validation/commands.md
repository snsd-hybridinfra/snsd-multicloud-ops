# Commands

Scenario: S013-root-login-denial-validation
Level: L2-security-baseline
Capability: Root Login Denial Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include passwords, credentials, SSH private keys, real public IPs, account-specific usernames, tfstate, kubeconfig content, cloud account IDs, subscription IDs, tenant IDs, or provider-specific secrets.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | sshd_config PermitRootLogin setting validation plan | Review `/etc/ssh/sshd_config` or approved equivalent for `PermitRootLogin no` or equivalent denial. | Confirm planned static configuration check. | TODO: record sanitized output after approved execution. |
| V002 | sshd effective configuration validation plan using sshd -T | `sshd -T | Select-String permitrootlogin` or approved equivalent. | Confirm planned effective configuration check. | TODO: record sanitized output after approved execution. |
| V003 | Bastion root login denial validation plan | Attempt approved direct root login denial test to `<bastion-host>`. | Confirm Bastion denies direct root login. | TODO: record sanitized output after approved execution. |
| V004 | On-Prem DB node root login denial validation plan | Attempt approved direct root login denial test to `<db-primary-node>`. | Confirm DB node denies direct root login. | TODO: record sanitized output after approved execution. |
| V005 | On-Prem Monitoring node root login denial validation plan | Attempt approved direct root login denial test to `<monitoring-node>`. | Confirm monitoring node denies direct root login. | TODO: record sanitized output after approved execution. |
| V006 | AWS service node root login denial validation plan | Attempt approved direct root login denial test to `<aws-service-node>`. | Confirm AWS node denies direct root login. | TODO: record sanitized output after approved execution. |
| V007 | Azure service node root login denial validation plan | Attempt approved direct root login denial test to `<azure-service-node>`. | Confirm Azure node denies direct root login. | TODO: record sanitized output after approved execution. |
| V008 | OpenStack service node root login denial validation plan | Attempt approved direct root login denial test to `<openstack-service-node>`. | Confirm OpenStack node denies direct root login. | TODO: record sanitized output after approved execution. |
| V009 | Authentication failure log capture plan | Review approved SSH authentication failure logs. | Confirm denied direct root login evidence can be captured and sanitized. | TODO: record sanitized output after approved execution. |
| V010 | PermitRootLogin enabled, root login success, missing sshd config, or missing failure evidence failure condition | Review failed root-denial findings. | Confirm failure criteria produce `FAIL` or `BLOCKED` status. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/sshd-root-login-summary.md`
- `configs/sshd-effective-config-summary.md`
- `logs/root-login-denial-validation.log`
- `screenshots/root-login-denial-test.png`
