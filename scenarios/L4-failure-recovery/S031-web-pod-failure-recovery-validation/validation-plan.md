# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Required recovery baseline files | Test three paths. | All exist. | commands; summary |
| V002 | Required recovery samples | Test five paths. | All exist. | samples; summary |
| V003 | Recovery workflow documentation | Match phases/placeholders/modes. | Complete. | runbook; summary |
| V004 | Recovery criteria matrix | Match ten phases. | Complete. | criteria; summary |
| V005 | Command and manual fault boundary | Match commands/manual warning. | Safe. | command reference; summary |
| V006 | Pre-failure Pod evidence | Parse Running Ready. | Healthy. | pre sample; summary |
| V007 | Manual fault injection evidence | Parse explicit sample marker/event. | Controlled. | fault sample; summary |
| V008 | Replacement Pod recovery evidence | Parse original inactive/replacement Ready. | Recovered. | post sample; summary |
| V009 | Rollout status evidence | Match successful rollout. | Successful. | rollout sample; summary |
| V010 | Service endpoint continuity evidence | Require placeholder endpoint. | Non-empty. | endpoint sample; summary |
| V011 | Recovery time evidence | Parse numeric time or warn. | Expected WARN if unmeasured. | fault sample; summary |
| V012 | Post-recovery failure indicators | Reject bad status/0-Ready/none. | None. | post/endpoint; summary |
| V013 | Kubernetes credential file safety | Scan kube/TLS filenames. | None. | log; summary |
| V014 | Cluster endpoint and secret safety | Scan content. | None. | log; summary |
| V015 | Execution safety boundary | Require four read-only args/no mutation. | Safe. | script; summary |
| V016 | Validation mode and live recovery state | Evaluate Static/live. | Safe/healthy. | log; summary |
