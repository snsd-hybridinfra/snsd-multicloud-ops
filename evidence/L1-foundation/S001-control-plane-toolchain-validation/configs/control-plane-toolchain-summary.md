# Control Plane Toolchain Summary

- Scenario: S001-control-plane-toolchain-validation
- Generated: 2026-07-13T14:13:08+09:00
- Overall result: **PASS**
- Exit rule: non-zero only when a core tool is unavailable or cannot return version output

| Check ID | Tool | Classification | Result | Version or Detail |
|---|---|---|---|---|
| V001 | Git | CORE | PASS | git version 2.55.0.windows.2 |
| V002 | PowerShell | CORE | PASS | 5.1.22621.6133 |
| V003 | SSH | CORE | PASS | OpenSSH_for_Windows_9.5p1, LibreSSL 3.8.2 |
| V004 | Python | CORE | PASS | Python 3.13.13 |
| V005 | Terraform | LATER_STAGE | WARN | Command not found. |
| V006 | Ansible | LATER_STAGE | WARN | Command not found. |
| V007 | kubectl | LATER_STAGE | WARN | Command not found. |
| V008 | Docker | LATER_STAGE | WARN | Command not found. |

## Safety Boundary

The validation used command discovery and local version-only invocations. It did not authenticate to cloud providers or registries, connect to Kubernetes clusters, read kubeconfig or credentials, access tfstate, or change infrastructure.
