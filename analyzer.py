import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openrouter import OpenRouter

# Load environment variables from .env file
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

def llm_call(description, instructions, prompt):
    llm_agent = Agent(
        model=OpenRouter(id="deepseek/deepseek-chat:free", api_key=OPENROUTER_API_KEY),
        markdown=True,
        description=description,
        instructions=instructions
    )
    response = llm_agent.run(prompt)
    return response.content

def jd_create(prompt):
    description = (
        "You are an expert Job Description Writer with deep industry knowledge, "
        "specializing in crafting structured, compelling, and well-formatted job descriptions."
    )
    instructions = [
        "Take the user-provided job details and generate a professional job description.",
        "Ensure the output includes a clear role summary, responsibilities, required skills, preferred qualifications, employment type, and location.",
        "Maintain a structured and industry-appropriate tone, adapting to the job level and field.",
        "Format the job description for readability, using bullet points where necessary.",
    ]
    job_description = llm_call(description, instructions, prompt)
    # Specify encoding="utf-8" to handle all Unicode characters
    with open("job_description.txt", "w", encoding="utf-8") as w:
        w.write(job_description)
    return job_description

def questions_create(job_description):
    description = (
        "You are an AI-powered Critical Questions Generator, specializing in extracting key aspects "
        "of a job description to generate insightful interview questions."
    )
    instructions = [
        "Analyze the given job description to identify essential skills, experience, responsibilities, and industry context.",
        "Generate six critical interview questions covering Skills, Experience, Critical Thinking, Responsibilities, Problem-Solving, and Industry Knowledge.",
        "Ensure that the questions are thought-provoking, role-specific, and aligned with the job level.",
        "Format the output clearly with each question labeled according to its category.",
    ]
    prompt = f"""
        Generate six critical interview questions assessing a candidate’s Skills,
        Experience, Critical Thinking, and Responsibilities. Ensure the questions are job-specific,
        thought-provoking, and aligned with the role's seniority level.
        Given the following job description:
        {job_description}
    """
    questions = llm_call(description, instructions, prompt)
    with open("questions.txt", "w", encoding="utf-8") as w:
        w.write(questions)
    return questions

def transcript_create(questions):
    description = (
        "You are an AI-powered Dummy Transcript Creator, capable of generating realistic interview transcripts "
        "based on provided questions, from both the Interviewer and Applicant perspectives."
    )
    instructions = [
        "Take the provided interview questions and generate a natural, structured dialogue between an Interviewer and an Applicant.",
        "Ensure that the Applicant’s responses reflect relevant skills, experience, and problem-solving abilities based on the role.",
        "Maintain a professional yet conversational tone to simulate a real-world interview.",
        "Include follow-up questions where necessary to create a dynamic and engaging interaction.",
        "Format the output with clear dialogue labels (e.g., 'Interviewer:', 'Applicant:').",
    ]
    prompt = (
        f"Generate a realistic interview transcript between an **Interviewer** and an **Applicant**. "
        f"Use the job responsibilities, required skills, and qualifications to formulate relevant questions. "
        f"Ensure the conversation flows naturally, with structured responses that showcase expertise, "
        f"problem-solving, and alignment with the role. Include follow-up questions where necessary. "
        f"Maintain a professional and engaging tone. Based on the following questions: {questions}"
    )
    transcript = llm_call(description, instructions, prompt)
    with open("transcript.txt", "w", encoding="utf-8") as w:
        w.write(transcript)
    return transcript

def analyses_scoring(job_description, transcript):
    description = (
        "You are an AI-powered Interview Scoring & Analysis Assistant, specializing in evaluating applicant responses "
    )
    instructions = [
        "Review the interview transcript and job description and give score out of 10, also create a short summary of applicient performance .",
        "Score the Applicant’s performance based on key factors: technical skills, experience, problem-solving ability, critical thinking."
    ]
    prompt = (
        f"Review the interview transcript and job description and give score out of 10, also create a 4 line short summary of applicient performance, avoid details"
        f"Transcript: \n{transcript}\nJob Description: \n{job_description}"
    )
    analysis = llm_call(description, instructions, prompt)
    return analysis
