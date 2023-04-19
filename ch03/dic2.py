# 딕셔너리
d = {'Tomas': 13, 'Jane': 9}

# 요소 추가 - Mike : 10살
d['Mike'] = 10
print(d)

#list() - 리스트 자료로 출력 
# 모든 key값 가져오기 - keys()
#print(d.keys())
print(list(d.keys()))

# 모든 값(value) 가져오기 - values()
print(d.values())

# 모든 키와 모든 값 가져오기 - items()
for key, val in d.items():
    print(key, ':', val)
