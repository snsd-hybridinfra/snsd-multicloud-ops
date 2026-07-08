# Scope

## Included

- Validate local command availability for the required control plane tools.
- Record planned version check commands.
- Define the evidence required to confirm toolchain readiness.
- Use TODO placeholders until actual command output is collected.

## Excluded

- Authenticating to AWS, Azure, OpenStack, Kubernetes, or any other platform.
- Creating or modifying cloud resources.
- Running Terraform plans or applies.
- Running Ansible playbooks.
- Creating kubeconfig files, credentials, private keys, tfstate, or account-specific files.
- Capturing real account IDs, subscription IDs, tenant IDs, project IDs, IP addresses, or secrets.

## Assumptions

- Validation is performed from the repository root on an approved local control-plane host such as `<target-node>`.
- Tool version output is safe to capture after review.
- Missing tools are reported as validation failures or blockers, not remediated automatically by this scenario.
