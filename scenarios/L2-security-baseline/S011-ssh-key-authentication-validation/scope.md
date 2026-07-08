# Scope

## Included

- SSH private key permission validation plan.
- SSH public key placement validation plan.
- Control Plane to Bastion key authentication plan.
- Bastion to On-Prem DB node key authentication plan.
- Bastion to Monitoring node key authentication plan.
- Bastion to AWS service node key authentication plan.
- Bastion to Azure service node key authentication plan.
- Bastion to OpenStack service node key authentication plan.
- SSH ProxyJump command pattern validation plan.
- Failure condition for missing key, wrong key permission, missing `authorized_keys` entry, or unreachable target.

## Excluded

- Creating real SSH private keys.
- Storing real credentials, public IPs, private keys, cloud account values, subscription IDs, tenant IDs, tfstate, kubeconfig files, or account-specific files.
- Password login denial validation, which is handled in S012.
- Root login denial validation, which is handled in S013.
- Real Ansible automation implementation.
- Terraform, Kubernetes, monitoring, ML, backup, or cloud provisioning logic.

## Assumptions

- Use placeholders such as `<ssh-private-key-path>`, `<bastion-host>`, `<target-node>`, and `<target-user>`.
- Usernames are placeholders unless they are generic and non-account-specific.
- Future execution requires explicit approval before any real SSH connection attempt.
