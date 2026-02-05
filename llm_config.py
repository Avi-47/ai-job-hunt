import os
from crewai import LLM   # ✅ correct for your CrewAI version

groq_llm = LLM(
    provider="groq",
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
)
