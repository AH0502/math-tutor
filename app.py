import streamlit as st 
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.schema import HumanMessage
from PIL import Image
import io
from base64 import b64encode
import tempfile



st.title("🧑‍🏫 Math Tutor ")

# Need to make form field here to enter API Key

with st.form("main"):   
    file = st.file_uploader("Upload notes or homework:", type=['jpg', 'jpeg', 'png', 'pdf'])
    text = st.text_area("Enter tutor prompt:")
    submitted = st.form_submit_button()

if file is not None and submitted and file.type != 'application/pdf':
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
elif file is not None and file.type == 'application/pdf':

    with tempfile.NamedTemporaryFile(delete=False, suffix="pdf") as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    loader = PyMuPDFLoader(tmp_path)

    pages = loader.load()

    pdf_data = "\n".join([page.page_content for page in pages])

    llm = ChatOpenAI(
    model='gpt-4o',
    temperature=0
    )

    messages = [
        HumanMessage(content=[
            {"type": "text", "text": text},
            {"type": "text", "text": pdf_data}
        ])
    ]
    with st.spinner("Thinking"):
        response = llm.invoke(messages)
        st.success("Response:")
        st.write(response.content)

