# Target Architecture

## Logical view

```text
Business and engineering users
        |
        v
Developer Portal
  - dashboard and catalog
  - request/change/extend/return
  - resource inventory and cost view
        |
        v
IDP control plane
  - OIDC/MFA and role mapping
  - policy/quota/budget checks
  - approval and immutable audit
  - lifecycle state machine
        |
        v
Automation plane
  - Terraform: infrastructure desired state
  - Ansible: OS and k3s configuration
  - GitOps: Kubernetes desired state
  - agent job orchestrator: queue, approval, checkpoint and budget
        |
        +------------------------+
        |                        |
        v                        v
OpenStack private IaaS       k3s PaaS
Nova/Neutron/Cinder/Glance   namespaces/apps/data services
        |                        |
        +-----------+------------+
                    v
Financial network underlay
Nexus NX-OS / IOS-XE / routing / multicast / segmentation

Cross-cutting: Zero Trust | observability | audit | backup/restore | FinOps
Extension: provider adapter -> approved public cloud (deferred)
```

## Flagship PaaS blueprint: Project Mini-Ona

`AI_AGENT_SANDBOX` accepts a bounded asynchronous engineering task and retains
its job state, policy decisions and checkpoints in the control plane. A
strongly isolated k3s sandbox pod clones through a task-scoped GitHub App
identity, edits and tests only the bounded workspace, records atomic checkpoint
commits and proposes a Draft pull request. Completion, cancellation, failure or
timeout destroys the pod; approval waiting checkpoints and releases compute,
then resumes in a new pod.

The required boundary is Kata Containers or gVisor class isolation, non-root
and capability-free execution, no host namespace or mount access, no automatic
service-account token, and CPU/memory/PID/storage quotas. Default-deny
NetworkPolicy is paired with controlled DNS and an authenticated FQDN-aware
egress broker; NetworkPolicy alone cannot prove domain-only egress. Git,
approved package mirrors, the model broker and platform telemetry are the only
destination classes. Wall time, iterations, tokens, cost, calls, concurrency
and egress bytes are hard budgets.

Trace continuity covers queue, scheduling, image pull, clone, inference, tool
execution, tests, checkpoints, push, PR creation and cleanup without exporting
raw prompts, source code or secrets. The authoritative contract is
`ai-agent-sandbox.yaml`. A service-only local simulation now persists job
transitions and emits an inert Job/NetworkPolicy/ResourceQuota bundle, but no
live k3s, Istio, queue, model, GitHub or storage integration is claimed.

## Trust boundaries

1. The portal never accepts arbitrary Terraform, provider IDs or unrestricted shell input.
2. Approval and execution identities are separate. A request cannot approve itself.
3. The runner receives only an allow-listed product and short-lived or externally supplied credentials.
4. OpenStack resources use private networks by default; public exposure requires a separate product and policy.
5. k3s bootstrap is digest-pinned, fail-closed and rollback-capable.
6. Network management is isolated from workload traffic and has an independent recovery path.
7. Backup and declarative rebuild tests use synthetic services and do not claim multi-site DR.
8. Public-cloud adapters cannot bypass the common request, policy, evidence and lifecycle contracts.

## Financial-network emphasis

- Model one site with deterministic address, VRF/VLAN and routing ownership.
- Exercise BGP/OSPF policy, route filtering, convergence and rollback in a non-production emulator.
- Add multicast only for an approved synthetic market-data workload; validate source/group boundaries and failure behavior.
- Keep out-of-band management and break-glass access independent from the IDP and identity provider.
- Use vendor images only when separately licensed and supplied outside Git. Configuration templates may be version controlled after sanitization.

## Service catalog boundary

The authoritative product model is `composite-service-catalog.yaml`. Eight
internal components are assembled only into eight operator-approved composite
blueprints. Users select a blueprint and the bounded environment, size,
duration and purpose inputs; they cannot select components, submit an arbitrary
dependency graph, supply HCL or choose provider identifiers.

The portal candidate's three private VM sizes and two private k3s profiles are
internal provider-bound execution profiles, not user-facing products. The local
resolver turns an approved blueprint into a digest-bound immutable deployment
manifest. `VM_APPLICATION_STACK` carries that manifest through request,
approval and mock-runner verification; every other blueprint remains blocked
where an adapter is absent. Deployment is all-or-nothing, and rollback follows
reverse dependency order. PostgreSQL, object storage, load-balancing, VDI and
other components receive no separate direct catalog exposure merely because
they participate in a blueprint.

The former `CI_CD_RUNNER` catalog entry is replaced by
`AI_AGENT_SANDBOX`, which includes bounded build/test behavior plus persistent
job control, isolation, approval, cost and observability requirements. It does
not expose arbitrary shell, repository credentials or model keys as product
inputs.

## Public-cloud extension

The common provider contract covers identity mapping, network intent, resource request, policy decision, state backend, telemetry, cost tags and destroy confirmation. A provider-specific module is not authoritative merely because it exists in `platform/`; it must be reconciled and accepted through this contract.
