# Architecture

```text
S041 reference + decision + approval + rollback + no-drift sample
                             |
                             v
 validate-terraform-drift-remediation.ps1
                             |
                             v
       local log/summary + S043/S045 mappings
```

The static validator cannot execute Terraform, access state/providers, call cloud APIs, or mutate infrastructure.
