import asyncio
from typing import Dict, List
from llm_clients import call_groq  # Ensure this function is implemented correctly

async def agent2_process(query: str, documents: List[str]) -> Dict:
    if not documents:
        return {
            "query": query,
            "response": "No documents provided to answer the query."
        }

    # Join all documents into one text block
    combined_docs = "\n\n".join(documents)

    # Create a prompt for answering the query
    prompt = (
        f"Based on the following documents, answer the question:\n\n"
        f"Documents:\n{combined_docs}\n\n"
        f"Question: {query}\n\nAnswer:"
    )

    # Get response from Groq (LLM)
    response = await call_groq(prompt)

    return {
        "query": query,
        "response": response.strip()
    }
