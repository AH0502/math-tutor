import streamlit as st
from src.User import User

st.title("Settings 🛠️")
st.logo('./Images/logo2.png', size='large')

profile_tab, courses_tab, model_tab = st.tabs(["Profile", "Courses", "Model"])

st.session_state.user = User('', '', ) 

with profile_tab:
    with st.form("Profile"):
        name = st.text_input("Name:")
        email = st.text_input("Email Address:")
        dob = st.date_input("Date of Birth:", min_value='1925-05-11', max_value='today')
        education = st.selectbox("Education", ["Middle School", "High School", "Undergraduate", "Graduate"])
        submitted = st.form_submit_button("Save")
        if submitted:
            st.session_state.user = User(name, email, dob, education, []) 
            st.success("Saved")

with courses_tab:
    with st.form("courses"):
        course = st.text_input("Enter course:")
        submitted = submitted = st.form_submit_button("Add")
        if submitted:
            st.session_state.user.add_course(course)
            st.success("Course added")

    if st.session_state.user.courses == ['']:
        st.markdown("There are no courses to display")

    else:
            st.markdown("Current Courses:")
            for i, course in enumerate(st.session_state.user.courses, start=1):
                st.markdown(f"{i}. {course}")


with model_tab:
    with st.form("Model Settings"):
        model = st.selectbox("Model", ["GPT-4o", "GPT-3-Turbo"])
        api_key = st.text_input("OpenAI API Key:", type="password")
        submitted = st.form_submit_button("Save")
        if submitted:
            st.session_state.api_key = api_key
            st.success("Saved")




