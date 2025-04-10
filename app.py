from dotenv import load_dotenv
import streamlit as st
import os
import PyPDF2 as pdf
import google.generativeai as genai

# Load environment variable
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# === Apply Custom CSS for UI Styling ===
def apply_custom_styles():
    st.markdown("""
        <style>
            body {
                background-color: #f0f2f6;
            }
            .main {
                background-color: #ffffff;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
            }
            h1, h2, h3 {
                color: #1f2937;
            }
            .stTextArea textarea {
                font-size: 16px;
            }
            .stFileUploader {
                padding-top: 1rem;
            }
            .uniform-button button {
                width: 100% !important;
                height: 3em;
                font-size: 1rem;
                background-color: #2563eb;
                color: white;
                border-radius: 8px;
                font-weight: bold;
                transition: 0.3s ease;
            }
            .uniform-button button:hover {
                background-color: #1d4ed8;
            }
        </style>
    """, unsafe_allow_html=True)

# === PDF Text Extraction ===
def extract_text_from_pdf(upload_file):
    if upload_file is not None:
        reader = pdf.PdfReader(upload_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        if not text.strip():
            raise ValueError("No readable text found in the uploaded PDF.")
        return [text]
    else:
        raise FileNotFoundError("No file uploaded.")

# === Gemini API Call ===
def get_gemini_response(input_prompt, pdf_text, job_description):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([input_prompt, pdf_text[0], job_description])
    return response.text

# === Streamlit App Setup ===
st.set_page_config(page_title="ATS Resume Checker", layout="centered")
apply_custom_styles()
st.markdown("<div class='main'>", unsafe_allow_html=True)

# === Header ===
st.markdown("## :mag: ATS Resume Scanning System")
st.markdown("Upload your resume and get professional feedback based on your job description.")

# === Inputs ===
input_text = st.text_area("📄 Job Description: ", key="input")
uploaded_file = st.file_uploader("📎 Upload Your Resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ PDF Uploaded Successfully")

# === Button Section with Uniform Size ===
st.markdown('<div class="uniform-button">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    submit3 = st.button("📊 Percentage Match", key="match", use_container_width=True)
with col2:
    submit1 = st.button("🧾 Tell me About the Resume", key="about", use_container_width=True)
with col3:
    submit2 = st.button("🛠️ How can I Improve my Skill", key="improve", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# === PROMPTS (Unchanged, as you requested) ===

input_prompt1 = """
You are an experienced HR professional with deep technical knowledge across various domains including SOFTWARE DEVELOPMENT, DATA SCIENCE, FULL STACK, WEB DEVELOPMENT, BIG DATA ENGINEERING, CLOUD COMPUTING, DEVOPS, DATA ANALYTICS, MACHINE LEARNING, ARTIFICIAL INTELLIGENCE, CYBERSECURITY, and more.
Your task is to thoroughly review the candidate's resume against a provided job description from any technical field.
Evaluate whether the candidate aligns with the job role, highlight their strengths, and point out areas where they fall short.
Provide a professional summary of your findings in an HR-friendly tone.
"""

input_prompt2 = """
You are a skilled technical mentor and career advisor with expertise in all major technical fields including SOFTWARE DEVELOPMENT, DATA SCIENCE, MACHINE LEARNING, FULL STACK, FRONTEND/BACKEND, DEVOPS, BIG DATA, CLOUD, CYBERSECURITY, BLOCKCHAIN, and more.
Your task is to analyze the candidate's resume and suggest practical, role-specific improvements to help them upskill.
List out any missing skills, tools, certifications, or experiences that could make them a stronger candidate in their field.
Recommend suitable learning resources, online courses, or project ideas tailored to the job roles they are interested in.
"""

input_prompt3 = """
You are an intelligent ATS (Applicant Tracking System) scanner and technical evaluator with deep knowledge across all technology domains including DATA SCIENCE, SOFTWARE DEVELOPMENT, FULL STACK, DEVOPS, CLOUD COMPUTING, AI/ML, CYBERSECURITY, DATA ENGINEERING, and more.
Evaluate the candidate's resume against the provided job description and provide a percentage match that reflects how closely they align.
Start with a percentage score.
Then list the important **keywords/skills missing** from the resume.
End with **final thoughts** on what the candidate could do to improve their chances for this role.
Be precise, role-specific, and concise in your analysis.
"""

# === Button Logic ===
if submit1:
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_text, input_text)
        st.subheader("🧾 Resume Overview:")
        st.write(response)
    else:
        st.warning("⚠️ Please Upload the Resume")

elif submit2:
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_text, input_text)
        st.subheader("🛠️ Skill Improvement Suggestions:")
        st.write(response)
    else:
        st.warning("⚠️ Please Upload the Resume")

elif submit3:
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_text, input_text)
        st.subheader("📊 ATS Match Percentage and Insights:")
        st.write(response)
    else:
        st.warning("⚠️ Please Upload the Resume")

st.markdown("</div>", unsafe_allow_html=True)
