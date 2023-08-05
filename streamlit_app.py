import streamlit as st

st.header('st.write')

dict = {"apple":"red", "lemon":"yellow"}
list = ["ogami", "akinobu", "kana", "ryo"]

st.subheader('dict')
st.write(dict)

st.subheader('list')
st.write(list)

st.subheader('markdown')
st.write('Hello, *World!* emoji')

a = 45
b = 1234
st.subheader('number')
st.write(12)
st.write(123.4567)
st.write(a+b)
