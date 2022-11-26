import streamlit as st
from datetime import date

st.title("Hello Streamlit App")

st.header("My name is Veton and this is my first deployed app")

today = date.today()
st.write(today)