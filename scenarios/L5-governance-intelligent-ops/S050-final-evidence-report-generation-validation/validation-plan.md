# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | Inputs, samples, generator, outputs exist. | validator log |
| V002 | Generation | Markdown/JSON generated locally. | generation log |
| V003 | Required sections | All report sections exist. | generated report |
| V004 | Scenario coverage | S001-S050 and total 50 exist. | generated report |
| V005 | Summary JSON | Complete and valid judgment. | generated JSON |
| V006 | Manifest | Required references/ranges exist. | manifest |
| V007 | Sample evidence | Discovery/coverage/sections/final samples pass. | sample logs |
| V008 | Governance references | Matrices, risk, excluded scope referenced. | generated report |
| V009 | Safety boundary | No live validation/secrets/real identifiers. | safety sample/report |
| V010 | Intelligent Ops | S047-S049 summarized. | generated report |
| V011 | Certification safety | No affirmative audit/certification claim. | policy/report |
| V012 | Artifact safety | No state/tfvars/kube/cloud/key/packet artifact. | validator log |
| V013 | Sensitive safety | No real network/ID/credential/secret. | validator log |
| V014 | Execution safety | No external/infrastructure command. | validator source/log |
| V015 | Final summary | Sample summary ready. | final sample |
| V016 | Maturity | Report judgment and sample maturity recorded. | validation summary |
