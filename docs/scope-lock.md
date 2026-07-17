# Scope Lock

This repository is locked to the initial foundation for the SNSD Multi-Cloud Secure Operations Validation Platform.

The target is a hybrid and multicloud secure operations validation platform
capable of mapping, implementing, validating, and assessing selected
capabilities from the Korean Zero Trust Guideline 2.0. Selection and assessment
are evidence-based; the target does not require every capability to reach
Optimal maturity.

## Allowed Scope

- Scenario-based validation model across five levels.
- Documentation for scope, exclusions, naming, evidence, and Codex workflow.
- Empty foundation directories for scenarios, evidence, Terraform, Ansible, Kubernetes, EVE-NG, observability, ML security, policy, runbooks, cost governance, and tools.
- Text-only placeholders such as `.gitkeep`.
- Future scenario definitions that remain implementation-neutral until approved.
- Sanitized, text-only evidence from operator-authorized execution in the
  disposable non-production lab when it maps to an existing S001-S050
  scenario and contains no credential, account-specific identifier, raw state,
  or secret.
- Source-traceable Zero Trust capability mapping, gap analysis, maturity
  assessment method, and roadmap documentation under `docs/zero-trust/`.

## Locked Technology Areas

- Terraform structure under `terraform/`
- Ansible structure under `ansible/`
- Kubernetes manifests under `kubernetes/`
- EVE-NG topology and network configuration references under `eve-ng/`
- Prometheus, Grafana, and exporters under `observability/`
- ML security assets under `ml-security/`
- Policy, runbooks, cost governance, traffic management, and security baseline documentation

## Foundation Constraints

- The repository must not create, modify, or delete real cloud resources by
  itself. Operator-authorized disposable lab execution occurs outside the
  repository automation boundary.
- No Terraform providers, credentials, backend configuration, or state.
- No secrets, private keys, kubeconfig files, tokens, account IDs, subscription IDs, tenant IDs, or project IDs.
- No binary files.
- No technology expansion without an ADR and scope document update.

## Change Control

Any expansion beyond this scope must be proposed in `docs/adr/` before implementation.

The runtime-evidence boundary for the existing OpenStack technology area is
defined by `docs/adr/0002-non-production-runtime-evidence-boundary.md`.
