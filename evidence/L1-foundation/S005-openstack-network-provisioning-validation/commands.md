# Commands

- Scenario: S005-openstack-network-provisioning-validation
- Validation date: 2026-07-16
- Initial runtime authority: operator-executed OpenStack/EVE-NG lab session
- Current restricted authority: Codex may execute one forced read-only command
- General shell and mutation authority: not granted

Raw terminal output, authentication material, and command history are not
stored. The following sanitized patterns identify the command context reported
by the operator; placeholders replace environment-specific values.

## Codex-Executed Restricted Command

```powershell
powershell -ExecutionPolicy Bypass -File tools\openstack-validator\invoke-openstack-validation.ps1
```

The wrapper invokes exactly:

```text
ssh -o BatchMode=yes openstack-validator validate-all
```

The SSH alias and dedicated private key are outside the repository. The remote
forced-command dispatcher rejects an empty request, an interactive shell, and
every command other than `validate-all`. The validator performs current-state
read-only checks and returns a non-zero exit code if any required check fails.

## Kolla-Ansible Workflow Context

```text
kolla-ansible -i <AIO_INVENTORY> bootstrap-servers
kolla-ansible -i <AIO_INVENTORY> prechecks
kolla-ansible -i <AIO_INVENTORY> pull
kolla-ansible -i <AIO_INVENTORY> deploy
kolla-ansible -i <AIO_INVENTORY> post-deploy
```

The operator reported successful completion after correcting the documented
sudo, virtual-environment dependency, test-image guard, option-support, and
inventory-path issues. No authentication-file content is retained.

## Control-Plane Read-Only Context

```text
openstack --os-cloud <ADMIN_CLOUD_PROFILE> token issue
openstack --os-cloud <ADMIN_CLOUD_PROFILE> service list
openstack --os-cloud <ADMIN_CLOUD_PROFILE> endpoint list
openstack --os-cloud <ADMIN_CLOUD_PROFILE> compute service list
openstack --os-cloud <ADMIN_CLOUD_PROFILE> hypervisor list
openstack --os-cloud <ADMIN_CLOUD_PROFILE> network agent list
```

The token value, endpoint URLs containing management addresses, service IDs,
project/user IDs, and hypervisor management address are omitted.

## Resource Read-Only Context

```text
openstack --os-cloud <ADMIN_CLOUD_PROFILE> network show <PROVIDER_NETWORK>
openstack --os-cloud <ADMIN_CLOUD_PROFILE> network show <TENANT_NETWORK>
openstack --os-cloud <ADMIN_CLOUD_PROFILE> router show <ROUTER>
openstack --os-cloud <ADMIN_CLOUD_PROFILE> image show <IMAGE>
openstack --os-cloud <ADMIN_CLOUD_PROFILE> server show <INSTANCE>
openstack --os-cloud <ADMIN_CLOUD_PROFILE> floating ip show <FLOATING_IP>
openstack --os-cloud <ADMIN_CLOUD_PROFILE> console log show <INSTANCE>
```

Expected provider attributes use the actual CLI field names
`provider:network_type`, `provider:physical_network`, and `router:external`.

## Namespace and Open vSwitch Context

```text
ip netns list
docker exec <OVS_DB_CONTAINER> ovs-vsctl show
docker exec <OVS_DB_CONTAINER> ovs-vsctl port-to-br <PROVIDER_NIC>
docker exec <OVS_VSWITCHD_CONTAINER> ovs-ofctl show br-ex
```

The earlier individual commands were operator-executed. Codex later
corroborated their current-state results only through the restricted validator;
it did not receive direct shell or arbitrary command access. Container names,
namespace IDs, port names, MAC addresses, and dynamic interface names are not
retained.

## Data-Plane Probe Context

```text
EVE-NG router: ping <ROUTER_EXTERNAL_IP>
EVE-NG router: ping <FLOATING_IP>
tenant instance: ping <TENANT_GATEWAY>
tenant instance: ping <PUBLIC_CONNECTIVITY_TEST_ADDRESS>
```

## Local Repository Checks Executed by Codex

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-repo-structure.ps1
powershell -ExecutionPolicy Bypass -File tools\validate-scenario-quality.ps1
git diff --check
git status --short
```

## Planned Follow-Up, Not Run

Terraform reproduction, idempotency, destroy/recreate, storage, backup,
monitoring, hardening, AWS/Azure, and Kubernetes integration commands remain
planned and were not run for S005.
