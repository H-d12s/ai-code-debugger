import streamlit as st
from debugger import debug_code

st.title("AI Code Debugger")

code = st.text_area("Paste your code here", height=300)
language = st.selectbox("Select language", ["Python", "JavaScript", "C++"])

if st.button("Debug"):
    if code:
        result = debug_code(code, language)
        st.markdown(result)