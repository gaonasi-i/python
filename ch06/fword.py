# 영어 단어장 만들기

import random
word = ['ant', 'bee', 'chicken', 'deer', 'fox', 'elephant', 'horse', 'lion'
        , 'monkey', 'penguin']
try:
    with open("./output/word.txt", 'w') as f:
        for i in word:
            if i == word[-1]:
                f.write(i)
            else:
                f.write(i + ' ')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 파일 읽기
try:
    with open("./output/word.txt", 'r') as f:
        data = f.read().split(' ') # split() 리스트로 변환 - 공백문자로 구분
        #word = random.choice(data) # 단어 1개를 랜덤하게 추출
        print(word)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

#------------------------------------------------------------------------------------#
"""
# 영어 단어장 만들기
import random
word = ['ant', 'bee', 'chicken', 'deer', 'fox', 'elephant', 'horse', 'lion'
        , 'monkey', 'penguin']
try:
    with open("./output/word.txt", 'w') as f:
        for i in word:
            f.write(i + ' ')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 파일 읽기
try:
    with open("./output/word.txt", 'r') as f:
        data = f.read().split() # split() 리스트로 변환 - 공백문자로 구분
        #word = random.choice(data) # 단어 1개를 랜덤하게 추출
        print(word)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
"""