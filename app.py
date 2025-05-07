import streamlit as st
from interview_analyzer.analyzer import jd_create, questions_create, transcript_create, analyses_scoring

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Interview Analyzer",
    layout="centered",
    initial_sidebar_state="collapsed",
    page_icon= "❤"
)

# --- CUSTOM CSS & HTML FOR LAYOUT AND STYLING ---
page_bg = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
    background-color: #ffffff; /* Entire page is white */
    margin: 0;
    padding: 0;
}

/* Positioning shapes in corners */
.bg-shape-blue {
    position: absolute;
    top: 2%;
    left: 2%;
    width: 90px;
    height: 90px;
    background-color: #70c8f4;
    border-radius: 15px;
    opacity: 0.35;
    z-index: -1;
}

.bg-shape-pink {
    position: absolute;
    bottom: 2%;
    right: 2%;
    width: 120px;
    height: 120px;
    background-color: #ff5588;
    border-radius: 30px;
    opacity: 0.35;
    z-index: -1;
}

/* Container for the form */
.form-container {
    max-width: 800px;
    padding: 0 2rem;
    position: relative;
}

/* Title and subtitle styling with black headings */
.title-text {
    text-align: center;
    font-size: 2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: 111111;
}
.subtitle-text {
    text-align: center;
    font-size: 1rem;
    color:111111;
    margin-bottom: 2rem;
}

/* Streamlit button override to create a round pink button */
.stButton>button {
    background-color: #ff2f66 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 30px !important;
    padding: 0.6rem 2.5rem !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    margin-top: 1rem !important;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #ff5588 !important;
}

/* Center the entire Streamlit block so shapes appear behind it */
.css-1v0mbdj, .css-12oz5g7, .css-18e3th9 {
    align-items: center;
    justify-content: center;
}
</style>
"""

# Inject the CSS and the corner shapes into the page
st.markdown(page_bg, unsafe_allow_html=True)
st.markdown('<div class="bg-shape-blue"></div>', unsafe_allow_html=True)
st.markdown('<div class="bg-shape-pink"></div>', unsafe_allow_html=True)

def main():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    # Title and subtitle with black headings
    st.markdown('<div class="title-text">✔ Interview Analyzer</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle-text">'
        'Generate Job Descriptions, Interview Questions and get an in-depth Interview Analysis.'
        '</div>', 
        unsafe_allow_html=True
    )
    
    # Using a form for user inputs with mandatory fields marked with an asterisk (*)
    with st.form(key="job_details_form"):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Job Title *", help="Enter the job title.")
            company_industry = st.text_input("Company or Industry *", help="e.g., 'FinTech startup' or 'E-commerce'")
            location = st.text_input("Job Location *", help="City, state or region.")
            employment_type = st.text_input("Employment Type *", help="e.g., Full-time, Part-time, Contract")
        with col2:
            experience = st.text_input("Experience Level *", help="e.g., Entry-level, Mid-level, Senior")
            salary_benefits = st.text_input("Salary Range & Benefits", help="Optional: Specify salary details")
            company_overview = st.text_area("Company Culture & Mission", help="Optional: Brief info about company culture")
        
        responsibilities = st.text_area("Responsibilities *", help="List the main responsibilities")
        skills_qualification = st.text_area("Required Skills & Qualifications *", help="List the essential skills/qualifications")
        preferred_skills = st.text_area("Preferred Qualifications", help="List any preferred skills/qualifications")
        
        submit_button = st.form_submit_button(label="Generate Analysis")
    
    if submit_button:
        # Check for mandatory fields
        if not (title and company_industry and location and employment_type and experience and responsibilities and skills_qualification):
            st.error("Please fill in all mandatory fields marked with *")
        else:
            # Build prompt by including only non-empty fields
            details = []
            if title:
                details.append(f"Job Title = {title}")
            if company_industry:
                details.append(f"Company or Industry = {company_industry}")
            if location:
                details.append(f"Location = {location}")
            if employment_type:
                details.append(f"Job Type = {employment_type}")
            if experience:
                details.append(f"Experience = {experience}")
            if responsibilities:
                details.append(f"Responsibilities = {responsibilities}")
            if skills_qualification:
                details.append(f"Skills and Qualification = {skills_qualification}")
            if preferred_skills:
                details.append(f"Preferred Skills or Qualifications = {preferred_skills}")
            if salary_benefits:
                details.append(f"Salary and Benefits = {salary_benefits}")
            if company_overview:
                details.append(f"Company Overview = {company_overview}")
            
            prompt = (
                "Create a brief job description for a post like LinkedIn or Indeed job posts, "
                "according to the details given below:\n" + ",\n".join(details)
            )
            
            with st.spinner("Generating job description..."):
                job_description = jd_create(prompt)
            with st.spinner("Generating Interview Questions..."):
                questions = questions_create(job_description)
            with st.spinner("Generating Interview Transcript..."):
                transcript = transcript_create(questions)
            with st.spinner("Analyzing Interview Performance..."):
                analysis = analyses_scoring(job_description, transcript)
            
            # Display final analysis without an extra container box
            st.subheader("Final Interview Analysis & Score")
            st.write(analysis)
            
            # Expanders to show/hide detailed sections
            with st.expander("Show Job Description"):
                st.text_area("Job Description", job_description, height=250)
            with st.expander("Show Interview Questions"):
                st.text_area("Interview Questions", questions, height=200)
            with st.expander("Show Interview Transcript"):
                st.text_area("Interview Transcript", transcript, height=300)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
