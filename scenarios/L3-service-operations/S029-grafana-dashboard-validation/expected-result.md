# Expected Result

S029 passes when all artifacts parse, datasource fields are correct, the dashboard has exactly the ten required panel titles with placeholder datasource/query coverage, samples contain the dashboard/datasource, and safety checks find no real or sensitive values.

Static mode performs no Grafana query. LiveGrafana passes if dashboard/datasource are anonymously discoverable, warns for S020 authentication or missing lab artifacts, and fails only for invalid/unreachable URLs, exceptions, or server errors.

Only aggregate match judgments and timestamps are retained.
