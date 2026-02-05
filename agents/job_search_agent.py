from crewai import Agent
from llm_config import groq_llm
from tools.usajobs_tool import fetch_usajobs


job_search_agent = Agent(
    role="Job Search Specialist",
    goal="Fetch real job listings from USAJobs",
    backstory="Expert in government job search",
    tools=[fetch_usajobs],
    llm=groq_llm,
    verbose=True
)
