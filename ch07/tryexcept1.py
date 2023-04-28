# 다중 예외 처리

try:
    date = [15, 20, 99, 8, 0]
    x = input("정수 입력(0~4까지 입력) : ")
    num = int(x)
    print(date[num])
except IndexError as e: #인덱스 요소 접근 에러
    print(e)
# except IndexError:
#     print(IndexError)
except ValueError as e: #숫자형말고 문자형을 넣었을때 에러
    print(e) #invalid literal for int() with base 10: 'adss' 유효하지 않은 문자다
