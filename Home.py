import streamlit as st 

st.set_page_config()

st.title("Home")
st.logo('./Images/logo2.png', size='large' )

st.image("./Images/logo2.png", )

st.markdown("## About")
st.markdown("Math Tutor Smart Assistant (MTSA) is an open-source web application designed to help students struggling in mathematics courses. " \
"Many students may not have the means or time to meet with a tutor, MTSA seeks to meet their needs.")


st.markdown("## Demo")
st.video("./Images/demo1.mov")