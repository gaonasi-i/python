# match(), search() 객체의 메서드
# 그루핑(grouping())
# group(1) 첫번째 그룹
import re

# sub()- sub 함수(메서드)를 사용하면 정규식과 매치되는 부분을 다른 문자로 바꿀 수 있다.

"""
p = re.compile('[a-z]+')
m = p.match('hello')
print(m)
print(m.group())  # 문자열로 출력
print(m.start())  # 문자열 인덱스의 시작위치
print(m.end())    # 문자열 인덱스의 마지막위치
print(m.span())   # 구간(시작, 끝)
"""

# 이름과 전화번호를 분리해서 추출하기
# () - 소괄호가 그룹

str = "lee 010-1234-5678"
"""
pat = re.compile("(\w+)\s{1,2}(\d+[-]\d{4}[-]\d{4})") #\s{1,2}: 공백이 1~2개
mat = pat.match(str)

print(mat)
print(mat.group())
print('이름 :', mat.group(1))
print('전화번호 :', mat.group(2))
"""

# 그루핑의 문자옆에 이름 붙이기
# 정규 표현식 - (?P<그룹이름>) !!! P 대문자로 !!!
pat2 = re.compile('(?P<name>\w+)\s{1,2}(?P<phone>\d+[-]\d{4}[-]\d{4})')
mat2 = pat2.match(str)
print('이름 :', mat2.group('name'))
print('전화번호 :', mat2.group('phone'))

print("--------------------------------------")

# sub(\g<그룹이름>)
s1 = pat2.sub('\g<name>', 'park 010-3333-4444')
s2 = pat2.sub('\g<phone>', 'park 010-3333-4444')
print('이름:', s1)
print('전화번호:',s2)

# 문자열 바꾸기
data = """
kim 871212-1234567
lee 770707-2345678
"""
jumin = re.compile("(\d+)[-]\d+")
jumin2 = jumin.sub('\g<1>-*******', data)
print(jumin2)

# 전화번호 맨 끝자리 ****
phone = """
010-8718-6095
010-4737-6063
"""
jum = re.compile("(\d+[-]\d+)[-]\d+")
jum2 = jum.sub('\g<1>-****', phone)
print(jum2)