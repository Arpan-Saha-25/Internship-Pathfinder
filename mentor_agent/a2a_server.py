from google.adk.a2a.utils.agent_to_a2a import to_a2a
from mentor_agent.agent import mentor


# Expose mentor as A2A app on port 8000
app = to_a2a(mentor, port=8000)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)