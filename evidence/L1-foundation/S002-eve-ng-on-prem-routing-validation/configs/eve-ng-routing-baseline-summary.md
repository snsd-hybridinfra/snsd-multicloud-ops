# EVE-NG Routing Baseline Summary

- Scenario: S002-eve-ng-on-prem-routing-validation
- Generated: 2026-07-11T12:58:51+09:00
- Overall result: **PASS**
- Scope: repository topology and non-production example configs

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Topology document | PASS | Required topology document exists. |
| V002 | Router example configs | PASS | All four required example configs exist. |
| V003 | Required zones | PASS | All required zones are documented. |
| V004 | Placeholder devices | PASS | All required placeholder devices are documented. |
| V005 | CIDR placeholders | PASS | All required CIDR placeholder tokens are documented. |
| V006 | Example config structure | PASS | All configs are marked non-production and contain placeholder interfaces and routes. |
| V007 | Secret-like content | PASS | No private-key or credential assignment pattern was detected. |
| V008 | Literal IP addresses | PASS | No IPv4 literal was detected in example configs. |

## Safety Boundary

The validation read only repository documentation and example configuration files. It did not authenticate to EVE-NG, use its API, connect to routers, read credentials, contact cloud providers, inspect kubeconfig, or access tfstate.
