import streamlit as st
from src.User import User

st.title("Settings 🛠️")
st.logo('./Images/logo2.png', size='large')

profile, model = st.tabs(["Profile", "Model"])

with profile:
    with st.form("Profile"):
        name = st.text_input("Name:")
        email = st.text_input("Email Address:")
        dob = st.date_input("Date of Birth:", min_value='1925-05-11', max_value='today')
        education = st.selectbox("Education", ["Middle School", "High School", "Undergraduate", "Graduate"])
        courses = st.text_input("Courses")
        submitted = st.form_submit_button("Save")
        if submitted:
            st.session_state.user = User(name, email, dob, education, courses)
            st.success("Saved")

            # Add functionality for user to add courses.

with model:
    model = st.selectbox("Model", ["GPT-4o", "GPT-3-Turbo"])
    api_key = st.text_input("OpenAI API Key:", type="password")



