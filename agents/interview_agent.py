from crewai import Agent
from llm_config import groq_llm
interview_agent = Agent(
    role="Technical Interview Coach",
    goal="Generate realistic interview questions and strong answers based on job requirements and candidate resume",
    backstory=(
        "You are a senior software engineer and hiring manager who prepares candidates for technical interviews."
    ),
    verbose=True
)
