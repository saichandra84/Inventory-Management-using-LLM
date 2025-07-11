import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key securely
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Improved prompt for robust parsing
system_prompt = """
You are a helpful assistant that converts user queries about clothing inventory into specific HTTP API instructions.

Given a query, respond only with:
- A GET request if the user wants to view inventory.
- A POST request if the user wants to add or subtract items.

Output format:
<HTTP_METHOD> /inventory with JSON payload {"item": "<item_name>", "change": <+int or -int>}

Valid items are: "tshirts", "pants"

Examples:
"I sold 3 t shirts" → POST /inventory with JSON payload {"item": "tshirts", "change": -3}
"I added 2 pants" → POST /inventory with JSON payload {"item": "pants", "change": 2}
"How many tshirts are left?" → GET /inventory
"""

def interpret_query(query: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            temperature=0
        )
        response_text = chat_completion.choices[0].message.content.strip()
        return response_text
    except Exception as e:
        return f"Error: {str(e)}"
