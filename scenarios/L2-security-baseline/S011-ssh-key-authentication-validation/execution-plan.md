# Execution Plan

## Preparation

1. Review S008 bastion reachability path assumptions.
2. Review S007 inventory placeholder assumptions.
3. Confirm this scenario is documentation and evidence planning only.
4. Confirm no real SSH private keys, credentials, public IPs, tfstate, kubeconfig files, or account-specific values are present or required.
5. Confirm password login denial and root login denial are excluded from S011.

## Execution Steps

1. Define SSH private key permission validation plan.
2. Define SSH public key placement validation plan.
3. Define Control Plane to Bastion key authentication plan.
4. Define Bastion to On-Prem DB node key authentication plan.
5. Define Bastion to Monitoring node key authentication plan.
6. Define Bastion to AWS service node key authentication plan.
7. Define Bastion to Azure service node key authentication plan.
8. Define Bastion to OpenStack service node key authentication plan.
9. Define SSH ProxyJump command pattern validation plan.
10. Define failure conditions for missing key, wrong key permission, missing `authorized_keys` entry, or unreachable target.

## Evidence Capture

1. Record planned SSH key validation commands and placeholders in `commands.md`.
2. Record validation checks and TODO results in `validation.md`.
3. Map SSH key authentication plan evidence to `configs/ssh-key-authentication-plan.md`.
4. Map SSH ProxyJump evidence to `configs/ssh-proxyjump-pattern-summary.md`.
5. Map future SSH command logs to `logs/ssh-key-authentication-validation.log`.
6. Map future screenshot evidence to `screenshots/ssh-key-authentication-test.png` only after binary evidence is approved and sanitized.
