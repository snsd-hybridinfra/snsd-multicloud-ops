# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| V001 Root denial baseline | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V002 SSHD root-denial example | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V003 Non-production marker | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V004 PermitRootLogin setting | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V005 PubkeyAuthentication setting | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V006 PasswordAuthentication setting | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V007 ChallengeResponseAuthentication setting | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V008 KbdInteractiveAuthentication setting | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V009 AuthenticationMethods setting | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V010 Root denial policy statements | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V011 Root password safety | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V012 Private key safety | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V013 Authorized keys safety | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V014 Secret and account content | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| V015 Execution safety boundary | `logs/root-login-denial-validation.log`; `configs/root-login-denial-summary.md` | generated log and summary | yes |
| Script invocation and evidence inspection | `commands.md` | operator command record | yes |
| Final validation judgment | `validation.md` | validation result | yes |

## Evidence Notes

The log is reproducible. Root-login attempts, privilege output, passwords, keys, users, host output, credentials, and screenshots are neither required nor permitted.
