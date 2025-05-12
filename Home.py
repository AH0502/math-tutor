import streamlit as st 

st.set_page_config()

st.title("Home")
st.logo('./Images/logo2.png', size='large' )

st.image("./Images/logo2.png", )

st.markdown("## About")
st.markdown("Math Tutor Smart Assistant (MTSA) is an open-source web application designed to help students struggling in mathematics courses. " \
"Many students may not have the means or time to meet with a tutor, MTSA seeks to meet their needs.")

st.markdown(
    """
    ## Instructions
    1. Go to *Settings*
    2. Enter profile information
    3. Save your changes
    4. Select model and enter OpenAI API Key
    5. Save model settings
    """)

st.markdown("## Demo")
st.video("./Images/demo1.mov")

