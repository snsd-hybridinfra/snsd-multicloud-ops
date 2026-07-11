# Objective

## Operational Capability

Validate local control plane readiness through safe command discovery and version-only invocation for:

- Core tools: Git, PowerShell, SSH, Python
- Later-stage tools: Terraform, Ansible, kubectl, Docker

## Success Definition

The scenario succeeds when every core tool is discoverable and returns version output. Later-stage tools are also inspected, but their absence is recorded as a warning rather than a core readiness failure.

No cloud, cluster, registry, credential, kubeconfig, tfstate, or infrastructure access is required.
