# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| sshd_config PasswordAuthentication setting validation plan | `commands.md`; `configs/sshd-password-authentication-summary.md`; `validation.md` | command plan, sshd setting summary, validation record | yes |
| sshd effective configuration validation plan using sshd -T | `commands.md`; `configs/sshd-effective-config-summary.md`; `validation.md` | command plan, effective config summary, validation record | yes |
| Bastion password login denial validation plan | `commands.md`; `logs/password-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| On-Prem DB node password login denial validation plan | `commands.md`; `logs/password-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| On-Prem Monitoring node password login denial validation plan | `commands.md`; `logs/password-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| AWS service node password login denial validation plan | `commands.md`; `logs/password-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| Azure service node password login denial validation plan | `commands.md`; `logs/password-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| OpenStack service node password login denial validation plan | `commands.md`; `logs/password-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| Authentication failure log capture plan | `logs/password-login-denial-validation.log`; `screenshots/password-login-denial-test.png`; `validation.md` | denial log, screenshot reference, validation record | yes |
| PasswordAuthentication enabled, password login success, missing sshd config, or missing failure evidence failure condition | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real password-login denial output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
