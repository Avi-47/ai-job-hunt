import os
from crewai import LLM

groq_llm = LLM(
    provider="groq",
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
<<<<<<< HEAD
)
=======
)
>>>>>>> 7a23e050ce75b5f6771d0ca546654504479212e2
