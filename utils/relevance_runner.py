from crewai import Crew
from tasks.rank_projects import rank_projects_task
from utils.json_parser import extract_json


def normalize_scores(ranking):
    if not ranking:
        return ranking

    max_score = max(item["score"] for item in ranking)
    if max_score == 0:
        return ranking

    for item in ranking:
        item["score"] = round((item["score"] / max_score) * 100, 1)

    return ranking


def rank_projects_ai(job_requirements, projects_text):

    crew = Crew(
        agents=[rank_projects_task.agent],
        tasks=[rank_projects_task],
        verbose=False
    )

    raw = crew.kickoff(
        inputs={
            "job_requirements": job_requirements,
            "projects": projects_text
        }
    )

    try:
        ranked = extract_json(str(raw))
        ranked = normalize_scores(ranked)   # ⭐ normalize here
        return ranked
    except Exception:
        return []
