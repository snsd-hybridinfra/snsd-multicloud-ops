# Evidence Map

| Check ID | Validation Item | Evidence File |
|---|---|---|
| V001 | Required baseline files | `commands.md`; summary |
| V002 | Scrape job definitions | config; summary |
| V003 | Target and Kubernetes discovery model | config; summary |
| V004 | Target discovery rule matrix | matrix; summary |
| V005 | Prometheus API command reference | command reference; summary |
| V006 | Authentication and TLS config safety | config/log; summary |
| V007 | Endpoint address and domain safety | generated log; summary |
| V008 | Required sample evidence | three samples; summary |
| V009 | Targets JSON syntax | targets sample; summary |
| V010 | Target discovery and health evidence | targets sample; summary |
| V011 | UP query JSON syntax | up sample; summary |
| V012 | UP query required job values | up sample; summary |
| V013 | Job label evidence | labels sample; summary |
| V014 | Credential token and account safety | generated log; summary |
| V015 | Execution safety boundary | validator; summary |
| V016 | Validation mode and live API result | generated log; summary |

The generated `.log` is ignored. The committed summary and sanitized samples provide durable evidence without live endpoint or raw API content.
