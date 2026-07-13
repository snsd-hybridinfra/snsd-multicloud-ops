# Failure Condition

The implementation fails on missing IDs/sections/matrices/risks/exclusions, invalid judgment, unsafe certification claims, live-validation claims, state/config/key artifacts, real identifiers/networks, secrets, or production data.

The scenario fails if:

- A required status matrix, checklist, implementation log, or risk register is missing.
- Scenario or evidence coverage is incomplete without being reported.
- Progress totals conflict with scenario or evidence records.
- Failed, blocked, partial, or missing-evidence items are omitted.
- A required final report section or final judgment is missing.
- More than one final judgment is presented as authoritative.
- An unsupported compliance, certification, production audit readiness, automated enforcement, or GRC integration claim is made.
- Evidence references cannot be traced to a scenario validation item.
- Credentials, secrets, private keys, tfstate, kubeconfig, account identifiers, billing identifiers, or account-specific values are exposed.
