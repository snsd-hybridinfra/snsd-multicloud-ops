# Execution Plan

1. Confirm required static artifacts.
2. Parse no-drift, drift, and critical-drift evidence.
3. Validate classification and S042/S043 mappings.
4. Parse the sanitized JSON examples and manifest.
5. scan for forbidden Terraform artifacts, identifiers, network values, and secrets.
6. Generate the validation log and summary.

No Terraform, cloud API, remediation, remote-state, or infrastructure operation occurs.
