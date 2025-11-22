import os
import uuid
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

MODEL = "gemini-2.5-flash-lite"

# Remote agent card URLs (if running locally via to_a2a, set ports accordingly)
DISCOVERY_CARD = os.environ.get("DISCOVERY_AGENT_CARD", "http://localhost:8001/.well-known/agent-card.json")
EVAL_CARD = os.environ.get("EVAL_AGENT_CARD", "http://localhost:8002/.well-known/agent-card.json")


remote_discovery = RemoteA2aAgent(name="discovery_proxy", agent_card=DISCOVERY_CARD)
remote_eval = RemoteA2aAgent(name="eval_proxy", agent_card=EVAL_CARD)


mentor = LlmAgent(
    name="mentor_agent",
    model=Gemini(model=MODEL),
    instruction="""
    You are Internship Mentor. Gather user's preferences, call discovery agent to find listings,
    call evaluation agent to score, then produce a ranked list with action items.
    """,
    sub_agents=[remote_discovery, remote_eval],
)


if __name__ == "__main__":
    print("Run mentor via to_a2a or adk runner. Exposes a conversational endpoint.")