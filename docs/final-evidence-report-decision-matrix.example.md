# Final Evidence Report Decision Matrix — Non-Production

| Evaluation Result | Example Evidence | Operational Meaning | Required Action | Final Judgment |
|---|---|---|---|---|
| All scenario IDs accounted for | coverage | complete | continue | FINAL_REPORT_READY |
| Scenario status matrix missing | missing | incomplete | restore | FINAL_REPORT_INCOMPLETE |
| Evidence status matrix missing | missing | incomplete | restore | FINAL_REPORT_INCOMPLETE |
| Required report section missing | missing | incomplete | correct | FINAL_REPORT_INCOMPLETE |
| Evidence coverage incomplete | partial | review | improve | FINAL_REPORT_WARNING |
| Blocked scenario exists | matrix | blocked | investigate | FINAL_REPORT_BLOCKED |
| Risk register has unresolved critical blocker | risk | blocked | investigate | FINAL_REPORT_BLOCKED |
| Excluded scope violated | finding | unsafe | reject | FINAL_REPORT_INVALID |
| Secret-like content detected | finding | unsafe | reject | FINAL_REPORT_INVALID |
| Real infrastructure identifier detected | finding | unsafe | reject | FINAL_REPORT_INVALID |
| Unsafe production certification claim detected | finding | unsafe | reject | FINAL_REPORT_INVALID |
| Report generated successfully | output | complete | validate | FINAL_REPORT_READY |
| Report validation passed | validation | complete | archive locally | FINAL_REPORT_READY |
