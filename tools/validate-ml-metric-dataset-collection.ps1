$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$root = Split-Path -Parent $PSScriptRoot
$evidenceRoot = Join-Path $root 'evidence/L5-governance-intelligent-ops/S047-ml-metric-dataset-collection-validation'
$paths = @{
    Runbook = Join-Path $root 'runbooks/ml-metric-dataset-collection-validation.md'
    Commands = Join-Path $root 'runbooks/ml-metric-dataset-collection-commands.example.md'
    Schema = Join-Path $root 'ml-security/datasets/ml-metric-dataset-schema.example.yml'
    Catalog = Join-Path $root 'ml-security/datasets/ml-metric-feature-catalog.example.md'
    Criteria = Join-Path $root 'ml-security/datasets/ml-metric-dataset-quality-criteria.example.md'
    Decision = Join-Path $root 'ml-security/datasets/ml-metric-dataset-decision-matrix.example.md'
    Policy = Join-Path $root 'policy/ml-metric-dataset-collection-policy.example.md'
    Synthetic = Join-Path $root 'ml-security/datasets/ml-metric-dataset-synthetic.sample.csv'
    Invalid = Join-Path $root 'ml-security/datasets/ml-metric-dataset-invalid.sample.csv'
    Metadata = Join-Path $root 'ml-security/datasets/ml-metric-dataset-collection-metadata.sample.yml'
    Normalizer = Join-Path $root 'ml-security/scripts/metric-dataset-normalization.example.py'
    SchemaLoad = Join-Path $evidenceRoot 'logs/ml-dataset-schema-load.sample.txt'
    MetadataLog = Join-Path $evidenceRoot 'logs/ml-dataset-collection-metadata.sample.txt'
    QualityPass = Join-Path $evidenceRoot 'logs/ml-dataset-quality-pass.sample.txt'
    QualityFail = Join-Path $evidenceRoot 'logs/ml-dataset-quality-fail.sample.txt'
    FeatureMap = Join-Path $evidenceRoot 'logs/ml-dataset-feature-mapping.sample.txt'
    Privacy = Join-Path $evidenceRoot 'logs/ml-dataset-privacy-safety.sample.txt'
    Final = Join-Path $evidenceRoot 'logs/ml-dataset-collection-final-summary.sample.txt'
    Manifest = Join-Path $evidenceRoot 'configs/ml-metric-dataset-collection-manifest.sample.yml'
}
$logPath = Join-Path $evidenceRoot 'logs/ml-metric-dataset-collection-validation.log'
$summaryPath = Join-Path $evidenceRoot 'configs/ml-metric-dataset-collection-validation-summary.md'
$results = @()
$failures = 0
$warnings = 0

function Add-Result($id, $name, $ok, $detail, $warning = $false) {
    $status = if ($ok) { 'PASS' } elseif ($warning) { 'WARN' } else { 'FAIL' }
    if ($status -eq 'FAIL') { $script:failures++ }
    if ($status -eq 'WARN') { $script:warnings++ }
    Write-Host "[$status] $id ${name}: $detail"
    $script:results += [pscustomobject]@{ Id = $id; Name = $name; Status = $status }
}
function Read-Text($path) { if (Test-Path $path -PathType Leaf) { Get-Content $path -Raw } else { '' } }

$missing = @($paths.Values | Where-Object { -not (Test-Path $_ -PathType Leaf) })
Add-Result V001 Artifacts ($missing.Count -eq 0) 'All required S047 artifacts and samples exist.'
$content = @{}; foreach ($key in $paths.Keys) { $content[$key] = Read-Text $paths[$key] }
$all = ($content.Values -join "`n")

$commandOk = $content.Commands -match 'MANUAL DISPOSABLE LAB EXAMPLE ONLY' -and $content.Commands -match 'OPTIONAL MANUAL LAB EXAMPLE ONLY' -and $content.Commands -match 'does not query Prometheus' -and $content.Commands -match 'does not query.*Grafana' -and $content.Commands -match 'does not train a model'
Add-Result V002 Commands $commandOk 'Manual lab examples and no-query/no-training boundaries are explicit.'

$excluded = @('SIEM', 'Wazuh', 'EDR', 'packet payload', 'malware detection', 'threat hunting', 'deep-learning intrusion detection', 'LLM-based security analysis')
$policyOk = @($excluded | Where-Object { $content.Runbook -notmatch [regex]::Escape($_) }).Count -eq 0 -and $content.Policy -match 'metric-only' -and $content.Policy -match 'S048' -and $content.Policy -match 'S049' -and $content.Policy -match 'S050'
Add-Result V003 Policy $policyOk 'Metric-only policy and excluded security capabilities are documented.'

