# Validation

Scenario: S011-ssh-key-authentication-validation

Level: L2-security-baseline

Date: 2026-07-13

Overall status: PASS

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | SSH baseline document | File exists. | Baseline document exists. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V002 | SSHD example config | File exists. | Example config exists. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V003 | Non-production marker | Marker exists. | Example is explicitly marked. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V004 | PubkeyAuthentication setting | Value is `yes`. | Required value is present. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V005 | PasswordAuthentication setting | Value is `no`. | Required value is present. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V006 | PermitRootLogin setting | Value is `no`. | Required value is present. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V007 | ChallengeResponseAuthentication setting | Value is `no`. | Required value is present. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V008 | KbdInteractiveAuthentication setting | Value is `no`. | Required value is present. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V009 | AuthorizedKeysFile setting | Placeholder path exists. | Required directive is present. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V010 | Baseline policy statements | Every rule and placeholder exists. | All required statements exist. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V011 | Private key safety | No key file or material exists. | No private key was detected. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V012 | Authorized keys safety | No file exists. | No `authorized_keys` file was detected. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V013 | Secret and account content | No forbidden content exists. | No sensitive value, key, numeric IP, or account identifier was detected. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |
| V014 | Execution safety boundary | No active SSH or external command exists. | No prohibited command was detected. | PASS | `logs/ssh-key-authentication-validation.log`, `configs/ssh-key-authentication-summary.md` |

## Generated Result

All fourteen file, directive, policy, key-safety, secret, and execution-boundary checks passed. No sshd configuration was modified, no SSH service was restarted, no host connection occurred, and no key or credential was read.
