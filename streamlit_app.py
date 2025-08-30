import streamlit as st
import requests

st.title("AI-Powered Resume Generator")

name = st.text_input("Enter your name")
job_role = st.text_input("Enter the job role you are applying for")
skills = st.text_area("Enter your skills (comma separated)").split(",")

if st.button("Generate Resume"):
    response = requests.post("http://127.0.0.1:8000/generate_resume/", json={
        "name": name,
        "job_role": job_role,
        "skills": skills
    })
    if response.status_code == 200:
        st.subheader("Generated Resume")
        st.text(response.json()["resume_text"])
    else:
        st.error("Error generating resume. Please check backend.")
