# Prerequisites

## Required Previous Scenarios

- `S011-ssh-key-authentication-validation` is planned and defines SSH key authentication separately.
- `S012-password-login-denial-validation` is planned and defines password login denial separately.
- `S008-bastion-reachability-validation` is planned and defines reachability paths.
- `S007-multi-cloud-inventory-validation` is planned and defines placeholder inventory targets.

## Required Tools

- SSH client availability on the Control Plane.
- Shell access planning for future approved lab targets.
- Repository access for documenting evidence.

## Required Access Assumptions

- No root credentials are required for this skeleton.
- No real private keys, credentials, public IPs, tfstate, kubeconfig files, or account-specific values are required.
- Future execution must use approved lab targets and sanitized output only.
