# Financial Hybrid-Ready IDP

This directory is the authority for the platform product boundary. Zero Trust package authorities remain under `docs/zero-trust/` and must not be inferred from this product view.

## Product promise

Provide approved, repeatable and observable private-cloud IaaS and PaaS services to a virtual securities-company organization through one developer experience. Requests must pass identity, policy and approval controls before deterministic automation can provision or change a target.

## Authorities

- `target-architecture.md`: component and trust-boundary design.
- `architecture-baseline.yaml`: machine-readable current/target truth.
- `implementation-roadmap.md`: ordered work and acceptance gates.
- `asset-reconciliation.yaml`: disposition and ownership of pre-existing repository assets.
- `composite-service-catalog.yaml`: approved component and user-facing blueprint authority.
- `financial-saas-development-paas.yaml`: Financial SaaS Development PaaS composite-product, tenant-bundle and runtime-gate authority.
- `terraform-supply-chain.yaml`: customized Terraform wrapper, artifact lock, plan policy and runtime-input boundary.
- `container-supply-chain.yaml`: CI image build, SBOM, scan, signature, immutable promotion and k3s installation boundary.
- `container-supply-chain-runtime-readiness.yaml`: sanitized runner, GitHub, registry and Argo CD execution blockers.
- `ai-agent-sandbox.yaml`: Project Mini-Ona persistent-job, isolation, approval, budget and observability contract.
- `ai-agent-runtime-readiness.yaml`: sanitized external runtime blocker and live-readiness authority.
- `private-iaas-golden-path.yaml`: Stage B state, source digests, gates and stop conditions.
- `../adr/0018-financial-hybrid-ready-idp.md`: approved architecture decision.
- `../adr/0019-approved-composite-service-catalog.md`: approved catalog construction decision.
- `../adr/0020-persistent-ai-agent-sandbox.md`: approved flagship PaaS sandbox decision.
- `../adr/0021-financial-saas-development-paas.md`: central-IDP Financial SaaS Development PaaS decision.
- `../adr/0022-managed-terraform-supply-chain.md`: managed Terraform supply-chain customization decision.
- `../adr/0023-container-image-supply-chain-and-k3s-delivery.md`: container release and k3s delivery decision.

## Status vocabulary

- `REUSED_CANDIDATE`: existing code is potentially reusable but not integrated by this decision.
- `PARTIAL`: some relevant assets or bounded runtime evidence exist, but the platform capability is incomplete.
- `DESIGN_ONLY`: design exists without accepted implementation/runtime proof.
- `DEFERRED`: intentionally outside the current implementation sequence.
- `NOT_VALIDATED`: no accepted integrated runtime evidence exists.

## Guardrails

- No automatic inheritance between platform status and Zero Trust package status.
- No public-cloud or hybrid-operation claim until an adapter and private path are runtime validated.
- No production financial or personal data.
- No credential, state, kubeconfig, raw evidence or licensed network image in Git.
- No live apply, playbook, device change or validator without separate authorization.
- Users select only approved composite blueprints and bounded inputs; internal components, execution profiles, provider identifiers and free-form graphs are not products.
