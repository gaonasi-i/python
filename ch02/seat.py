#자리배치
#입장객 수, 좌석 열, 줄 수
#입장객수가 열수로 나누어떨어지는 경우, 그렇지 않은 경우
customer = 22
col = 5

#몫 = customer//col
#나머지 = customer % col

customer = int(input("입장객 수를 입력하세요\n"))
col = int(input("좌석 열수를 입력하세\n"))

if customer % col == 0:
#row = customer // col
    row = int(customer / col)
else:
#row = customer // col + 1
    row = int(customer / col) + 1
print("줄수 :", row)



    
