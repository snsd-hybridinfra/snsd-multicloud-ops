# Cloud Cost Guardrails

**Status: PLANNED — no AWS, Azure, or OpenStack resource exists.**

## Purpose

AWS and Azure are minimum, credit-bounded validation environments. OpenStack is
the private-cloud validation axis. No document authorizes provider spend or
proves that a resource exists.

## Resource Limits

| Platform | Maximum Compute | Public Address Rule | Default Compute Setting |
|---|---:|---|---|
| AWS | 1 EC2 instance | Short approved validation window only | Disabled where practical |
| Azure | 1 VM | Short approved validation window only | Disabled where practical |
| OpenStack | 1 initial Nova instance | Floating IP only during approved validation | Disabled where practical |

The initial Nova flavor target is approximately 1 vCPU and 1GB RAM. Increasing
the count or size requires a host-capacity review and a revised planning record.

## Prohibited by Default

### AWS

- NAT Gateway;
- Application or Network Load Balancer;
- Site-to-Site VPN;
- RDS;
- EKS;
- always-on public IPv4.

### Azure

- NAT Gateway;
- VPN Gateway;
- Application Gateway;
- Azure Bastion;
- AKS;
- managed database;
- always-on public IP.

Exceptions require a documented purpose, owner, estimate, TTL, approval, and
cleanup proof before implementation. No exception is implied by this baseline.

## Required Tags

Every cloud resource must define:

- `Project`;
- `Environment`;
- `Owner`;
- `ManagedBy`;
- `TTL`;
- `Purpose`.

Missing ownership or TTL prevents apply. Tags must not contain account IDs,
credentials, personal data, or secrets.

## Pre-Apply Guardrail

1. Confirm provider/region is explicitly approved.
2. Review Terraform plan and resource counts.
3. Reject prohibited services and unbounded public addresses.
4. Confirm free-tier/credit fit and document the estimate privately.
5. Confirm cleanup owner and expiry.
6. Keep compute deployment disabled until the validation window opens.

## Post-Validation Guardrail

- Destroy temporary compute and public addresses immediately after evidence
  collection.
- Verify resource inventories are empty or match the approved retained set.
- Record cleanup evidence without billing IDs, account values, or real public
  addresses.
- Treat cleanup failure as a blocker for additional public-cloud apply.

## Non-Production Disclaimer

This is a portfolio cost-control baseline, not production FinOps, budget
enforcement, or a billing integration.
