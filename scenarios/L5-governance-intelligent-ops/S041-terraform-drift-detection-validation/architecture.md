# Architecture

```text
Sanitized plan JSON/text + runbook/policy/matrices
                     |
                     v
 validate-terraform-drift-detection.ps1
                     |
                     v
 local log + summary + S042/S043 linkage
```

The validator reads repository files only. Terraform, providers, remote backends, cloud APIs, credentials, and infrastructure are outside the execution boundary.
