# While 반복문
# Hello를 10번 출력

'''
i = 1
while i <= 10:
    print("hello", i)
    i += 1
'''

# 1부터 10까지 더하기
'''
i = 0
sum_v = 0
while i < 10:
    i += 1
    sum_v = sum_v + i
    print("i =", i, ", sum_v =", sum_v)
print(f'합계 : {sum_v}')
'''

# 반복 조건문(break)
'''
i = 0
sum_v = 0
while True:
    i += 1
    if i > 10:
        break
    sum_v += 1
    print(f'i={i}, sum_v={sum_v}')
print(f'합계 : {sum_v}')
'''

#반복 조건
while True:
    answer = input("반복을 계속 할까요?(y/n)")
    if answer == 'y' or answer == 'Y':
        print("반복을 계속 합니다.")
    elif answer == 'n' or answer == 'N':
        print("반복을 중단 합니다")
        break
    else:
        print("정산 답변이 아닙니다.")

