import asyncio
from typing import Dict, List
from llm_clients import call_groq

async def agent2_process(query: str, documents: List[str]) -> Dict:
    if not documents:
        return {
            "query": query,
            "response": "No documents provided to answer the query."
        }
    combined_docs = "\n\n".join(documents)
    prompt = f"Based on the following documents, answer the question:\n\nDocuments:\n{combined_docs}\n\nQuestion: {query}\nAnswer:"
    response = await call_groq(prompt)
    return {
        "query": query,
        "response": response.strip()
    }
