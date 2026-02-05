# tools/usajobs_api.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_usajobs_api(keyword: str, num_jobs: int = 1):
    if not keyword:
        raise ValueError("Keyword is required")

    headers = {
        "Authorization-Key": os.getenv("USAJOBS_API_KEY"),
        "User-Agent": os.getenv("USAJOBS_EMAIL")
    }

    params = {
        "Keyword": keyword,
        "ResultsPerPage": num_jobs
    }

    response = requests.get(
        "https://data.usajobs.gov/api/search",
        headers=headers,
        params=params,
        timeout=15
    )

    data = response.json()

    if "SearchResult" not in data:
        raise ValueError(f"USAJobs API error: {data}")

    results = []
    for item in data["SearchResult"]["SearchResultItems"]:
        job = item["MatchedObjectDescriptor"]
        results.append({
            "job_title": job.get("PositionTitle", "N/A"),
            "location": job.get("PositionLocationDisplay", "N/A"),
            "job_description": job.get("UserArea", {})
                .get("Details", {})
                .get("MajorDuties", [])
        })

    return results
