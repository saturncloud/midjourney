import streamlit as st
import pandas as pd
from io import StringIO
import streamlit.components.v1 as components
import numpy as np
from PIL import Image
import os
import requests
from urllib.parse import urlencode


API_URL = os.getenv('MIDJOURNEY_API_URL')
if API_URL is None:
    raise ValueError('must set MIDJOURNEY_API_URK')
if 'generate_image' not in API_URL:
    raise ValueError('API_URL should be full path to the image generation route')
    

html_temp = """
<div style = "background.color:teal; padding:10px">
<h2 style = "color:white; text_align:center;"> Saturn Cloud Demo - Text to image</h2>
<p style = "color:white; text_align:center;"> </p>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)


#st.cache()
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

text = st.text_input("Input your prompt")


import time
import streamlit as st

with st.spinner('Wait for it...'):
    

    if st.button('Generate Image'):
        if len(text) == 0:
            st.write("input your prompt")
        else:
            pass
        url = API_URL + "?" + urlencode({'prompt': text})
        response = requests.post(url)
        st.image(response.content, caption=text)


    st.success('Done!')