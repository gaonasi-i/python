class City:
    a = ['Seoul', 'Inchen', 'Daejon', 'Jeju'] # 클래스 리스트

str1 = ""
for i in City.a:  #클래스 이름으로 직접 접근 (객체 생성을 하지않음)
    #str1 += i[0]
    str1 += i

print(City.a)
print("----------")
print(str1)
