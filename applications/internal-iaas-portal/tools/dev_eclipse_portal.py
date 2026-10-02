"""Loopback-only development stack. SQLite and keys never enter the repository."""
from __future__ import annotations

import argparse
import logging
import secrets
import sys
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for service in ("request-api", "approval-api", "grant-api", "terraform-runner"):
    sys.path.insert(0, str(ROOT / "services" / service))

import httpx
import uvicorn
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from approval_api.config import Settings as ApprovalSettings
from approval_api.main import create_app as create_approval
from grant_api.config import Settings as GrantSettings
from grant_api.main import create_app as create_grant
from request_api.config import Settings as RequestSettings
from request_api.main import create_app as create_request
from terraform_runner.client import ApprovalClient
from terraform_runner.config import Settings as RunnerSettings
from terraform_runner.executor import Executor


def checked_runtime_root(path: Path) -> Path:
    if not path.is_absolute():
        raise ValueError("runtime-root must be absolute")
    resolved = path.resolve()
    if any((parent / ".git").exists() for parent in (resolved, *resolved.parents)):
        raise ValueError("runtime-root must remain outside every Git checkout")
    return resolved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=18080, help="Loopback UI/API port; +1/+2 reserved for internal APIs")
    parser.add_argument("--runtime-root", type=Path, default=Path(tempfile.gettempdir()) / "snsd-eclipse-local")
    parser.add_argument("--simulate-provisioning", action="store_true", help="Run the existing mock runner; never Terraform")
    parser.add_argument("--simulate-llm", action="store_true", help="Enable inert local replies; never call a model")
    args = parser.parse_args()
    if not 1024 <= args.port <= 65533:
        parser.error("port must be between 1024 and 65533")
    try:
        runtime = checked_runtime_root(args.runtime_root)
    except ValueError as exc:
        parser.error(str(exc))
    runtime.mkdir(parents=True, exist_ok=True)
    for name in ("request.db", "approval.db", "grant.db"):
        target = runtime / name
        if target.is_symlink() or target.resolve().parent != runtime:
            parser.error("runtime database redirects are forbidden")
    urls = [f"http://127.0.0.1:{args.port + offset}" for offset in range(3)]
    db = lambda name: f"sqlite+pysqlite:///{(runtime / (name + '.db')).as_posix()}"
    request = create_request(RequestSettings(database_url=db("request"), auto_create_schema=True, auth_mode="dev",
        approval_api_url=urls[1], grant_api_url=urls[2], enable_local_llm_simulator=args.simulate_llm))
    approval = create_approval(ApprovalSettings(database_url=db("approval"), auto_create_schema=True, auth_mode="dev",
        request_api_url=urls[0], grant_api_url=urls[2], enable_provisioning_jobs=True))
    grant = create_grant(GrantSettings(database_url=db("grant"), auto_create_schema=True, auth_mode="dev",
        request_api_url=urls[0], approval_api_url=urls[1], grant_signing_key=secrets.token_urlsafe(48),
        grant_signing_algorithm="HS256"))
    request.mount("/eclipse", StaticFiles(directory=ROOT / "services/user-portal/eclipse", html=True), name="eclipse")
    @request.get("/", include_in_schema=False)
    def index():
        return RedirectResponse("/eclipse/local.html")

    servers = [uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=args.port+i, log_level="warning",
                                            access_log=False)) for i, app in enumerate((request, approval, grant))]
    stop = threading.Event()
    threads = [threading.Thread(target=s.run, daemon=True) for s in servers[1:]]
    for thread in threads:
        thread.start()

    def worker():
        settings = RunnerSettings(approval_api_url=urls[1], auth_mode="dev", runner_mode="mock",
                                  runner_id="eclipse-local-simulator", mock_delay_seconds=0.2)
        client, executor = ApprovalClient(settings), Executor(settings)
        while not stop.wait(0.5):
            try:
                job = client.claim()
                if job:
                    executor.run(job, lambda payload: client.report(job["job_id"], payload))
            except (httpx.HTTPError, OSError, RuntimeError, ValueError):
                logging.warning("Local mock queue is unavailable; retrying")
    if args.simulate_provisioning:
        thread = threading.Thread(target=worker, daemon=True)
        threads.append(thread)
        thread.start()
    print(f"Eclipse local portal: {urls[0]}/eclipse/local.html", flush=True)
    print("Loopback development; synthetic data only; runtime NOT_VALIDATED.", flush=True)
    print(f"Provisioning simulator={args.simulate_provisioning}; LLM simulator={args.simulate_llm}", flush=True)
    try:
        servers[0].run()
    finally:
        stop.set()
        for server in servers:
            server.should_exit = True
        for thread in threads:
            thread.join(timeout=5)


if __name__ == "__main__":
    main()
