import streamlit as st
from PIL import Image
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

import streamlit as st
import pandas

col1, col2 = st.columns(2)
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

with col1:
    st.image("fulllogo.png", width=350)

with col2:
    st.title("Phuc Le's Projects")
    st.markdown(
        "**Below you can find some of the apps I have built in Python and Source Code in Github, feel free to contact "
        "me!**")



col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=",")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        image_path = f'images/{index+1}.png'
        st.image(image=image_path, width=500)
        st.markdown(f"<a style=\"color:red;\" href=\"{row['url']}\"><b>SOURCE CODE</b></a>", unsafe_allow_html=True)
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'], width=400)
        st.markdown(f"<a style=\"color:red;\" href=\"{row['url']}\"><b>SOURCE CODE</b></a>", unsafe_allow_html=True)

