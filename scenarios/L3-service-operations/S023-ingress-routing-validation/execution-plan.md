# Execution Plan

1. Run the validator without parameters for static validation.
2. Confirm documentation, Ingress files, command examples, and samples.
3. Validate Ingress kind/name/namespace/class and host/path/pathType.
4. Compare backend name/port/namespace with the S022 Service.
5. Reject wildcard host, Secret resource, TLS material, and sensitive content.
6. Parse ingress list, describe, and endpoint evidence; report placeholder ADDRESS as WARN.
7. Confirm four guarded read-only live argument sets and no automatic curl.
8. Use `-LiveKubectl` only when explicitly approved.

## Execution Boundary

Default mode invokes neither kubectl nor curl. Live mode only observes Ingress, Service, and Endpoints resources.
