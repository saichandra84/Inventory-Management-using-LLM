import requests
import json
import re

BASE_URL = "http://localhost:8000"

def call_inventory_api(response_text: str):
    try:
        if "GET /inventory" in response_text:
            res = requests.get(f"{BASE_URL}/inventory")
            return res.json()

        elif "POST /inventory" in response_text:
            # Extract the JSON string from the LLM response
            json_match = re.search(r"\{.*\}", response_text)
            if not json_match:
                return {"error": "No JSON payload found in LLM response"}

            raw_payload = json_match.group()

            # First unescape the string if it's double-escaped
            try:
                # This handles: "{\"item\": \"tshirts\", \"change\": -3}"
                payload = json.loads(raw_payload)
            except json.JSONDecodeError:
                # Try again after decoding the escaped string
                unescaped = json.loads(f'"{raw_payload}"')  # extra decode step
                payload = json.loads(unescaped)

            # Synonym normalization
            synonyms = {
            "jeans": "pants",
            "trousers": "pants",
            "t-shirt": "tshirts",
            "shirt": "tshirts"
            }
            item = payload.get("item", "").lower()
            payload["item"] = synonyms.get(item, item)
    

            # Send the request to inventory API
            res = requests.post(f"{BASE_URL}/inventory", json=payload)
            return res.json()

        else:
            return {"error": "Unrecognized LLM response format", "raw": response_text}

    except Exception as e:
        return {
            "error": "Failed to parse POST payload",
            "details": str(e),
            "raw_llm_response": response_text
        }
