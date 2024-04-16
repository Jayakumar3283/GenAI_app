from openai import OpenAI
import streamlit as st


f = open('API_key\.openai_key.txt')
OPENAI_API_KEY = f.read()
client = OpenAI(api_key = OPENAI_API_KEY)

st.title("Gen AI : A Code Correction using AI")

prompt = st.text_input("User input")

def chat_bot(prompt):

    st.snow()
    response = client.chat.completions.create(
                      model="gpt-3.5-turbo-16k-0613",
                      messages=[
                        {"role": "system", "content": """You are a teaching assistant for students .. 
                         you are need to explain and fix the bugs and explain student where he is done mistakes
                                        """},
                        {"role": "user", "content": prompt}
                      ]
                )
    return response.choices[0].message.content
if st.button("Code Fixer"):

    st.write(chat_bot(prompt))