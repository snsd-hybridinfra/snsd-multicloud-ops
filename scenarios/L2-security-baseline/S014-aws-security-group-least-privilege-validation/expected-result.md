# Expected Result

S014 is successful when the AWS Security Group least privilege validation plan is complete and ready for future approved execution.

## Success Conditions

- AWS Security Group existence can be validated using placeholder identifiers.
- SSH ingress is planned only from `<bastion-cidr>`.
- HTTP and HTTPS exposure is explicitly documented where applicable.
- DB port `3306` is not exposed to public internet sources.
- App-to-On-Prem DB access is scoped to `<onprem-db-cidr>`.
- Monitoring scrape access is scoped to `<monitoring-cidr>`.
- No `0.0.0.0/0` SSH rule is accepted.
- No unrestricted all-ports ingress rule is accepted.
- Egress policy is reviewed and broad egress is clearly flagged.
- All validation checks map to required evidence files.

## Evidence Conditions

- `commands.md` lists planned command or review actions with TODO output placeholders.
- `validation.md` lists each check with `NOT_RUN` status until execution.
- Future supporting evidence is expected in `configs/aws-security-group-rule-summary.md`, `configs/aws-sg-least-privilege-policy.md`, `logs/aws-security-group-validation.log`, and `screenshots/aws-security-group-rules.png`.
