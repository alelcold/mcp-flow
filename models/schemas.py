from pydantic import BaseModel
from typing import Dict

class ChatWorkflowRequest(BaseModel):
    workflow: str
    input: Dict