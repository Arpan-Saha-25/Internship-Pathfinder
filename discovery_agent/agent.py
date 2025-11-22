import os
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from tools.internship_search import search_internships
from typing import List, Dict

MODEL = "gemini-2.5-flash-lite"

# Simple tool wrapper for ADK
def find_internships(query: str, limit: int = 10) -> List[Dict]:
    return search_internships(query, limit=limit)

retry_config = None

root_agent = LlmAgent(
    name="internship_discovery_agent",
    model=Gemini(model=MODEL),
    instruction="""
    You are an Internship Discovery Agent. Given a user query, use the find_internships tool
    to return a JSON array with fields: title, company, location, skills, link, posted.
    Return only valid JSON.
    """,
    tools=[find_internships],
)

if __name__ == "__main__":
    print("Run this agent via ADK Runner or expose via A2A in the mentor agent.")