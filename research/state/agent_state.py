from typing import TypedDict

class AgentState(TypedDict):
    messages: list
    decision: str
    report: str
    pdf_path: str
