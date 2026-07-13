# Scope

## Included

- OpenStack Security Group baseline and non-production rule matrix validation.
- Default-deny, explicit-allow, public-web exception, internal access, and egress policy checks.
- Local inspection of `openstack_networking_secgroup_v2` and `openstack_networking_secgroup_rule_v2` placeholders.
- Dangerous public ingress detection for ports 22, 3306, 5432, 6379, 9200, 5601, 9090, and 3000.
- Sensitive-content, public-address, state, tfvars, clouds.yaml, openrc, backend, and execution-boundary checks.

## Excluded

- OpenStack authentication, OpenStack CLI, cloud API calls, and live Security Group queries.
- Terraform init, plan, apply, destroy, backend, state, or real variables.
- OpenStack resource creation or modification.
- Network provisioning (S005), provider validation (S006), SSH controls (S011-S013), AWS Security Groups (S014), and Azure NSGs (S015).
- OpenStack multi-node HA, Ceph, Octavia, and production-grade private cloud HA.
