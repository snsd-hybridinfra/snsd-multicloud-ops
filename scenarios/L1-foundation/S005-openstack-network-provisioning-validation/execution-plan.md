# Execution Plan

## Preparation

1. Confirm Profile B/C capacity limits and nested virtualization.
2. Confirm the EVE-NG VLAN 70 provider path and one-small-Nova-instance ceiling.
3. Keep credentials, generated authentication files, and keys outside the repository.

## Executed Workflow

1. Run Kolla-Ansible bootstrap and prechecks.
2. Pull the approved lab images and deploy the AIO services.
3. Generate post-deploy client configuration with the explicit inventory path.
4. Confirm authentication, service registration, endpoints, Nova health, hypervisor state, and Neutron agents.
5. Create the provider and tenant network resources, router, image, minimal flavor, Security Group reference, key-pair reference, instance, and Floating IP.
6. Validate namespaces, Open vSwitch bridges/ports, resource states, EVE-NG ingress, instance gateway reachability, public IPv4 egress, and cloud-init completion.
7. Normalize the operator-supplied results and remove all sensitive/dynamic values before writing evidence.

## Evidence Capture

Only the sanitized result categories and verdicts are retained. Raw command
output, token values, authentication files, IDs, MAC addresses, and dynamic
addresses are not committed.

## Planned Follow-Up

Terraform reproduction, idempotency, destroy/recreate, Security Group policy,
backup, monitoring, and hardening remain planned under their owning scenarios.
