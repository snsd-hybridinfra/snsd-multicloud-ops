# Architecture

## Relevant Components

- Control Plane: records validation commands and evidence.
- AWS Service Zone: contains the planned AWS service node protected by Security Group rules.
- AWS Security Group: represents ingress and egress controls for the AWS service node.
- Bastion: approved management entry source for SSH access.
- On-Prem DB Zone: placeholder destination for application database access.
- Monitoring Zone: placeholder source for scrape or probe access.

## Access Model

- SSH access to `<aws-app-node>` must be allowed only from `<bastion-cidr>`.
- HTTP and HTTPS ingress may be planned only when the service exposure requirement is documented.
- DB port `3306` must not be exposed to `0.0.0.0/0` or other unrestricted sources.
- App-to-On-Prem DB access must use explicit placeholders such as `<onprem-db-cidr>`.
- Monitoring scrape access must use an explicit placeholder such as `<monitoring-cidr>`.
- Egress must be reviewed and justified for the AWS service node role.

## Boundary Notes

This scenario validates AWS Security Group design only. Azure NSG and OpenStack Security Group behavior are separate scenario responsibilities.
