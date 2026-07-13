# Execution Plan

## Preparation

1. Confirm the sshd example is marked non-production.
2. Confirm no root password, SSH password, key, user, credential, or host address is present.

## Execution Steps

1. Run `tools/validate-ssh-root-login-denial-baseline.ps1` from the repository root.
2. Review V001-V015 in the generated summary.
3. Inspect the generated log and summary.
4. Run repository structure and scenario quality validation.

## Safety Boundary

Execution reads repository files only. It does not modify sshd, restart SSH, execute root login or privilege escalation, connect to hosts, read private keys or credentials, or require live network access.
