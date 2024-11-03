# streamlit
import streamlit as st


with st.sidebar:
    st.title("Welcome")
    st.sidebar.markdown("---")
    files = st.file_uploader("Upload Data files.", accept_multiple_files=True)


st.markdown("### Hello World!")