# Interview Analyzer

**Interview Analyzer** is a Streamlit-based application that automates the creation of professional job descriptions, interview questions, interview transcripts, and detailed interview performance analysis using AI. Designed for recruiters and HR professionals, this tool streamlines the interview preparation and evaluation process.

---

## Features

- **Job Description Generation**: Automatically creates structured, compelling job descriptions based on user-provided details.
- **Interview Questions Creation**: Generates role-specific, insightful interview questions.
- **Detailed Analysis**: Provides in-depth analysis including scores and conclusions based on the generated content.
- **Modern UI**: Clean, white-themed interface with mandatory field validation and expandable sections for detailed outputs.
- **Unicode Support**: Ensures robust file handling with UTF-8 encoding, supporting all Unicode characters.

---

## Prerequisites

- **Python 3.10+** (or your preferred Python version)
- A valid API key for the AI service (to be set as `OPEN_ROUTER_API_KEY`)

---

## Installation

1. **Clone the Repository**  
   Open your terminal and run:  
   `git clone https://github.com/AzharAli5/Interview-Analyzer.git`  
   Then, navigate into the project directory:  
   `cd Interview-Analyzer`

2. **Create a Virtual Environment**  
   For **Windows**:  
   `python -m venv venv`  
   `venv\Scripts\activate`  
   For **macOS/Linux**:  
   `python3 -m venv venv`  
   `source venv/bin/activate`

3. **Install Dependencies**  
   Install the required packages using:  
   `pip install -r requirements.txt`  
   *(Ensure your `requirements.txt` includes packages such as streamlit, python-dotenv, and the appropriate AI package.)*

4. **Configure the API Key**  
   Create a file named `.env` in the root directory and add your API key:  
   `OPEN_ROUTER_API_KEY=your_api_key_here`  
   Replace `your_api_key_here` with your actual API key.

---

## Running the Application

Launch the Streamlit app with the following command:  
`streamlit run app.py`  
This will open the application in your default web browser.

