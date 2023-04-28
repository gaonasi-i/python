# 영어 타자 게임
import random
import time
try:
    with open("./output/word.txt", 'r') as f:
        data = f.read().split()
        word = random.choice(data)

    input("[타자 게임] 준비되면 엔터")
    start = time.time()
    n = 1 # 문제 번호 (while문의 초기값)
    while n <= 10:
        question = random.choice(data)
        print(f'문제 {n}')
        print(question)
        user = input()
        if question == user:
            print('정답!')
            n += 1
        else:
            print('오답! 다시 입력하여 주세요.')
    end = time.time()
    print(f'게임 소요 시간 : {end-start :.2f}초')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")