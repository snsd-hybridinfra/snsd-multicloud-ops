# Evidence Map

| Validation Check | Evidence |
|---|---|
| V001 Required artifacts | Runbooks, schema, catalog, policy, datasets, samples, manifest, and generated validator log |
| V002 Command boundary | `runbooks/ml-metric-dataset-collection-commands.example.md` |
| V003 Policy | `policy/ml-metric-dataset-collection-policy.example.md` |
| V004 Schema | `ml-security/datasets/ml-metric-dataset-schema.example.yml` |
| V005 Synthetic dataset | `ml-security/datasets/ml-metric-dataset-synthetic.sample.csv` |
| V006 Invalid dataset | `ml-security/datasets/ml-metric-dataset-invalid.sample.csv` |
| V007 Metadata | `ml-security/datasets/ml-metric-dataset-collection-metadata.sample.yml` |
| V008 Feature catalog | `ml-security/datasets/ml-metric-feature-catalog.example.md` |
| V009 Schema evidence | `logs/ml-dataset-schema-load.sample.txt`, `logs/ml-dataset-collection-metadata.sample.txt` |
| V010 Quality evidence | `logs/ml-dataset-quality-pass.sample.txt`, `logs/ml-dataset-quality-fail.sample.txt` |
| V011 Feature/privacy evidence | `logs/ml-dataset-feature-mapping.sample.txt`, `logs/ml-dataset-privacy-safety.sample.txt` |
| V012 Final summary | `logs/ml-dataset-collection-final-summary.sample.txt` |
| V013 Manifest | `configs/ml-metric-dataset-collection-manifest.sample.yml` |
| V014 Optional normalizer | `ml-security/scripts/metric-dataset-normalization.example.py` |
| V015 Safety | `logs/ml-metric-dataset-collection-validation.log` |
| V016 Maturity | `configs/ml-metric-dataset-collection-validation-summary.md` |

No live metric export, raw log, packet data, or trained model is evidence for S047.
