# Prerequisites

## Required Repository State

- The repository can be read locally.
- The S005 scenario and evidence directories exist.
- PowerShell can run the validation script.

## Optional Tool

- Terraform is optional for the formatting check. Its absence produces a warning and does not fail required repository validation.

## Not Required

- OpenStack CLI, login, `clouds.yaml`, or openrc.
- Provider credentials, authentication URLs, or account identifiers.
- Terraform initialization, backend access, state, plan, or cloud access.

S001 records local toolchain readiness. S006 owns provider validation.
