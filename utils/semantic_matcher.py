from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(skill_a, skill_b):
    emb_a = model.encode(skill_a)
    emb_b = model.encode(skill_b)

    sim = cosine_similarity(
        [emb_a],
        [emb_b]
    )[0][0]

    return float(sim)

def semantic_match_skills(job_skills, user_skills):
    results = []

    for js in job_skills:
        best_score = 0
        best_match = None

        for us in user_skills:
            score = semantic_similarity(js, us)

            if score > best_score:
                best_score = score
                best_match = us

        results.append({
            "job_skill": js,
            "user_skill": best_match,
            "score": round(best_score, 2)
        })

    return results
