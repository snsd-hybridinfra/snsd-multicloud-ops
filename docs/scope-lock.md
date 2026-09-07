# Scope Lock

The repository is locked to a Financial Hybrid-Ready Internal Developer Platform for a bounded non-production laboratory. OpenStack is the private IaaS plane, k3s is the PaaS plane, and Zero Trust is the cross-cutting security and validation plane.

## Active scope

- A self-service portal, approved composite-blueprint service catalog, request/approval workflow, resource inventory, lifecycle management, and cost/notification interfaces.
- A locally specified persistent AI-agent job service whose durable control-plane state survives disposable, strongly isolated k3s sandbox pods; live arbitrary-code execution remains separately gated.
- Terraform-based OpenStack provisioning, Ansible-based host and k3s configuration, and GitOps/CI-CD delivery with explicit human approval gates.
- A financial network target design using Nexus NX-OS/IOS-XE concepts, dynamic routing, multicast controls, segmentation, management-plane isolation, and recoverable operations.
- Provider-neutral contracts for a future public-cloud adapter. The current claim is Hybrid-Ready, not active hybrid-cloud operation.
- Canonical Zero Trust capability taxonomy and evidence-based assessment.
- Package-owned control implementation, validation, rollback, and evidence.
- The Phase 1 flow defined in `docs/zero-trust/package-flow.yaml`.
- Read-only local validators, negative tests, package synchronization, and report checks.
- Sanitized text evidence under reviewed package evidence authorities.
- The authenticated KISA 2026 source metadata and the source-verified `ZT-GOV-MAP-001` mapping framework. Mapping remains distinct from implementation, runtime validation, maturity, compliance and certification.

## Retired scope

The numbered scenario framework, dedicated scenario evidence tree, scenario matrices, aggregate execution, and scenario-count progress were removed. Git history is the only historical recovery authority; no active replacement scenario series exists.

## Constraints

- No repository-driven live infrastructure mutation.
- No credentials, private keys, tokens, state, kubeconfigs, account identifiers, personal data, or raw runtime output.
- No binary deliverables.
- No package status, acceptance, evidence continuity, compliance, or maturity claim without matching authority.
- Architecture and scope expansion require an ADR and explicit approval.
- No licensed network operating-system image, appliance binary, or vendor entitlement in Git.
- No claim that `platform/`, the portal candidate, or provider templates are integrated or runtime validated solely because files exist.
- No direct user exposure of internal components, provider-bound execution profiles, arbitrary composition graphs, raw provider identifiers or user-supplied HCL.
- No direct main-branch push, personal credentials in a sandbox, unbounded agent loop, plain container runtime as the sole untrusted-code boundary, or raw prompt/source telemetry.
