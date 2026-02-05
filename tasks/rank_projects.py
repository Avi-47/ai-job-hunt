from crewai import Task
from agents.relevance_agent import relevance_agent

rank_projects_task = Task(
    description="""
    Job Requirements:
    {job_requirements}

    Candidate Projects:
    {projects}

    Return STRICT JSON ONLY in this format:

    [
      {
        "project": "<project name>",
        "score": <0-100>,
        "matched_skills": ["skill1", "skill2"],
        "reason": "short explanation"
      }
    ]

    Rules:
    - No extra text
    - No markdown
    - No commentary
    - Score realistically based on relevance
    """,
    expected_output="Strict JSON list of ranked projects",
    agent=relevance_agent
)
