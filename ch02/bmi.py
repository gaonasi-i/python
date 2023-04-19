# bmi.py
# 체질량 지수 공식 = 몸무게 / 키의 제곱
# 키 = 키 / 100
# 거듭제곱 2 ** 3 = 2 x 2 x 2 / 3 ** 2 = 3 x 3

name = input("이름을 입력하세요 : ")
weight = float(input("몸무게를 입력하세요 : "))
height = float(input("키(cm) 입력하세요 : "))
height = height / 100


bmi = weight / (height ** 2) 
print(f"{name}님의 bmi는 {bmi:.2f} 입니다.") # f스트링 방식
# %s - 문자, %f - 실수, %d - 정수
#print("%s님의 bmi는 %.2f입니다." % (name, bmi) ) # %포맷 방식

if bmi < 20:
    print("저체중입니다")
elif bmi >= 20 and bmi < 24:
    print("정상입니다")
elif bmi >= 25 and bmi < 29:
    print("과체중입니다")
else:
    print("비만입니다ㅜ_ㅜ")
    
