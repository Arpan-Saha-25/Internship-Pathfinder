from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from tools.resume_matcher import score_resume_against_job

MODEL = "gemini-2.5-flash-lite"

# Tool that returns a match score and explanation
def evaluate_fit(resume: dict, job: dict) -> dict:
    score = score_resume_against_job(resume, job)
    explanation = f"Matched {score}% of listed job skills with user's resume."
    return {"score": score, "explanation": explanation}

root_agent = LlmAgent(
    name="fit_evaluation_agent",
    model=Gemini(model=MODEL),
    instruction="""
    You are a Fit Evaluation Agent. Use evaluate_fit tool to score how well a user's resume
    fits a given internship. Return JSON: {score: number, explanation: str}
    """,
    tools=[evaluate_fit],
)


if __name__ == "__main__":
    print("Evaluate via Runner or expose it to mentor via A2A.")