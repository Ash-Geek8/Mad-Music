import webbrowser
import streamlit as st
from streamlit_webrtc import webrtc_streamer

lang='Tamil'
emotion='Happy'
singer='Rahman'

st.header("Emotion Based Music Recommender")

#webbrowser.open(f"https://www.youtube.com/results?search_query={lang}+{emotion}+song by+{singer}")