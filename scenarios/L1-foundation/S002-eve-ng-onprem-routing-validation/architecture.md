# Architecture

## Relevant Components

- Management Zone: administrative access segment represented by `<management-gateway>`.
- Bastion Zone: controlled access segment represented by `<bastion-gateway>`.
- Transit Zone: routing exchange segment represented by `<transit-router>`.
- Internal Server Zone: internal workload segment represented by `<internal-server-gateway>`.
- Monitoring Zone: observability segment represented by `<monitoring-gateway>`.
- EVE-NG topology file and router configuration snapshots.

## Logical Flow

1. Management Zone reaches Bastion Zone through the expected routed path.
2. Bastion Zone reaches Internal Server Zone through the expected routed path.
3. Monitoring Zone reaches Internal Server Zone for operational visibility.
4. Transit Zone exposes required routes for upstream or cross-zone forwarding.
5. Default routes exist only where the approved lab design requires them.

## Firewall Boundary Awareness

Firewall boundaries may exist between zones, but this scenario does not implement or modify firewall rules. Any blocked path must be recorded as a routing or boundary observation, not remediated here.

## Out-of-Scope Components

Cloud networks, Kubernetes clusters, Terraform state, Ansible automation, monitoring configuration, ML pipelines, and backup systems are not accessed by this scenario.
