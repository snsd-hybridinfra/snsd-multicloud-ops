# Prerequisites

## Required Previous Scenarios

- `S001-control-plane-toolchain-validation` is planned and identifies SSH-capable control plane readiness.
- `S007-multi-cloud-inventory-validation` is planned and defines placeholder inventory groups.
- `S008-bastion-reachability-validation` is planned and defines bastion reachability paths.
- `S009-dns-hostname-resolution-validation` is planned and defines placeholder hostname mappings.

## Required Tools

- SSH client availability on the Control Plane.
- Repository access for documenting evidence.
- Future shell access to approved lab targets after explicit authorization.

## Required Access Assumptions

- No real SSH private key is required for this skeleton.
- No credentials, public IPs, tfstate, kubeconfig files, or account-specific values are required.
- Future execution must use approved lab key material outside this repository.
