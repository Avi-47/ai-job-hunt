from crewai import Task
from agents.job_search_agent import job_search_agent

fetch_jobs_task = Task(
    description="""
    Call fetch_usajobs ONCE.

    Keyword: {keyword}
    Number of jobs: {num_jobs}

    Return tool output as-is.
    """,
    agent=job_search_agent,
    expected_output="Raw job listings",
    output_key="job_results",
    max_retries=0   # 🔥 THIS STOPS LOOPING
)


# instructions cause the LLM to deadlock.
# from crewai import Task
# from agents.job_search_agent import job_search_agent

# fetch_jobs_task = Task(
#     description="""
#     Use the fetch_usajobs tool to search for jobs.

#     Rules:
#     - You MUST call the tool
#     - Do NOT explain anything
#     - Return ONLY the raw tool output

#     Keyword: {keyword}
#     Number of jobs: {num_jobs}
#     """,
#     expected_output="List of real job listings from USAJobs API",
#     agent=job_search_agent,
#     output_key="job_results"
# )


# from crewai import Task
# from agents.job_search_agent import job_search_agent

# fetch_jobs_task = Task(
#     description="""
#     Search USAJobs fro '{keyword}' roles.
#     Fetch the top {num_jobs} job listings.
#     For each job, return:
#     - Job Title
#     - Location
#     - Job Description
#     """,
#     expected_output="A list of job postings with title, location, and full job description.",
#     agent=job_search_agent
# )