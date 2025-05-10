import streamlit as st 
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage


st.title("🧑‍🏫 Math Tutor ")

# Need to make form field here to enter API Key

with st.form("main"):   
    file = st.file_uploader("Upload notes or homework:", type=['jpg', 'jpeg', 'png', 'pdf'])
    text = st.text_area("Enter tutor prompt:")
    submitted = st.form_submit_button()

if file is not None and submitted:
    data = file.read()

    llm = ChatOpenAI(
        model='gpt-4o',
        temperature=0
    )

    messages = [
        HumanMessage(content=[
        {"type": "text", "text": text},
        {"type": "image", "image": data}
    ])
    ]

    with st.spinner("Thinking"):
        response = llm.invoke(messages)
        st.success("Response:")
        st.write(response.content)






