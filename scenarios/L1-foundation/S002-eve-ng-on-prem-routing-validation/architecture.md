# Architecture

## Relevant Components

- Management Zone and `mgmt-router-01`
- Bastion Zone and `bastion-host-01`
- Transit Zone and `transit-router-01`
- Internal Server Zone and `internal-router-01`
- Monitoring Zone and `monitoring-router-01`
- Repository-local topology, examples, validator, and evidence

## Logical Flow

1. The topology document defines the five-zone logical model with CIDR placeholders.
2. Four example configurations describe placeholder interfaces and static routes.
3. The PowerShell validator reads those repository files only.
4. Results are written to the matching S002 evidence directory.

## Out-of-Scope Components

Live EVE-NG nodes, router sessions, device APIs, firewalls, cloud networks, Terraform, Ansible, Kubernetes, and monitoring systems are not accessed.
