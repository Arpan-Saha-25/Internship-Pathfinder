from typing import List

# Minimal skill extractor that finds keywords. Replace with a better NLP model in prod.
COMMON_SKILLS = ["python","sql","excel","tensorflow","pytorch","nlp","machine learning","data analysis"]

def extract_skills(text: str) -> List[str]:
    t = text.lower()
    found = []
    for s in COMMON_SKILLS:
        if s in t:
            found.append(s)
    return found