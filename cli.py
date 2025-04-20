import asyncio
import click
from workflows.format_and_answer import run as run_format_and_answer
from workflows.adk_agent_runner import run as run_adk_agent

@click.command()
@click.option('--workflow', default="format_and_answer", help='Workflow name')
@click.option('--question', prompt='Your question', help='問題')
@click.option('--context', default="", help='補充資料')
def cli(workflow, question, context):
    input_data = {"question": question, "context": context}

    if workflow == "format_and_answer":
        result = asyncio.run(run_format_and_answer(input_data))
        print("\n--- 格式化後問題 ---\n", result["formatted_question"])
        print("\n--- 回答 ---\n", result["answer"])
    elif workflow == "adk_agent":
        result = asyncio.run(run_adk_agent(input_data))
        print("\n--- ADK Agent 輸出 ---\n", result["agent_output"])
    else:
        print("Unknown workflow")

if __name__ == '__main__':
    cli()