# S012-password-login-denial-validation

| Field | Value |
|---|---|
| Scenario ID | S012 |
| Scenario Name | Password Login Denial Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | Repository-side SSH password-login denial baseline |
| Related Components | SSH denial policy, example sshd settings, repository secret safety |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S012-password-login-denial-validation/ |
| Status | NOT_STARTED |

## Objective Summary

Validate that password-based SSH login denial is mandatory in the repository baseline without storing password values or modifying and testing real SSH servers.

## Scope Summary

S012 checks two baseline files, five sshd directives, policy and break-glass statements, password-value safety, private-key and `authorized_keys` absence, sensitive content, and execution safety.

## Related Components

- `security-baseline/ssh-password-login-denial-baseline.md`
- `security-baseline/sshd_config.password-denial.example`
- `tools/validate-ssh-password-login-denial-baseline.ps1`

## Validation Summary

All checks inspect repository files only. The validator does not modify sshd, restart SSH, attempt password authentication, connect to hosts, or read keys and credentials.

## Evidence Output Summary

- `logs/password-login-denial-validation.log`
- `configs/password-login-denial-summary.md`
- `commands.md`
- `validation.md`
