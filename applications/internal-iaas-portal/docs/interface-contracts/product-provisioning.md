# Product provisioning contract

The provider-bound execution-profile catalog is `terraform/catalog.json`. Its
five fixed profiles are `DEV-OS-VM-S/M/L` and `DEV-OS-K3S-S/M`. The
user-facing authority is the repository-level
`docs/platform/composite-service-catalog.yaml`: requesters select one approved
composite blueprint and bounded inputs. The current local API still exposes an
execution profile only through a service-authorized internal endpoint. The
public API and portal expose approved blueprints. `VM_APPLICATION_STACK`
persists its immutable manifest and carries it through approval to independent
runner verification; blueprints with an unimplemented component are rejected.
The legacy direct-profile request route is disabled by default and exists only
for explicit local compatibility tests.

Until that resolver exists, requesters supply only a lowercase project name,
an approved purpose, one internal execution profile, and one allowed duration.

CPU, memory, storage minimum, provider module, image, flavor, network, security
groups, key pair, and artifact digest are server-owned. Attempts to supply
unsupported parameters or a mismatched fixed runtime specification are denied.

The lifecycle uses three independent but correlated state machines:

```text
Request/Grant: PENDING -> APPROVED -> GRANTED -> REVOKED or EXPIRED
                       \-> REJECTED
                       \-> CANCELLED

Resource:      PROVISIONING -> RUNNING -> TERMINATING -> TERMINATED
                    |             |              \-> TERMINATION_FAILED -> TERMINATING
                    \-> PROVISION_FAILED -> PROVISIONING or TERMINATING

Runner job:    QUEUED -> PLANNING -> APPLYING -> SUCCEEDED
                    \-> explicit failure -> reviewed retry or destroy
```

Resource callbacks update the resource projection and `resource_status`; they
do not impersonate request or Grant transitions. The request remains
`APPROVED` until successful post-apply validation causes the Grant service to
issue a Grant and project `GRANTED`.

Grant issuance requires both successful apply and post-apply validation. k3s
then runs the approved Ansible configuration and requires
`bootstrap_status=READY`. Configuration failure automatically queues immediate
Terraform destroy inside the runner; rollback failure remains explicit. Revoke
or expiry blocks the Grant before queuing ordinary destroy. Failure states do
not issue a Grant.
