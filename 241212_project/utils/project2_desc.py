import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

#disney = pd.read_csv("/data/disney_plus_titles.csv")

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
         # 결측치를 0 또는 다른 값으로 채우고 int로 변환 -> 결과적으로 date added는 2019~2021에 몰려있어서 year_added 안씀!
        disney['year_added'] = disney['year_added'].fillna(0).astype(int)
    else:
        disney['year_added'] = 0  # date_added 열이 없으면 year_added를 0으로 설정
    return disney

def disney_palette():
    """
    Disney 브랜드 색상 팔레트를 시각화합니다.
    """
    disney_colors = ['#fbf9ff', '#f3cc64', '#efbeb7', '#12194a']  # Disney 색상 코드
    fig, ax = plt.subplots(figsize=(8, 1))

    # 색상 팔레트 시각화
    for i, color in enumerate(disney_colors):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))  # 사각형으로 색상 표시
    ax.set_xlim(0, len(disney_colors))
    ax.set_ylim(0, 1)
    ax.axis('off')  # 축 숨기기
    ax.set_title("Disney Brand Palette", loc='center', fontsize=15, fontfamily="serif")
    return fig

#type 값 반환
def get_type_ratio(disney):
    return pd.DataFrame(disney['type'].value_counts()).T

#연도별 비율 시각화
def plot_by_year(data, x_col='release_year', hue_col='type', palette=['#f3cc64', '#efbeb7']):
    # 데이터 필터링: 2008~2021년만 포함
    filtered_data = data[(data[x_col] >= 2008) & (data[x_col] <= 2021)]

    # 명시적으로 figure 객체 생성
    fig, ax = plt.subplots(figsize=(15, 5))

    # Seaborn 그래프 그리기
    sns.countplot(data=filtered_data, x=x_col, hue=hue_col, palette=palette, ax=ax)

    # 제목 및 라벨 설정
    ax.set_title('Movies & TV Shows Added by Year', fontfamily='serif', fontsize=15, fontweight='bold')
    ax.set_xlabel(x_col)
    ax.set_ylabel("Count")

    return fig

# Rating 분석 및 Age Group 변환
def plot_rating_analysis(disney):
    age_group = {
        'TV-MA': 'Adults', 'R': 'Adults', 'PG-13': 'Teens', 'TV-14': 'Young Adults',
        'TV-PG': 'Older Kids', 'NR': 'Adults', 'TV-G': 'Kids', 'TV-Y': 'Kids',
        'TV-Y7': 'Older Kids', 'PG': 'Older Kids', 'G': 'Kids', 'NC-17': 'Adults',
        'TV-Y7-FV': 'Older Kids', 'UR': 'Adults'
    }
    disney['age_group'] = disney['rating'].map(age_group)
    return disney

# 나라별 연령 타겟 히트맵 시각화
def plot_age_heatmap(disney):
    # 데이터 준비 -> 이게 왜 생겼는지 다시 알아보기
    disney = disney.assign(listed_in=disney['listed_in'].str.split(', '))
    disney = disney.explode('listed_in')
    ##그룹화
    disney_age_genre = disney.groupby('age_group')['listed_in'].value_counts(normalize=True).unstack(fill_value=0)
 	##특정 연령 및 국가 선택
    age_order = ['Kids','Older Kids','Teens','Young Adults']
    genre_order = ['Animation', 'Comedy', 'Musical', 'Lifestyle', 'Family', 
                   'Superhero', 'Kids', 'Fantasy', 'Documentary','Romance']
    disney_age_genre = disney_age_genre.loc[age_order, genre_order]

    # 히트맵 생성
    fig, ax = plt.subplots(figsize=(15, 5))
    #cmap = sns.color_palette("flare", as_cmap=True)
    disney_colors = ['#fbf9ff', '#f3cc64', '#efbeb7', '#12194a']
    cmap = LinearSegmentedColormap.from_list("custom_palette", disney_colors)
    sns.heatmap(disney_age_genre, cmap=cmap, linewidth=2.5, annot=True, fmt='.1%')

    # 제목 설정
    ax.set_title('Target ages proportion of total content by country', fontweight='bold', fontfamily='serif', fontsize=15)
    return fig

