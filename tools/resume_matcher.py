from typing import List, Dict, Set
from .skill_extractor import extract_skills

def score_match(resume_skills, job_dict) -> float:
    """
    Test expectations:
    - resume_skills is a *list* of skills, already extracted.
    - job_dict is a dict with "description".
    """
    # Validate inputs
    if not isinstance(resume_skills, list):
        resume_skills = []

    if not isinstance(job_dict, dict) or "description" not in job_dict:
        return 0.0

    # Extract skills from job description
    jd_skills = set(extract_skills(job_dict["description"]))
    resume_set = set(resume_skills)

    if not jd_skills:
        return 0.0

    # Compute overlap
    overlap = resume_set & jd_skills
    score = len(overlap) / len(jd_skills)

    return round(score, 3)
