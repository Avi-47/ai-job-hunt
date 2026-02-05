from crewai import Crew
from tasks.rank_projects import rank_projects_task

crew = Crew(
    agents=[rank_projects_task.agent],
    tasks=[rank_projects_task],
    verbose=True
)

job_requirements = """
Python, Machine Learning, REST APIs, Data Analysis, Streamlit
"""

projects = """
1. Automated Student Attendance System using face recognition and ML.
2. Movie Recommendation System using content-based filtering in Python.
3. Line Following Robot using sensors and microcontroller.
"""

result = crew.kickoff(
    inputs={
        "job_requirements": job_requirements,
        "projects": projects
    }
)

print(result)
