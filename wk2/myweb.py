





import streamlit as st
import pandas as pd
import logging
import datetime
import os




logger = logging.getLogger(__name__) # 예: '__main__' 또는 모듈 이름
# 2. 로거 레벨 설정 (처리할 메시지 최저 레벨)
logger.setLevel(logging.DEBUG) # DEBUG 이상 모든 메시지 처리 시작


# --- 핸들러 설정 (중복 추가 방지 로직 포함) ---
if not logger.hasHandlers():
    # 3. 핸들러 생성
    # 콘솔 핸들러 (INFO 레벨 이상만 콘솔 출력)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)


    # 일반 파일 핸들러 (DEBUG 레벨 이상 파일에 기록)
    if not os.path.isdir("./logs"):
        os.mkdir("./logs")
    log_filename = os.path.join("./logs", f"app_{datetime.date.today()}.log")
    file_handler = logging.FileHandler(log_filename, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)


    # 회전 파일 핸들러 (DEBUG 레벨 이상, 크기 기반 회전)
    rotate_filename = os.path.join("./logs", "app_rotate.log")
    # 예: 1KB 마다 회전, 백업 3개 유지
    rotate_handler = logging.handlers.RotatingFileHandler(
        rotate_filename, maxBytes=1024, backupCount=3, encoding='utf-8'
    )
    rotate_handler.setLevel(logging.DEBUG)


   
    # 콘솔용 포맷 (간단하게)
    console_format = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%H:%M:%S')
    # 파일용 포맷 (더 상세하게)
    file_format = logging.Formatter('%(asctime)s [%(levelname)-8s] %(name)s %(filename)s:%(lineno)d - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


    # 5. 핸들러에 포매터 설정
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)
    rotate_handler.setFormatter(file_format)


    # --- 로거에 핸들러 추가 ---
    # 6. 로거에 핸들러들 추가
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(rotate_handler)






kbo_df = pd.read_csv("./kbo2.csv")


st.title('KBO')




with st.sidebar:
    st.title("팀선택")
    # kbo_df에서 팀 이름을 아래 options에 넣기
    myteam = st.selectbox(label='팀선택', options= kbo_df.Team.unique() ,
                 index=3 )
    logger.info(f"사용자가 {myteam}를 선택함")


    myele = st.selectbox(label='초등학교', options= [' ']  + kbo_df.출신초등학교.unique().tolist())
    logger.info(f"사용자가 {myele}를 선택함")


# st.write(myteam)
if myele == ' ':
    st.write(myteam)
    st.dataframe(kbo_df[(kbo_df['Team'] == myteam)])
else:
    st.write(myele)
    st.dataframe(kbo_df[(kbo_df['출신초등학교'] == myele)])

