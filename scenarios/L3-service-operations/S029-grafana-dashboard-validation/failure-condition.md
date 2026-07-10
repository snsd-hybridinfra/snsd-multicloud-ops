# Failure Condition

S029 fails if Grafana dashboard visibility or datasource-backed panel rendering cannot be validated.

## Failure Conditions

- Grafana service access cannot be reviewed.
- Login requirement reference from S020 is missing.
- Prometheus datasource is missing.
- Prometheus datasource connection fails.
- Dashboard placeholder is missing for a required category.
- Dashboard is empty.
- Dashboard panel is broken.
- Panel query returns no time-series or status data when data is expected.
- Dashboard time range prevents expected data from rendering and is not explained.
- Dashboard screenshot is missing.
- Anonymous dashboard exposure is detected.
- Evidence contains Grafana passwords, credentials, secrets, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder dashboard model exists.
- Future Grafana service, datasource, panel, or screenshot evidence is unavailable.
- Required evidence files are missing.
