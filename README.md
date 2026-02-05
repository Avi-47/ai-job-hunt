Live website - https://ai-job-hunt-ekjdgfrvndzbsxynng2y8n.streamlit.app/

# 🤖 AI Job Hunt Assistant

<div align="center">

**Intelligent Resume & Job Matching System**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange.svg)](https://www.crewai.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

*Fight AI with AI. Automate job discovery, resume optimization, and interview prep using multi-agent AI reasoning.*

[Demo](#-demo) • [Features](#-core-features) • [Installation](#-installation) • [Architecture](#-system-architecture) • [Roadmap](#-roadmap)

</div>

---

## 🎯 The Problem

The modern job market is **asymmetric**:

| Job Seekers (Manual) | Recruiters (Automated) |
|---------------------|------------------------|
| ❌ Manually search hundreds of postings | ✅ AI-powered screening |
| ❌ Rewrite resumes repeatedly | ✅ Semantic skill matching |
| ❌ Guess what keywords to use | ✅ Automated ranking systems |
| ❌ Fail ATS filters unknowingly | ✅ Data-driven decisions |

**The reality:** Job seekers are competing against AI using manual workflows.

## ✨ The Solution

**Fight AI with AI.**

This platform builds an intelligent multi-agent system that automates the entire job hunting workflow:

- 🔍 **Fetches** real job postings from USAJobs API
- 🧠 **Understands** requirements using LLM reasoning
- 🎯 **Matches** skills semantically (not just keywords)
- 📊 **Ranks** your projects by relevance
- ✍️ **Rewrites** resume bullets with impact metrics
- 📈 **Tracks** match score improvements
- 🎤 **Generates** personalized interview prep

---

## 🚀 Core Features

### 1️⃣ Real Job Discovery
- Fetches **live job postings** from USAJobs API
- Extracts job descriptions, requirements, and metadata
- No fake or static data — real market intelligence

### 2️⃣ AI Job Understanding Agent
Uses LLM reasoning to extract structured data:
- ✅ Required skills
- ✅ Preferred qualifications
- ✅ Responsibilities
- ✅ Experience expectations

**Output:** Clean JSON for downstream processing

### 3️⃣ Semantic Skill Matching

**Beyond keyword matching** — uses AI similarity scoring:

| Job Requirement | Your Resume | Match Score |
|----------------|-------------|-------------|
| REST APIs | API integration | 88% ✅ |
| Docker | Containerization | 92% ✅ |
| Performance tuning | System optimization | 84% ✅ |

**Why this matters:**
- Mimics real ATS systems
- Catches semantic equivalents
- Higher true match accuracy

### 4️⃣ AI Project Relevance Ranking

Automatically ranks your projects based on job requirements:

```
🥇 Online Code Judge — 100% Match
   ✓ Python, Algorithms, Performance Engineering
   Why: Algorithm design (44%) + Backend systems (39%)

🥈 E-commerce Platform — 87% Match
   ✓ REST APIs, Database Design, Cloud Deployment
   Why: Full-stack development (52%) + API integration (35%)
```

### 5️⃣ AI Resume Bullet Optimization

Transforms generic bullets into **recruiter-style impact statements**:

| Before | After |
|--------|-------|
| Built a backend system | Developed scalable Python backend services improving evaluation throughput by **500%** and reducing latency by **37%** |
| Worked on algorithms | Designed and implemented **15+ algorithmic solutions** serving **10K+ daily users** with **99.9% uptime** |

**Automatically adds:**
- ✅ Quantified metrics
- ✅ Strong action verbs
- ✅ Role-relevant phrasing

### 6️⃣ Resume Match Engine

Calculates comprehensive match scores:
- **Matched skills** (exact + semantic)
- **Partial matches** (related skills)
- **Missing skill gaps** (what to learn)
- **Overall match percentage**

Visualized with heatmaps and progress charts.

### 7️⃣ Interview Preparation Generator

AI generates personalized prep materials:
- 🎯 Technical questions based on job requirements
- 🏗️ System design scenarios
- 💬 Behavioral STAR responses
- 📚 Study guides for skill gaps

---

## 🏗️ System Architecture

```
┌─────────────────┐
│   USAJobs API   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ AI Job Analyzer Agent   │ ← Groq LLM
│ (Extracts requirements) │
└────────┬────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Semantic Skill Matcher   │ ← AI Similarity
│ (Not keyword matching)   │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Project Ranking Agent    │ ← CrewAI
│ (Relevance scoring)      │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Resume Optimization Agent│ ← Impact rewriting
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Match Scoring Engine     │ ← Analytics
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│   Streamlit Frontend     │ ← Interactive UI
└──────────────────────────┘
```

**Multi-Agent Orchestration:** CrewAI coordinates specialized agents for each task.

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **AI & Agents** | CrewAI, Groq LLM API, Semantic Similarity Matching |
| **Backend** | Python 3.8+, JSON Pipelines, Weighted Scoring |
| **Frontend** | Streamlit, Interactive Charts, Heatmaps |
| **APIs** | USAJobs (live data) |
| **Output** | PDF Export, Resume Templates |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com))
- USAJobs API key ([Get one here](https://developer.usajobs.gov/))

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-job-hunt-assistant.git
cd ai-job-hunt-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env with your API keys
```

### Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
USAJOBS_API_KEY=your_usajobs_api_key_here
USAJOBS_USER_AGENT=your_email@example.com
```

### Run the Application

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your browser.

---

## 🎮 Usage

### 1. Search for Jobs
Enter keywords (e.g., "Software Engineer", "Data Scientist")

### 2. Select a Job
Choose from real job postings

### 3. Input Your Profile
- Add your skills
- List your projects
- Upload or paste resume bullets

### 4. Get AI Analysis
- View semantic skill matches
- See ranked projects
- Get optimized resume bullets
- Check match score improvements

### 5. Export Results
- Download optimized resume (PDF)
- Save interview prep questions
- Track application progress

---

## 📊 Demo

<!-- Add screenshots or GIFs here -->

### Skill Matching Dashboard
![Skill Match Example](docs/images/skill-match.png)

### Resume Optimization
![Resume Optimization](docs/images/resume-optimize.png)

### Match Score Improvement
```
Before AI Optimization:  55% match
After AI Optimization:   87% match
                        ────────────
Improvement:            +32% 📈
```

---

## 🎯 Why This Project Stands Out

| Traditional Projects | This Project |
|---------------------|--------------|
| ❌ Toy recommender systems | ✅ Real job market data |
| ❌ Static ML demos | ✅ Agentic AI workflows |
| ❌ Keyword matching only | ✅ Semantic NLP reasoning |
| ❌ Academic exercises | ✅ Production-ready system |

**This demonstrates:**
- AI agent orchestration
- Real-world NLP applications
- Product engineering thinking
- Full-stack development
- Practical automation

---

## 🗺️ Roadmap

### ✅ Phase 1 (Current)
- [x] Multi-agent AI system
- [x] Real job API integration
- [x] Semantic skill matching
- [x] Resume optimization
- [x] Streamlit dashboard

### 🚧 Phase 2 (In Progress)
- [ ] FastAPI backend
- [ ] PostgreSQL database
- [ ] User authentication
- [ ] Resume version history
- [ ] Application tracking

### 🔮 Phase 3 (Planned)
- [ ] Multiple job board APIs (LinkedIn, Indeed)
- [ ] Advanced analytics dashboard
- [ ] Email notifications
- [ ] Chrome extension
- [ ] Mobile app

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) for multi-agent orchestration
- [Groq](https://groq.com/) for fast LLM inference
- [USAJobs](https://www.usajobs.gov/) for job data API
- [Streamlit](https://streamlit.io/) for the amazing UI framework

---

## 📧 Contact

Avimanyu Goswami

🐦 X (Twitter): [@AvimanyuGo71678](https://x.com/AvimanyuGo71678)

📧 Email (University): avimanyug.ee.ug@jadavpuruniversity.in

📧 Email (Personal): avimanyugoswami02@gmail.com

🔗 Project Repository: AI Job Hunt Assistant

<div align="center">

⭐ If this project helped you, please consider giving it a star! ⭐
<br/>
Made with ❤️ and 🤖 AI

</div>
