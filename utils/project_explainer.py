from utils.semantic_matcher import semantic_similarity

def explain_project_score(project_text, job_skills):
    explanations = []

    for skill in job_skills:
        score = semantic_similarity(skill, project_text)

        explanations.append({
            "skill": skill,
            "score": round(score * 100, 1)
        })

    explanations.sort(key=lambda x: x["score"], reverse=True)

    return explanations[:6]   # top contributing skills
