from apex_omnia.policy import evaluate_policy

def test_research_is_blocked_by_default():
    decision = evaluate_policy()
    assert decision.allowed is False
    assert decision.target == "protocolbuffers/protobuf"
