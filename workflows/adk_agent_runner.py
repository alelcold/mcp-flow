from adk_agents.simple_agent.agent_config import create_simple_agent

async def run(input):
    question = input.get("question", "")
    context = input.get("context", "")
    full_prompt = f"{question}\n\n背景資料：{context}"

    agent = create_simple_agent()
    result = agent.run(user_input=full_prompt)
    return {
        "agent_output": result.output
    }