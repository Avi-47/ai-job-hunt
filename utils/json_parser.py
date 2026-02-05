import json
import re

def extract_json(text):
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON found in output")
    return json.loads(match.group())