import re

str = "12345yy7890 hi 999 hello"

# compile() : byte로 바꿈
# compile()후 findall()을 하면 검색할 내용이 많은 경우 빠른 속도로 처리가능
#pat = re.compile('\d{1,3}') #숫자 0~9에서 1~3개까지 찾음
#m = re.findall(pat, str)
"""
m = re.findall('\d{1,3}', str)

print(m)

m2 = re.findall('[1-5][1,2]', str) # 1~5까지 1~2개까지 찾음
print(m2)
"""

# '*', '+'의 차이
# '*' 앞문자를 0번 이상 반복
"""
p = re.compile('ca*t')
m1 = re.findall(p, 'caat')
print(m1)

m2 = re.findall(p, 'ct')
print(m2)

# '+' 앞문자를 1번이상 반복
p2 = re.compile('ca+t')
m3 = re.findall(p2, 'caat')
print(m3)

m4 = re.findall(p2, 'ct')
print(m4)
"""

# '.' : 임이의 문자 - 소괄호는 서브클래스(그룹)

str = "abcd<hr>Thank you"
pat1 = re.compile("<(.*)>")  #각괄호 미포함
m1 = re.findall(pat1, str)
print(m1)

pat2 = re.compile("(<.*>)")  #각괄호 포함
m2 = re.findall(pat2, str)
print(m2)

