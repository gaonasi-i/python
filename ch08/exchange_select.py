import requests
from bs4 import BeautifulSoup

# select_one(태그요소, 선택자(이름) - 1개 검색
# select(태그요소, 선택자(이름) - 전체검색(리스트 형태)

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')
ul = html.select_one('ul.data_lst')
#print(ul)
first_li = ul.select_one('li.on')
#print(first_li)
exchange = first_li.select_one('span.blind')
print(exchange.string)
value = first_li.select_one('span.value')
print(value.string)

print("*******************")

all_li = ul.select('ul.data_lst li')
#print(all_li)
for li in all_li:
    exchange = li.select_one('span.blind')
    value = li.select_one('span.value')
    print(exchange.string.split(' ')[0], ':', value.string)


