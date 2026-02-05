import json
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
import streamlit as st
import time
from tools.usajobs_api import fetch_usajobs_api
from crewai import Crew
from tasks.analyze_job import get_analyze_job_task
from agents.job_analyzer import job_analyzer
from utils.logger import log_action
# from data.resume_skills import MY_SKILLS
from data.resume_skills import USER_PROFILE
# from utils.match_engine import skill_match
from utils.match_engine import weighted_match, experience_match, overall_match
from utils.json_utils import extract_json
# from utils.resume_parser import parse_resume
from utils.skill_extractor import extract_skills
from utils.file_reader import extract_text
from utils.interview_runner import run_interview_prep
from utils.profile_manager import load_profile, save_profile
from utils.resume_tailor import tailor_resume, format_resume
from utils.relevance_runner import rank_projects_ai
from utils.bullet_runner import rewrite_bullets_ai
from utils.relevance_parser import extract_top_projects
from utils.pdf_exporter import export_resume_pdf
from utils.pdf_exporter import export_resume_pdf
from utils.heatmap_builder import build_skill_heatmap, color_scale, color_match
from utils.semantic_matcher import semantic_match_skills
from utils.project_explainer import explain_project_score
from utils.recruiter_resume_formatter import format_recruiter_resume
from utils.bullet_parser import parse_bullets
from utils.faang_formatter import format_faang_resume



st.session_state.setdefault("job_analysis", {})   # key: idx
st.session_state.setdefault("job_resume", {})
st.session_state.setdefault("job_message", {})

if "resume_text" not in st.session_state:
    st.session_state["resume_text"] = ""

def compress_projects(projects, max_len=400):
    text = ""
    for p in projects:
        snippet = f"{p['title']}: {p['description'][:120]}\n"
        if len(text) + len(snippet) > max_len:
            break
        text += snippet
    return text

resume_skills = []

if st.session_state["resume_text"]:
    # resume_skills = extract_skills(st.session_state["resume_text"])
    profile = load_profile()
    resume_skills = profile["skills"]

st.subheader("📄 Upload Your Resume (PDF)")

uploaded_file = st.file_uploader(
    "Upload resume",
    type=["pdf", "docx", "txt", "png", "jpg", "jpeg"]
)
resume_file = uploaded_file

if resume_file:
    resume_text = resume_file.read().decode(errors="ignore")
    st.session_state["resume_text"] = resume_text
    st.success("✅ Resume uploaded & parsed successfully")

st.set_page_config(page_title="AI Job Hunt", layout="wide")
st.title("🤖 AI Job Hunt Assistant")


st.subheader("👤 My Profile")

profile = load_profile()

skills_input = st.text_input(
    "Skills (comma separated)",
    ", ".join(profile["skills"])
)

projects_input = st.text_area(
    "Projects (one per line: title | tech | description)",
    "\n".join(
        f"{p['title']} | {','.join(p['tech'])} | {p['description']}"
        for p in profile["projects"]
    )
)

experience_input = st.text_area(
    "Experience (one per line: role | company | work)",
    "\n".join(
        f"{e['role']} | {e['company']} | {e['work']}"
        for e in profile["experience"]
    )
)

if st.button("💾 Save Profile"):
    profile["skills"] = [s.strip().lower() for s in skills_input.split(",") if s]

    profile["projects"] = []
    for line in projects_input.split("\n"):
        if "|" in line:
            t, tech, d = line.split("|", 2)
            profile["projects"].append({
                "title": t.strip(),
                "tech": [x.strip().lower() for x in tech.split(",")],
                "description": d.strip()
            })

    profile["experience"] = []
    for line in experience_input.split("\n"):
        if "|" in line:
            r, c, w = line.split("|", 2)
            profile["experience"].append({
                "role": r.strip(),
                "company": c.strip(),
                "work": w.strip()
            })

    save_profile(profile)
    st.success("✅ Profile saved")


# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("🔍 Job Search")
    keyword = st.text_input("Job keyword", "python developer")
    # num_jobs = st.selectbox("Number of jobs", [1, 100], index=0)
    num_jobs = st.slider("Number of jobs", min_value=1, max_value=15, value=1)

    fetch_btn = st.button("🔍 Fetch Jobs")
    analyze_btn = st.button("🧠 Analyze Job")

# ---------------- Session State ----------------
st.session_state.setdefault("jobs", None)
st.session_state.setdefault("analysis", None)

# ---------------- Fetch Jobs (NO LLM) ----------------
if fetch_btn:
    log_action(
        action="fetch_jobs",
        details={
            "keyword": keyword,
            "num_jobs": num_jobs
        }
    )

    with st.spinner("Fetching jobs..."):
        try:
            st.session_state.jobs = fetch_usajobs_api(
                keyword=keyword,
                num_jobs=num_jobs
            )
        except Exception as e:
            st.error(f"❌ USAJobs API Error: {e}")


