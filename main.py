#from transformers import pipeline
#ummerizer=pipeline("summarization",model="t5-base")

#print(summerizer("I made a promise to myself last year 2024 that I will learn programming but so far I have not kept that promise this year 2025, I always quit man, am ashamed about that while my parents see me as their hope from this financial burden we have as a family and I look at myself at that time, seeing myself as a person whose not capable while they see me as their passage. I feel ashamed because they had put so much trust in me and hopes and the investment pushing me to have a better future than her, and I haven’t delivered believe it or not, it is not the first time writing this been writing this for like three years now and nothing has changed, said the same things over and over again. Why I keep this happening is it my goals that are not clear but I have been asking the same thing for like 3 or 4 years now, software engineering. Maybe then I have to change my ways the way I think and how I do things so how do I change the way I think?                                           What do I want to accomplish this year? What do I expect from myself? And I think I have found my purpose and it is to give people other perspectives in life like change the way they think making them aware like educating them changing their minds not by force or being propaganda.",max_length=256, min_length=100, do_sample=False))
import chardet
import string
import streamlit as st
from transformers import pipeline

# --- App title ---
st.title("Web application for summarizing Texts using AI📚 ")
st.write("Enter or paste long text or upload a file below, and let AI summarize it for you!")

# --- Load model once ---
@st.cache_resource
def load_model():
    summarizer = pipeline("summarization", model="t5-base")
    return summarizer

summarizer = load_model()

# --- Text input ---
text = st.text_area("Please enter your text or paste it down below", height=250)

# --- Summary parameters ---
max_len = st.slider("Maximum summary length:", 50, 500, 150)
min_len = st.slider("Minimum summary length:", 20, 200, 50)

# --- Summarize button ---
if st.button("🔍 Summarize"):
   
     if len(text.strip()) == 0:
          st.warning("Please enter some text first.")

     else:
            with st.spinner("Summarizing... please wait"):
               summary = summarizer(text,max_length=max_len,min_length=min_len,do_sample=False)[0]['summary_text']
               st.subheader("🧾 Summary:")
               st.success(summary)
               with open("summarize1.txt","a") as f:
                    f.write(summary+"\n")

               f=open("summarize1.txt","r")
            st.subheader("You summary is also saved on summarize1.txt file")
