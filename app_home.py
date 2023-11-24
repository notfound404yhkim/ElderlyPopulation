import streamlit as st
from PIL import Image

def run_home_app():
    
    st.subheader('이 앱은 인천 광역시 인구추이 와 노인 인구 예측 데이터에 대한 내용입니다.')
    st.text('대한민국 남녀, 외국인 남녀 인구를 입력하면 노인 인구를 예측합니다.')

    st.text('AWS에 배포까지 된 앱 입니다.')
    st.text('이 데이터의 출처는 kosis 통계정보 입니다.')

    img = Image.open('./data/출처.png')
    st.image(img)
