import streamlit as st
from PIL import Image


def app():
	
    
	st.header("Architecture")
    # 방법 1: 로컬 이미지 파일 표시
	local_image = Image.open("data/diagram.png")
	st.image(local_image, caption='Architecture Diagram', use_container_width=True)