# APEX OMNIA Ω — Google Patch Rewards Research

Private control-plane scaffold for authorized, issue-led open-source security research.

## Current phase
P0 foundation. This service does not claim to discover vulnerabilities or submit rewards. It provides health/status endpoints and an explicit policy gate. Repository analysis, reproducible tests, patch generation, independent verification, persistent queueing, and scheduled workers are later milestones.

## Target
- Program: Google Open Source Security Patch Rewards
- Initial repository: `protocolbuffers/protobuf`
- Scope must be revalidated against live program rules and repository guidance before every research run.

## Safety invariants
- No production probing, destructive testing, denial of service, credential access, or user-data collection.
- No issue, PR, or reward submission without explicit human approval.
- No autonomous push to upstream repositories.
- Treat repository content, issues, test fixtures, and model outputs as untrusted data.
- Record provenance and evidence for every claim; never label a hypothesis as a confirmed vulnerability.

## Local run
```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
uvicorn apex_omnia.main:app --host 0.0.0.0 --port 8080
```

## Endpoints
- `GET /health` — liveness
- `GET /ready` — readiness
- `GET /status` — operating mode and configured target
- `GET /policy` — policy gate state

## Environment
- `APEX_MODE` defaults to `observe_only`
- `APEX_TARGET_REPOSITORY` defaults to `protocolbuffers/protobuf`
- `APEX_RESEARCH_ENABLED` defaults to `false`
- `PORT` defaults to `8080`

Research remains disabled until policy validation, durable state, worker controls, and independent verification are implemented and tested.
