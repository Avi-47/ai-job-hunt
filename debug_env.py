import os
from dotenv import load_dotenv

load_dotenv()

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("OPENAI_BASE_URL:", os.getenv("OPENAI_BASE_URL"))
print("OPENAI_MODEL_NAME:", os.getenv("OPENAI_MODEL_NAME"))
