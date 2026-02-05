from crewai import Task
from agents.job_analyzer import job_analyzer

analyze_job_task = Task(
    agent=job_analyzer,
    description="""
Extract ONLY concrete technical skills from the job posting.

Job Data:
{job_data}

Rules:
- Include programming languages, tools, frameworks, platforms, ML topics, databases, cloud
- Examples: python, sql, machine learning, docker, aws, rest apis, tensorflow
- Exclude soft skills, processes, roles, documentation, management words
- Normalize terms (ml → machine learning)
- Lowercase everything
- Keep skills short (1–3 words)

Return STRICT JSON only:

{
  "job_title": "",
  "required_skills": []
}
""",
    expected_output="JSON only",
    output_key="analysis"
)
