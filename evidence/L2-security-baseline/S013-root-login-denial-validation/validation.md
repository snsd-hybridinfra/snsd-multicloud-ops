# Validation

Scenario: S013-root-login-denial-validation

Level: L2-security-baseline

Date: 2026-07-13

Overall status: PASS

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Root denial baseline | File exists. | Baseline document exists. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V002 | SSHD root-denial example | File exists. | Example config exists. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V003 | Non-production marker | Marker exists. | Example is explicitly marked. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V004 | PermitRootLogin setting | Value is `no`. | Required value is present. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V005 | PubkeyAuthentication setting | Value is `yes`. | Required value is present. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V006 | PasswordAuthentication setting | Value is `no`. | Required value is present. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V007 | ChallengeResponseAuthentication setting | Value is `no`. | Required value is present. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V008 | KbdInteractiveAuthentication setting | Value is `no`. | Required value is present. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V009 | AuthenticationMethods setting | Value is `publickey`. | Required value is present. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V010 | Root denial policy statements | Every rule and placeholder exists. | All required statements exist. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V011 | Root password safety | No prohibited root value exists. | No enabled root login or root-password value was detected. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V012 | Private key safety | No key file or material exists. | No private key was detected. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V013 | Authorized keys safety | No file exists. | No `authorized_keys` file was detected. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V014 | Secret and account content | No forbidden content exists. | No sensitive value, key, numeric IP, or account identifier was detected. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |
| V015 | Execution safety boundary | No SSH, sudo, or external command exists. | No prohibited command was detected. | PASS | `logs/root-login-denial-validation.log`, `configs/root-login-denial-summary.md` |

## Generated Result

All fifteen file, directive, policy, root-password, key-safety, secret, and execution-boundary checks passed. No sshd configuration was modified, no SSH service was restarted, no root-login or privilege-escalation attempt occurred, and no key or credential was read.
