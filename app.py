import streamlit as st
from streamlit_option_menu import option_menu
from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app

def main():
    img_url = 'https://blog.kakaocdn.net/dn/vkQUE/btqwAmq4AD4/0i9MoDFZ3manZfEzUOGmd0/img.jpg'
    st.image(img_url)
    st.title('인천 광역시 노인인구 예측 대시보드')
    
    menu = [ 'Home','EDA','ML']
    with st.sidebar:
        st.image("https://blog.kakaocdn.net/dn/8y60x/btrFiofCS6U/RoHe9lALAtiw44Pafd5Zt1/img.png")
        choice = option_menu("App Menu", ["Home", "EDA", "ML"],
                            icons=['house', 'bar-chart', 'kanban'],
                            menu_icon="bi bi-menu-up", default_index=0,
                            styles={
                            # default_index = 처음에 보여줄 페이지 인덱스 번호
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        } # css 설정
        )

    #choice = st.sidebar.selectbox('메뉴',menu)

    if choice == menu[0]:
        run_home_app()
    elif choice == menu[1]:
        run_eda_app()
    elif choice == menu[2]:
        run_ml_app()


if __name__ == '__main__':
    main()


