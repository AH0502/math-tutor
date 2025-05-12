from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.tools.e2b_data_analysis.tool import UploadedFile
import streamlit as st
import io
from base64 import b64encode
from PIL import Image
import tempfile


def get_llm(api_key: str):
    return ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        api_key=api_key
    )

def process_jpeg(file, text, llm:ChatOpenAI):
    image = Image.open(file)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_b64 = b64encode(buffered.getvalue()).decode()

    messages = [
        SystemMessage(content=( "You are a helpful math tutor. Your output must be in markdown.")),

        HumanMessage(content=[
        {"type": "text", "text": text},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}  
        ])

    ]
    return llm.invoke(messages)

def process_pdf(file: UploadedFile, text: str, llm: ChatOpenAI):
        
    with tempfile.NamedTemporaryFile(delete=False, suffix="pdf") as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    loader = PyMuPDFLoader(tmp_path)

    pages = loader.load()

    pdf_data = "\n".join([page.page_content for page in pages])

    messages = [
        HumanMessage(content=[
            {"type": "text", "text": text},
            {"type": "text", "text": pdf_data}
        ])
    ]

    return llm.invoke(messages)
