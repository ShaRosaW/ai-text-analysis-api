from pydantic import BaseModel


# --- Models ---
class TextInput(BaseModel):
    text: str


class AnalysisResponse(BaseModel):
    summary: str
    keywords: list[str]
    action_items: list[str]