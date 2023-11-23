import streamlit as st
import joblib
import numpy as np

def run_ml_app():
    st.subheader('노인 인구 예측')

    #인공지능 파일을 읽어와서
    #예측하는 화면을 개발한다.
    regressor = joblib.load('./model/regressor.pkl')

    man_kr = st.number_input('한국인 남자 인구를 입력하세요.',1000,10000000)

    woman_kr = st.number_input('한국인 여자 인구를 입력하세요.',1000,10000000)

    man_fr = st.number_input('외국인 남자 인구를 입력하세요.',1000,10000000)

    woman_fr = st.number_input('외국인 여자 인구를 입력하세요.',1000,10000000)

    if st.button('구매 예상 금액'):
        #예측한 결과를 화면에 보여준다.
        new_data = []
        
        # 1. 넘파이 어레이 만들어야 한다.
        new_data = np.array([man_kr, woman_kr, man_fr,man_fr,woman_fr])
        new_data = new_data.reshape(1,5)
        y_pred = regressor.predict(new_data)
        result = y_pred[0]

        if result <= 0:
            st.text('노인 인구를 예측하기 어렵습니다.')
        else:
            st.text('인천 광역시의 노인 인구는  {} 명으로 예측 됩니다.'.format(result))
       
       
    else :
        st.text('')