# Architecture

## Repository Components

- Least-privilege baseline: inbound, internal, public-web, egress, and evidence principles.
- Rule matrix: reviewable rule expectations and judgments.
- AWS network module: existing empty `aws_security_group` placeholder.
- Local validator: file, policy, matrix-row, Terraform, sensitive-content, and execution checks.

## Rule Model

Public HTTP/HTTPS terminates only at `aws-public-web-sg`. Bastion, private services, databases, and monitoring use management CIDR or Security Group-reference placeholders. The rule matrix contains no dangerous public inbound row.

## Validation Flow

The validator parses matrix rows, checks public-source and port combinations, validates the Terraform placeholder and repository safety, then generates evidence. It does not authenticate, query AWS, initialize Terraform, or create resources.
