SKILL_SYNONYMS = {
    "docker": ["containerization", "containers"],
    "sql": ["database", "dbms"],
    "rest apis": ["api integration", "web services"],
    "machine learning": ["ml", "applied machine learning"],
    "ci cd": ["continuous integration", "pipelines"]
}

def normalize(skill):
    return (
        skill.lower()
        .replace("/", " ")
        .replace("-", " ")
        .strip()
    )

def similar(a, b):
    a = normalize(a)
    b = normalize(b)
    if a in b or b in a:
        return True

    for key, values in SKILL_SYNONYMS.items():
        if a == key and b in values:
            return True
        if b == key and a in values:
            return True

    return False

def weighted_match(resume_skills, job_skills):
    matched = []
    missing = []

    for job_skill in job_skills:
        found = False

        for res_skill in resume_skills:
            if similar(job_skill, res_skill):
                matched.append(job_skill)
                found = True
                break

        if not found:
            missing.append(job_skill)

    total = len(job_skills)
    score = round((len(matched) / total) * 100, 2) if total else 0

    return {
        "match_percentage": score,
        "matched_skills": matched,
        "missing_skills": missing
    }


def experience_match(required_years, user_years=0):
    if not required_years:
        return 100

    if user_years >= required_years:
        return 100

    return round((user_years / required_years) * 100, 2)


def overall_match(skill_score, exp_score, skill_weight=0.8, exp_weight=0.2):
    return round(
        skill_score * skill_weight + exp_score * exp_weight,
        2
    )