# Failure Condition

## Failure Conditions

- `PasswordAuthentication` is enabled in planned configuration.
- `sshd -T` effective configuration indicates password authentication is enabled.
- Password-based SSH login succeeds for any planned target.
- sshd configuration evidence is missing.
- Authentication failure evidence is missing.
- SSH key authentication success or root login denial is implemented in this scenario.
- Evidence includes passwords, credentials, private keys, real public IPs, tfstate, kubeconfig content, subscription IDs, tenant IDs, or account-specific values.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `configs/sshd-password-authentication-summary.md`, `configs/sshd-effective-config-summary.md`, or `logs/password-login-denial-validation.log`.

## Follow-Up Requirement

Create a follow-up task to correct SSH daemon password authentication settings, evidence capture, or target scope before future execution proceeds.
