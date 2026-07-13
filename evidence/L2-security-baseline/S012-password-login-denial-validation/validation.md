# Validation

Scenario: S012-password-login-denial-validation

Level: L2-security-baseline

Date: 2026-07-13

Overall status: PASS

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Password denial baseline | File exists. | Baseline document exists. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V002 | SSHD password-denial example | File exists. | Example config exists. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V003 | Non-production marker | Marker exists. | Example is explicitly marked. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V004 | PasswordAuthentication setting | Value is `no`. | Required value is present. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V005 | ChallengeResponseAuthentication setting | Value is `no`. | Required value is present. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V006 | KbdInteractiveAuthentication setting | Value is `no`. | Required value is present. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V007 | PubkeyAuthentication setting | Value is `yes`. | Required value is present. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V008 | AuthenticationMethods setting | Value is `publickey`. | Required value is present. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V009 | Password denial policy statements | Every rule and placeholder exists. | All required statements exist. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V010 | Password value safety | No prohibited password value exists. | No enabled password authentication or password value was detected. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V011 | Private key safety | No key file or material exists. | No private key was detected. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V012 | Authorized keys safety | No file exists. | No `authorized_keys` file was detected. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V013 | Secret and account content | No forbidden content exists. | No sensitive value, key, numeric IP, or account identifier was detected. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |
| V014 | Execution safety boundary | No active SSH or external command exists. | No prohibited command was detected. | PASS | `logs/password-login-denial-validation.log`, `configs/password-login-denial-summary.md` |

## Generated Result

All fourteen file, directive, policy, password-value, key-safety, secret, and execution-boundary checks passed. No sshd configuration was modified, no SSH service was restarted, no password attempt or host connection occurred, and no key or credential was read.
