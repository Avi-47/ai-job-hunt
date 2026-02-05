# tools/usajobs_tool.py
from crewai.tools import tool
from tools.usajobs_api import fetch_usajobs_api

@tool("fetch_usajobs")
def fetch_usajobs(keyword: str, num_jobs: int = 1):
    """Fetch job listings from USAJobs"""
    return fetch_usajobs_api(keyword, num_jobs)
