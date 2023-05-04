# 주식 증폭 가져오기
import requests
from bs4 import BeautifulSoup

def getcontent(item_code):
    url = 'https://finance.naver.com/item/main.naver?code=' + item_code
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    return content

def getprice(item_code):
    content = getcontent(item_code) # 호출
    today = content.select_one('div.today')
    #print(today)
    price = today.select_one('span.blind')
    return price.text

에코프로 = getprice('086520')
삼성전자 = getprice('005930')
네이버 = getprice('035420')
print(f'에포프로 주가 : {에코프로}원')
print(f'삼성전자 주가 : {삼성전자}원')
print(f'네이버 주가 : {네이버}원')