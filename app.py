import streamlit as st 
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from PIL import Image
import io
from base64 import b64encode


st.title("🧑‍🏫 Math Tutor ")

# Need to make form field here to enter API Key

with st.form("main"):   
    file = st.file_uploader("Upload notes or homework:", type=['jpg', 'jpeg', 'png', 'pdf'])
    text = st.text_area("Enter tutor prompt:")
    submitted = st.form_submit_button()

if file is not None and submitted:
    image = Image.open(file)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_b64 = b64encode(buffered.getvalue()).decode()
    

    llm = ChatOpenAI(
        model='gpt-4o',
        temperature=0
    )

    messages = [
        HumanMessage(content=[
        {"type": "text", "text": text},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}  
    ])
    ]

    with st.spinner("Thinking"):
        response = llm.invoke(messages)
        st.success("Response:")
        st.write(response.content)






