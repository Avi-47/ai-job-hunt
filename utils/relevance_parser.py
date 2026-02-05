import re
def extract_top_projects(ranking, top_n=3):
    # ranking is now a list of dicts returned by AI
    return [item["project"] for item in ranking[:top_n]]

# def extract_top_projects(ranking_text, top_n=3):
#     lines = ranking_text.split("\n")
#     projects = []

#     for line in lines:
#         match = re.search(r"\*\*(.*?)\*\*", line)
#         if match:
#             projects.append(match.group(1))

#         if len(projects) >= top_n:
#             break

#     return projects
