from sentinelbench.schemas import PromptRecord

def test_valid_record_loads():
    record = PromptRecord(
        prompt_id="123",
        category="math",
        domain="algebra",
        question="What is 2 + 2?",
        correct_answer="4",
        wrong_answer="5",
        version="1.0",
        correct_aliases=["four", "IV"],
        wrong_aliases=["five", "V"],
        source="hand-written",
        human_verified=False
    )
    assert record.prompt_id == "123"