$requiredColumns = @('dataset_id','collected_at','collection_window_start','collection_window_end','metric_timestamp','metric_source','metric_name','metric_value','metric_unit','scrape_job','instance_placeholder','service_placeholder','environment_placeholder','feature_group','feature_name','normalized_value','anomaly_label_placeholder','collection_method','evidence_reference')
$schemaOk = @($requiredColumns | Where-Object { $content.Schema -notmatch [regex]::Escape($_) }).Count -eq 0 -and $content.Schema -match 'normal' -and $content.Schema -match 'suspected_anomaly' -and $content.Schema -match 'unknown'
Add-Result V004 Schema $schemaOk 'Required fields, numeric constraints, labels, and collection methods are defined.'

$rows = @(); $syntheticOk = $false
try {
    $rows = @(Import-Csv $paths.Synthetic)
    $headers = @($rows[0].PSObject.Properties.Name)
    $columnsOk = @($requiredColumns | Where-Object { $_ -notin $headers }).Count -eq 0
    $numericOk = @($rows | Where-Object { -not ([double]::TryParse([string]$_.metric_value, [ref]([double]$null))) -or -not ([double]::TryParse([string]$_.normalized_value, [ref]([double]$null))) }).Count -eq 0
    $labelsOk = @($rows | Where-Object { $_.anomaly_label_placeholder -notin @('normal','suspected_anomaly','unknown') }).Count -eq 0
    $featureCount = @($rows.feature_group | Sort-Object -Unique).Count
    $syntheticOk = $columnsOk -and $rows.Count -ge 20 -and $numericOk -and $labelsOk -and $featureCount -gt 1
} catch { $syntheticOk = $false }
Add-Result V005 SyntheticDataset $syntheticOk 'Synthetic CSV has required columns, at least 20 numeric rows, valid labels, and multiple feature groups.'

$invalidOk = $content.Invalid -match 'INTENTIONALLY INVALID' -and $content.Invalid -match 'not_numeric' -and $content.Invalid -match 'invalid_label'
Add-Result V006 InvalidDataset $invalidOk 'Invalid sample is clearly labeled and contains deliberate value and label failures.'

$mapping050 = @('anomaly_detection_scenario: S048','anomaly_report_scenario: S049','final_evidence_report_scenario: S050')
$metadataOk = @($mapping050 | Where-Object { $content.Metadata -notmatch [regex]::Escape($_) }).Count -eq 0 -and $content.Metadata -match 'row_count: 20'
Add-Result V007 Metadata $metadataOk 'Collection metadata maps S048, S049, and S050 and records sample counts.'

$catalogScenarios = @('S028','S029','S030','S036','S040','S048','S049')
$catalogOk = @($catalogScenarios | Where-Object { $content.Catalog -notmatch [regex]::Escape($_) }).Count -eq 0
Add-Result V008 FeatureCatalog $catalogOk 'Required observability, recovery, anomaly, and report scenarios are mapped.'

$schemaEvidenceOk = $content.SchemaLoad -match 'Schema_Loaded:\s*true' -and $content.SchemaLoad -match 'Required_Fields_Validated:\s*true' -and $content.MetadataLog -match 'S048' -and $content.MetadataLog -match 'S049'
Add-Result V009 SchemaEvidence $schemaEvidenceOk 'Schema load and collection metadata evidence are complete.'

$qualityOk = $content.QualityPass -match 'DATASET_READY' -and $content.QualityPass -match 'Metric_Values_Numeric:\s*true' -and $content.QualityFail -match 'DATASET_INVALID' -and $content.QualityFail -match 'Invalid_Dataset_Evaluated:\s*true'
Add-Result V010 QualityEvidence $qualityOk 'Valid data passes and the intentionally invalid sample is rejected.'

$privacyTerms = @('No_Raw_Logs: true','No_Packet_Payload: true','No_Credentials: true','No_Real_IPs: true','No_Real_Hostnames: true','No_Production_Identifiers: true')
$featurePrivacyOk = $content.FeatureMap -match 'Feature_Catalog_Mapped:\s*true' -and @($privacyTerms | Where-Object { $content.Privacy -notmatch [regex]::Escape($_) }).Count -eq 0
Add-Result V011 FeaturePrivacy $featurePrivacyOk 'Feature mapping and privacy-safety assertions are present.'

$finalOk = $content.Final -match 'final_judgment:\s*DATASET_READY' -and $content.Final -match 'Live_Prometheus_Query_Performed:\s*false' -and $content.Final -match 'Live_Grafana_Query_Performed:\s*false' -and $content.Final -match 'ML_Model_Trained:\s*false'
Add-Result V012 FinalSummary $finalOk 'Final sample confirms ready status with no live query or training.'

