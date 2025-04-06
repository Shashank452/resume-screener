import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def load_resumes(resume_folder):
    resumes = {}
    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf"):
            path = os.path.join(resume_folder, filename)
            text = extract_text_from_pdf(path)
            resumes[filename] = text
    return resumes
