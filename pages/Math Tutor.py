import streamlit as st 
import src.utils
from pages.Settings import api_key

st.title("Math Tutor")
st.logo('./Images/logo2.png', size='large')

with st.form("tutor"):   
    file = st.file_uploader("Upload notes or homework:", type=['jpeg', 'pdf'])
    text = st.text_area("Enter tutor prompt:")
    submitted = st.form_submit_button()

if file is not None and submitted and file.type != 'application/pdf':

    llm = src.utils.get_llm(st.session_state.api_key)

    with st.spinner("Thinking"):
        response = src.utils.process_jpeg(file, text, llm)
        st.success("Response:")
        st.markdown(response.content)


elif file is not None and file.type == 'application/pdf':

    llm = src.utils.get_llm(st.session_state.api_key)

    with st.spinner("Thinking"):
        response = src.utils.process_pdf(file, text, llm)
        st.success("Response:")
        st.markdown(response.content, unsafe_allow_html=True)
        st.code(response.content)
