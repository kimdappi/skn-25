import requests 
import json 


def get_krx():
    url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"
    
    payload={"bld":"dbms/MDC/STAT/standard/MDCSTAT01901",
    "locale":"ko_KR",
    "mktId":"ALL",
    "share":"1",
    "csvxls_isNo":"false",}
    
    request_headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "88",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "data.krx.co.kr",
        "Origin": "http://data.krx.co.kr",
        "Referer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    r= requests.post(url, data=payload, headers=request_headers)
    krx = json.loads(r.text)

    return krx 

def get_code(comany_name):
    krx=get_krx()
    return [stock['ISU_SRT_CD'] for stock in krx['OutBlock_1'] if stock['ISU_ABBRV'] == comany_name] 

import requests, json

def get_tv(code,type_):
    """
    code : 종목 코드
    type_ :  
    """
    url = f"https://polling.finance.naver.com/api/realtime/domestic/stock/{code}"
    result = requests.get(url).text
    result_dict = json.loads(result)

    if len(result_dict['datas'])==0:
        return "종목코드확인"

    if type_ == 'value':
        return int(result_dict['datas'][0]["accumulatedTradingValue"].replace("백만","").replace(',',''))*1000000
    elif type_ == 'volume':
        return int(result_dict['datas'][0]["accumulatedTradingVolume"].replace(',',''))
    
