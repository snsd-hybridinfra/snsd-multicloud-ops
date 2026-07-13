# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Example inventory file | Test the expected YAML path. | Example inventory exists. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V002 | Inventory schema file | Test the schema path. | Schema document exists. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V003 | Non-production marker | Search the inventory header. | Explicit marker exists. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V004 | Required groups | Search for all ten group keys. | Every group exists. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V005 | Required placeholder hosts | Search for all ten aliases. | Every host alias exists. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V006 | Required schema fields | Search the schema for eight fields. | Every field is documented. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V007 | Provider or zone values | Search for all approved placement values. | Every allowed value is documented. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V008 | Component type values | Search for all approved component values. | Every allowed value is documented. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V009 | Host address placeholders | Validate `ansible_host` formats and scan for numeric IPs. | Only angle-bracket placeholders exist. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V010 | Sensitive inventory content | Scan for credentials, key paths, usernames, IDs, UUIDs, and tokens. | No forbidden content exists. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V011 | Live inventory artifacts | Inspect inventory filenames. | No production, live, hosts.ini, or vault file exists. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |
| V012 | Execution safety boundary | Scan validator source for active external commands. | No live execution command exists. | `logs/multicloud-inventory-validation.log`, `configs/multicloud-inventory-summary.md` |

## Review Notes

All checks are required and any failure produces a non-zero exit.
