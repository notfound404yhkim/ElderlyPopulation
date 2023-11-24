import streamlit as st
import joblib
import numpy as np
from PIL import Image

def run_ml_app():
    st.subheader('노인 인구 예측')

    #인공지능 파일을 읽어와서
    #예측하는 화면을 개발한다.

    img_url = 'https://www.sciencetimes.co.kr/wp-content/uploads/2021/05/30212411048_2a1d7200e2_b-480x384.jpg'
    st.image(img_url)

    st.text('샘플 데이터 보기')
    if st.checkbox('샘플 : 2013~2022년 통계'):
        img = Image.open('./data/data_img.jpg')
        st.image(img)
    else :
        st.text('')

    regressor = joblib.load('./model/regressor.pkl')

    man_kr = st.number_input('한국인 남자 인구를 입력하세요. (최소 백만 입력)',1000000,10000000)

    woman_kr = st.number_input('한국인 여자 인구를 입력하세요. (최소 백만 입력)',1000000,10000000)

    man_fr = st.number_input('외국인 남자 인구를 입력하세요. (최소 만 단위)',10000,10000000)

    woman_fr = st.number_input('외국인 여자 인구를 입력하세요. (최소 만 단위)',10000,10000000)

    total = man_kr+woman_kr+man_fr+woman_fr
    total = "{:,}".format(total)

    st.markdown("""<style> 
            [class='row-widget stButton'] > button {
                border-radius: 50px;
                background : #D9D9D9;
                filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
                border : hidden;
            }
            [class='row-widget stButton'] > button > div {
                color : #FFFFFF;
            }
            [class='row-widget stButton'] > button:hover {
                background : #2D5AF0;
                transform : scale(1.1);
                transition : .5s;
            }
    </style>""", unsafe_allow_html=True)

    if st.button('노인 인구 예측'):
        #예측한 결과를 화면에 보여준다.

        new_data = []
        percent = ((woman_kr / man_kr * 100.0))
        if percent >= 98 and percent <= 103 :
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