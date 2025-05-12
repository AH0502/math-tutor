import streamlit as st

st.title("Practice")
st.logo('./Images/logo2.png', size='large')



if 'user' in st.session_state and st.session_state.user.name != '':
    user = st.session_state.user
    st.markdown(f"## Welcome {user.name}!")
    

else:
    st.markdown("## Please complete profile information.")

#with st.form("practice"):
    # Checkbox to practice based on user courses.