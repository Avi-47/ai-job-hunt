from crewai import Agent
from llm_config import groq_llm


job_analyzer = Agent(
    role="Job Description Analyzer",
    goal="Extract skills and responsibilities from job descriptions",
    backstory="Expert HR analyst.",
    llm=groq_llm,          # ✅ REQUIRED
    verbose=True
)
