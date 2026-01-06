import streamlit as st 
import requests 
import time, random

name = st.text_input("종목명을 입력하세요")
sdate = st.text_input("시작 날짜를 입력하세요(20250101)")
edate = st.text_input("끝나는 날짜를 입력하세요")


if st.button("진행"):
    st.markdown(f"{name}, {sdate}, {edate}")

    
with open(r"C:\skn-25\wk2\data_krx.csv","r",encoding='cp949') as f:
    data = f.read()

for x in data.split("\n")[1:]:

    y  = x.replace('"', '').split(",")
    if y[1] == name:
        url = f"https://api.stock.naver.com/chart/domestic/item/{y[0]}/day?startDateTime={sdate}&endDateTime={edate}"
        with open(f"{name}.csv", "a", encoding='utf-8') as f:
            for x in requests.get(url).json():
                f.write(','.join(map(str,x.values())) + "\n")
    time.sleep(abs(random.gauss(0,1)))


