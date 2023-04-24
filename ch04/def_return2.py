# 사각형의 넓이 계산 함수
# 함수이름 - calc_area()

def calc_area(w, h):
    area = w * h
    return area

result =  calc_area(4, 3)
print('사각형의 면적', result)   #12
print(f'사각형 면적 : {result}') #12
# 가로가 4센치 세로가 3센치의 사각형의 넓이
# 가로의길이 * 세로의길이 = 사각형의 넓이

#---------------------------------------#


# 삼각형의 넓이 계산 함수
# 함수이름 - tri_area()

def tri_area(x, y):
    area = int((x * y) / 2) # 소수점자리 없애기 int()
    return area

result2 = tri_area(4, 5)
print(f'삼각형의 면적 : {result2}') #10
# 밑변 4, 높이 5의 삼각형의 넓이
# (밑변 * 높이) ÷ 2 = 삼각형의 넓이


#---------------------------------------#

# 정사각형의 면적
"""
size = int(input("숫자를 입력: "))
area = size * size
print(area)
"""
def calc_size(n):
    area = n * n
    return area
print(calc_size(100))
