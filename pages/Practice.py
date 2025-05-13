import streamlit as st
from src import utils
from langchain.schema import SystemMessage

st.title("Practice")
st.logo('./Images/logo2.png', size='large')

user = st.session_state.get('user', None)
api_key = st.session_state.get("api_key", None)

if 'user' in st.session_state and st.session_state.user.name != '':

    st.markdown(f"## Welcome {user.name}!")

else:
    st.markdown("## Please complete profile information.")

with st.form("practice"):
    choices = st.multiselect("Select practice courses:", user.courses)
    difficulty = st.select_slider("Difficulty", ["Easy", "Moderate", "Hard"])
    num_of_problems = st.slider("Number of Problems", step=1, min_value=1, max_value=10)
    submitted = st.form_submit_button()

llm = utils.get_llm(api_key)
message = [SystemMessage(
    content=f"""
    You are a math tutor. You are to generate practice problems for {user.name}. {user.name} is currently a 
    {user.education} student who is taking the following courses: {user.courses}. Generate the problems appropriate to their education
    level and age. {user.name} was born on {user.dob}. 
    Generate {num_of_problems} practice problem(s) for the following courses: {choices} with a difficulty level of {difficulty}
    Generate four possible answers in quiz form: a), b), c), d). Don't say the answer.
    Give the problems and say nothing else.
    """
)]

if submitted:
    with st.spinner("Generating problems"):
        response = llm.invoke(message)
        st.success("Done")

    st.markdown(response.content)