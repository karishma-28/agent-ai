import asyncio
from typing import Dict
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from llm_clients import call_gemini

# Download punkt tokenizer once
nltk.download('punkt')

def extract_keywords(text: str, n=5) -> list:
    vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_array = vectorizer.get_feature_names_out()
    tfidf_sorting = tfidf_matrix.toarray().flatten().argsort()[::-1]
    top_n = tfidf_sorting[:n]
    keywords = [feature_array[i] for i in top_n]
    return keywords

async def agent1_process(document: str) -> Dict:
    prompt = f"Please provide a concise summary of the following document:\n\n{document}"
    print("Agent1: Sending prompt to Gemini...")
    try:
        summary = await call_gemini(prompt)
        print("Agent1: Received summary from Gemini.")
    except Exception as e:
        print("Agent1: Gemini API call failed:", e)
        summary = "Summary not available due to API error."
    keywords = extract_keywords(document)
    print(f"Agent1: Extracted keywords: {keywords}")
    return {
        "document": summary,
        "keywords": keywords
    }

