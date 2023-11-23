import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb 


def run_eda_app():
    st.subheader('데이터 분석')

    st.text('전체 데이터 프레임 확인하기')
    df = pd.read_csv('./data/Incheon_populationv2.csv',encoding = 'euc-kr')
    df['year'] = df['year'].astype(str)
    df = df.set_index('year') #문자열로 하여야 ,가 붙지 않음.
    st.dataframe(df)
    
    st.text('기초 통계 데이터 확인')
    if st.checkbox('통계 데이터보기'):
        st.dataframe(df.describe())
    else :
        st.text('')

    st.text('최대 / 최소 데이터 확인하기')

    column_list = df.columns[:]
    # selected_column = st.selectbox('컬럼을 선택하세요',column_list)
    st.text('노인 인구가 제일 적었던 해 ')
    st.dataframe(df.loc[ df['oldman'] == df['oldman'].min() , ])
    st.text('노인 인구가 제일 많았던 해 ')
    st.dataframe(df.loc[ df['oldman'] == df['oldman'].max() , ])

    # st.text(selected_column + '컬럼의 최소 값')
    # st.dataframe(df.loc[ df[selected_column] == df[selected_column].min() , ])
    # st.text(selected_column + '컬럼의 최대 값')
    # st.dataframe(df.loc[ df[selected_column] == df[selected_column].max() , ])

    
    # st.text('년 도별 데이터 확인하기')
    if st.checkbox('년도별 데이터 보기'):
        selected_column2 = st.selectbox('컬럼을 선택하세요',column_list)
        ylabel = selected_column2
        plt.ylabel('')
        fig = plt.figure()
        plt.style.use('ggplot')
        plt.title( ylabel +  ' population data by ' + 'year')
        plt.xlabel('year')
        plt.ylabel(ylabel)
        plt.plot( df[selected_column2] )
        st.pyplot(fig)
    else :
        st.text('')




    if st.checkbox('상관 관계 데이터 보기'):
        df2=df.sum(axis=1)
        df['Population'] = df2
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
        if 'Population' in df.columns:  #sum 컬럼이 있다면 삭제
            df = df.drop(labels='Population',axis=1,inplace=True)

    
   



    
 