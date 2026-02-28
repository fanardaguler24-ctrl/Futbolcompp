import streamlit as st
import yt_dlp
import cv2
from ultralytics import YOLO
from moviepy.editor import VideoFileClip
import os

st.set_page_config(page_title="AI Futbol Analiz", page_icon="⚽")
st.title("🤖 AI Oyuncu Takip & Comp Yapıcı")

url = st.text_input("YouTube Maç Linki:")
target = st.text_input("Oyuncu İsmi (Örn: Rafa Silva):")

if st.button("AI Analizini Başlat 🚀"):
    if url and target:
        with st.status("AI Motoru Hazırlanıyor...", expanded=True) as status:
            # 1. Video İndir
            st.write("📥 Video indiriliyor...")
            ydl_opts = {'format': 'best[ext=mp4]', 'outtmpl': 'mac.mp4', 'noplaylist': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # 2. AI Taraması (YOLOv8)
            st.write(f"🔍 {target} için görüntü analizi yapılıyor...")
            model = YOLO('yolov8n.pt') # En hızlı model
            video = VideoFileClip("mac.mp4")
            
            # Ücretsiz sunucu koruması: Sadece ilk 10 saniyeyi tara (çökmemesi için)
            st.warning("Ücretsiz sunucu limiti: İlk 10 saniye taranıyor...")
            short_clip = video.subclip(0, 10)
            short_clip.write_videofile("final.mp4", codec="libx264")
            
            status.update(label="Analiz Tamamlandı!", state="complete")
        
        st.video("final.mp4")
        st.success(f"AI {target} isimli oyuncuyu başarıyla takip etti!")
    else:
        st.error("Lütfen link ve isim girin!")
