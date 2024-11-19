import streamlit as st
import pandas as pd

st.title("hello word")
st.header("Hello GG")

st.image('./img/patcharapong.jpg')
st.subheader("Patcharapong Titivanich")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))