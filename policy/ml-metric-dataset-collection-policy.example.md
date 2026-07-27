# ML Metric Dataset Collection Policy — Non-Production Example

- ML dataset collection must use metric-only data.
- Dataset evidence must be synthetic or sanitized.
- Raw logs and packet payloads must not be included.
- SIEM, Wazuh, and EDR telemetry are out of scope.
- Production identifiers, credentials, and secrets must not be included.
- The dataset schema must be validated before anomaly detection.
- Feature catalog mapping is required.
- retired-numbered-case owns ML anomaly detection, retired-numbered-case owns ML anomaly report generation, and retired-numbered-case owns final evidence reporting.

This example contains placeholders only and no real monitoring or security telemetry.
