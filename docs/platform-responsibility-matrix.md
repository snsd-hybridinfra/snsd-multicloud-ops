# Platform Responsibility Matrix

**Status: PLANNED — responsibilities describe intended future roles only.**

## Purpose

This matrix prevents overlap and inflated claims across the lab platforms.

| Platform | Primary Responsibility | Validation Focus | Explicitly Not Responsible For |
|---|---|---|---|
| EVE-NG / On-Prem | Network zoning, routing, ACLs, and failure paths | On-Prem segmentation and controlled transit | Cloud resource lifecycle, application runtime, database service |
| OpenStack | Private Cloud | Neutron, Security Group, Floating IP window, Terraform, drift, cleanup | Public Cloud A/B claims, EKS/AKS, production HA |
| AWS | Public Cloud A minimum environment | VPC/subnets/SG, optional one EC2, Terraform/inventory/drift/policy/cleanup | Full application runtime, EKS, RDS, always-on public service |
| Azure | Public Cloud B minimum environment | VNet/subnets/NSG, optional one VM, Terraform/inventory/drift/policy/cleanup | Full application runtime, AKS, managed DB, always-on public service |
| Local Kubernetes | Application runtime | Nodes, workloads, Ingress, reverse proxy, load balancing, controlled failures | Cloud networking authority, public management plane, database persistence |
| Local MariaDB | Internal data platform | Access control, primary/replica, lag, backup, restore | Public database service, managed-cloud database, application ingress |
| Observability | Metrics and availability | Prometheus, Grafana, exporters, Blackbox | SIEM, EDR, SOAR, automated blocking |
| External address | Optional HTTP/HTTPS entry | External availability and Blackbox validation | SSH, database, APIs, monitoring, or management exposure |
| Control workstation | Tooling and evidence orchestration | Terraform/Ansible/CLI execution and sanitization | Permanent runtime service or public entry point |

## Ownership Rules

- Every resource has one named owner and one cleanup owner.
- Terraform-managed resources use `ManagedBy=Terraform`; manual exceptions need
  a change record and explicit cleanup steps.
- Cloud providers remain validation environments; local Kubernetes and MariaDB
  remain the application and data runtime axes.
- Cross-platform evidence must still be stored under the owning S001-S050
  scenario rather than a new scenario.

## Non-Production Disclaimer

The matrix assigns portfolio-lab responsibilities only. It is not an operating
model for a production organization.
