from crewai import Agent
from llm_config import groq_llm

bullet_agent = Agent(
    role="Resume Bullet Optimizer",
    goal="Rewrite resume project bullets to strongly match job requirements while remaining truthful",
    backstory=(
        "You are an expert technical recruiter and resume writer specializing in ATS optimization. "
        "You align candidate experience with job keywords and responsibilities."
    ),
    llm=groq_llm,
    verbose=True
)
