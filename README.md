<h1 align="center">🤖 RecruitX: AI Recruitment</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20With-CrewAI-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Frontend-Streamlit-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/LLM-GPT%204-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=flat-square" />
</p>

<p align="center">
  <strong>RecruitX</strong> is an agentic, generative AI-powered recruitment system built with <code>CrewAI</code>, streamlining the entire hiring pipeline — from JD creation to interview scoring and onboarding automation.
</p>

---

<h2>🌐 Project Overview</h2>

RecruitX automates the full recruitment cycle using autonomous agents. It transforms how hiring teams:

<ul>
  <li>Create and manage job descriptions</li>
  <li>Collect and screen resumes at scale</li>
  <li>Schedule interviews and analyze transcripts</li>
  <li>Score candidates using custom AI agents</li>
  <li>Manage decisions and onboarding flows</li>
</ul>

---
<h2>🚀 Installation</h2>

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/RecruitX.git
cd RecruitX

# 2. Set up a virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Streamlit Frontend
streamlit run frontend/streamlit_app.py
```
---

<h2>🧠 System Architecture</h2>

<h3>🎭 Agents</h3>

- <strong>JD Research Agent:</strong> Gathers info from hiring team
- <strong>JD Drafting Agent:</strong> Writes optimized JDs
- <strong>Job Posting Agent:</strong> Posts to job boards
- <strong>Applicant Collector Agent:</strong> Parses and stores resumes
- <strong>Screening Agent:</strong> Scores resume vs JD
- <strong>Interview Scheduler Agent:</strong> Auto-books interviews
- <strong>Email Automation Agent:</strong> Sends interview/offers
- <strong>Question Generator Agent:</strong> Creates technical questions
- <strong>Transcript Analyst Agent:</strong> Analyzes performance
- <strong>Decision Agent:</strong> Calculates final selection
- <strong>Database Agent:</strong> Stores, updates applicant records

<h3>🛠️ Tools</h3>

- PDF/DOCX Parser (PyMuPDF, docx2txt)
- Vector Database (FAISS or Pinecone)
- Whisper (for transcripts)
- BERT/GPT Embeddings
- Google Calendar API
- SendGrid Email API
- MySQL/MongoDB

---
<h2>📁 Repository Structure</h2>

<pre>
RecruitX/
├── agents/
│   ├── jd_research_agent.py
│   ├── jd_drafting_agent.py
│   ├── job_posting_agent.py
│   ├── applicant_collector_agent.py
│   ├── screening_agent.py
│   ├── interview_scheduler_agent.py
│   ├── email_automation_agent.py
│   ├── question_generator_agent.py
│   ├── transcript_analyst_agent.py
│   ├── decision_agent.py
│   └── database_agent.py
│
├── tools/
│   ├── resume_parser.py
│   ├── calendar_connector.py
│   ├── email_sender.py
│   ├── vector_store.py
│   ├── transcript_parser.py
│   └── job_board_poster.py
│
├── config/
│   ├── agents.yaml
│   ├── tools.yaml
│   ├── tasks.yaml
│
├── backend/
│   ├── main.py
│   └── api/
│       └── jd_api.py
│
├── frontend/
│   ├── streamlit_app.py
│   └── components/
│       └── jd_form.py
│
├── database/
│   ├── models.py
│   ├── schema.sql
│   └── db_connection.py
│
├── data/
│   ├── resumes/
│   ├── transcripts/
│
├── tests/
│   ├── test_agents.py
│   ├── test_tools.py
│
├── requirements.txt
├── README.md
└── .gitignore
</pre>
