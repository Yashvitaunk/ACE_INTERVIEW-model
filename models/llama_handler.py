import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(prompt):

    payload = {
       "model": "qwen2.5:3b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=180
    )

    response.raise_for_status()

    return response.json()["response"]