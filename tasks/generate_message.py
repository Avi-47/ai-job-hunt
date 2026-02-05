from crewai import Task
from agents.messaging_agent import messaging_agent
from tasks.analyze_job import analyze_job_task

generate_message_task = Task(
    description="""
Using the analyzed job data, generate a concise and professional
LinkedIn outreach message to a hiring manager or recruiter.

The message should:
- Mention relevant skills
- Show interest in the role
- Be polite and confident
""",
    agent=messaging_agent,
    context=[analyze_job_task],
    expected_output="""
A short professional LinkedIn message (3–5 sentences) tailored to the job.
""",
    output_key="message_output"
)
