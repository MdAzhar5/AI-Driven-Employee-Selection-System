import os

# Define folders that need __init__.py
python_packages = [
    "RecruitX/agents",
    "RecruitX/tools",
    "RecruitX/backend",
    "RecruitX/backend/api",
    "RecruitX/backend/services",
    "RecruitX/frontend",
    "RecruitX/frontend/components",
    "RecruitX/database",
    "RecruitX/tests",
]

# Define file structure
structure = {
    "RecruitX": [
        "agents/jd_research_agent.py",
        "agents/jd_drafting_agent.py",
        "agents/job_posting_agent.py",
        "agents/applicant_collector_agent.py",
        "agents/screening_agent.py",
        "agents/interview_scheduler_agent.py",
        "agents/email_automation_agent.py",
        "agents/question_generator_agent.py",
        "agents/transcript_analyst_agent.py",
        "agents/decision_agent.py",
        "agents/database_agent.py",

        "config/agents.yaml",
        "config/tools.yaml",
        "config/tasks.yaml",
        "config/crew_config.yaml",
        "config/settings.yaml",

        "tools/resume_parser.py",
        "tools/web_scraper.py",
        "tools/email_sender.py",
        "tools/calendar_connector.py",
        "tools/pdf_docx_loader.py",
        "tools/vector_store.py",
        "tools/llm_interface.py",

        "backend/main.py",
        "backend/api/jd_api.py",
        "backend/api/resume_api.py",
        "backend/api/interview_api.py",
        "backend/services/scoring_engine.py",
        "backend/services/workflow_runner.py",
        "backend/services/whisper_transcriber.py",

        "frontend/streamlit_app.py",
        "frontend/components/jd_form.py",
        "frontend/components/resume_uploader.py",
        "frontend/components/interview_dashboard.py",

        "data/resumes/.keep",
        "data/transcripts/.keep",
        "data/jd_templates/.keep",

        "database/models.py",
        "database/schema.sql",
        "database/db_config.py",

        "tests/test_agents.py",
        "tests/test_tools.py",
        "tests/test_api.py",
        "tests/test_utils.py",

        "requirements.txt",
        "README.md",
        ".env",
        ".gitignore"
    ]
}


def create_structure(base_dir, files):
    for filepath in files:
        path = os.path.join(base_dir, filepath)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                if path.endswith('.py'):
                    f.write("# " + os.path.basename(path))
                elif path.endswith('.yaml'):
                    f.write("# YAML configuration for " + os.path.basename(path))
                elif os.path.basename(path) == ".keep":
                    pass
                else:
                    f.write("")

def create_init_files(package_dirs):
    for folder in package_dirs:
        init_file = os.path.join(folder, "__init__.py")
        os.makedirs(folder, exist_ok=True)
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write("# Package initializer")

# Build everything
for root, file_list in structure.items():
    create_structure(root, file_list)

create_init_files(python_packages)
