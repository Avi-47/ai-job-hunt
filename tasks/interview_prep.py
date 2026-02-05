from crewai import Task
from agents.interview_agent import interview_agent

interview_task = Task(
    description="""
    Job Requirements:
    {job_requirements}

    Candidate Resume:
    {resume_text}

    Generate:
    - 5 technical interview questions
    - 3 behavioral questions
    - Provide strong sample answers for each
    """,
    expected_output="Interview questions with model answers",
    agent=interview_agent
)
