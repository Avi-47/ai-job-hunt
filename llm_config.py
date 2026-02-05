import os
from dotenv import load_dotenv
from crewai.llm import LLM

load_dotenv()

groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
    max_tokens=512
)
