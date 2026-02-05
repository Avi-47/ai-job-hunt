def format_recruiter_resume(profile,optimized_bullets):
    skills = ", ".join(profile["skills"])

    experience_section = ""
    for e in profile["experience"]:
        experience_section += f"""
        {e['role']}-{e['company']}
        • {e['work']}
"""
    
    projects_section = optimized_bullets.strip()

    resume = f""" 
    {profile.get('name', 'YOUR NAME')}
    Email | Github | Linkedin
    =================================================

    SKILLS
    {skills}
    =================================================

    EXPERIENCE
    {experience_section}
    =================================================

    PROJECTS
    {projects_section}

    Education 
    Bachelor of Engineering

    """
    return resume.strip()