import re

def parse_bullets(text):
    projects = []
    current = None

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        # Detect project title (many formats)
        if (
            line.startswith("**") and line.endswith("**")
            or re.match(r"Project\s*\d+:", line)
            or (line and not line.startswith("-") and not line.startswith("•") and len(line) < 80)
        ):
            title = line.replace("*","").replace("Project","").replace(":","").strip()

            current = {
                "title": title,
                "bullets": []
            }
            projects.append(current)

        elif current and (line.startswith("-") or line.startswith("•")):
            current["bullets"].append(line.lstrip("-• ").strip())

    # Remove empty ones
    return [p for p in projects if p["bullets"]]
