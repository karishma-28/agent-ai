from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import agent4

app = FastAPI(title="Modular AI Agents System with Gemini & Groq")

class UserInput(BaseModel):
    input_text: str
    documents: Optional[list[str]] = None

@app.post("/process")
async def process_input(user_input: UserInput):
    try:
        response = await agent4.manager_agent_process(user_input.input_text, user_input.documents)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
