# Failure Condition

S016 fails if a required baseline, matrix, group placeholder, policy statement, or Terraform resource is absent; a dangerous port is public; the public-web exception is overbroad; or unsafe configuration, identity, secret, state, variable, backend, address, or active cloud command content is detected.

## Critical Failure Behavior

Any failed check produces a non-zero exit. Missing or ambiguous evidence is not treated as successful validation.

## Safety Failure

Detection of OpenStack credentials, configuration files, identity values, private material, state, real tfvars, public addresses, or account-specific content requires removal and rerunning the scenario.
