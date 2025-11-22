from typing import Dict, List
# Very simple matching score for demo purposes

def score_resume_against_job(resume: Dict, job: Dict) -> float:
    # resume: {"skills": [..], "title": ".."}
    rskills = set([s.lower() for s in resume.get("skills", [])])
    jskills = set([s.lower() for s in job.get("skills", [])])
    if not jskills:
        return 0.0
    match = len(rskills & jskills) / len(jskills)
    
    return round(match * 100, 2)