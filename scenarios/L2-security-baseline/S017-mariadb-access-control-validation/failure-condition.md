# Failure Condition

S017 fails if a required artifact, account, or policy statement is absent; a grant is missing or overbroad; an application or monitoring grant contains a dangerous privilege; or unsafe password, connection, dump, secret, address, identifier, or active database command content is detected.

## Critical Failure Behavior

Any failed check produces a non-zero exit. Missing or ambiguous evidence is not treated as successful validation.

## Safety Failure

Detection of a real database credential, host, connection string, dump, export, private key, state, cloud identity, or account-specific value requires removal and rerunning the scenario.
