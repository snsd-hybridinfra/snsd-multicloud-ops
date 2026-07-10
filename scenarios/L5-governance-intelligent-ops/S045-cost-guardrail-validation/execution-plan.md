# Execution Plan

1. Confirm that cost guardrail validation is placeholder governance review only.
2. Identify `<provider>`, `<resource-name>`, `<resource-type>`, `<cost-owner>`, `<environment>`, `<monthly-cost-estimate>`, and `<cost-threshold>`.
3. Review cost input artifact placeholders.
4. Review resource inventory placeholders.
5. Validate required cost owner tag or label.
6. Validate required environment tag or label.
7. Review approved resource type placeholder.
8. Review resource count threshold placeholder.
9. Review compute size threshold placeholder.
10. Review public IP usage justification.
11. Review unattached volume placeholder.
12. Review load balancer or reverse proxy cost justification.
13. Document cleanup candidate decision point without performing cleanup.
14. Classify each result as `COST_OK`, `COST_WARNING`, `COST_RISK`, `COST_UNKNOWN`, or `COST_OUT_OF_SCOPE`.
15. Capture TODO evidence references in `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.

No real billing API, Terraform command, cloud account, or cleanup action is used in this skeleton.
