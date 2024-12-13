import streamlit as st
#from utils import project1_desc as p1d
from utils.project1_desc import disney_data, disney_info, disney_head


def app():
    st.header("💟 Project 1: Disney Data Processing")

    # 데이터 로드
    disney = disney_data()
    st.subheader("1. Disney Dataset")
    st.dataframe(disney.head(10))  # 데이터 미리보기

    # 데이터 요약
    st.subheader("2. Dataset Summary")
    summary = disney_info(disney)  # 데이터 요약 정보 호출

    # Streamlit을 사용하여 데이터 요약 표시
    st.text("==== Disney 데이터 정보 ====")
    st.text(summary["info"])
    st.text("\n==== Disney 데이터 요약 통계 ====")
    st.dataframe(summary["describe"])
    st.text("\n==== Disney 데이터 결측치 개수 ====")
    st.dataframe(summary["missing_values"])

    # 상단 2개 행 출력
    st.subheader("3. Top n-Rows")
    st.dataframe(disney_head(disney))