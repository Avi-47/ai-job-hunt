from crewai import Task
from agents.resume_agent import resume_agent
from tasks.analyze_job import analyze_job_task

generate_resume_task = Task(
    description="""
    Using the analyzed job data, do the following:

    1. Generate 5–7 ATS-optimized resume bullet points
    2. Write a professional, customized cover letter (150–200 words)

    Output only the final resume bullets and cover letter.
    """,
    agent=resume_agent,
    context=[analyze_job_task],  # ✅ FIX
    expected_output="Resume bullets and a professional cover letter"
)




# from crewai import Task
# from agents.resume_agent import resume_agent
# from test_usajobs import job

# generate_resume_task = Task(
#     description="""
#     Using the following job details:
    
#     Job Title:
#     {job_title}
    
#     Required Skills:
#     {required_skills}

#     Key Responsibilities:
#     {responsibilities}

#     Do the following:
#     1. Generate 5-7 ATS-optimized resume bullet points
#     2. Write a professional, customized cover letter (150-200 words)
#     """,
#     expected_output="""
#     Resume Bullets:
#     - Bullets points aligned to the job

#     Cover Letter:
#     - A concise, tailored cover letter
#     """,
#     agent=resume_agent
# )