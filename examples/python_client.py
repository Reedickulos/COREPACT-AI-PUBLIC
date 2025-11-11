"""
Example: Public-safe Python client skeleton for a CORE PACT–style service.
No real endpoints or tokens are included. Replace placeholders with your own.
"""

import os
import json
import requests


API_URL = os.environ.get("COREPACT_API_URL", "https://your-api.example.com/v1/demo")
API_KEY = os.environ.get("COREPACT_API_KEY", "YOUR_API_KEY_HERE")

"""
Also see curl example in examples/curl_example.txt
"""


def demo_request(prompt: str) -> dict:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "query": prompt,
        # Add public-safe, generic fields only
        "options": {"temperature": 0.2},
    }

    resp = requests.post(API_URL, headers=headers, data=json.dumps(payload), timeout=60)
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    try:
        result = demo_request("Summarize the benefits of multi-agent collaboration.")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Request failed: {e}")
