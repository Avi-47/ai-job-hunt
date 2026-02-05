from crewai import Crew

from tasks.fetch_jobs import fetch_jobs_task
from tasks.analyze_job import analyze_job_task
from tasks.generate_resume import generate_resume_task
from tasks.generate_message import generate_message_task

from agents.job_search_agent import job_search_agent
from agents.job_analyzer import job_analyzer
from agents.resume_agent import resume_agent
from agents.messaging_agent import messaging_agent

from utils.match_engine import weighted_match, experience_match, overall_match

crew = Crew(
    agents=[
        job_search_agent,
        job_analyzer,
        resume_agent,
        messaging_agent
    ],
    tasks=[
        fetch_jobs_task,
        analyze_job_task,
        generate_resume_task,
        generate_message_task
    ],
    verbose=False
)

SKILL_WEIGHTS = {
    "python": 0.3,
    "machine learning": 0.25,
    "rest apis": 0.2,
    "streamlit": 0.15,
    "data analysis": 0.1
}

import time

try:
    result = crew.kickoff(
        inputs={
            "keyword": "python developer",
            "num_jobs": 1
        }
    )
    # analysis_output = analyze_job_task.output  # CrewAI stores last output here
    analysis_output = result.get("analyze_job_task")

    job_skills = analysis_output.get("required_skills", [])

    skill_score, gaps = weighted_match(
        job_skills,
        SKILL_WEIGHTS
    )

    exp_score = experience_match(
        analysis_output.get("years_required")
    )

    final_score = overall_match(skill_score, exp_score)

    print("\n🔥 MATCH RESULTS")
    print("Skill Match:", skill_score, "%")
    print("Experience Match:", exp_score, "%")
    print("Overall Fit:", final_score, "%")
    print("Missing Skills:", gaps)


    # ⏳ Groq cooldown to avoid TPM burst
    time.sleep(6)

    print("\n" + "=" * 50)
    print("CREW EXECUTION COMPLETED")
    print("=" * 50)
    print(result)

except Exception as e:
    print("\n❌ Crew execution failed")
    print(type(e).__name__, ":", e)




# from crewai import Crew
# from tasks.analyze_job import analyze_job_task
# from tasks.fetch_jobs import fetch_jobs_task

# crew = Crew(
#     agents=[fetch_jobs_task.agent,analyze_job_task.agent],
#     tasks=[fetch_jobs_task,analyze_job_task],
#     verbose=True
# )

# job_description="""
# We are looking for a Python developer with experience in machine learning,
# REST APIs, and data analysis. Experience with Streamlit is a plus.
# """

# result = crew.kickoff(inputs={
#     "keyword": "python developer",
#     "num_jobs":2,
#     "job_description":job_description
# })
# print(result)


# # from crewai import Crew
# # from tasks.analyze_job import analyze_job_task
# # job_description="""
# # We are looking for a Python developer with experience in machine learning,
# # REST APIs, and data analysis. Experience with Streamlit is a plus.
# # """
# # crew = Crew(
# #     agents=[analyze_job_task.agent],
# #     tasks=[analyze_job_task],
# #     verbose=True
# # )
# # result = crew.kickoff(inputs={"job_description":job_description})
# # print(result)