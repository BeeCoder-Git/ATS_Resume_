Here’s a clean and informative `README.md` for your **ATS Resume Checker** project using **Streamlit** and **Gemini API**:

---

# 🧠 ATS Resume Checker

A powerful web application built using **Streamlit** and **Google Gemini Pro API** that helps job seekers analyze their resume against any job description. The app simulates the behavior of an **HR Professional**, **Technical Mentor**, and **ATS Scanner** to evaluate resumes, suggest improvements, and estimate job-fit percentage.

---

## 🚀 Features

- ✅ Upload your resume in PDF format.
- 📝 Paste the job description you're applying for.
- 🤖 Choose one of the following analyses:
  - **Tell Me About the Resume** – HR-style feedback.
  - **How Can I Improve My Skill** – Skill gap analysis and upskilling suggestions.
  - **Percentage Match** – ATS-style match percentage and missing keywords.
- 🧠 Uses Google's Gemini 1.5 Pro for intelligent content generation.
- 📷 Converts the first page of the PDF into an image to be processed as input.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Model**: [Google Gemini 1.5 Pro](https://ai.google.dev/)
- **PDF Handling**: `pdf2image`, `Pillow`
- **Environment Management**: `python-dotenv`

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ats-resume-checker.git
cd ats-resume-checker
```

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

### 3. Set Your API Key

Create a `.env` file in the root folder and add your Gemini API key:

```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---

## 📄 Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

1. Enter or paste a job description in the text area.
2. Upload your resume in PDF format.
3. Click one of the three buttons to get feedback:
   - Tell Me About the Resume
   - How Can I Improve My Skill
   - Percentage Match

---

## 🧠 How It Works

- **Resume Parsing**: Only the **first page** of the resume is converted into an image using `pdf2image`.
- **Base64 Encoding**: The image is base64 encoded and sent to the Gemini model as part of the input.
- **Prompt Engineering**: Carefully crafted prompts simulate expert personas (HR, mentor, ATS).
- **Gemini Response**: The model returns detailed text responses, rendered directly in Streamlit.

---

## 📂 Project Structure

```
.
├── app.py                  # Main Streamlit app
├── .env                    # API key (not included in repo)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## ✅ Requirements

- Python 3.8+
- Google Gemini API key
- Poppler installed (for `pdf2image` to work properly)

### On Ubuntu:

```bash
sudo apt-get install poppler-utils
```

### On Windows:

- Download Poppler from [http://blog.alivate.com.au/poppler-windows/](http://blog.alivate.com.au/poppler-windows/)
- Add its `/bin` folder to your system PATH.

---

## 📌 TODO / Improvements

- Parse full PDF content, not just the first page.
- Add multi-page PDF handling.
- Highlight matched/missing keywords visually.
- Add support for DOCX/RTF resumes.

---

## 📄 License

MIT License. Free to use and modify.

---
