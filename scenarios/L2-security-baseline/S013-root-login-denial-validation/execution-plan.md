# Execution Plan

## Preparation

1. Review S011 to confirm SSH key authentication is handled separately.
2. Review S012 to confirm password login denial is handled separately.
3. Confirm sudo policy validation is excluded from S013.
4. Confirm this scenario is documentation and evidence planning only.
5. Confirm no passwords, credentials, private keys, public IPs, tfstate, kubeconfig files, or account-specific values are present or required.

## Execution Steps

1. Define `sshd_config` `PermitRootLogin` setting validation plan.
2. Define `sshd -T` effective configuration validation plan.
3. Define Bastion root login denial validation plan.
4. Define On-Prem DB node root login denial validation plan.
5. Define On-Prem Monitoring node root login denial validation plan.
6. Define AWS service node root login denial validation plan.
7. Define Azure service node root login denial validation plan.
8. Define OpenStack service node root login denial validation plan.
9. Define authentication failure log capture plan.
10. Define failure condition for `PermitRootLogin` enabled, root login success, missing sshd config, or missing failure evidence.

## Evidence Capture

1. Record planned root login denial validation commands and placeholders in `commands.md`.
2. Record validation checks and TODO results in `validation.md`.
3. Map root-login setting evidence to `configs/sshd-root-login-summary.md`.
4. Map effective configuration evidence to `configs/sshd-effective-config-summary.md`.
5. Map future authentication failure logs to `logs/root-login-denial-validation.log`.
6. Map future screenshot evidence to `screenshots/root-login-denial-test.png` only after binary evidence is approved and sanitized.
