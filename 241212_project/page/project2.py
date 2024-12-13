import streamlit as st
from utils.project2_desc import disney_palette, disney_data, get_type_ratio, plot_by_year, plot_rating_analysis, plot_age_heatmap
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.header("💟 Project 2: Disney Plus Data Visualization")

	#데이터 로드
    disney = disney_data()
 
    # Disney 색상 팔레트 시각화
    st.subheader("1. Disney Brand Palette")
    st.pyplot(disney_palette())
 
    # type 값 비율 반환
    st.subheader("2. Content Type Ratio (Movies vs TV Shows)")
    type_ratio = get_type_ratio(disney)
    st.write(type_ratio)

    # 연도별 Movies & TV Shows 시각화
    st.subheader("3. Movies & TV Shows Added by Year")
    st.pyplot(plot_by_year(disney))

	# Rating별 고유값 확인 및 Age Group 변환
    st.subheader("4. Age Group Mapping")
    disney = plot_rating_analysis(disney)
    st.dataframe(disney[['rating', 'age_group']].drop_duplicates())  # Rating 및 Age Group 표시

    # 나라별 연령 타겟 히트맵
    st.subheader("5. Target Age Group by Genre")
    st.pyplot(plot_age_heatmap(disney))
    