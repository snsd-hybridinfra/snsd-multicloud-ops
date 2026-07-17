# Objective

## Operational Capability

Validate that a non-production Kolla-Ansible single-node OpenStack AIO control
plane can provision and operate the minimum Neutron provider/tenant network
path required for one instance.

## Success Definition

Success requires healthy core control-plane services and agents, active
provider/tenant resources, a correctly mapped Open vSwitch provider path,
EVE-NG reachability to the external router and Floating IP, and instance
reachability to its gateway and the public IPv4 network.

This scenario does not validate Terraform provider behavior (S006), OpenStack
Security Group least privilege (S016), drift, HA, storage, backup, monitoring,
or production hardening.
