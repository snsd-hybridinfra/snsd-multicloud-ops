# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | All S049 artifacts exist. | validator log |
| V002 | Command safety | No live/model/LLM/blocking actions. | command runbook |
| V003 | Report template | Required sections and judgments exist. | template |
| V004 | Input summary | Counts, evidence, S047/S048/S050 exist. | input YAML |
| V005 | Valid report | Sections, mappings, human review, disclaimers pass. | report Markdown |
| V006 | Summary JSON | Parseable, complete, mapped, REPORT_READY. | summary JSON |
| V007 | Invalid report | Deliberate missing/invalid content recognized. | invalid report |
| V008 | Report evidence | Template/input/run/pass/fail/mapping consistent. | sample logs |
| V009 | Privacy | Prohibited telemetry and identifiers absent. | privacy log |
| V010 | Final summary | No live/model/LLM/blocking action. | final sample |
| V011 | Manifest | Required fields and mappings exist. | manifest |
| V012 | Policy | Human review and safety requirements exist. | policy |
| V013 | Binary safety | No model/packet binary. | validator log |
| V014 | Sensitive/execution safety | No endpoint, secret, external execution. | validator log |
| V015 | Optional script | Deterministic standard-library reporting. | Python example |
| V016 | Maturity | Synthetic interpretation/count warning. | summary |
