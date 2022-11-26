import streamlit as st
from datetime import date, datetime

st.title("Hello Streamlit App")

st.header("My name is Veton and this is my first deployed app")

today = date.today()
time_now = datetime.now()
st.write(time_now)
st.write(today)