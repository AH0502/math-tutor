import streamlit as st 
import src.utils


st.title("🧑‍🏫 Math Tutor ")


with st.form("main"):   
    api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    file = st.file_uploader("Upload notes or homework:", type=['jpg', 'jpeg', 'png', 'pdf'])
    text = st.text_area("Enter tutor prompt:")
    submitted = st.form_submit_button()

if file is not None and submitted and file.type != 'application/pdf':

    llm = src.utils.get_llm(api_key=api_key)

    with st.spinner("Thinking"):
        response = src.utils.process_jpeg(file, text, llm)
        st.success("Response:")
        st.markdown(response.content)


elif file is not None and file.type == 'application/pdf':

    llm = src.utils.get_llm(api_key)

    with st.spinner("Thinking"):
        response = src.utils.process_pdf(file, text, llm)
        st.success("Response:")
        st.markdown(response.content, unsafe_allow_html=True)
        st.code(response.content)
