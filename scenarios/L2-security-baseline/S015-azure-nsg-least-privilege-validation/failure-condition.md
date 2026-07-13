# Failure Condition

S015 fails if a required baseline, matrix, NSG placeholder, policy statement, or Terraform structural placeholder is absent; a dangerous port is public; the public-web exception is overbroad; or unsafe identity, secret, state, variable, backend, address, or active cloud command content is detected.

## Critical Failure Behavior

Any failed check produces a non-zero exit. Missing or ambiguous evidence is not treated as successful validation.

## Safety Failure

Detection of Azure identity values, credentials, private material, state, real tfvars, real public addresses, or account-specific content requires removal and rerunning the scenario.
