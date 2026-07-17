# Validation Checklist

Use this checklist before marking scenario work complete.

## Repository Foundation Checklist

- [ ] Required top-level files exist: `README.md`, `AGENTS.md`, `.gitignore`.
- [ ] Required docs exist under `docs/`.
- [ ] Required top-level directories exist.
- [ ] Scope lock and excluded scope remain unchanged unless explicitly approved.
- [ ] Repository structure validation script passes.

## Scenario Structure Checklist

- [ ] Scenario directory is under the correct validation level.
- [ ] Scenario directory name follows `S###-kebab-case-description`.
- [ ] All required scenario markdown files exist.
- [ ] Scenario status matrix is updated.
- [ ] Progress tracker is updated.

## Evidence Structure Checklist

- [ ] Matching evidence directory exists under the same validation level.
- [ ] `commands.md` exists.
- [ ] `validation.md` exists.
- [ ] `logs/.gitkeep` exists.
- [ ] `screenshots/.gitkeep` exists.
- [ ] `configs/.gitkeep` exists.
- [ ] Evidence status matrix is updated.

## Security and Sensitive File Checklist

- [ ] No secrets are committed.
- [ ] No credentials are committed.
- [ ] No private keys are committed.
- [ ] No tfstate files are committed.
- [ ] No kubeconfig files are committed.
- [ ] No account-specific identifiers are committed.
- [ ] Evidence is sanitized before review.

## Implementation Readiness Checklist

- [ ] Scenario objective is clear.
- [ ] Scope includes explicit included and excluded items.
- [ ] Prerequisites are documented.
- [ ] Execution plan is step-by-step.
- [ ] Validation plan maps every check to evidence.
- [ ] Expected result is measurable.
- [ ] Failure conditions are explicit.
- [ ] Rollback plan is realistic.
- [ ] Implementation log is updated.

## Zero Trust Governance Checklist

- [ ] `python tools/validate_zero_trust.py --verbose` passes.
- [ ] `python tools/check_zero_trust_sync.py` passes.
- [ ] `python tools/generate_zero_trust_reports.py --check` passes.
- [ ] `powershell -ExecutionPolicy Bypass -File tools/validate-zero-trust.ps1` passes.
- [ ] `python -m unittest discover -s tests -v` passes.
- [ ] Catalog and baseline YAML remain the machine-readable authorities.
- [ ] Markdown changes outside reviewed generated markers are human-authored and reviewed.
- [ ] No maturity, implementation, validation, or compliance overclaim was introduced.
- [ ] S001-S050 remain locked and no unauthorized scenario was created.
- [ ] No live access, secret, network connection, or remote infrastructure is required by governance validation.

## S005 OpenStack AIO Runtime Checklist

The original checks below are based on user-executed runtime results supplied
on 2026-07-16. Codex later corroborated current state through a separately
authorized forced-command read-only endpoint; it did not receive a general
shell or mutation authority.

- [x] Kolla prechecks and deployment completed.
- [x] Post-deploy client configuration generated outside the repository.
- [x] Keystone authentication succeeded; token value omitted.
- [x] Core services/endpoints, Nova services, hypervisor, and Neutron agents are healthy.
- [x] Provider and tenant networks, router, image, instance, and Floating IP are active.
- [x] Router/DHCP namespaces and Open vSwitch provider mapping are present.
- [x] EVE-NG external-router and Floating IP probes succeeded.
- [x] Tenant gateway, public IPv4, and cloud-init completion checks succeeded.
- [x] Raw output and sensitive/dynamic values are not committed.
- [ ] Terraform reproduction, destroy/recreate, persistent storage, backup/recovery, HA, monitoring, and hardening remain separate validations.
