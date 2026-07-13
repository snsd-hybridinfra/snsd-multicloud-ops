# Failure Condition

S019 fails if a required artifact, directive, header, exact value, placeholder, `always`, matrix entry, evidence rule, or limitation is absent; or unsafe TLS material, domain, address, credential, identifier, or active Nginx/network command is detected.

## Critical Failure Behavior

Any failed check produces a non-zero exit. Missing or ambiguous evidence is not treated as successful validation.

## Safety Failure

Detection of real service data, TLS keys, certificates, backend addresses, credentials, secrets, or account-specific values requires removal and rerunning the scenario.
