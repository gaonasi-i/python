# list1.py
# 리스트 생성
cart = [] # 빈리스트

# 리스트 요소 추가 - append() 함수 / 맨뒤에서 추가가됨
cart.append('닭알')
cart.append('사과')
cart.append('생수')
cart.append('콩나물')

# 특정한 위치에 요소 추가
cart.insert(2, '양파')

# 리스트 형태로 조회
print(cart)

#리스트의 개수 - len() 함수
print(len(cart))

#리스트 수정
cart[2] = '커피'

# 리스트 요소 삭제
#del cart[0] # 명령어로 삭제
#cart.remove('닭알') # 함수로 삭제 - remove() / 특정요소가 삭제
cart.pop() # 맨뒤에 요소가 삭제

# 전체 조회
for i in cart:
    print(i)

# 특정한 값을 조회
print(cart[-1])

#cart2 = ['닭알','사과', '생수' ]
#print(cart)
#print(cart2)