def extract_raw_output(result):
    # CrewAI v0.30+
    if hasattr(result, "tasks_output") and result.tasks_output:
        return result.tasks_output[0].raw

    # Older versions
    if hasattr(result, "raw"):
        return result.raw

    # Last fallback
    return str(result)

# ---------------- Show Jobs ----------------
if st.session_state.jobs:
    st.subheader("📄 Job Results")

    for idx, job in enumerate(st.session_state.jobs):
        with st.container(border=True):

            st.markdown(f"### {job['job_title']}")
            st.markdown(f"📍 **Location:** {job['location']}")

            with st.expander("📋 Job Description"):
                for line in job["job_description"]:
                    st.write("•", line)

            col1, col2, col3, col4 = st.columns(4)

            # ---------- ANALYZE ----------
            resume_ready = "resume_text" in st.session_state

            if col1.button(
                "🧠 Analyze",
                key=f"analyze_{idx}",
                disabled=not resume_ready
            ):
                with st.spinner("Analyzing job..."):

                    crew_analyze = Crew(
                        agents=[job_analyzer],
                        tasks=[analyze_job_task],
                        verbose=False
                    )

                    result = crew_analyze.kickoff(
                        inputs={"job_data": job}
                    )

                    time.sleep(6)

                raw = extract_raw_output(result)

                try:
                    analysis_json = extract_json(raw)
                except Exception as e:
                    st.error("❌ AI returned invalid JSON")
                    st.code(raw)
                    st.stop()

                st.session_state.job_analysis[idx] = analysis_json

                log_action(
                    action="analyze_job",
                    details={
                        "job_title": job["job_title"],
                        "skills_count": len(analysis_json["required_skills"])
                    }
                )

            # ---------- SHOW ANALYSIS + MATCH SCORE ----------
            if idx in st.session_state.job_analysis:

                analysis = st.session_state.job_analysis[idx]

                st.subheader("🎯 AI Project Relevance Ranking")

                short_projects = profile["projects"][:5]   # only top 5
                projects_text = compress_projects(short_projects)

                job_requirements = ", ".join(analysis["required_skills"][:12])
                with st.spinner("Ranking projects with AI..."):
                    ranking = rank_projects_ai(
                        job_requirements,
                        projects_text
                    )
                
                st.subheader("🧾 AI Optimized Resume Bullets")

                top_project_names = extract_top_projects(ranking, top_n=3)

                top_projects = [
                    p for p in profile["projects"]
                    if p["title"] in top_project_names
                ]

                top_projects_text = "\n".join(
                    f"{p['title']} | tech: {', '.join(p['tech'])} | {p['description']}"
                    for p in top_projects
                )
                job_req_text = ", ".join(analysis["required_skills"])

                with st.spinner("Rewriting bullets with AI..."):
                    optimized_bullets = rewrite_bullets_ai(job_req_text,top_projects_text)

                structured_projects = parse_bullets(optimized_bullets)
                # inject tech stack from profile
                for p in structured_projects:
                    for orig in profile["projects"]:
                        if orig["title"] == p["title"]:
                            p["tech"] = orig["tech"]
                faang_resume = format_faang_resume(profile, structured_projects, analysis["required_skills"])
                st.text_area("📄 Recruiter Style Resume", faang_resume, height=500)


                st.text_area("✨ Optimized Bullets", optimized_bullets, height=300)

                # st.text_area("📊 Relevance Results", ranking, height=250)
                st.subheader("📊 Relevance Results")

                for item in ranking:
                    st.write(f"**{item['project']}** — {item['score']}%")

                    st.caption(f"Matched: {', '.join(item['matched_skills'])}")

                    st.write(item['reason'])
                    st.markdown("**Why this project scored:**")

                    project_text = item["project"] + " " + item["reason"]

                    bars = explain_project_score(
                        project_text,
                        analysis["required_skills"]
                    )
                    for b in bars:
                        st.progress(b["score"] / 100)
                        st.caption(f"{b['skill']} — {b['score']}%")

                    st.divider()

                with st.expander("🧠 Analysis Result"):
                    st.json(analysis)

                # 🎯 MATCH ENGINE (BEFORE AI)
                structured_projects = parse_bullets(optimized_bullets)

                for p in structured_projects:
                    for orig in profile["projects"]:
                        if orig["title"] == p["title"]:
                            p["tech"] = orig["tech"]

                resume_text = format_faang_resume(profile, structured_projects, analysis["required_skills"])
                st.session_state["resume_text"] = resume_text

                tailored = tailor_resume(
                    analysis["required_skills"],
                    profile
                )

                match = weighted_match(
                    tailored["skills"],
                    analysis["required_skills"]
                )
                semantic_results = semantic_match_skills(
                    analysis["required_skills"],
                    profile["skills"]
                )

                st.subheader("🔥 Smart Semantic Skill Matching")

                for m in semantic_results:
                    if m["score"] >= 0.8:
                        emoji = "🟢"
                    elif m["score"] >= 0.6:
                        emoji = "🟡"
                    else:
                        emoji = "🔴"


                    st.write(
                        f"{emoji} {m['job_skill']} → {m['user_skill']} ({m['score']})"
                    )

                if semantic_results:
                    semantic_score = round(
                        sum(m["score"] for m in semantic_results) / len(semantic_results) * 100,
                        2
                    )
                else:
                    semantic_score = 0


                st.metric("Semantic Match %", f"{semantic_score}%")

                st.session_state.setdefault("match_history", {})

                before_score = match["match_percentage"]

                # 🎯 TEMP AFTER SCORE (until real recompute added)
                optimized_match = weighted_match(
                    tailored["skills"] + analysis["required_skills"],
                    analysis["required_skills"]
                )

                after_score = optimized_match["match_percentage"]

                st.session_state.match_history[idx] = {
                    "before": before_score,
                    "after": after_score
                }

                # 📈 IMPROVEMENT CHART
                st.subheader("📈 Match Improvement")

                chart_data = {
                    "Stage": ["Before AI", "After AI"],
                    "Match %": [before_score, after_score]
                }

                st.bar_chart(chart_data, x="Stage", y="Match %")


                # 📊 CURRENT MATCH
                st.subheader("📊 Resume Match Score")
                st.metric("Match", f"{before_score}%")

                st.subheader("🔥 Skill Match Heatmap")
                heatmap_df = build_skill_heatmap(
                    profile["skills"],
                    analysis["required_skills"]
                )

                st.dataframe(
                    heatmap_df.style.applymap(color_scale, subset=["Match Score"]),
                    use_container_width=True
                )





                c1, c2 = st.columns(2)

                with c1:
                    st.success("Matched Skills")
                    for s in match["matched_skills"]:
                        st.write("✅", s)

                with c2:
                    st.error("Missing Skills (Skill Gaps)")
                    for s in match["missing_skills"]:
                        st.write("❌", s)

                # ---------- RESUME ----------
                if col2.button("📄 Resume", key=f"resume_{idx}"):

                    st.session_state.job_resume[idx] = "v1"

                    log_action(
                        action="generate_resume",
                        details={
                            "job_title": job["job_title"],
                            "resume_version": "v1"
                        }
                    )

                    st.success("Resume generated")
                
                if st.button("🧾 Auto Tailor Resume", key=f"tailor_{idx}"):

                    structured_projects = parse_bullets(optimized_bullets)

                    for p in structured_projects:
                        for orig in profile["projects"]:
                            if orig["title"] == p["title"]:
                                p["tech"] = orig["tech"]

                    resume_text = format_faang_resume(profile, structured_projects, analysis["required_skills"])
                    st.session_state["resume_text"] = resume_text


                    st.success("✅ Resume tailored successfully!")
                    st.text_area("📄 Recruiter Style Resume", resume_text, height=600)


                # ---------- PDF EXPORT ----------
                if st.session_state["resume_text"]:
                    if st.button("📄 Export Resume PDF", key=f"pdf_export_{idx}"):

                        file_path = export_resume_pdf(
                            st.session_state["resume_text"]
                        )

                        with open(file_path, "rb") as f:
                            st.download_button(
                                "⬇ Download Resume PDF",
                                f,
                                file_name="AI_Tailored_Resume.pdf",
                                mime="application/pdf",
                                key=f"download_{idx}"
                            )



                if st.button("🎤 Generate Interview Prep", key=f"interview_{idx}"):
                    with st.spinner("Preparing interview questions..."):
                        interview_pack = run_interview_prep(job_req_text, st.session_state["resume_text"])
                    st.text_area("🎯 Interview Questions & Answers", interview_pack, height=400)

                # ---------- MESSAGE ----------
                if col3.button("✉️ Message", key=f"message_{idx}"):

                    message = "Dear Hiring Manager, I am excited to apply..."

                    st.session_state.job_message[idx] = message

                    log_action(
                        action="generate_message",
                        details={
                            "job_title": job["job_title"],
                            "preview": message[:120]
                        }
                    )

                    st.success("Message generated")

                # ---------- APPLY ----------
                if idx in st.session_state.job_message:
                    if col4.button("🚀 Apply", key=f"apply_{idx}"):

                        log_action(
                            action="apply",
                            details={
                                "job_title": job["job_title"],
                                "status": "sent"
                            }
                        )

                        st.success("Application sent (simulated)")
