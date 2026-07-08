# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| sshd_config PermitRootLogin setting validation plan | `commands.md`; `configs/sshd-root-login-summary.md`; `validation.md` | command plan, sshd root-login summary, validation record | yes |
| sshd effective configuration validation plan using sshd -T | `commands.md`; `configs/sshd-effective-config-summary.md`; `validation.md` | command plan, effective config summary, validation record | yes |
| Bastion root login denial validation plan | `commands.md`; `logs/root-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| On-Prem DB node root login denial validation plan | `commands.md`; `logs/root-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| On-Prem Monitoring node root login denial validation plan | `commands.md`; `logs/root-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| AWS service node root login denial validation plan | `commands.md`; `logs/root-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| Azure service node root login denial validation plan | `commands.md`; `logs/root-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| OpenStack service node root login denial validation plan | `commands.md`; `logs/root-login-denial-validation.log`; `validation.md` | command plan, denial log, validation record | yes |
| Authentication failure log capture plan | `logs/root-login-denial-validation.log`; `screenshots/root-login-denial-test.png`; `validation.md` | denial log, screenshot reference, validation record | yes |
| PermitRootLogin enabled, root login success, missing sshd config, or missing failure evidence failure condition | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real root-login denial output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
