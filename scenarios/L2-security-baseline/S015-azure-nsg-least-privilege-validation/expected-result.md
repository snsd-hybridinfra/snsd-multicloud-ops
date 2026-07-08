# Expected Result

S015 is successful when the Azure NSG least privilege validation plan is complete and ready for future approved execution.

## Success Conditions

- Azure NSG existence can be validated using placeholder identifiers.
- SSH inbound access is planned only from `<bastion-cidr>`.
- HTTP and HTTPS exposure is explicitly documented where applicable.
- DB port `3306` is not exposed to public internet sources.
- Azure App-to-On-Prem DB access is scoped to `<onprem-db-cidr>`.
- Monitoring scrape access is scoped to `<monitoring-cidr>`.
- No `Any` or `Internet` SSH rule is accepted.
- No unrestricted all-ports inbound rule is accepted.
- Outbound policy is reviewed and broad outbound access is clearly flagged.
- All validation checks map to required evidence files.

## Evidence Conditions

- `commands.md` lists planned command or review actions with TODO output placeholders.
- `validation.md` lists each check with `NOT_RUN` status until execution.
- Future supporting evidence is expected in `configs/azure-nsg-rule-summary.md`, `configs/azure-nsg-least-privilege-policy.md`, `logs/azure-nsg-validation.log`, and `screenshots/azure-nsg-rules.png`.
