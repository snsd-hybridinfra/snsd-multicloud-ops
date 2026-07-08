# Scope Lock

This repository is locked to the initial foundation for the SNSD Multi-Cloud Secure Operations Validation Platform.

## Allowed Scope

- Scenario-based validation model across five levels.
- Documentation for scope, exclusions, naming, evidence, and Codex workflow.
- Empty foundation directories for scenarios, evidence, Terraform, Ansible, Kubernetes, EVE-NG, observability, ML security, policy, runbooks, cost governance, and tools.
- Text-only placeholders such as `.gitkeep`.
- Future scenario definitions that remain implementation-neutral until approved.

## Locked Technology Areas

- Terraform structure under `terraform/`
- Ansible structure under `ansible/`
- Kubernetes manifests under `kubernetes/`
- EVE-NG topology and network configuration references under `eve-ng/`
- Prometheus, Grafana, and exporters under `observability/`
- ML security assets under `ml-security/`
- Policy, runbooks, cost governance, traffic management, and security baseline documentation

## Foundation Constraints

- No real cloud resources.
- No Terraform providers, credentials, backend configuration, or state.
- No secrets, private keys, kubeconfig files, tokens, account IDs, subscription IDs, tenant IDs, or project IDs.
- No binary files.
- No technology expansion without an ADR and scope document update.

## Change Control

Any expansion beyond this scope must be proposed in `docs/adr/` before implementation.
