from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import asyncio
from agents.manager_agent import manager_agent_process

app = FastAPI()

class ProcessRequest(BaseModel):
    input_text: str
    documents: Optional[List[str]] = None

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Agent API! Use the /process endpoint via POST."}

@app.post("/process")
async def process(request: ProcessRequest):
    user_input = request.input_text
    documents = request.documents if request.documents else None

    if not user_input:
        raise HTTPException(status_code=400, detail="input_text is required.")

    result = await manager_agent_process(user_input, documents)
    return result
