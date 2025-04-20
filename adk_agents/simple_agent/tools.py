from adk.tools import Tool, ToolInput

class LookupTool(Tool):
    def run(self, tool_input: ToolInput) -> str:
        query = tool_input.input_text
        fake_db = {
            "python": "Python 是一種直譯式、動態語言。",
            "fastapi": "FastAPI 是一個高效的 Web 框架。"
        }
        return fake_db.get(query.lower(), "查無資料")