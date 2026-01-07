import argparse
import requests
## 윗단의 코드들은 다른 코드에서 모듈로 불러올 수 있음
def stock(code, sdate, edate, type_):
    return f"https://api.stock.naver.com/chart/domestic/item/{code}/{type_}?startDateTime={sdate}&endDateTime={edate}"

if __name__=="__main__":
    ## 이 코드를 독단적으로 돌리기 위함. __name__ 이 main인 것임
    ## 터미널에서 실행 시 돌아갈 수 있음
    parser = argparse.ArgumentParser()


    parser.add_argument('--code', help="종목 코드를 입력")
    parser.add_argument('--sdate', help="시작 날짜")
    parser.add_argument('--edate', help="끝 날짜")
    parser.add_argument('--type', help="일, 주, 월 선택")


    args = parser.parse_args()


    # print(args.code, args.sdate, args.edate, args.type)
    print(stock(args.code, args.sdate, args.edate, args.type))