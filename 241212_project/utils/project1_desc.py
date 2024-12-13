import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# 데이터 로드 및 결측치 처리
#def disney_data():
#    file_path = "data/disney_plus_titles.csv"
#    disney = pd.read_csv(file_path)
#    disney.fillna('No Data', inplace=True)
#    return disney

# 데이터 로드 및 결측치 처리
def disney_data():
    #데이터 로드
    file_path = "data/disney_plus_titles.csv"
    disney = pd.read_csv(file_path)
    #결측치 처리
    disney.fillna('No Data', inplace=True)
    # date_added를 datetime 형식으로 변환
    if 'date_added' in disney.columns:
        disney['date_added'] = pd.to_datetime(disney['date_added'], errors='coerce')
        disney['year_added'] = disney['date_added'].dt.year  # year_added 열 생성
    else:
        disney['year_added'] = None  # date_added 열이 없으면 year_added를 None으로 설정
    return disney

# 데이터 정보 출력
def disney_info(disney):
    buffer = io.StringIO()  # 문자열 버퍼 생성
    disney.info(buf=buffer)  # info 내용을 버퍼에 작성
    info_str = buffer.getvalue()  # 버퍼의 내용을 문자열로 가져오기

    info = {
        "info": info_str,  # 문자열로 반환된 info
        "describe": disney.describe().reset_index(),  # describe 결과를 DataFrame으로 반환
        "missing_values": disney.isna().sum().reset_index(name='missing_count')  # 결측치 정보를 DataFrame으로 반환
    }
    return info

# 상단 N개 행 출력
def disney_head(disney, n=30):
    return disney.head(n)

# Disney 색상 팔레트
def disney_palette():
    disney_colors = ['#fbf9ff', '#f3cc64', '#efbeb7', '#12194a']
    fig, ax = plt.subplots(figsize=(8, 2))
    #sns.heatmap([disney_colors], ax=ax, cbar=False, annot=False, linewidths=0.5)
    #ax.set_title("Disney Brand Palette", loc='left', fontfamily='serif', fontsize=15, y=1.2)
    #ax.axis('off')  # 축 숨기기