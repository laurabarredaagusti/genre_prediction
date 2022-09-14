import streamlit as st
from functions import *
from classes.extract import *
from classes.predict import *
# from classes import *

config_page()

st.title('Find the genre')

if 'song_name' not in st.session_state:
    st.session_state['song_name'] = None

song_name = st.text_input('Enter song name', '')

st.session_state['song_name'] = song_name

Predict(song_name)

