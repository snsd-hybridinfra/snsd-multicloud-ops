# S017-mariadb-access-control-validation

| Field | Value |
|---|---|
| Scenario ID | S017 |
| Scenario Name | MariaDB Access Control Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | Database access security |
| Related Components | On-Prem DB Primary, On-Prem DB Replicas, MariaDB users, application nodes, Bastion, management access path |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S017-mariadb-access-control-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the MariaDB access control model for the On-Prem Internal Server Zone in the SNSD Multi-Cloud Ops project.

## Scope Summary

This scenario validates MariaDB access control design only. It covers DB primary and replica access policy, application user access, replication user separation, backup user separation, denial of public DB access, denial of direct Web node DB access, cloud App/API node placeholders, management-only administrative access placeholders, user/host/grant review, and DB port exposure review.

## Validation Summary

Validation checks confirm that MariaDB access is bound to approved hosts and roles, that root remote access and public DB exposure are denied, and that overly broad grants are treated as failures. Replication, replication lag, backup, and restore validation are handled by separate scenarios.

## Evidence Output Summary

Evidence must be recorded under `evidence/L2-security-baseline/S017-mariadb-access-control-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
