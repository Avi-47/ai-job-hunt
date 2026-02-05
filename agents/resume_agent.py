from crewai import Agent
from llm_config import groq_llm

resume_agent = Agent(
    role="Resume and Cover Letter Specialist",
    goal="Generate ATS-optimized resumes and cover letters",
    backstory="Senior technical recruiter.",
    llm=groq_llm,
    verbose=True
)
