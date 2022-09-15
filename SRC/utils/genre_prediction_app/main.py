import streamlit as st
from functions import *
from classes.extract_all import *
from classes.extract_electronic import *
from classes.predict_all import *
from classes.predict_electronic import *

config_page()

# menú
# menu = st.sidebar.selectbox('Selecciona la página', ['All genres', 'EDM'])

# if menu == 'EDM':
edm()

st.markdown("""
<style>
.big-font {
    font-size:24px !important;
    font-weight:600 !important;
    font-family:Roboto !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">FIND THE GENRE</p>', unsafe_allow_html=True)

menu = st.sidebar.selectbox('Selecciona la página', ['EDM', 'All genres'])

if menu == 'EDM':
    input = st.text_input('Enter track url', '')
    Predict_electronic(input)


elif menu == 'All genres':
    input = st.text_input('Enter track name', '')
    Predict_all(input)



    # st.title('Find the genre')

    # if 'song_name' not in st.session_state:
    #     st.session_state['song_name'] = None

    # song_name = st.text_input('Enter song name', '')

    # st.session_state['song_name'] = song_name

    # Predict(song_name)

