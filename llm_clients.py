import os
from dotenv import load_dotenv
import httpx

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def call_gemini(prompt: str) -> str:
    url = "https://api.gemini.llm/v1/generate"  # Replace with actual Gemini LLM API endpoint
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json",
    }
    json_data = {
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.7,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=json_data)
        response.raise_for_status()
        data = response.json()
        return data.get("text") or data.get("choices", [{}])[0].get("text", "")

async def call_groq(prompt: str) -> str:
    url = "https://api.groq.ai/v1/llm/generate"  # Replace with actual Groq LLM API endpoint
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    json_data = {
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.7,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=json_data)
        response.raise_for_status()
        data = response.json()
        return data.get("text") or data.get("choices", [{}])[0].get("text", "")
