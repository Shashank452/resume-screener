# 🧠 AI-Powered Resume Screening System

An intelligent resume shortlisting tool developed using **Machine Learning** and **NLP** to help recruiters and HR teams quickly assess the suitability of candidates for specific roles.

---

## 📌 Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Project Structure](#project-structure)
- [System Requirements](#system-requirements)
- [Tech Stack Used](#tech-stack-used)
- [How to Run the Project](#how-to-run-the-project)
- [Features](#features)
- [Future Enhancements](#future-enhancements)
- [Contact](#contact)

---

## 📖 Introduction

With the increasing number of job applicants, manual resume screening becomes time-consuming and inefficient. This AI-powered system simplifies the process by extracting the content of resumes, comparing it with the job description using cosine similarity, and providing a match score that helps recruiters identify the best-fit candidates faster.

---

## ❓ Problem Statement

> **Manual resume screening is inefficient, error-prone, and time-consuming.**

This project addresses the need for automating resume screening by:
- Extracting useful text from resumes in PDF format.
- Comparing resumes to job descriptions based on relevant keywords and skills.
- Ranking resumes based on how well they match the role.

---

## 📂 Project Structure

```bash
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── sample_resumes/ # Sample resume PDFs for testing (optional)
└── utils/ # Utility functions (optional for future enhancement)
```

---

## 💻 System Requirements

- Python 3.8 or later
- Web browser (Chrome/Firefox)
- Internet connection (for using Streamlit Cloud)

---

## 🔧 Tech Stack Used

| Component         | Technology               |
|------------------|--------------------------|
| Programming Lang | Python                   |
| UI Framework     | Streamlit                |
| PDF Processing   | PyPDF2                   |
| NLP/Similarity   | Scikit-learn (CountVectorizer, Cosine Similarity) |
| Text Extraction  | PDF Parsing              |
| Hosting (Optional) | Streamlit Cloud / Localhost |

---

## ▶️ How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/resume-screening-app.git
cd resume-screening-app
```

### 2. Install Dependencies

### 3. Run the App

### 4. Upload Resume & Paste JD

- Upload any PDF resume
- Paste the Job Description
- View the match score and resume details

---

## ✨ Features

- Upload resume in PDF format
- Paste or input job description
- Extract text automatically from resume
- Calculate match score using cosine similarity
- Display full extracted resume content for verification

---

## 🚀 Future Enhancements

- Extract specific details: name, email, skills, education
- Highlight matching keywords between resume & JD
- Rank multiple resumes in batch upload
- Add support for DOCX or TXT resumes
- Use deep learning (BERT) for semantic matching
- Add an admin dashboard for HR users

---

## 📬 Contact
Internship Project @ GTTC Magadi, Feel free to reach out for queries or collaboration:
- Author: [Shashanka C K](mailto:shashankcks2002@gmail.com)  
- GitHub: [Shashank452](https://github.com/Shashank452)  
- LinkedIn: [Shashanka C K](https://www.linkedin.com/in/shashanka-c-k)
