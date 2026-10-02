# Implementation Roadmap

This roadmap orders product work without introducing new Zero Trust package IDs. Status promotion requires matching implementation and accepted evidence.

Current stage progress and the bounded securities-domain track are recorded in [project-progress.md](project-progress.md). The dashboard never supersedes the exit gates below.

## Stage A — Authority and inventory

Status: `COMPLETED_LOCAL`

- Establish the platform-first project definition and architecture baseline.
- Inventory and classify root, `applications/` and `platform/` assets as adopt, adapt, quarantine or defer.
- Define single owners for catalog, identity, network, state, telemetry, backup and cost data.

Exit: architecture validator passes, `asset-reconciliation.yaml` assigns every major pre-existing asset a disposition and owner, and no existing asset is represented as integrated solely by file presence.

## Stage B — Private IaaS golden path

Status: `IN_PROGRESS_LOCAL`

- Reconcile the portal candidate with the existing OpenStack environment.
- Validate request, approval, policy, plan, apply, inventory, expiry and destroy as separate transitions.
- Preserve private-only default networking and external state/credential handling.
- Enforce the customized Terraform module/provider/plan supply chain before any real apply.

Local checkpoint: the catalog and protection profile are hash-pinned in
`private-iaas-golden-path.yaml`; the portal validator passes 22/22 and its full
test suite passes 69 tests, including the coupled request/approval/runner/Grant
and destroy flow. The eight-component/eight-blueprint composite catalog is
locally design-validated. The portal now provides locally tested public
blueprint discovery, safe resolution and a service-only resolved manifest.
`VM_APPLICATION_STACK` now completes the local request, approval and mock-runner
manifest path with independent digest verification. The other seven blueprints
remain fail-closed where component adapters are absent. The five OpenStack
entries are service-only execution profiles. This establishes no OpenStack
runtime credit.

Destroy and automatic k3s rollback now require a post-destroy state read with
no resources in the root or nested modules before reporting completion. Local
fake-command regressions cover residual resources, malformed or unsupported
state and unavailable inspection. This closes a local completion-reporting gap;
independent OpenStack absence and recovery evidence remain `NOT_VALIDATED`.

The runner also binds the state key and ownership tags to the approved request,
rejects unsupported operations, checks absolute/disjoint external runtime
paths and protects pre-existing workspaces. Workspace creation is exclusive;
cleanup applies only to the current invocation's workspace. Local rejection
tests cover cross-request state, metadata tampering, Git-contained credentials,
overlapping roots and recovery-material preservation.

Frontend checkpoint (2026-10-02): use the read-only `ecl2-portal` frontend at
`e8c4c1d26b9177929a0e04b7b9db1d6885ac5215`, imported into the existing
SNSD user-portal image. Changes apply only to this downstream copy and SNSD
APIs; the upstream checkout and its `.deploy/` remain untouched. Developer,
Manufacturing, Finance and Public views now use persistent tenant/domain/owner
requests, the eight-blueprint catalog, existing approval decisions, mock runner
callbacks, bound grant revocation and recovery. MSP and LLM views have sanitized
operational projections and opt-in numeric-only local simulation. Session
caches are invalidated at logout, identity changes and stale-response boundaries.
The final portal working-tree suite passes 174 tests; the browser demonstrates
one saved request, independent MSP approval and a mock RUNNING resource.
See `applications/internal-iaas-portal/docs/interface-contracts/ecl2-frontend.md`.
The seven other products, identity directory, monitoring, real billing/model
providers and industry adapters remain unavailable. Production authority-file
image packaging, database migration, OIDC/PEP/service audiences and the exact
Grant/callback/recovery network paths still require validation before deployment.
No live platform or Zero Trust status is promoted.

Exit: one synthetic VM product completes positive, negative, bypass, persistence and rollback checks with sanitized evidence.

## Stage C — k3s PaaS golden path

Status: `PARTIAL`

- Reconcile offline k3s provisioning with the reusable GitOps platform baseline.
- Fix namespace, quota, network policy, ingress, registry and observability contracts.
- Separate cluster bootstrap, platform add-ons and tenant applications.
- Build the seven central-IDP images through CI with digest-pinned bases, SBOM,
  provenance, zero-HIGH/CRITICAL scanning and signature verification; create an
  immutable GitOps promotion pull request, then let Argo CD install only the
  merge-approved digest overlays with sync, health and Git-revert rollback gates.
- Implement `AI_AGENT_SANDBOX` (Project Mini-Ona) as the flagship PaaS blueprint: durable control-plane jobs, disposable Kata/gVisor-class pods, task-scoped Git/model credentials, brokered egress, hard cost/runtime budgets, checkpoint/resume approval and end-to-end traces.

