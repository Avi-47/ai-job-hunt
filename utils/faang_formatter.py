from utils.skill_cluster import cluster_skills
from utils.metric_injector import add_metrics, smart_metrics
from utils.ats_optimizer import inject_keywords


def format_faang_resume(profile, projects, job_skills):

    MAX_PROJECTS = 4
    MAX_BULLETS = 3
    MAX_SKILLS_PER_CLUSTER = 5
    MAX_SKILL_LINES = 5

    lines = []

    lines.append("YOUR NAME")
    lines.append("Email | GitHub | LinkedIn")
    lines.append("")

    # ---------- SKILLS ----------
    lines.append("SKILLS")
    clusters = cluster_skills(profile["skills"])

    for cat, items in clusters.items():
        if items:
            lines.append(f"{cat}: {', '.join(items[:MAX_SKILLS_PER_CLUSTER])}")

    skill_start = lines.index("SKILLS") + 1
    skill_lines = lines[skill_start:skill_start + MAX_SKILL_LINES]
    lines = lines[:skill_start] + skill_lines
    lines.append("")

    # ---------- EXPERIENCE ----------
    lines.append("EXPERIENCE")
    for exp in profile["experience"]:
        lines.append(f"{exp['role']} — {exp['company']}")
        lines.append(f"• {exp['work']}")
        lines.append("")

    # ---------- PROJECTS ----------
    lines.append("PROJECTS")

    for p in projects[:MAX_PROJECTS]:
        tech = ", ".join(p.get("tech", []))
        lines.append(f"{p['title']}  ({tech})")

        enhanced = [smart_metrics(b) for b in p["bullets"]]
        enhanced = enhanced[:MAX_BULLETS]
        # enhanced = inject_keywords(enhanced, job_skills)

        for bullet in enhanced:
            lines.append(f"• {bullet}")

        lines.append("")

    # ---------- EDUCATION ----------
    lines.append("EDUCATION")
    lines.append("Bachelor of Engineering")

    return "\n".join(lines)
