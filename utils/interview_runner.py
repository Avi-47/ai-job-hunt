from crewai import Crew
from tasks.interview_prep import interview_task

def clean_llm_output(text):
    if "Thought:" in text:
        text = text.split("Thought:")[-1]
    return text.strip()

def interview_prep(job_requirements, resume_text):

    crew = Crew(
        agents=[interview_task.agent],
        tasks=[interview_task],
        verbose=False
    )

    result = crew.kickoff(
        inputs={
            "job_requirements": job_requirements,
            "resume_text": resume_text
        }
    )

    # CrewAI new versions
    if hasattr(result, "tasks_output") and result.tasks_output:
        raw = result.tasks_output[0].raw
        return clean_llm_output(raw)

    # fallback
    return clean_llm_output(str(result))
