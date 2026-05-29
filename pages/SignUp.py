'''
Q.Create a online student signup form using streamlit componets like:-
i)text_input
ii)text_area
iii)selectbox
iv)date_input
v)file_uploader
vi)radio
vii)slider
viii)checkbox
ix)button

'''
import streamlit as st
import pymongo
import random
conn=pymongo.MongoClient("mongodb+srv://kunalg15_db_user:UchdhJoflEo7GMli@citcapp.mong26u.mongodb.net/?appName=CitcApp")

mydb=conn["ojt2"]
my=mydb["student"]

st.header("C V Analysis using AI and Machine Learning")
st.subheader("📝 SignUp")
st.logo("cv.png",size="large")
c1,c2,c3=st.columns(3)
with st.form("SignUp Form"):
       username=st.text_input("Username 👨‍💼")
       password=st.text_input("🔑 Password ",type="password" )
       address=st.text_area("Address")
       course=st.selectbox("Select Your Course",["B.SC CA","B.SC IT","B.SC CS"])
       dob=st.date_input("Dob")
       photo=st.file_uploader("Upload Your Picture 📩")
       mobile=st.text_input("Mobile Number 📞")
       gender=st.radio("Gender",['M','F'])
       age=st.slider("Age",16,28)
       st.write("Languages Known")
       l1=st.checkbox("Hindi")
       l2=st.checkbox("English")
       l3=st.checkbox("Nagpuri")
       live_photo=st.camera_input("Upload Your Live Picture")
       count=random.randrange(1,10)
       str1="img"
       str1=str1+str(count)
       str1=str1+".png"
       count=count+1
       if live_photo:
              with open(str1,"wb") as f:
                            f.write(live_photo.getvalue())


       if st.form_submit_button("SignIn"):
              my.insert_one({"username":username,"password":password,"address":address,"course":course,"dob":str(dob),"mobileno":mobile,"gender":gender,"age":age,"photo":str1})
              st.success("SIGN UP SYCCESSFULLY ✅")






