import json
import re

def extract_json(text):
    """
    Extract first valid JSON object from LLM output
    """
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON object found in LLM output")

    json_str = match.group()
    return json.loads(json_str)

# def extract_json(text):
#     match = re.search(r"\{.*\}", text, re.DOTALL)
#     if not match:
#         return None
#     try:
#         return json.loads(match.group())
#     except:
#         return None