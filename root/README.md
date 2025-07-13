## 🔧 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/saichandra84/inventory-management-using-LLM.git
   cd inventory-management-using-LLM


2. Set up virtual environments and install dependencies for both services:
   #Inventory Service
   cd inventory_service
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --host 0.0.0.0 --port 8000

   #MCP Server
   Open a new terminal/tab:
   cd mcp_server
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --host 0.0.0.0 --port 8500

3. Set your OpenAI API Key:
   Create a .env file in mcp-server/:
   OPENAI_API_KEY=your-api-key


📮 API Examples (Curl or Postman)

Inventory API (localhost:8000):
# Add inventory
curl -X POST http://localhost:8000/inventory \
  -H "Content-Type: application/json" \
  -d '{"item": "tshirts", "change": 5}'

# Get inventory
curl http://localhost:8000/inventory

MCP Server (localhost:8500):
curl -X POST http://localhost:8500/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "I sold 3 t shirts"}'

## 📘 API Documentation

OpenAPI documentation is auto-generated via FastAPI and can be accessed at:

- `http://localhost:8000/docs` for Inventory Service
- `http://localhost:8500/docs` for MCP Server

These interactive docs are powered by Swagger UI and include schema definitions for all endpoints.


🧠 Design Reasoning & Plan

## 🔍 Design & Integration Approach

- Chose **FastAPI** for its built-in OpenAPI support and speed.
- Integrated **OpenAI's GPT-3.5 Turbo API** to parse user input and map to REST actions.
- Used a modular setup (`llm_parser.py`, `client.py`) to separate LLM logic and service communication.
- Researched OpenAI’s Python SDK v1.x migration and updated code accordingly.
- Carefully tested prompt variations to ensure consistency.

## 🧩 MCP Logic

- Receives natural language via `/ask`
- Uses OpenAI's `gpt-3.5-turbo` to convert to actionable API call
- Extracts and sends actual API call to Inventory Service
- Returns the result or an error

## ⚠️ Known Limitations

- Hardcoded item list (e.g., "tshirts", "pants")
- No authentication
- No persistent database (in-memory store)
- Simple prompt engineering without history or context memory

## 📈 Future Improvements
- Add synonym support (e.g., “trousers” = “pants”)
- Add persistent DB (like SQLite or PostgreSQL)
- Better natural language understanding for compound commands




