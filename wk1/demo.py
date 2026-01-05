import streamlit as st
import requests 
import json 


st.title("안녕")
code = st.text_input("종목 코드를 입력하세요 (예: 005930)", value="005930")


## 1년치 데이터 수집 방법
import requests

url = f"https://api.stock.naver.com/chart/domestic/item/{code}/day?startDateTime=202501010000&endDateTime=202512310000"

requests.get(url).text

with open("./053700.txt", "w", encoding='utf-8') as f :
    f.write(requests.get(url).text)

with open("./053700.txt", "r", encoding='utf-8') as f :
    data = f.read()

import json
data = json.loads(data)


with open(f"./stock/{code}stock.csv", "w", encoding='utf-8') as f:
    for x in data:
        f.write(str(list(x.values())) + "\n")


with open(f"./stock/{code}stock.csv", "w", encoding='utf-8') as f:
    for x in data:
        f.write(",".join(list(map(str, x.values()))) + "\n")

display_data = []
for x in data:
    display_data.append(list(x.values()))
st.subheader("데이터 미리보기")
st.table(display_data[:10]) # 너무 많으면 화면이 길어지므로 상위 10개만 예시로 출력