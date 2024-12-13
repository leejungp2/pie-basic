import streamlit as st

def app():
	
    
    ### 주요 기능
#    - **데이터 탐색:** Disney 데이터를 요약 및 시각화합니다.
#    - **결측치 처리:** 결측치 데이터를 처리하고 분석에 적합한 형태로 변환합니다.
#    - **데이터 시각화:** 그래프와 표로 데이터를 직관적으로 이해할 수 있습니다.
#    - **지도 시각화:** Folium을 사용해 위치 데이터를 시각화합니다.
#    """)


	st.header("About the Project")
	st.write("""
    이 앱은 Streamlit과 Python을 사용하여 데이터 분석 및 시각화 기술을 학습하기 위해 개발되었습니다. 
    Disney 데이터를 다루며 실습을 통해 주요 데이터 처리 기술을 익힐 수 있습니다.
       - 본 웹사이트는 Kaggle의 'Disney+ Movies and TV Shows' 데이터를 사용하였습니다. : https://www.kaggle.com/datasets/shivamb/disney-movies-and-tv-shows?resource=download
    """)
 
	st.header("How to Use")
	st.write("""
    1. **사이드바를 사용하여 페이지를 탐색하세요.**
       - "Data Processing"에서는 데이터 정보 및 결측치 처리 결과를 확인할 수 있습니다.
       - "Visualization"에서는 해당 데이터에 대한 시각화 결과를 볼 수 있습니다.
       
    2. **페이지별 기능을 살펴보세요.**
       - 각 페이지에는 데이터와 관련된 다양한 시각화가 포함되어 있습니다.
    """)

	st.info("👈 사이드바에서 페이지를 선택하여 탐색을 시작하세요!")