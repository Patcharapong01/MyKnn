import streamlit as st
import pandas as pd

st.title("hello")
st.header("hello")

st.image('./img/patcharapong.jpg')
st.subheader("Patcharapong Titivanich")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลส่วนตัว")