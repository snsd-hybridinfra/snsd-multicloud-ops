#!/usr/bin/env python3
"""Read-only validation for the Project Mini-Ona sandbox contract."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = Path("docs/platform/ai-agent-sandbox.yaml")
CATALOG = Path("docs/platform/composite-service-catalog.yaml")
ADR = Path("docs/adr/0020-persistent-ai-agent-sandbox.md")
AGENT_MODULE = Path("applications/internal-iaas-portal/services/request-api/request_api/agent_jobs.py")
INTEGRATION_MODULE = Path("applications/internal-iaas-portal/services/request-api/request_api/agent_integrations.py")
RUNTIME_MODULE = Path("applications/internal-iaas-portal/services/request-api/request_api/agent_runtime.py")
RUNTIME_READINESS = Path("docs/platform/ai-agent-runtime-readiness.yaml")
RUNTIME_REQUIREMENTS = Path("applications/internal-iaas-portal/requirements-runtime.txt")
REQUEST_MAIN = Path("applications/internal-iaas-portal/services/request-api/request_api/main.py")
REQUEST_MODELS = Path("applications/internal-iaas-portal/services/request-api/request_api/models.py")
REQUEST_SCHEMAS = Path("applications/internal-iaas-portal/services/request-api/request_api/schemas.py")
MIGRATION = Path("applications/internal-iaas-portal/database/migrations/request-db/versions/0003_agent_job_simulation.py")
INTEGRATION_MIGRATION = Path("applications/internal-iaas-portal/database/migrations/request-db/versions/0004_agent_integration_outbox.py")
BUDGET_MIGRATION = Path("applications/internal-iaas-portal/database/migrations/request-db/versions/0005_agent_budget_telemetry.py")
ORCHESTRATOR_TEST = Path("applications/internal-iaas-portal/tests/api/test_agent_job_orchestrator.py")
RUNTIME_TEST = Path("applications/internal-iaas-portal/tests/api/test_agent_runtime_adapters.py")
KATA_VALUES = Path("platform/kubernetes/mini-ona/kata-deploy-values.yaml")
VM_BOOTSTRAP = Path("tools/local-vm/New-MiniOnaK3sVm.ps1")
REQUIRED_FILES = (
    CONTRACT,
    CATALOG,
    ADR,
    AGENT_MODULE,
    INTEGRATION_MODULE,
    RUNTIME_MODULE,
    RUNTIME_READINESS,
    RUNTIME_REQUIREMENTS,
    REQUEST_MAIN,
    REQUEST_MODELS,
    REQUEST_SCHEMAS,
    MIGRATION,
    INTEGRATION_MIGRATION,
    BUDGET_MIGRATION,
    ORCHESTRATOR_TEST,
    RUNTIME_TEST,
    KATA_VALUES,
    VM_BOOTSTRAP,
)


@dataclass
class Result:
    passes: list[str] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)

    def require(self, condition: bool, message: str) -> None:
        (self.passes if condition else self.failures).append(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(root: Path) -> Result:
    result = Result()
    for relative in REQUIRED_FILES:
        result.require((root / relative).is_file(), f"required sandbox authority exists: {relative.as_posix()}")
    if result.failures:
        return result
    try:
        contract = load(root / CONTRACT)
        catalog = load(root / CATALOG)
    except (OSError, json.JSONDecodeError) as exc:
        result.failures.append(f"sandbox authority cannot be loaded: {exc}")
        return result

    result.require(contract.get("schema_version") == "1.0.0", "sandbox schema version is pinned")
    result.require(contract.get("blueprint_id") == "AI_AGENT_SANDBOX", "sandbox blueprint identity is fixed")
    result.require(contract.get("project_alias") == "PROJECT_MINI_ONA", "project alias is fixed")
    status = contract.get("status", {})
    result.require(status == {"design": "LOCAL_VALIDATED", "implementation": "PARTIALLY_IMPLEMENTED_LOCAL", "control_plane_slice": "LOCAL_SIMULATION_VALIDATED", "runtime": "NOT_VALIDATED"}, "status truth remains bounded local implementation")

    local = contract.get("local_implementation", {})
    result.require(local.get("service") == AGENT_MODULE.as_posix(), "local orchestrator implementation path is pinned")
    result.require(local.get("api_mode") == "SERVICE_ONLY_LOCAL_SIMULATION", "local API is explicitly service-only simulation")
    result.require(local.get("database_migration") == MIGRATION.as_posix(), "agent job migration is pinned")
    result.require(set(local.get("additional_migrations", [])) == {INTEGRATION_MIGRATION.as_posix(), BUDGET_MIGRATION.as_posix()}, "integration and budget migrations are pinned")
    result.require(set(local.get("sandbox_bundle", [])) == {"KUBERNETES_JOB", "NETWORK_POLICY", "RESOURCE_QUOTA"}, "inert sandbox bundle is complete")
    result.require(local.get("bundle_deployable") is False and local.get("external_side_effects") is False, "local implementation remains inert")
    result.require(local.get("queue_transport_contract") == "REDIS_STREAMS_XADD_XREADGROUP", "Redis Streams transport contract is pinned")
    result.require(local.get("local_queue_adapter") == "DATABASE_OUTBOX", "local queue uses the database outbox")
    result.require(local.get("credential_lease_mode") == "NON_SECRET_LOCAL_INVALID_REFERENCE", "local credential lease contains no usable token")
    result.require(local.get("credential_lease_ttl_seconds") == 900, "credential lease TTL is bounded to 15 minutes")
    result.require(local.get("egress_decision_mode") == "EXACT_CLASS_PROTOCOL_PORT_VIA_AUTHENTICATED_BROKER", "egress decision is exact and brokered")
    result.require(local.get("runtime_adapter") == RUNTIME_MODULE.as_posix(), "Redis/Kubernetes runtime adapter path is pinned")
    result.require(local.get("runtime_readiness") == RUNTIME_READINESS.as_posix(), "runtime readiness authority is pinned")

    queue = contract.get("queue", {})
    result.require(queue.get("target_transport") == "REDIS_STREAMS", "target queue transport is Redis Streams")
    result.require(set(queue.get("delivery_contract", [])) == {"XADD", "XREADGROUP", "ACK_AFTER_ACCEPTED_TRANSITION", "IDEMPOTENT_JOB_ID"}, "queue delivery contract is complete")
    result.require(queue.get("local_adapter") == "DATABASE_OUTBOX" and queue.get("live_redis_connection") is False, "queue remains local and disconnected")
    result.require(queue.get("raw_task_text_allowed") is False and queue.get("credential_material_allowed") is False, "queue excludes raw task and credential material")

    blueprints = {item.get("blueprint_id"): item for item in catalog.get("blueprints", []) if isinstance(item, dict)}
    sandbox_blueprint = blueprints.get("AI_AGENT_SANDBOX", {})
    result.require(len(blueprints) == 8 and "CI_CD_RUNNER" not in blueprints, "sandbox replaces the runner without creating a ninth product")
    result.require(sandbox_blueprint.get("network_profile") == "AI_AGENT_EGRESS_BROKERED", "catalog pins brokered agent egress")
    result.require(sandbox_blueprint.get("components") == ["K3S_RUNTIME", "OBJECT_STORAGE", "NETWORK_POLICY", "OPERATIONS_PROFILE"], "catalog pins the sandbox composition")

    model = contract.get("execution_model", {})
    result.require(model.get("durable_authority") == "CONTROL_PLANE_JOB_STATE", "control-plane job state is durable authority")
    result.require(model.get("compute_unit") == "DISPOSABLE_SANDBOX_POD", "sandbox pod is disposable")
    result.require(model.get("pod_is_durable_authority") is False, "pod is not durable job authority")
    result.require(model.get("live_runtime_authorized") is False, "live sandbox runtime remains unauthorized")
    result.require(model.get("approval_wait_behavior") == "CHECKPOINT_DELETE_POD_RESUME_NEW_POD", "approval waiting checkpoints and releases compute")
    required_states = {"RECEIVED", "QUEUED", "STARTING", "RUNNING", "AWAITING_APPROVAL", "CHECKPOINTED", "RESUMING", "COMPLETED", "FAILED", "CANCELLED", "TIMED_OUT", "BUDGET_EXHAUSTED"}
    result.require(set(model.get("lifecycle", [])) == required_states, "job lifecycle is complete and bounded")

    sandbox = contract.get("sandbox", {})
    result.require(sandbox.get("runtime_class_requirement") == "KATA_OR_GVISOR_REQUIRED", "strong sandbox RuntimeClass is mandatory")
    for key in ("plain_runc_accepted", "privileged", "host_path", "host_network", "host_pid", "host_ipc", "automount_service_account_token"):
        result.require(sandbox.get(key) is False, f"sandbox escape surface remains denied: {key}")
    for key in ("run_as_non_root", "read_only_root_filesystem", "drop_all_capabilities", "task_namespace_isolation", "resource_quota_required"):
        result.require(sandbox.get(key) is True, f"sandbox hardening remains required: {key}")
    result.require(set(sandbox.get("limits_required", [])) == {"CPU", "MEMORY", "PID", "EPHEMERAL_STORAGE"}, "pod resource limits are complete")

    credentials = contract.get("credentials", {})
    result.require(credentials.get("task_scoped") is True, "credentials are task scoped")
    result.require(credentials.get("expiration_behavior") == "FAIL_CLOSED_AND_REQUIRE_NEW_LEASE", "expired credential leases fail closed")
    for key in ("developer_ssh_keys_allowed", "browser_sessions_allowed", "raw_provider_api_keys_allowed"):
        result.require(credentials.get(key) is False, f"personal or raw credential is denied: {key}")

    egress = contract.get("egress", {})
    result.require(egress.get("default_deny") is True, "egress is default deny")
    result.require("AUTHENTICATED_FQDN_AWARE_EGRESS_BROKER" in egress.get("enforcement", []), "FQDN-aware broker is required")
    for key in ("direct_ip_allowed", "alternate_dns_allowed", "tunneling_allowed", "network_policy_alone_is_sufficient"):
        result.require(egress.get(key) is False, f"egress bypass or weak claim is denied: {key}")

    budgets = contract.get("budgets", {})
    required_budgets = {"WALL_CLOCK", "ITERATIONS", "MODEL_TOKENS", "MONETARY_COST", "EXTERNAL_CALLS", "CONCURRENCY", "EGRESS_BYTES"}
    result.require(set(budgets.get("hard_limits_required", [])) == required_budgets, "agent hard-budget dimensions are complete")
    result.require(budgets.get("limit_action") == "CHECKPOINT_CANCEL_AND_DELETE_POD", "budget breach has a hard-stop action")
    result.require(budgets.get("request_rate_only_is_sufficient") is False, "request count alone cannot represent cost control")
    local_budget = contract.get("local_budget_enforcement", {})
    result.require(local_budget.get("mode") == "PRE_EXECUTION_ATOMIC_RESERVATION", "budget enforcement reserves before execution")
    result.require(local_budget.get("ledger") == "PERSISTENT_OPTIMISTIC_VERSIONED" and local_budget.get("idempotent") is True, "budget ledger is persistent, versioned and idempotent")
    result.require(local_budget.get("overrun_outcome") == "BUDGET_EXHAUSTED", "budget overrun has an explicit terminal state")
    result.require(set(local_budget.get("overrun_actions", [])) == {"DENY_RESERVATION", "CANCEL_QUEUE_ITEM", "REVOKE_ACTIVE_LEASES", "RELEASE_COMPUTE"}, "budget overrun cleanup is complete")
    result.require(local_budget.get("external_meter_connected") is False, "external cost meter remains disconnected")

    hitl = contract.get("human_in_the_loop", {})
    required_approvals = {"MAIN_BRANCH_MUTATION", "BRANCH_PROTECTION_BYPASS", "PRODUCTION_ACCESS", "DATABASE_SCHEMA_CHANGE", "SECRET_ACCESS", "NEW_EGRESS_DESTINATION", "INFRASTRUCTURE_MUTATION", "DEPENDENCY_SOURCE_CHANGE"}
    result.require(set(hitl.get("approval_required", [])) == required_approvals, "high-risk approval gates are complete")
    result.require(hitl.get("decision_is_recorded") is True and hitl.get("indefinite_pod_suspension") is False, "approval is recorded without indefinite pod suspension")

    delivery = contract.get("git_delivery", {})
    result.require(delivery.get("task_branch_required") is True and delivery.get("atomic_checkpoint_commits") is True and delivery.get("draft_pull_request") is True, "Git checkpoint delivery is fixed")
    result.require(delivery.get("direct_main_push") is False, "direct main push is prohibited")
    result.require(set(delivery.get("pre_push_checks", [])) == {"DIFF_POLICY", "SECRET_SCAN", "TEST_RESULT", "PROVENANCE"}, "pre-push checks are complete")

    telemetry = contract.get("observability", {})
    for key in ("raw_prompts_allowed", "source_code_allowed", "secrets_allowed"):
        result.require(telemetry.get(key) is False, f"sensitive telemetry is denied: {key}")
    result.require("cleanup" in telemetry.get("trace_spans", []) and "COLD_START_P50_P95_P99" in telemetry.get("metrics", []), "end-to-end latency and cleanup telemetry are present")
    result.require(telemetry.get("local_event_store") == "SANITIZED_FIXED_SCHEMA" and telemetry.get("otel_exporter_connected") is False, "trace storage is sanitized and has no live exporter")

    required_acceptance = {"POSITIVE_TASK", "NEGATIVE_EGRESS", "EGRESS_BYPASS", "CHECKPOINT_RESUME", "ROLLBACK_CLEANUP", "RUNAWAY_BUDGET_TERMINATION", "APPROVAL_CHECKPOINT", "TOKEN_EXPIRY", "SANDBOX_ISOLATION"}
    result.require(set(contract.get("acceptance_checks", [])) == required_acceptance, "acceptance checks cover positive, negative, bypass, persistence and rollback")
    prohibited = set(contract.get("prohibited_scope", []))
    result.require({"DIRECT_MAIN_PUSH", "UNBOUNDED_AGENT_LOOP", "PLAIN_CONTAINER_AS_SECURITY_BOUNDARY", "LIVE_DEPLOYMENT_BY_THIS_CONTRACT"} <= prohibited, "critical prohibited scope is explicit")

    module_text = (root / AGENT_MODULE).read_text(encoding="utf-8")
    integration_text = (root / INTEGRATION_MODULE).read_text(encoding="utf-8")
    runtime_text = (root / RUNTIME_MODULE).read_text(encoding="utf-8")
    requirements_text = (root / RUNTIME_REQUIREMENTS).read_text(encoding="utf-8")
    main_text = (root / REQUEST_MAIN).read_text(encoding="utf-8")
    model_text = (root / REQUEST_MODELS).read_text(encoding="utf-8")
    schema_text = (root / REQUEST_SCHEMAS).read_text(encoding="utf-8")
    migration_text = (root / MIGRATION).read_text(encoding="utf-8")
    integration_migration_text = (root / INTEGRATION_MIGRATION).read_text(encoding="utf-8")
    budget_migration_text = (root / BUDGET_MIGRATION).read_text(encoding="utf-8")
    test_text = (root / ORCHESTRATOR_TEST).read_text(encoding="utf-8")
    runtime_test_text = (root / RUNTIME_TEST).read_text(encoding="utf-8")
    kata_values_text = (root / KATA_VALUES).read_text(encoding="utf-8")
    vm_bootstrap_text = (root / VM_BOOTSTRAP).read_text(encoding="utf-8")
    for token in (
        'RUNTIME_CLASS = "kata-qemu-runtime-rs"',
        '"runtime_authorized": False',
        '"deployable": False',
        '"automountServiceAccountToken": False',
        '"hostNetwork": False',
        '"readOnlyRootFilesystem": True',
        '"capabilities": {"drop": ["ALL"]}',
        '"authenticated-egress-broker"',
        '"CHECKPOINT": "CHECKPOINTED"',
        '"WAIT_FOR_APPROVAL": "AWAITING_APPROVAL"',
    ):
        result.require(token in module_text, f"local orchestrator safety contract is present: {token}")
    result.require('/internal/v1/agent-job-simulations"' in main_text, "service-only job simulation create endpoint exists")
    result.require("class AgentJob(Base)" in model_text, "persistent agent job model exists")
    result.require("class AgentJobCreate(BaseModel)" in schema_text and 'extra="forbid"' in schema_text, "agent job input schema fails closed")
    result.require('runtime_authorized = false' in migration_text, "database migration denies runtime authorization")
    for token in (
        'QUEUE_TRANSPORT_CONTRACT = "REDIS_STREAMS_XADD_XREADGROUP"',
        'LOCAL_QUEUE_ADAPTER = "DATABASE_OUTBOX"',
        'LEASE_TTL_SECONDS = 900',
        'CREDENTIAL_CLASSES = ("GITHUB_APP", "MODEL_BROKER")',
        '"runtime_authorized": False',
        '"direct_network_allowed": False',
        '"raw_ip_allowed": False',
        'return "DENY"',
        'local-invalid://credential-lease/',
    ):
        result.require(token in integration_text, f"local integration boundary is present: {token}")
    result.require('down_revision: str | None = "0003_agent_jobs"' in integration_migration_text, "integration migration follows the agent-job migration")
    result.require('down_revision: str | None = "0004_agent_integrations"' in budget_migration_text, "budget migration follows the integration migration")
    result.require("class AgentQueueItem(Base)" in model_text and "class AgentCredentialLease(Base)" in model_text, "queue and credential lease models exist")
    result.require("class AgentBudgetLedger(Base)" in model_text and "class AgentTraceEvent(Base)" in model_text, "budget ledger and sanitized trace models exist")
    result.require('/integrations"' in main_text, "service-only integration projection endpoint exists")
    result.require('lease.status = "EXPIRED"' in main_text, "expired local credential leases fail closed")
    result.require('/usage-reservations"' in main_text and 'status="BUDGET_EXHAUSTED"' in main_text, "budget reservation endpoint enforces the terminal stop")
    result.require('/trace-events"' in main_text and "AgentTraceEventCreate" in schema_text, "fixed-schema trace endpoint exists")
    for token in ("service_only_idempotent_and_inert", "strongly_isolated_and_broker_only", "checkpoint_approval_resume_and_completion_persist", "invalid_transition_replay", "timeout_and_rejection_release_compute", "cannot_supply_url_image_command_or_budget", "egress_decision_allows_only_exact_authenticated_broker_routes", "expired_credential_lease_is_failed_closed", "budget_reservation_is_idempotent_and_hard_stops_before_overrun", "trace_events_accept_only_fixed_sanitized_measurements"):
        result.require(token in test_text, f"local orchestrator regression coverage exists: {token}")
    for token in (
        "class RedisStreamsAdapter",
        "xreadgroup",
        "xack",
        "class KubernetesSandboxController",
        "APPROVED_IMAGE_PATTERN",
        "sandbox activation digest mismatch",
        "create_namespaced_network_policy",
        "create_namespaced_job",
        "delete_namespace",
    ):
        result.require(token in runtime_text, f"runtime adapter gate is implemented: {token}")
    for token in ("redis>=6.4,<7", "kubernetes>=34.1,<35", "opentelemetry-sdk>=1.44,<2", "opentelemetry-exporter-otlp-proto-grpc>=1.44,<2"):
        result.require(token in requirements_text, f"approved runtime dependency is pinned: {token}")
    for token in ("activation_requires_digest_decision_expiry_image_and_runtime_class", "redis_stream_adapter_publishes_claims_and_acknowledges", "kubernetes_controller_applies_in_order_and_rolls_back_namespace_on_failure"):
        result.require(token in runtime_test_text, f"runtime adapter regression coverage exists: {token}")
    for token in (
        "deploymentMode: job",
        "k8sDistribution: k3s",
        "disableAll: true",
        "qemu-runtime-rs:",
        "quay.io/kata-containers/kata-deploy@sha256:460128eea49aee30fd023f1eabd94dc75fd694dff9a09ed82daeba5c126b2b0e",
        "quay.io/kata-containers/kata-deploy-job-dispatcher@sha256:ceee369efe1a4796a93c3d013e513fa61b0904f5cbc4cbdaa69e32396efd7c42",
        "quay.io/kata-containers/kubectl@sha256:7f3b773c4761a1e31d19e11f4af0779e489a0972b0da181506f4da7e7b5c5ab7",
    ):
        result.require(token in kata_values_text, f"Kata deployment is bounded and digest pinned: {token}")
    result.require(kata_values_text.count("kind: RuntimeClass") == 0, "Kata values do not bypass chart-owned RuntimeClass generation")
    for token in (
        'groups: [adm, users]',
        'NOPASSWD: /usr/local/sbin/mini-ona-runtime-status',
        '$helmVersion = "v4.2.3"',
        '$kataVersion = "4.0.0"',
        "helm upgrade --install kata-deploy",
        "get runtimeclass kata-qemu-runtime-rs",
        "NOPASSWD: /usr/local/sbin/mini-ona-kata-live-validator",
        "MINI_ONA_KATA_LIVE_VALIDATION",
        "ValidatingAdmissionPolicy",
        "mini-ona-kata-validation",
        "bypass_default_runtime",
        "negative_privilege",
        "positive_vm_process",
        "persistence_recreate",
        "egress_direct_ip_denied",
        "deadline_enforced",
        "fail_sanitized",
        "wait_for_log_line",
        "rollback_cleanup",
        "docker.io/library/busybox@sha256:b7f3d86d6e84fc17718c48bcde1450807faa2d56704205c697b4bd5df7b9e29f",
    ):
        result.require(token in vm_bootstrap_text, f"VM bootstrap safety contract is present: {token}")
    result.require("groups: [adm, sudo, users]" not in vm_bootstrap_text, "VM operator is not a general sudo-group member")
    result.require("NOPASSWD:/usr/bin" not in vm_bootstrap_text and "NOPASSWD:/usr/sbin" not in vm_bootstrap_text, "VM bootstrap grants no generic package, service or network mutation sudo")
    try:
        readiness = load(root / RUNTIME_READINESS)
    except (OSError, json.JSONDecodeError) as exc:
        result.failures.append(f"runtime readiness authority cannot be loaded: {exc}")
        return result
    result.require(readiness.get("status") == "BLOCKED_EXTERNAL_RUNTIME", "runtime readiness remains blocked on external inputs")
    foundation = readiness.get("runtime_foundation", {})
    result.require(
        foundation.get("state") == "PROVISIONED_BOUNDED_SANDBOX_VALIDATED"
        and foundation.get("scope") == "NON_PRODUCTION_LOCAL_VM"
        and foundation.get("runtime_class") == "kata-qemu-runtime-rs",
        "local VM runtime foundation records only the bounded Kata workload result",
    )
    result.require(
        foundation.get("live_sandbox_workload") == "BOUNDED_VALIDATOR_PASSED"
        and foundation.get("acceptance_evidence") == "SANITIZED_BOUNDED_DECISION_RECORDED"
        and foundation.get("request_api_integration") == "NOT_CONFIGURED",
        "bounded workload result does not promote request API integration",
    )
    blocker_conditions = {item.get("condition") for item in readiness.get("blockers", []) if isinstance(item, dict)}
    result.require({"REDIS_ENDPOINT_NOT_PROVIDED", "REQUEST_API_KUBERNETES_CONTEXT_NOT_CONFIGURED", "APPROVED_AGENT_IMAGE_MISSING", "GITHUB_AUTH_INVALID_AND_APP_NOT_CONFIGURED", "MODEL_BROKER_NOT_CONFIGURED", "EGRESS_BROKER_NOT_DEPLOYED", "CHECKPOINT_OBJECT_STORAGE_NOT_CONFIGURED", "OTLP_COLLECTOR_NOT_CONFIGURED"} <= blocker_conditions, "remaining external runtime blockers are explicit")
    result.require("KATA_SANDBOX_WORKLOAD_NOT_VALIDATED" not in blocker_conditions, "bounded Kata workload blocker is closed")
    bounded = readiness.get("bounded_validation", {})
    result.require(
        bounded.get("decision") == "PASSED"
        and bounded.get("scope") == "MINI_ONA_KATA_LIVE_VALIDATION"
        and set(bounded.get("checks", [])) == {
            "POSITIVE_KATA_POD",
            "NEGATIVE_PRIVILEGE",
            "BYPASS_DEFAULT_RUNTIME",
            "DIRECT_IP_EGRESS_DENIED",
            "CHECKPOINT_RECREATE",
            "ACTIVE_DEADLINE_ENFORCED",
            "SANDBOX_VM_PROCESS",
            "ROLLBACK_CLEANUP",
        }
        and bounded.get("raw_runtime_output_stored") is False,
        "sanitized bounded Kata validation decision is exact",
    )
    result.require(
        set(bounded.get("limitations", [])) == {
            "VALIDATOR_IMAGE_IS_NOT_THE_AGENT_IMAGE",
            "REQUEST_API_NOT_CONNECTED",
            "REDIS_STREAMS_NOT_CONNECTED_TO_REQUEST_API",
            "FQDN_EGRESS_BROKER_NOT_DEPLOYED",
            "NO_END_TO_END_AGENT_TASK",
        },
        "bounded validation limitations prevent an end-to-end runtime claim",
    )
    live = readiness.get("live_execution", {})
    result.require(live == {"authorized": True, "performed": True, "runtime_evidence": "SANITIZED_BOUNDED_DECISION_RECORDED"}, "authorized bounded live execution is recorded without raw evidence")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    result = validate(args.root.resolve())
    for message in result.passes:
        print(f"[PASS] {message}")
    for message in result.failures:
        print(f"[FAIL] {message}")
    print(f"AI agent sandbox summary: passed={len(result.passes)} failed={len(result.failures)}")
    return 1 if result.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
