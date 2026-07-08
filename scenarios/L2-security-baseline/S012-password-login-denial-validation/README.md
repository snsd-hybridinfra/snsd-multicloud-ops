# S012-password-login-denial-validation

| Field | Value |
|---|---|
| Scenario ID | S012 |
| Scenario Name | Password Login Denial Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | SSH access security |
| Related Components | Bastion, On-Prem DB nodes, On-Prem Monitoring nodes, AWS service nodes, Azure service nodes, OpenStack service nodes, sshd_config, sshd effective configuration |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S012-password-login-denial-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate that password-based SSH login is disabled across the SNSD Multi-Cloud Ops management and service node access model.

## Scope Summary

This scenario validates password login denial only. SSH key authentication success is handled in S011, and root login denial is handled in S013.

## Validation Summary

Validation checks cover `PasswordAuthentication` configuration, `sshd -T` effective configuration, password login denial plans for bastion and service nodes, authentication failure evidence, and failure conditions.

## Evidence Output Summary

Evidence must be recorded under `evidence/L2-security-baseline/S012-password-login-denial-validation/`, with command plans in `commands.md` and validation results in `validation.md`.
