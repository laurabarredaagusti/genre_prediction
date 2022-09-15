import streamlit as st
import base64
from PIL import Image 


def config_page():
    '''
    This function will set the initial configuration of the page
    '''
    st.set_page_config(page_title = 'Find the genre',
                        page_icon = ':fire:',
                        layout= 'wide')

def edm():
    img = Image.open('background.jpg')
    st.image(img,use_column_width='auto')
    pass
