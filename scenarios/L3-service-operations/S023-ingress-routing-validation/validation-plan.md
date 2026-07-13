# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Ingress documentation | Baseline and commands exist. | generated evidence |
| V002 | Ingress example files | Manifest and README exist. | files, generated evidence |
| V003 | Ingress sample evidence | Three samples exist. | samples, generated evidence |
| V004 | Required command examples | kubectl and manual curl examples exist. | generated evidence |
| V005 | Routing model and placeholders | Required path, objects, and modes exist. | generated evidence |
| V006 | Ingress object and scope | Correct kind/name/namespace/class/marker. | manifest, generated evidence |
| V007 | Host and path routing | Approved host, `/`, Prefix. | manifest, generated evidence |
| V008 | Backend Service reference | Name, port 80, namespace align. | manifests, generated evidence |
| V009 | Ingress and TLS safety | No wildcard, Secret, certificate, key, TLS data. | generated evidence |
| V010 | Ingress list evidence | Approved host and port 80. | sample or live judgment |
| V011 | Ingress backend evidence | Describe and Service contain backend. | sample or live judgment |
| V012 | Endpoint evidence | At least one port-80 target. | sample or live judgment |
| V013 | Ingress address awareness | Static placeholder WARN; live observation PASS. | generated evidence |
| V014 | Kubernetes/TLS credential files | No forbidden file. | generated evidence |
| V015 | Routing content safety | No real endpoint/domain/IP/secret. | generated evidence |
| V016 | Execution safety boundary | Four read-only queries; no curl. | generated evidence |
| V017 | Validation mode | Static no execution or successful explicit live read. | generated evidence |

Every validation item maps to stable evidence by check ID.
