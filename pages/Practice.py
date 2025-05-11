import streamlit as st

st.title("Practice")

while True:

    if 'user' in st.session_state:
        user = st.session_state.user
        st.markdown(f"## Welcome {user.name}!")
        break

    else:
        st.markdown("## Please complete profile information.")

with st.form("practice"):
    # Checkbox to practice based on user courses.