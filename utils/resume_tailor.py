def tailor_resume(job_skills, profile):

    job_skills = [s.lower() for s in job_skills]

    matched_skills = []
    selected_projects = []
    tailored_experience = []

    # ---- Match skills ----
    for skill in profile["skills"]:
        if skill.lower() in job_skills:
            matched_skills.append(skill)

    # ---- Match projects ----
    for proj in profile["projects"]:
        tech_stack = " ".join(proj["tech"]).lower()
        desc = proj["description"].lower()

        score = sum(skill in tech_stack or skill in desc for skill in job_skills)

        if score > 0:
            selected_projects.append(proj)

    # ---- Match experience ----
    for exp in profile["experience"]:
        text = exp["work"].lower()
        score = sum(skill in text for skill in job_skills)

        if score > 0:
            tailored_experience.append(exp)

    return {
        "skills": matched_skills,
        "projects": selected_projects,
        "experience": tailored_experience
    }

    
def format_resume(data):
    lines = []

    lines.append("SKILLS")
    lines.append(", ".join(data["skills"]))
    lines.append("")

    lines.append("PROJECTS")
    for p in data["projects"]:
        lines.append(f"{p['title']} | {p['tech']}")
        lines.append(p["description"])
        lines.append("")

    lines.append("EXPERIENCE")
    for e in data["experience"]:
        lines.append(f"{e['role']} – {e['company']}")
        lines.append(e["work"])
        lines.append("")

    return "\n".join(lines)
