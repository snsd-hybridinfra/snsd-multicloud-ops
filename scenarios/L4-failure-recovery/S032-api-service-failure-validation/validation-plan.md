# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | All exist | samples; summary |
| V002 | Workflow and placeholders | Complete | runbook; summary |
| V003 | Manual fault boundary | Manual only | command reference; summary |
| V004 | Failure criteria matrix | Complete | criteria; summary |
| V005 | Pre-failure Pod evidence | Running/Ready | pre Pod sample; summary |
| V006 | Pre-failure endpoint evidence | Non-empty | pre endpoint sample; summary |
| V007 | Pre-failure HTTP evidence | Healthy | pre HTTP sample; summary |
| V008 | Manual injection evidence | Explicit/manual | injection sample; summary |
| V009 | Failure detection evidence | Expected failure | detection sample; summary |
| V010 | Post-recovery Pod evidence | Replacement Ready | post Pod sample; summary |
| V011 | Post-recovery endpoint evidence | Non-empty | post endpoint sample; summary |
| V012 | Post-recovery HTTP evidence | Healthy | post HTTP sample; summary |
| V013 | Rollout evidence | Successful | rollout sample; summary |
| V014 | Recovered-state health | No bad indicator | post samples; summary |
| V015 | Recovery timing | Value or WARN | injection sample; summary |
| V016 | Endpoint and secret safety | Safe | log; summary |
| V017 | Execution safety boundary | Read-only | validator; summary |
| V018 | LiveKubectl read-only state | Healthy or NOT_RUN | log; summary |
| V019 | LiveHttp read-only health | Healthy or NOT_RUN | log; summary |
