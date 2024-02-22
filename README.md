# 👨‍🦳 인천 광역시 노인인구 예측 대시보드 👀

## 📌 Project Explanation
* 통계청의 2011년부터 2022년 인천 인구추이 데이터를 활용하여, 인공지능을 활용하여 노인 인구를 예측하는 서비스를 제공.
* 인공지능 모델은 pkl 파일화하여 진행하였습니다.
* 통게청의 인구추이을 분석하여 예측 및 차트로 보여주는 앱입니다.
* EDA를 눌러보시면 데이터별로 분석된 차트를 확인하실 수 있습니다.
* AWS EC2를 이용하여 서버를 관리하였습니다.
* 유지보수작업을 수월하게 하기 위해서 다른 파일에서 함수를 만들고 그 함수를 import해서 작업을 하였습니다

## 📌Code block

# 파이차트 형태로 데이터 표시
```
 st.subheader('Pie 차트 형태로 비율 확인')
    selected_year = str(st.selectbox('년도 인구 선택', d_year))
    df2= df.loc[selected_year,['남자(한국인)','여자(한국인)','남자(외국인)','여자(외국인)']]
    fig = plt.figure()
    plt.pie(df2, labels = df2.index, autopct='%.1f',startangle=90,wedgeprops={'width':0.8})
    plt.legend()
    plt.title( selected_year +'년 인천 인구')
    st.pyplot(fig)
````

# 상관 계수
```fig = plt.figure()
   plt.scatter(data = df, x= selected_list[0], y= selected_list[1])
   plt.title( selected_list[0] + ' VS ' + selected_list[1])
   plt.xlabel(selected_list[0])
   plt.ylabel(selected_list[1])
   st.pyplot(fig)
   fig = plt.figure()
   st.text('상관 계수')
   st.dataframe(df[selected_list].corr())
   st.pyplot(fig)
```

## 📌 ML

# train 과 test 모델 분리
```
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2,  random_state= 42)
```

# 모델링 과정
```
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
```

# 모델 생성
```
import joblib
joblib.dump(regressor,'regressor.pkl')
```

## 📌 URL
 - http://ec2-43-201-154-87.ap-northeast-2.compute.amazonaws.com:8501/
 
## 📌 Screen Shot