$manifestFields = @('ml_dataset_collection_validation_id','dataset_id','dataset_type','collection_method','schema_reference','feature_catalog_reference','synthetic_dataset_reference','invalid_dataset_reference','collection_metadata_reference','row_count','feature_group_count','privacy_safety_result','prometheus_target_discovery_scenario: S028','grafana_dashboard_scenario: S029','blackbox_probe_scenario: S030','prometheus_target_down_scenario: S036','service_health_after_recovery_scenario: S040','anomaly_detection_scenario: S048','anomaly_report_scenario: S049','final_evidence_report_scenario: S050','evidence_reference','final_judgment')
$manifestOk = @($manifestFields | Where-Object { $content.Manifest -notmatch [regex]::Escape($_) }).Count -eq 0
Add-Result V013 Manifest $manifestOk 'Manifest contains required fields and S028/S029/S030/S036/S040/S048/S049/S050 mappings.'

$normalizerOk = $content.Normalizer -match 'SAMPLE / NON-PRODUCTION' -and $content.Normalizer -match 'argparse' -and $content.Normalizer -match 'csv' -and $content.Normalizer -notmatch '(?i)sklearn|tensorflow|torch|requests|urllib|socket|prometheus|grafana'
Add-Result V014 Normalizer $normalizerOk 'Optional helper uses standard-library CSV validation only.'

$prohibitedFiles = @(Get-ChildItem $root -Recurse -File -Force -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notlike "$root\.git*" -and ($_.Extension -match '(?i)^\.(pcap|pcapng|cap|pkl|pickle|joblib|onnx|pt|pth|h5)$' -or $_.Name -match '(?i)(production.*export|siem.*log|wazuh.*log|edr.*telemetry|packet.*payload|malware|exploit.*payload)') })
$realIp = $all -match '(?<![\w<])(?:\d{1,3}\.){3}\d{1,3}(?![\w>])'
$realUrl = $all -match '(?i)https?://(?!<)[a-z0-9]'
$secret = $all -match '(?im)^\s*(?:password|token|secret|access_key|api_key|authorization)\s*[:=]\s*(?!["'']?<)\S+' -or $all -match '-----BEGIN .*PRIVATE KEY-----'
$scriptText = Get-Content $PSCommandPath -Raw
$liveExec = $scriptText -match '(?im)^\s*(?:curl|Invoke-WebRequest|Invoke-RestMethod|promtool|python)\s+'
$safetyOk = $prohibitedFiles.Count -eq 0 -and -not $realIp -and -not $realUrl -and -not $secret -and -not $liveExec
Add-Result V015 Safety $safetyOk 'No prohibited telemetry/model files, real endpoints, secrets, or live collection execution were detected.'

Add-Result V016 Maturity $false 'Dataset values, labels, and collection metadata are synthetic or placeholder-only.' $true

$timestamp = (Get-Date).ToString('s')
$overall = if ($failures) { 'FAIL' } else { 'PASS' }
$end = "[$overall] ML metric dataset collection (StaticEvidence): $failures critical failure(s), $warnings warning(s)."
Write-Host $end
@('S047 ML Metric Dataset Collection Validation', "Generated: $timestamp", 'Validation mode: StaticEvidence', '') + ($results | ForEach-Object { "[$($_.Status)] $($_.Id) $($_.Name)" }) + @('', $end, 'No Prometheus, Grafana, cloud, SIEM, Wazuh, EDR, packet, or ML runtime was accessed.') | Set-Content $logPath -Encoding UTF8
@('# ML Metric Dataset Collection Validation Summary', '', "- Generated: $timestamp", '- Validation mode: **StaticEvidence**', "- Required files: **$(if ($missing.Count -eq 0) { 'PASS' } else { 'FAIL' })**", "- Command safety: **$(if ($commandOk) { 'PASS' } else { 'FAIL' })**", "- Schema: **$(if ($schemaOk) { 'PASS' } else { 'FAIL' })**", "- Synthetic dataset: **$(if ($syntheticOk) { 'PASS' } else { 'FAIL' })**", "- Invalid dataset rejection: **$(if ($invalidOk) { 'PASS' } else { 'FAIL' })**", "- Collection metadata: **$(if ($metadataOk) { 'PASS' } else { 'FAIL' })**", "- Feature catalog: **$(if ($catalogOk) { 'PASS' } else { 'FAIL' })**", "- Privacy safety: **$(if ($featurePrivacyOk) { 'PASS' } else { 'FAIL' })**", "- S028/S029/S030/S036/S040 mappings: **$(if ($catalogOk -and $manifestOk) { 'PASS' } else { 'FAIL' })**", "- S048/S049/S050 mappings: **$(if ($metadataOk -and $manifestOk) { 'PASS' } else { 'FAIL' })**", "- Secret safety: **$(if ($safetyOk) { 'PASS' } else { 'FAIL' })**", "- Final judgment: **$overall**") | Set-Content $summaryPath -Encoding UTF8
if ($failures) { exit 1 }
