import streamlit as st

st.markdown("<u><h2>C V Analysis using <span style='color:red'>AI and Machine Learning</span></h2></u>",unsafe_allow_html=True)
st.markdown("<h3><u>About Us</u></h3>",unsafe_allow_html=True)
st.logo("cv.png",size="large")
st.markdown("An AI CV analysis project automates resume screening by extracting candidate data, matching qualifications against job descriptions, and scoring candidates. Using Large Language Models (LLMs) and Optical Character Recognition (OCR), it highlights missing skills, formats JSON output, and ranks top talent to streamline the hiring process")
st.subheader("Key Project Features")
st.markdown("Document Parsing: Extracts raw text and structure from uploaded CV PDFs using OCR or libraries like PyPDF2.Semantic Keyword Matching: Uses text embeddings and cosine similarity (e.g., via OpenAI or HuggingFace) to score how closely a CV aligns with specific job requirements.AI-Driven Gap Analysis: Feeds the CV and job description into an LLM (like Google Gemini or GPT-4) to generate a customized match score, summarize strengths, and pinpoint missing skills.Structured Analytics: Outputs data into clean dashboards or spreadsheets (like Google Sheets) for HR teams to easily evaluate candidates")
st.subheader("Python packages")
st.code("import os")
st.code("from fastapi import FastAPI, UploadFile, File, Form, HTTPException")
st.code("from pydantic import BaseModel, Field")



