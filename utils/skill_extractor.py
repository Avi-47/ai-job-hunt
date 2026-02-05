import re

COMMON_SKILLS = [
    "python","machine learning","deep learning","sql","docker","aws",
    "rest apis","streamlit","tensorflow","pytorch","data analysis",
    "ci/cd","git","flask","fastapi"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in COMMON_SKILLS:
        if re.search(rf"\b{skill}\b", text):
            found.append(skill)

    return list(set(found))
