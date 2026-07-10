# Failure Condition

S028 fails if Prometheus target discovery cannot be validated or expected targets are missing, unhealthy, or ambiguously labeled.

## Failure Conditions

- Prometheus service status cannot be reviewed.
- Prometheus configuration syntax validation fails or is unavailable.
- `/targets` page cannot be accessed or captured.
- Required target category is missing.
- A required target is DOWN.
- Scrape configuration is invalid.
- Target labels are duplicated or ambiguous.
- Target job name is wrong or inconsistent.
- AWS, Azure, OpenStack, or On-Prem placeholder target mapping is missing.
- Node Exporter, DB Exporter, Blackbox Exporter, or kube-state-metrics placeholder mapping is missing.
- Evidence cannot be captured or reviewed.
- Evidence contains credentials, secrets, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder target model exists.
- Future Prometheus service, config, `/targets`, or target mapping output is unavailable.
- Required evidence files are missing.
