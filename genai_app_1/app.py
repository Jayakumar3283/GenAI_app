from openai import OpenAI
import streamlit as st


## read the API key and setup an openai client
f = open('API_key\.openai_key.txt')
OPENAI_API_KEY = f.read()
client = OpenAI(api_key = OPENAI_API_KEY)

st.header('First GenAI app')

## take user InPut
prompt = st.text_input("enter data science topic...")

## if the click on the button, generate responses 

if st.button("generate")==True:

    st.snow()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "system", "content": "Generate 3 data science questions and answers for MCQ test."},
            {"role": "user", "content": prompt }
        ]
    )
    # print the response on webapp
    st.write(response.choices[0].message.content)