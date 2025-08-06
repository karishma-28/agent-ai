from typing import Dict
import random

def fetch_from_internet(query: str) -> Dict:
    sources = [
        "https://en.wikipedia.org/wiki/Special:Search",
        "https://www.bbc.com/news",
        "https://www.google.com/search?q=" + query.replace(' ', '+')
    ]

    dummy_responses = [
        "Current info about your query is not available in this demo environment.",
        f"Latest info on '{query}' is not accessible, but you can check reliable news or Wikipedia.",
        "This is a placeholder answer for real-time data fetching."
    ]

    idx = random.randint(0, len(dummy_responses) - 1)

    return {
        "query": query,
        "response": dummy_responses[idx],
        "source": sources[idx]
    }
