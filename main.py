from fastapi import FastAPI
from models.schemas import ChatWorkflowRequest
from workflows.format_and_answer import run as run_format_and_answer
from workflows.adk_agent_runner import run as run_adk_agent

app = FastAPI()

@app.post("/chat")
async def chat(req: ChatWorkflowRequest):
    if req.workflow == "format_and_answer":
        return await run_format_and_answer(req.input)
    elif req.workflow == "adk_agent":
        return await run_adk_agent(req.input)
    return {"error": "Unknown workflow"}