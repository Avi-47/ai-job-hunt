from crewai import Task
from agents.bullet_agent import bullet_agent

rewrite_bullets_task = Task(
    description="""
    Job Requirements:
    {job_requirements}

    Selected Projects (ONLY use this data, do NOT invent new domains, companies, or technologies):
    {top_projects}

    Rewrite each project into 2–3 strong resume bullets that:
    - Use only technologies explicitly listed
    - Do NOT add new industries (no cybersecurity, no NLP, no companies)
    - Quantify impact realistically if possible
    - Emphasize performance, engineering, and job alignment

    If something is not in project data, DO NOT include it.
    """,
    expected_output="Optimized resume bullets for each project",
    agent=bullet_agent
)
