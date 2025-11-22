import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def search_internships(query: str, limit: int = 10):
    """Simple web-scraping fallback that returns a list of internship dicts.
    NOTE: For production use a proper API or paid data source and obey robots.txt.
    """
    results = []
    # Use a lightweight search (e.g., Bing / Google Custom Search API) in prod.
    # Here we simulate with a placeholder.
    for i in range(min(limit, 10)):
        results.append({
            "title": f"{query} Internship #{i+1}",
            "company": "ExampleCorp",
            "location": "Remote",
            "skills": ["Python", "Data Analysis"],
            "link": f"https://example.com/{query.replace(' ','-')}/{i+1}",
            "posted": "2025-11-01"
        })
    return results