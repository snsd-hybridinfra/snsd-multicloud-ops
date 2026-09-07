# Zero Trust Protected Internal IaaS and k3s PaaS Portal

This directory contains a locally validated candidate application adopted from
`F:/2차프로젝트.zip` and refactored from its former public-cloud design to the
repository's OpenStack private-cloud axis.

## Current authority

- Implementation: `LOCAL_CANDIDATE`
- Validation: `LOCAL_VALIDATED`
- Deployment: `NOT_AUTHORIZED`
- Runtime evidence: `NONE`
- Zero Trust package status promotion: `NONE`
- Phase 1 or maturity change: `NONE`

The application is intended to become a protected system. It is not yet behind
an accepted OIDC/MFA/PEP path and has not created an OpenStack resource.

## Internal execution-profile catalog

The five entries below are provider-bound execution profiles used by the
current local candidate. They are not the final user-facing service catalog.
The root authority is
`../../docs/platform/composite-service-catalog.yaml`, where users select one of
eight approved composite blueprints and only bounded inputs. A local resolver
now exposes safe blueprint discovery and resolution plus a service-only full
manifest. `VM_APPLICATION_STACK` persists and carries the manifest through
approval to independent runner verification. The other seven blueprints remain
blocked when an adapter is missing. Execution profiles are service-only and no
local result receives runtime credit.

| Product | Provider resource | Fixed boundary |
|---|---|---|
| `DEV-OS-VM-S` | Nova VM + Neutron port | 2 vCPU / 2 GiB / at least 30 GiB |
| `DEV-OS-VM-M` | Nova VM + Neutron port | 2 vCPU / 4 GiB / at least 50 GiB |
| `DEV-OS-VM-L` | Nova VM + Neutron port | 2 vCPU / 8 GiB / at least 80 GiB |
| `DEV-OS-K3S-S` | Nova VM + Neutron port + k3s profile | 2 vCPU / 4 GiB / at least 40 GiB |
| `DEV-OS-K3S-M` | Nova VM + Neutron port + k3s profile | 2 vCPU / 8 GiB / at least 80 GiB |

All execution profiles use an existing operator-approved private network, security
groups, image, key pair, and flavor. The modules cannot create a network,
subnet, router, security group, identity, or Floating IP. Users cannot submit
HCL or choose provider identifiers.

The k3s execution profiles start from an approved base Glance image. After Terraform
validates the private Nova instance and Neutron port, digest-pinned Ansible
copies a separately approved k3s binary and matching air-gap image archive,
configures kernel and systemd settings, and installs the PaaS baseline. It
validates API readiness, CoreDNS, metrics-server, local-path provisioning, a
`dev` namespace, ResourceQuota, LimitRange, and default-deny NetworkPolicy.
Only then does the runner return `READY`. Ansible failure automatically invokes
Terraform destroy and never creates a Grant.

## Zero Trust protection boundary

```text
User / Approver
      |
      v
OIDC + MFA + PEP (planned, not deployed)
      |
      v
Portal/API -> approval policy -> signed fixed product -> Terraform runner
                                                    |
                                                    v
                                  Keystone/Nova/Neutron/Glance
                                                    |
                                                    v
                                      private Nova base VM
                                                    |
                                                    v
                              digest-pinned Ansible -> k3s PaaS
```

The intended package relationships are:

- `ZT-ID-001` / later centralized identity: subject, role, MFA, service identity;
- `ZT-NET-001`: private path, default deny, no Floating IP;
- `ZT-APP-001`: protected application/workload inventory and deployment gates;
- `ZT-DATA-001`: request, approval, Grant, audit, state, backup classification;
- `ZT-VIS-001`: sanitized decision, provisioning, and service telemetry;
- `ZT-AUTO-001`: deterministic allow-list and approval-bound execution.

These are candidate mappings, not inherited implementation or runtime evidence.

## Fail-closed runtime switch

The runner defaults to `RUNNER_MODE=mock`. Real execution additionally requires
`TF_OPENSTACK_DEPLOYMENT_AUTHORIZED=true`, a runner-local `clouds.yaml`, a named
`OS_CLOUD`, and every approved OpenStack input. Credentials and state never
belong in Git. k3s additionally requires
`TF_K3S_CONFIGURATION_AUTHORIZED=true`, a reviewed SSH identity and known-hosts
authority, and matching offline k3s binary/image SHA-256 values. The checked-in
Kubernetes base remains mock and unauthorized; a reviewed runtime overlay must
supply credentials, protected state storage, private paths, and approved
artifact digests.

## Local validation

From this directory, with the dependencies in `requirements-mvp.txt` available:

```powershell
python -m pytest -q
```

The test suite covers request/approval/Grant state transitions, positive and
negative authorization, fixed catalog synchronization, module digests,
arbitrary-module denial, private-only Terraform policy, k3s security baseline,
rollback/destroy flow, and fail-closed real execution.

## Source adoption record

- Archive SHA-256: `3cda17c993e17465676f607410a03f16d7ff0648a62ed403abea133950b4edb3e8`
- Safe source extraction: 270 files
- Excluded from adoption: `.env`, `.venv`, caches, bytecode, coverage, raw
  historical evidence, former provider Terraform modules, and obsolete plans.
- Archive pre-adoption tests: 62 passed with four deprecation warnings.
- Adopted OpenStack/PaaS tests: see the current validation record.