Local checkpoint: the sandbox product, lifecycle, isolation, credential, egress,
budget, Git delivery, observability and acceptance boundaries are fixed in
`ai-agent-sandbox.yaml`. It replaces the narrower CI/CD runner without adding a
ninth catalog product. A service-only local slice now persists the job state
machine and produces an inert digest-bound Kubernetes bundle; it passes local
checkpoint/approval/resume/timeout and boundary tests. Status is
`PARTIALLY_IMPLEMENTED_LOCAL / NOT_VALIDATED`; `VM_APPLICATION_STACK` remains
the only locally executable composite deployment path.

The local control-plane slice also persists a Redis Streams-compatible queue
envelope through a database outbox and models short-lived GitHub App/model
broker leases without token material. Checkpoint and terminal transitions
revoke active leases; approval/resume rotates them. Exact brokered egress policy
decisions are locally tested. Redis, GitHub, model and egress services remain
unconnected.

Pre-execution budget reservations and a sanitized trace-event store are now
locally implemented. Over-budget reservations atomically stop the job, cancel
the queue and revoke leases before external work. The trace schema covers the
fixed end-to-end span vocabulary and numeric measurements only. External cost
meters, OpenTelemetry Collector, Jaeger, Prometheus and live exporters remain
unconnected.

Redis Streams publish/consumer-group claim/acknowledgement and ordered
Kubernetes namespace/quota/policy/job application are implemented behind
injectable adapters. Activation is fail-closed on source and approval digests,
decision expiry, `kata-qemu-runtime-rs` and an approved digest-pinned internal image;
partial namespace creation is rolled back. Local fake-client adapter tests pass,
but the Redis service, k3s context, RuntimeClass, image, GitHub App, model and
egress brokers, checkpoint storage and OTLP Collector remain external blockers.

A separately authorized bounded live validator has now passed on the dedicated
local VM for `kata-qemu-runtime-rs`: positive Kata execution, default-runtime
bypass denial, privileged-pod denial, direct-IP egress denial, checkpoint
recreate, active deadline and cleanup were verified. This closes only the Kata
workload-validation blocker. The approved agent image, request-API cluster and
Redis bindings, credential/model/egress brokers, object storage and telemetry
pipeline remain unconnected, so end-to-end Mini-Ona runtime stays blocked.

Exit: one k3s product is provisioned, configured, observed and destroyed through the approved lifecycle with recovery evidence.

Container supply-chain checkpoint: ADR 0023, the seven-image lock, local policy
validator, release resolver and protected CI/CD workflow are implemented. They
remain `PARTIALLY_IMPLEMENTED_LOCAL`; no registry publish or k3s installation is
claimed until approved base/tool digests, workload identity, private registry,
exact kube context and live installation evidence are supplied.

## Stage D — Financial network fabric

Status: `DESIGN_ONLY`

- Produce a single-site topology, address/VRF/VLAN ownership and management-plane boundary.
- Prepare sanitized NX-OS/IOS-XE templates and emulator tests after licensed images are supplied.
- Validate dynamic routing convergence, filtering, synthetic multicast and rollback.

Exit: deterministic non-production network acceptance records exist without storing vendor binaries.

## Stage E — Integrated operations

Status: `PARTIAL`

- Join observability, audit, backup/restore, FinOps and lifecycle telemetry.
- Expose resource status, alerts, cost attribution and expiry in the portal.
- Add the metric-only monitoring assistant after deterministic alerting. Keep
  model output advisory, require `monitoring:assist`, persist no signal body,
  and validate an external provider only with a separate service principal.
- Add the dual-stage NAS file-exchange adapter for the approved financial SaaS
  and data-processing blueprints. Validate SMB 3.1.1 enforcement, scan reject,
  digest-bound approval, zone bypass denial, expiry and restore before runtime
  promotion.
- Publish the user frontend at `gg-snsdinfra.cloud` only after DNS, exact-name
  TLS SANs, OIDC redirect origins and default-host rejection are validated.
- Run an end-to-end synthetic service recovery exercise.

Exit: portal, automation, service planes and network share correlated sanitized evidence.

## Stage F — Public-cloud adapter

Status: `DEFERRED`

- Select a provider only after the private platform golden paths are stable.
- Implement the common adapter contract and a private connectivity design.
- Prove identity, network, policy, cost, backup and teardown behavior.

Exit: only then may the project claim an operating hybrid-cloud path. Scheduling remains final work and does not block Stages A-E.
