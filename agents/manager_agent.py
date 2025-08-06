import agents.agent1 as agent1
import agents.agent2 as agent2
import agents.agent3 as agent3
import asyncio
from typing import List

async def manager_agent_process(user_input: str, documents: List[str] = None) -> dict:
    input_lower = user_input.lower()
    words = user_input.split()
    decision = ""
    selected_agents = []
    agent_responses = {}

    if len(words) > 100:
        decision = "Input looks like a document. Selected Agent1 for summarization and keyword extraction."
        selected_agents.append("Agent1")
        data = await agent1.agent1_process(user_input)
        agent_responses["Agent1"] = {"status": "success", "data": data}

    elif any(qword in input_lower for qword in ["what", "who", "when", "where", "how", "why", "explain", "?"]) and documents:
        decision = "Detected a query with documents provided. Selected Agent2 to respond based on documents."
        selected_agents.append("Agent2")
        data = await agent2.agent2_process(user_input, documents)
        agent_responses["Agent2"] = {"status": "success", "data": data}

    elif any(keyword in input_lower for keyword in ["current", "latest", "news", "update", "weather", "real-time"]):
        decision = "Detected keywords indicating need for real-time info. Selected Agent3 to fetch live data."
        selected_agents.append("Agent3")
        data = agent3.fetch_from_internet(user_input)
        agent_responses["Agent3"] = {"status": "success", "data": data}

    else:
        decision = "Default fallback to Agent3 for internet connected info."
        selected_agents.append("Agent3")
        data = agent3.fetch_from_internet(user_input)
        agent_responses["Agent3"] = {"status": "success", "data": data}

    return {
        "manager_agent": {
            "decision": decision,
            "selected_agents": selected_agents
        },
        "agent_responses": agent_responses
    }
