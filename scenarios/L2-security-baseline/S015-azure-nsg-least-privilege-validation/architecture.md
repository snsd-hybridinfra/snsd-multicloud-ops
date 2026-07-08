# Architecture

## Relevant Components

- Control Plane: records validation commands and evidence.
- Azure Service Zone: contains the planned Azure App Node protected by NSG rules.
- Azure Network Security Group: represents inbound and outbound controls for the Azure App Node.
- Bastion: approved management entry source for SSH access.
- On-Prem DB Zone: placeholder destination for application database access.
- Monitoring Zone: placeholder source for scrape or probe access.

## Access Model

- SSH access to `<azure-app-node>` must be allowed only from `<bastion-cidr>`.
- HTTP and HTTPS inbound exposure may be planned only when the service exposure requirement is documented.
- DB port `3306` must not be exposed to `Internet`, `Any`, `0.0.0.0/0`, or other unrestricted sources.
- Azure App-to-On-Prem DB access must use explicit placeholders such as `<onprem-db-cidr>`.
- Monitoring scrape access must use an explicit placeholder such as `<monitoring-cidr>`.
- Outbound rules must be reviewed and justified for the Azure App Node role.

## Boundary Notes

This scenario validates Azure NSG design only. AWS Security Group and OpenStack Security Group behavior are separate scenario responsibilities.
