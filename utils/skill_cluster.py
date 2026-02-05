def cluster_skills(skills):
    clusters = {
        "Languages": [],
        "Machine Learning & Data": [],
        "Backend & Systems": [],
        "Databases & APIs": [],
        "DevOps & Tools": []
    }

    for s in skills:
        s = s.lower().strip()

        # ---------- Languages ----------
        if s in {
            "python","java","c++","c","c#","go","rust",
            "javascript","typescript","bash","r","matlab"
        }:
            clusters["Languages"].append(s)

        # ---------- ML & Data ----------
        elif any(k in s for k in [
            "machine learning","deep learning","artificial intelligence",
            "computer vision","nlp",
            "scikit","tensorflow","pytorch",
            "numpy","pandas",
            "feature engineering","model evaluation",
            "classification","regression","clustering",
            "data analysis","data science"
        ]):
            clusters["Machine Learning & Data"].append(s)

        # ---------- Databases & APIs ----------
        elif any(k in s for k in [
            "sql","postgres","mysql","mongodb","nosql",
            "database","dbms",
            "rest api","rest apis","graphql",
            "json","xml"
        ]):
            clusters["Databases & APIs"].append(s)

        # ---------- DevOps & Tools ----------
        elif any(k in s for k in [
            "docker","kubernetes","ci/cd",
            "aws","cloud",
            "git","github",
            "devops"
        ]):
            clusters["DevOps & Tools"].append(s)

        # ---------- Backend & Systems ----------
        elif len(s.split()) <= 4:
            clusters["Backend & Systems"].append(s)

    MAX_SKILLS_PER_CLUSTER = 6
    for cat in clusters:
        clusters[cat] = sorted(set(clusters[cat]))[:MAX_SKILLS_PER_CLUSTER]

    return {k: v for k, v in clusters.items() if v}
