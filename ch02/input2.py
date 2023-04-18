# 입력 방법 저장
"""
print("당신이 좋아하는 색깔은 무엇이에요?(흰색)")
color = input() # 키보드 입력
print(color) 
"""

# \n - 줄바꿈
"""
color = input("당신이 좋아하는 색깔은 무엇이에요?(흰색)\n")
print("좋아하는 색깔은", color, "입니다.")
"""

#int() 문자를 정수로 바꿔줌
#str() 숫자를 문자로 바꿔줌
# '+' 숫자를 더하고  문자를 연결할때 사용 
number = int(input("숫자를 입력하새요\n"))
print("입력된 수는", (number + 4), "입니다.")
print("입력된 수는" + str(number + 4) + "입니다.")
