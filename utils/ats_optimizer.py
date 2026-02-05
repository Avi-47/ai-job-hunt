def inject_keywords(bullets, job_skills):
    optimized = []

    for bullet in bullets:
        boosted = bullet
        for skill in job_skills[:5]:   # top ATS skills only
            if skill.lower() not in boosted.lower():
                boosted += f" using {skill}"
                break
        optimized.append(boosted)

    return optimized
