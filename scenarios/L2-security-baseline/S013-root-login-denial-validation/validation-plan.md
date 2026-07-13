# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Root denial baseline | Test the baseline path. | Document exists. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V002 | SSHD root-denial example | Test the example path. | Config exists. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V003 | Non-production marker | Search the example header. | Explicit marker exists. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V004 | PermitRootLogin setting | Match the exact directive. | Value is `no`. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V005 | PubkeyAuthentication setting | Match the exact directive. | Value is `yes`. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V006 | PasswordAuthentication setting | Match the exact directive. | Value is `no`. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V007 | ChallengeResponseAuthentication setting | Match the exact directive. | Value is `no`. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V008 | KbdInteractiveAuthentication setting | Match the exact directive. | Value is `no`. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V009 | AuthenticationMethods setting | Match the exact directive. | Value is `publickey`. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V010 | Root denial policy statements | Search for required rules and placeholders. | Every statement exists. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V011 | Root password safety | Scan for enabled root login and root-password values. | No prohibited value exists. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V012 | Private key safety | Scan repository filenames and selected text. | No key file or material exists. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V013 | Authorized keys safety | Scan repository filenames. | No `authorized_keys` file exists. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V014 | Secret and account content | Scan baseline text for sensitive values and identifiers. | No forbidden content exists. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V015 | Execution safety boundary | Scan validator source for SSH, sudo, mutation, and external commands. | No prohibited command exists. | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |

## Review Notes

All checks are required and any failure produces a non-zero exit.
