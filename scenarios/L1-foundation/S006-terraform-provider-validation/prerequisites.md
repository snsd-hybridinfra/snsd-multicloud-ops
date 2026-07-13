# Prerequisites

## Required Repository State

- The repository can be read locally.
- The S006 scenario and evidence directories exist.
- PowerShell can run the validation script.

## Optional Tool

- Terraform is optional for the formatting check. Its absence produces a warning and does not fail required repository validation.

## Not Required

- AWS, Azure, or OpenStack CLI access or authentication.
- Provider credentials, account identifiers, `clouds.yaml`, or openrc.
- Terraform initialization, backend access, provider download, state, plan, or cloud access.

S001 records local toolchain readiness. S003-S005 own network definition validation.
