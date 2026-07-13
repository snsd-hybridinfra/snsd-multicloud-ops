# Failure Condition

S020 fails if a required artifact, section, disabled value, denial statement, matrix control, or placeholder is absent; anonymous access is enabled by config or environment; or an unsafe password, token, datasource credential, URL, address, identifier, private material, or active service/network command is detected.

## Critical Failure Behavior

Any failed check produces a non-zero exit. Missing or ambiguous evidence is not treated as successful validation.

## Safety Failure

Detection of real Grafana credentials, API tokens, datasource secrets, URLs, private material, or account-specific values requires removal and rerunning the scenario.
