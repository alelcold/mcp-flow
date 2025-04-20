from adk.agent_runner import AgentRunner
from adk.models import AgentConfig
from .tools import LookupTool

def create_simple_agent():
    return AgentRunner(
        config=AgentConfig(
            name="custom-tool-agent",
            instructions="你是一個能根據用戶輸入查找資料並回覆的助手。",
            tools=[LookupTool()],
            verbose=True
        )
    )