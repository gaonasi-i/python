# 튜플(tuple) - 요소의 수정과 삭제 불가, 소괄호 사용
t1 = (1, 2, 3)
print(t1)
print(type(t1))

# 인덱싱 - 리스트와 같음
print(t1[0])
print(t1[-1])

#t2 = (1) # 속성이 튜플로 지정되지 않고 inf로 지정됨
t2 = (1, ) # 튜플로 지정하려면 1개를 저장할때는 반드시 뒤에 ,를 붙힌다
print(t2)
print(type(t2))

# 수정 (새값을 할당)
#t1[2] = 4
#TypeError: 'tuple' object does not support item assignment

# 요소 삭제
#del t1[1]
# TypeError: 'tuple' object doesn't support item deletion

