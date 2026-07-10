# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Prometheus metric source availability reference validation plan | `commands.md`; `configs/ml-metric-source-mapping.md`; `validation.md` | review plan, source mapping, validation record | yes |
| Metric query input validation plan | `commands.md`; `configs/ml-metric-dataset-collection-summary.md`; `validation.md` | review plan, collection summary, validation record | yes |
| Node metric dataset collection placeholder validation plan | `configs/ml-metric-source-mapping.md`; `validation.md` | source mapping, validation record | yes |
| Kubernetes metric dataset collection placeholder validation plan | `configs/ml-metric-source-mapping.md`; `validation.md` | source mapping, validation record | yes |
| MariaDB metric dataset collection placeholder validation plan | `configs/ml-metric-source-mapping.md`; `validation.md` | source mapping, validation record | yes |
| Blackbox metric dataset collection placeholder validation plan | `configs/ml-metric-source-mapping.md`; `validation.md` | source mapping, validation record | yes |
| Dataset schema validation plan | `configs/ml-metric-dataset-schema.md`; `validation.md` | schema, validation record | yes |
| Timestamp field validation plan | `configs/ml-metric-dataset-schema.md`; `validation.md` | schema, validation record | yes |
| Metric value field validation plan | `configs/ml-metric-dataset-schema.md`; `validation.md` | schema, validation record | yes |
| Target label consistency validation plan | `configs/ml-metric-dataset-schema.md`; `configs/ml-metric-source-mapping.md`; `validation.md` | schema, source mapping, validation record | yes |
| Dataset file existence placeholder validation plan | `commands.md`; `configs/ml-metric-dataset-collection-summary.md`; `validation.md` | review plan, collection summary, validation record | yes |
| Dataset quality state validation plan | `configs/ml-dataset-quality-model.md`; `validation.md` | quality model, validation record | yes |
| Failure condition for missing metric source, empty dataset, invalid timestamp, missing target label, inconsistent schema, unsupported AI security claim, sensitive data exposure, or missing evidence | `validation.md`; `logs/ml-metric-dataset-collection-validation.log`; `screenshots/ml-metric-query-result.png`; `screenshots/ml-dataset-schema-validation.png` | failure criteria, validation log, screenshot reference | yes |

No real Prometheus output or dataset records have been collected. Use TODO placeholders until execution is approved and outputs are sanitized.
