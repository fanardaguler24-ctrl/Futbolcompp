import streamlit as st
import yt_dlp
from moviepy.editor import VideoFileClip
import cv2
import os

st.title("⚽ AI Futbol Comp Yapıcı")

url = st.text_input("YouTube Maç Linki:")
oyuncu = st.text_input("Oyuncu İsmi:")

if st.button("Analizi Başlat"):
    if url:
        st.write(f"🔍 {oyuncu} için sistem hazırlanıyor...")
        st.write("✅ Kütüphaneler başarıyla yüklendi!")
    else:
        st.error("Lütfen bir link girin.")
