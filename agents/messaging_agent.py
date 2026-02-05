from crewai import Agent
from llm_config import groq_llm
import os
from dotenv import load_dotenv

load_dotenv()

# llm = LLM(
#     model="groq/llama3-8b-8192",   # ✅ PROVIDER EMBEDDED IN MODEL
#     api_key=os.getenv("GROQ_API_KEY")
# )

messaging_agent = Agent(
    role="Recruiter Outreach Specialist",
    goal=(
        "Write concise, professional outreach messages that get responses "
        "from recruiters and hiring managers."
    ),
    backstory=(
        "You are an expert career coach specializing in LinkedIn outreach "
        "and recruiter communication.\n\n"
        "IMPORTANT:\n"
        "- Output ONLY the messages\n"
        "- No thoughts\n"
        "- No reasoning\n"
        "- No explanations"
    ),
    llm=groq_llm,          # ✅ REQUIRED
    verbose=True
)
