# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | Runbooks, schema, catalog, policy, datasets, evidence, and manifest exist. | `logs/ml-metric-dataset-collection-validation.log` |
| V002 | Command boundary | Lab commands are manual-only; validator queries no live source and trains no model. | `runbooks/ml-metric-dataset-collection-commands.example.md` |
| V003 | Policy | Metric-only scope and excluded security capabilities are explicit. | `policy/ml-metric-dataset-collection-policy.example.md` |
| V004 | Schema | Required fields, numeric constraints, labels, and methods exist. | `ml-security/datasets/ml-metric-dataset-schema.example.yml` |
| V005 | Synthetic dataset | At least 20 rows, numeric values, valid labels, and multiple feature groups exist. | `ml-security/datasets/ml-metric-dataset-synthetic.sample.csv` |
| V006 | Invalid dataset | Deliberate numeric and label failures are clearly marked. | `ml-security/datasets/ml-metric-dataset-invalid.sample.csv` |
| V007 | Metadata | S048/S049/S050 mappings and sample counts exist. | `ml-security/datasets/ml-metric-dataset-collection-metadata.sample.yml` |
| V008 | Feature catalog | S028/S029/S030/S036/S040/S048/S049 mappings exist. | `ml-security/datasets/ml-metric-feature-catalog.example.md` |
| V009 | Schema evidence | Schema-load and collection-metadata evidence are complete. | `logs/ml-dataset-schema-load.sample.txt`, `logs/ml-dataset-collection-metadata.sample.txt` |
| V010 | Quality evidence | Valid sample passes and invalid sample is rejected. | `logs/ml-dataset-quality-*.sample.txt` |
| V011 | Feature/privacy evidence | Catalog mapping and six privacy assertions pass. | `logs/ml-dataset-feature-mapping.sample.txt`, `logs/ml-dataset-privacy-safety.sample.txt` |
| V012 | Final summary | Dataset is ready; no live query or model training occurred. | `logs/ml-dataset-collection-final-summary.sample.txt` |
| V013 | Manifest | Required references and S028/S029/S030/S036/S040/S048/S049/S050 mappings exist. | `configs/ml-metric-dataset-collection-manifest.sample.yml` |
| V014 | Optional normalizer | Standard-library CSV validation only; no network or ML dependency. | `ml-security/scripts/metric-dataset-normalization.example.py` |
| V015 | Safety | No prohibited telemetry/model files, real endpoints, credentials, keys, or execution. | `logs/ml-metric-dataset-collection-validation.log` |
| V016 | Maturity | Synthetic/placeholder limitation is explicitly warned. | `configs/ml-metric-dataset-collection-validation-summary.md` |

All checks are implemented in `StaticEvidence` mode.
