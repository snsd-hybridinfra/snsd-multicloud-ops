# S013-root-login-denial-validation

| Field | Value |
|---|---|
| Scenario ID | S013 |
| Scenario Name | Root Login Denial Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | Repository-side SSH root-login denial baseline |
| Related Components | Root denial policy, example sshd settings, non-root and sudo placeholders |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S013-root-login-denial-validation/ |
| Status | NOT_STARTED |

## Objective Summary

Validate that direct root SSH login denial is mandatory and administrative access uses placeholder non-root and controlled sudo processes without storing credentials or changing SSH servers.

## Scope Summary

S013 checks baseline files, six sshd directives, root-denial and privilege policy statements, root-password safety, private-key and `authorized_keys` absence, sensitive content, and execution safety.

## Related Components

- `security-baseline/ssh-root-login-denial-baseline.md`
- `security-baseline/sshd_config.root-login-denial.example`
- `tools/validate-ssh-root-login-denial-baseline.ps1`

## Validation Summary

All checks inspect repository files only. The validator does not modify sshd, restart SSH, attempt root login or privilege escalation, connect to hosts, or read keys and credentials.

## Evidence Output Summary

- `logs/root-login-denial-validation.log`
- `configs/root-login-denial-summary.md`
- `commands.md`
- `validation.md`
