import streamlit as st
import time
p=st.progress(0,"Wait for Loading ....")
for i in range(1,100):
       time.sleep(0.05)
       p.progress(i,"Loading....")
p.empty()
       
st.balloons()

st.header("C V Analysis using AI and Machine Learning")
st.image("bg.png")
st.logo("cv.png",size="large")
st.subheader("Key Project Features")
st.success("Document Parsing: ")
st.write("Extracts raw text and structure from uploaded CV PDFs using OCR or libraries like PyPDF2.Semantic Keyword Matching: Uses text embeddings and cosine similarity (e.g., via OpenAI or HuggingFace) to score how closely a CV aligns with specific job requirements.AI-Driven Gap Analysis: Feeds the CV and job description into an LLM (like Google Gemini or GPT-4) to generate a customized match score, summarize strengths, and pinpoint missing skills.Structured Analytics: Outputs data into clean dashboards or spreadsheets (like Google Sheets) for HR teams to easily evaluate candidates")

