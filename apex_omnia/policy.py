from dataclasses import dataclass
from .config import settings

@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    mode: str
    target: str
    reasons: tuple[str, ...]

def evaluate_policy() -> PolicyDecision:
    reasons: list[str] = []
    if settings.APEX_MODE != "observe_only":
        reasons.append("Only observe_only mode is enabled in this scaffold.")
    if settings.APEX_RESEARCH_ENABLED:
        reasons.append("Research execution is deliberately blocked until full policy and evidence gates ship.")
    else:
        reasons.append("Research execution flag is disabled.")
    if settings.APEX_TARGET_REPOSITORY != "protocolbuffers/protobuf":
        reasons.append("Target differs from the approved initial repository; explicit scope review required.")
    return PolicyDecision(False, settings.APEX_MODE, settings.APEX_TARGET_REPOSITORY, tuple(reasons))
