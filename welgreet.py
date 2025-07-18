import streamlit as st

st.set_page_config(page_title="Greeting App", layout="centered")

st.title("Welcome!")
name = st.text_input("Enter your name:")

if name:
    st.markdown(f"Hi user {name}!")
