from fastapi import FastAPI
from .config import settings
from .policy import evaluate_policy

app = FastAPI(title="APEX OMNIA Ω", version="0.1.0", description="Scope-gated security research control plane; research execution is disabled in this foundation release.")

@app.get("/health")
async def health():
    return {"status": "ok", "service": "apex-omnia"}

@app.get("/ready")
async def ready():
    decision = evaluate_policy()
    return {"ready": True, "research_enabled": False, "policy_allowed": decision.allowed}

@app.get("/status")
async def status():
    decision = evaluate_policy()
    return {"service": "APEX OMNIA Ω", "version": app.version, "mode": settings.APEX_MODE, "target_repository": settings.APEX_TARGET_REPOSITORY, "research_enabled": False, "policy_allowed": decision.allowed, "phase": "P0_CONTROL_PLANE_SCAFFOLD"}

@app.get("/policy")
async def policy():
    decision = evaluate_policy()
    return {"allowed": decision.allowed, "mode": decision.mode, "target": decision.target, "reasons": list(decision.reasons), "human_approval_required_for": ["upstream_pull_request", "program_submission", "any_external_write"]}
