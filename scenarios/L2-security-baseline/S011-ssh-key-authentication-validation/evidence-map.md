# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| V001 SSH baseline document | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V002 SSHD example config | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V003 Non-production marker | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V004 PubkeyAuthentication setting | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V005 PasswordAuthentication setting | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V006 PermitRootLogin setting | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V007 ChallengeResponseAuthentication setting | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V008 KbdInteractiveAuthentication setting | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V009 AuthorizedKeysFile setting | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V010 Baseline policy statements | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V011 Private key safety | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V012 Authorized keys safety | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V013 Secret and account content | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| V014 Execution safety boundary | `logs/ssh-key-authentication-validation.log`; `configs/ssh-key-authentication-summary.md` | generated log and summary | yes |
| Script invocation and evidence inspection | `commands.md` | operator command record | yes |
| Final validation judgment | `validation.md` | validation result | yes |

## Evidence Notes

The log is reproducible. Real keys, users, host output, authentication output, credentials, and screenshots are neither required nor permitted.
