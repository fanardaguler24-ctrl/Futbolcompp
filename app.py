import streamlit as st
import cv2
import numpy as np
import yt_dlp
from moviepy.editor import VideoFileClip
import os

st.title("⚽ AI Futbol Dünyası")

url = st.text_input("YouTube Maç Linki:")
oyuncu = st.text_input("Oyuncu Adı (Rafa Silva):")

if st.button("Analizi Başlat"):
    st.write(f"🔍 {oyuncu} analiz ediliyor... (Kütüphaneler yüklendi!)")
    # Test için OpenCV versiyonunu yazdıralım
    st.write(f"Sistem Hazır! OpenCV Versiyonu: {cv2.__version__}")
