import streamlit as st
import joblib
import numpy as np

def run_ml_app():
    st.subheader('노인 인구 예측')

    #인공지능 파일을 읽어와서
    #예측하는 화면을 개발한다.

    img_url = 'https://www.sciencetimes.co.kr/wp-content/uploads/2021/05/30212411048_2a1d7200e2_b-480x384.jpg'
    st.image(img_url)

    regressor = joblib.load('./model/regressor.pkl')

    man_kr = st.number_input('한국인 남자 인구를 입력하세요. (최소 백만 입력)',1000000,10000000)

    woman_kr = st.number_input('한국인 여자 인구를 입력하세요. (최소 백만 입력)',1000000,10000000)

    man_fr = st.number_input('외국인 남자 인구를 입력하세요. (최소 만 단위)',10000,10000000)

    woman_fr = st.number_input('외국인 여자 인구를 입력하세요. (최소 만 단위)',10000,10000000)

    total = man_kr+woman_kr+man_fr+woman_fr
    total = "{:,}".format(total)

    if st.button('노인 인구 예측'):
        #예측한 결과를 화면에 보여준다.
        
        new_data = []
        percent = ((woman_kr / man_kr * 100.0))
        if percent >= 98:
            new_data = np.array([man_kr, woman_kr,man_fr,woman_fr])
            new_data = new_data.reshape(1,4)
            y_pred = regressor.predict(new_data)
            result = round(y_pred[0])
            result = "{:,}".format(result)
            st.text('인천 광역시의 전체 인구는 {} 이며, 노인 인구는 {}명으로 예측 됩니다.'.format(total,result))
        else:
            st.text('대한민국 남자 여자 비율이 3퍼센트 이상 차이가 나면 예측이 어렵습니다.')
       
    else :
        st.text('')