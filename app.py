import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- UI ---

st.title("🧠 AI-Powered Resume Screening System")
st.write("Upload a candidate's resume and compare it to the job description below.")

# --- Resume Upload ---
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

# --- Job Description Input ---
st.subheader("📌 Job Description")
job_description = st.text_area("Paste the job description here:", height=200, value="""
We are seeking a passionate and motivated Python Developer (Fresher) with a strong foundation in Artificial Intelligence and Machine Learning. The ideal candidate should be proficient in Python programming and have hands-on experience in web development using Flask, as well as machine learning tools like TensorFlow and OpenCV. Responsibilities include developing scalable ML-based applications, building backend systems using Flask, and working with tools like Pandas, NumPy, and Matplotlib. Knowledge of frontend technologies such as HTML, CSS, and JavaScript is a plus. Experience with real-time projects like facial emotion detection, online fraud detection, and chat applications will be highly valued. Candidates should be team players with good time management, communication, and problem-solving skills. A degree in AI & ML or Computer Science is required.
""")

# --- Function to Extract Text from Resume PDF ---
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

# --- Compare Resume and JD ---
def get_match_score(resume_text, jd_text):
    texts = [resume_text, jd_text]
    cv = CountVectorizer().fit_transform(texts)
    similarity = cosine_similarity(cv[0:1], cv[1:2])
    return round(float(similarity[0][0]) * 100, 2)

# --- Main Logic ---
if uploaded_file and job_description.strip():
    resume_text = extract_text_from_pdf(uploaded_file)
    
    if resume_text.strip():
        match_score = get_match_score(resume_text, job_description)
        st.success(f"✅ Match Score: **{match_score}%**")
        st.markdown("The match score represents how similar the resume is to the job description.")
        
        with st.expander("🔍 View Extracted Resume Text"):
            st.text(resume_text)
    else:
        st.error("Could not extract any text from the uploaded PDF.")
