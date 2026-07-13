# S011-ssh-key-authentication-validation

| Field | Value |
|---|---|
| Scenario ID | S011 |
| Scenario Name | SSH Key Authentication Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | Repository-side SSH key-authentication baseline |
| Related Components | SSH policy, example sshd settings, repository key safety |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S011-ssh-key-authentication-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate that SSH key authentication is the documented administrative baseline and that required example settings exist without storing keys, passwords, users, or host credentials.

## Scope Summary

S011 checks baseline files, six sshd settings, policy statements and placeholders, repository private-key and `authorized_keys` absence, sensitive content, and execution safety.

## Related Components

- `security-baseline/ssh-key-authentication-baseline.md`
- `security-baseline/sshd_config.key-auth.example`
- `tools/validate-ssh-key-authentication-baseline.ps1`

## Validation Summary

All checks inspect repository files only. The validator does not modify sshd configuration, restart SSH, connect to hosts, or read private keys and credentials.

## Evidence Output Summary

- `logs/ssh-key-authentication-validation.log`
- `configs/ssh-key-authentication-summary.md`
- `commands.md`
- `validation.md`
