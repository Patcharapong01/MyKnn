import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

st.header("โปรเจ็คการจำเเนกข้อมูลดอกไม้")
st.image("./img/patcharapong")

dt=pd.read_csv('./data/iris-3.csv')
st.subheader('ข้อมูลดิบของ iris')
st.write(dt.head(10))

st.subheader('การจำเเนกข้อมูลใหม่')

