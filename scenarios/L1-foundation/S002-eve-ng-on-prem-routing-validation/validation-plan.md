# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Topology document | Test the required Markdown path. | The topology document exists. | `logs/eve-ng-routing-baseline-validation.log`, `configs/eve-ng-routing-baseline-summary.md` |
| V002 | Router example configs | Test all four required config paths. | All example configs exist. | `logs/eve-ng-routing-baseline-validation.log`, `configs/eve-ng-routing-baseline-summary.md` |
| V003 | Required zones | Search the topology for five zone names. | All required zones are documented. | `logs/eve-ng-routing-baseline-validation.log`, `configs/eve-ng-routing-baseline-summary.md` |
| V004 | Placeholder devices | Search the topology for five device names. | All required devices are documented. | `logs/eve-ng-routing-baseline-validation.log`, `configs/eve-ng-routing-baseline-summary.md` |
| V005 | CIDR placeholders | Search the topology for five required tokens. | All required CIDR placeholders are documented. | `logs/eve-ng-routing-baseline-validation.log`, `configs/eve-ng-routing-baseline-summary.md` |
| V006 | Example config structure | Inspect non-production marker, placeholder interface, and placeholder route syntax. | Every example satisfies the repository model. | `logs/eve-ng-routing-baseline-validation.log`, `configs/eve-ng-routing-baseline-summary.md` |
| V007 | Secret-like content | Scan example configs for private-key and credential assignment patterns. | No forbidden pattern is detected. | `logs/eve-ng-routing-baseline-validation.log`, `configs/eve-ng-routing-baseline-summary.md` |
| V008 | Literal IP addresses | Scan example configs for IPv4 literals. | No literal IPv4 address is detected. | `logs/eve-ng-routing-baseline-validation.log`, `configs/eve-ng-routing-baseline-summary.md` |

## Review Notes

Every check is local and read-only except for evidence generation. Any required model or safety failure returns a non-zero exit code.
