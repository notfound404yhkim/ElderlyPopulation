import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb 

import matplotlib as mpl
import matplotlib.font_manager as fm

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_eda_app():
    st.subheader('데이터 분석')

    st.text('전체 데이터 프레임 확인하기')
    df = pd.read_csv('./data/Incheon_populationv3.csv',encoding = 'euc-kr')
    d_year = df['년도']
    df['년도'] = df['년도'].astype(str)
    df = df.set_index('년도') #문자열로 하여야 ,가 붙지 않음.
    st.dataframe(df)
    
    st.subheader('기초 통계 데이터 확인')
    if st.checkbox('통계 데이터보기'):
        st.dataframe(df.describe())
        st.text('노인 인구가 제일 적었던 해 ')
        st.dataframe(df.loc[ df['노인(65세이상)'] == df['노인(65세이상)'].min() , ])
        st.text('노인 인구가 제일 많았던 해 ')
        st.dataframe(df.loc[ df['노인(65세이상)'] == df['노인(65세이상)'].max() , ])
    else :
        st.text('')

    column_list = df.columns[:]
    # selected_column = st.selectbox('컬럼을 선택하세요',column_list)

    # st.text(selected_column + '컬럼의 최소 값')
    # st.dataframe(df.loc[ df[selected_column] == df[selected_column].min() , ])
    # st.text(selected_column + '컬럼의 최대 값')
    # st.dataframe(df.loc[ df[selected_column] == df[selected_column].max() , ])

    st.subheader('년도별 데이터 확인하기')
    selected_column2 = st.selectbox('컬럼을 선택하세요',column_list)
    ylabel = selected_column2

    plt.ylabel('')
    fig = plt.figure(figsize=(8,5))
    #plt.title( ylabel +  ' population data by ' + 'year')
    plt.title( ylabel )
    
    plt.xlabel('년도 별' + ylabel + ' 데이터 ' )
    plt.ylabel(ylabel)
    plt.plot( df[selected_column2] )
    st.pyplot(fig)

    st.subheader('Pie 차트 형태로 비율 확인')
    selected_year = str(st.selectbox('년도 인구 선택', d_year))
    df2= df.loc[selected_year,['남자(한국인)','여자(한국인)','남자(외국인)','여자(외국인)']]
    fig = plt.figure()
    plt.pie(df2, labels = df2.index, autopct='%.1f',startangle=90,wedgeprops={'width':0.8})
    plt.legend()
    plt.title( selected_year +'년 인천 인구')
    st.pyplot(fig)
  


    if st.checkbox('상관 관계 데이터 보기'):
        df2=df.sum(axis=1)
        df['인천 인구'] = df2
        selected_list = st.multiselect('두개의 컬럼을 선택하세요.' ,df.columns[:], max_selections=2)  

        #두개일때만 차트 그리기 
        if len(selected_list) == 2:
            fig = plt.figure()
            plt.scatter(data = df, x= selected_list[0], y= selected_list[1])
            plt.title( selected_list[0] + ' VS ' + selected_list[1])
            plt.xlabel(selected_list[0])
            plt.ylabel(selected_list[1])
            st.pyplot(fig)


            fig = plt.figure()
            st.text('상관 계수')
            st.dataframe(df[selected_list].corr())
            st.pyplot(fig)

        else:
            st.text('')
    
    else:
        if '인천 인구' in df.columns:  #sum 컬럼이 있다면 삭제
            df = df.drop(labels='인천 인구',axis=1,inplace=True)

    
   



    
 