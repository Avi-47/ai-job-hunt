import os
from crewai import LLM

groq_llm = LLM(
    provider="groq",
    model="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)