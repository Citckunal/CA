import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["ojt2"]
my=mydb["student"]

st.header("📊 CV Analysis using AI and ML")
st.subheader("👤 SignIn")
st.logo("cv.png",size="large")
with st.form("SignIn"):
       t1=st.text_input("👤User name")
       t2=st.text_input("🔒 Password",type="password")
       if st.form_submit_button("SignIn"):
              if not t1 or not t2:
                     st.error("Fill The Fields!!!")
              else:
                     res=my.find({"username":t1,"password":t2})
                     v=0
                     for data in res:
                            v=v+1
                            st.session_state["username"]=data['username']
                            st.session_state["password"]=data['password']
                            st.session_state["img"]=data['photo']
                            
                            st.switch_page("pages/profile.py")
                     if v==0:
                            st.error("Invalid Login Details")
                     
                     
                     
