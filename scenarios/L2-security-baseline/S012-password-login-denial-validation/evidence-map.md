# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| V001 Password denial baseline | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V002 SSHD password-denial example | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V003 Non-production marker | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V004 PasswordAuthentication setting | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V005 ChallengeResponseAuthentication setting | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V006 KbdInteractiveAuthentication setting | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V007 PubkeyAuthentication setting | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V008 AuthenticationMethods setting | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V009 Password denial policy statements | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V010 Password value safety | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V011 Private key safety | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V012 Authorized keys safety | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V013 Secret and account content | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| V014 Execution safety boundary | `logs/password-login-denial-validation.log`; `configs/password-login-denial-summary.md` | generated log and summary | yes |
| Script invocation and evidence inspection | `commands.md` | operator command record | yes |
| Final validation judgment | `validation.md` | validation result | yes |

## Evidence Notes

The log is reproducible. Password attempts, real values, keys, users, host output, credentials, and screenshots are neither required nor permitted.
