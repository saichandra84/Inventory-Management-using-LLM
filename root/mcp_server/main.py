# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from llm_parser import interpret_query
from client import call_inventory_api

app = FastAPI(title="MCP Server", description="Model Control Plane with GenAI", version="1.0.0")

class UserQuery(BaseModel):
    query: str

@app.post("/ask")
def ask(query: UserQuery):
    try:
        parsed = interpret_query(query.query)
        print("✅ Parsed LLM response:", parsed)
        result = call_inventory_api(parsed)
        return {
            "parsed": parsed,
            "result": result
        }
    except Exception as e:
        import traceback
        print("❌ EXCEPTION OCCURRED")
        traceback.print_exc()
        return {"error": str(e)}