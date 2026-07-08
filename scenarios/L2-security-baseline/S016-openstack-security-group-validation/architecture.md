# Architecture

## Relevant Components

- Control Plane: records validation commands and evidence.
- OpenStack Private Cloud Service Zone: contains the planned OpenStack App VM protected by Security Group rules.
- OpenStack Security Group: represents ingress and egress controls for the OpenStack App VM.
- Bastion: approved management entry source for SSH access.
- On-Prem DB Zone: placeholder destination for application database access.
- Monitoring Zone: placeholder source for scrape or probe access.

## Access Model

- SSH access to `<openstack-app-node>` must be allowed only from `<bastion-cidr>`.
- HTTP and HTTPS ingress may be planned only when the service exposure requirement is documented.
- DB port `3306` must not be exposed to `0.0.0.0/0`, public network sources, provider network sources, or other unrestricted sources.
- OpenStack App-to-On-Prem DB access must use explicit placeholders such as `<onprem-db-cidr>`.
- Monitoring scrape access must use an explicit placeholder such as `<monitoring-cidr>`.
- Egress rules must be reviewed and justified for the OpenStack App VM role.

## Boundary Notes

This scenario validates OpenStack Security Group design only. AWS Security Group and Azure NSG behavior are separate scenario responsibilities.
