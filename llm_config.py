import os
from crewai import Agent
from crewai.llms import Groq

groq_llm = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)
