import requests
import streamlit as st
import os
from constant import *


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


local_css("style/style.css")

st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)

st.title("📝 ASTRONOMY PICTURE OF THE DAY!!!")

ASTRO_KEY = os.getenv("ASTRO_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={ASTRO_KEY}"
response = requests.get(url)
content = response.json()

if 'title' in content:
    st.markdown(f"<h1 style='text-align: center;'>{content['title']}</h1>", unsafe_allow_html=True)

# Check if the 'url' key exists and if the URL is a YouTube URL
if 'url' in content and 'youtube' in content['url']:
    # Display the video
    st.video(content['url'])
elif 'url' in content:
    # Display the image
    st.image(image=content['url'])

if 'explanation' in content:
    st.write(content['explanation'])

# Check if 'copyright' key exists in the content
if 'copyright' in content:
    st.markdown(f"<p style='text-align: right;'><i>{content['copyright']}</i></p>", unsafe_allow_html=True)