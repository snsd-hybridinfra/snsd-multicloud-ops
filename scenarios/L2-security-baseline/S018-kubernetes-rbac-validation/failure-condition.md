# Failure Condition

S018 fails if a required artifact, policy subject, resource kind, or namespace is absent; a ClusterRoleBinding, cluster-admin, wildcard, default application account, application secrets permission, or monitoring write verb is present; or unsafe credential, Secret, endpoint, address, or active cluster command content is detected.

## Critical Failure Behavior

Any failed check produces a non-zero exit. Missing or ambiguous evidence is not treated as successful validation.

## Safety Failure

Detection of kubeconfig, tokens, certificates, keys, namespace secrets, endpoints, credentials, or account-specific values requires removal and rerunning the scenario.
