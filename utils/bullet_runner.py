from crewai import Crew
from tasks.rewrite_bullets import rewrite_bullets_task

def clean_output(text):
    if "Thought:" in text:
        text = text.split("Thought:")[-1]
    return text.strip()

def rewrite_bullets_ai(job_requirements, top_projects):

    crew = Crew(
        agents=[rewrite_bullets_task.agent],
        tasks=[rewrite_bullets_task],
        verbose=False
    )

    result = crew.kickoff(
        inputs={
            "job_requirements": job_requirements,
            "top_projects": top_projects
        }
    )

    # Always extract raw safely
    if hasattr(result, "tasks_output") and result.tasks_output:
        raw = result.tasks_output[0].raw
    elif hasattr(result, "raw"):
        raw = result.raw
    else:
        raw = str(result)

    return clean_output(raw)
