# Execution Plan

## Preparation

1. Review S011 to confirm SSH key authentication is handled separately.
2. Confirm S013 owns root login denial.
3. Confirm this scenario is documentation and evidence planning only.
4. Confirm no passwords, credentials, private keys, public IPs, tfstate, kubeconfig files, or account-specific values are present or required.

## Execution Steps

1. Define `sshd_config` `PasswordAuthentication` setting validation plan.
2. Define `sshd -T` effective configuration validation plan.
3. Define Bastion password login denial validation plan.
4. Define On-Prem DB node password login denial validation plan.
5. Define On-Prem Monitoring node password login denial validation plan.
6. Define AWS service node password login denial validation plan.
7. Define Azure service node password login denial validation plan.
8. Define OpenStack service node password login denial validation plan.
9. Define authentication failure log capture plan.
10. Define failure condition for `PasswordAuthentication` enabled, password login success, missing sshd config, or missing failure evidence.

## Evidence Capture

1. Record planned password denial validation commands and placeholders in `commands.md`.
2. Record validation checks and TODO results in `validation.md`.
3. Map sshd setting evidence to `configs/sshd-password-authentication-summary.md`.
4. Map effective configuration evidence to `configs/sshd-effective-config-summary.md`.
5. Map future authentication failure logs to `logs/password-login-denial-validation.log`.
6. Map future screenshot evidence to `screenshots/password-login-denial-test.png` only after binary evidence is approved and sanitized.
