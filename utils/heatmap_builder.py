import pandas as pd 
from difflib import SequenceMatcher

def similarity(a,b):
    return SequenceMatcher(None,a.lower(),b.lower()).ratio()

def color_match(val):
    if val == 1:
        return "background-color: #7CFF7C"   # green = matched
    return "background-color: #FF7C7C"       # red = missing

def color_scale(val):
    if val == 1:
        return "background-color:#6BFF6B"   # green
    elif val == 0.5:
        return "background-color:#FFE66B"   # yellow
    else:
        return "background-color:#FF6B6B"   # red


def build_skill_heatmap(user_skills,job_skills):
    rows = []
    user_skills = [s.lower() for s in user_skills]
    job_skills = [s.lower() for s in job_skills]

    # all_skills = sorted(job_set)

    for skill in job_skills:
        best_match = max(
            [similarity(skill,u) for u in user_skills],
            default=0
        )

        if best_match>0.8:
            score=1.0
        elif best_match >=0.45:
            score=0.50
        else:
            score=0.0

        rows.append({
            "Skill" : skill,
            "Match Score": score
        })
    
    return pd.DataFrame(rows)