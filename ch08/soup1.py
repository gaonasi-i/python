# BeautifulSoup4 라이브러리 - html 태그 파싱(parsing:분석)
# BeautifulSoup(html_str, 'html.parser')
# find(태그,attrs={키:값})
from bs4 import BeautifulSoup

html_str = """
<html>
    <head>
      <title>웹 스크래핑(크롤링)</title>
    </head>
    <body>
        <ul class='item'>
          <li>인공지능</li>
          <li>빅데이터</li>
          <li>로봇</li>
        </ul>
        <ul class='comlang'>
          <li>Python</li>
          <li>C/C#</li>
          <li>Java</li>
        </ul>
    </body>
</html>
"""

soup = BeautifulSoup(html_str, 'html.parser')
first_ul = soup.find('ul', attrs={'class':'item'}) # attrs : 키와 값을 찾아줌
#print(first_ul)
#print(first_ul.text) # text = 태그빼고 텍스트만 출력
first_li = soup.find('li') #첫번째 li만 찾음
#print(first_li.text)

all_li = first_ul.findAll('li') # findAll = 리스트 형태로 출력
#print(all_li)
#print(all_li[1])
#print(all_li[1].text)

for li in all_li:
    print(li)
    print(li.text)