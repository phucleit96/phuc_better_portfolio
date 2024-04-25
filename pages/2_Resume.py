import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

st.title("📝 Resume & Transcript")
st.write("[Click here if my Resume's blocked by your browser](https://drive.google.com/file/d/1oeo9kq8YMtlcmfeZ-NII5VVCHhQ_ee_y/view?usp=sharing)")
st.write("[Click here if my Transcript's blocked by your browser](https://drive.google.com/file/d/14dm6myh8RWncmxk1sn5K0v2PxO_JXbEX/view?usp=sharing)")
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def write_pdf_to_page(file_path):
    bin_str = get_base64_of_bin_file(file_path)
    st.markdown(f'<iframe src="data:application/pdf;base64,{bin_str}" width="100%" height="800" type="application/pdf"></iframe>', unsafe_allow_html=True)

write_pdf_to_page("images/resume_better.pdf")
  
