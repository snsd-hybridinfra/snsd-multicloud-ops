# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | SSH baseline document | Test the baseline path. | Document exists. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V002 | SSHD example config | Test the example path. | Config exists. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V003 | Non-production marker | Search the example header. | Explicit marker exists. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V004 | PubkeyAuthentication setting | Match the exact directive. | Value is `yes`. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V005 | PasswordAuthentication setting | Match the exact directive. | Value is `no`. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V006 | PermitRootLogin setting | Match the exact directive. | Value is `no`. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V007 | ChallengeResponseAuthentication setting | Match the exact directive. | Value is `no`. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V008 | KbdInteractiveAuthentication setting | Match the exact directive. | Value is `no`. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V009 | AuthorizedKeysFile setting | Match the exact directive. | Placeholder path is documented. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V010 | Baseline policy statements | Search for required rules and placeholders. | Every statement exists. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V011 | Private key safety | Scan repository filenames and selected text. | No key file or material exists. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V012 | Authorized keys safety | Scan repository filenames. | No `authorized_keys` file exists. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V013 | Secret and account content | Scan baseline text for sensitive values and identifiers. | No forbidden content exists. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V014 | Execution safety boundary | Scan validator source for SSH mutation and external commands. | No prohibited command exists. | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |

## Review Notes

All checks are required and any failure produces a non-zero exit.
