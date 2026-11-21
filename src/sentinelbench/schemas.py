from pydantic import BaseModel, Field, ConfigDict

class PromptRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")
    prompt_id: str
    category: str
    domain: str 
    question: str
    correct_answer: str
    wrong_answer: str
    version: str
    correct_aliases: list[str] = []
    wrong_aliases: list[str] = []
    source: str = "hand-written"
    human_verified: bool = False