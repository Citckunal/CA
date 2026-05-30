import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
st.title("C.V A n a l y z e r")
st.success("User CV")
save_dir = "./uploaded_files"
f1=st.file_uploader("Upload User CV")
file_path = os.path.join(save_dir,f1.name)
with open(file_path,'wb') as f:
        f.write(uploaded_file.getbuffer())
reader =PdfReader(f1)
cv = "".join(page.extract_text() for page in reader.pages)
st.write(cv)

st.success("Job Description")
f2=st.file_uploader("Upload Job Description")
file_path1 = os.path.join(save_dir,f2.name)
with open(file_path1,'wb') as fx:
        fx.write(uploaded_file.getbuffer())
reader1 = PdfReader(f2)
jd = "".join(page.extract_text() for page in reader1.pages)
st.write(jd)

x=CountVectorizer()
matrix=x.fit_transform([jd,cv])

similarity_matrix=cosine_similarity(matrix)
st.write(similarity_matrix)

st.write(str(similarity_matrix[1][0]*100)+'%')





