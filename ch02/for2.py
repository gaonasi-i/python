#for ~ in
languages = ['python', 'C', 'Java', 'Javascript']

for lang in languages:
    if lang in ['python', 'Javascript']:
        print(f'{lang} need interpreter') #인터프리터
    else:
        print(f'{lang} need complier') #컴파일러

        
#구구단 출력
dan = 4
result = ""

for i in range(1, 10):
    current_val = f'{dan} x {i} = {dan*i}\n'
    result += current_val
print(result)



'''
for i in range(1, 10):
    print(f'{dan} x {i} = {dan*i}\n')
'''
