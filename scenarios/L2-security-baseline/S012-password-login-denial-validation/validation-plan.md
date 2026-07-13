# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Password denial baseline | Test the baseline path. | Document exists. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V002 | SSHD password-denial example | Test the example path. | Config exists. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V003 | Non-production marker | Search the example header. | Explicit marker exists. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V004 | PasswordAuthentication setting | Match the exact directive. | Value is `no`. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V005 | ChallengeResponseAuthentication setting | Match the exact directive. | Value is `no`. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V006 | KbdInteractiveAuthentication setting | Match the exact directive. | Value is `no`. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V007 | PubkeyAuthentication setting | Match the exact directive. | Value is `yes`. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V008 | AuthenticationMethods setting | Match the exact directive. | Value is `publickey`. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V009 | Password denial policy statements | Search for required rules and placeholders. | Every statement exists. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V010 | Password value safety | Scan for enabled password authentication and password values. | No prohibited value exists. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V011 | Private key safety | Scan repository filenames and selected text. | No key file or material exists. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V012 | Authorized keys safety | Scan repository filenames. | No `authorized_keys` file exists. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V013 | Secret and account content | Scan baseline text for sensitive values and identifiers. | No forbidden content exists. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V014 | Execution safety boundary | Scan validator source for SSH mutation and external commands. | No prohibited command exists. | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |

## Review Notes

All checks are required and any failure produces a non-zero exit.
