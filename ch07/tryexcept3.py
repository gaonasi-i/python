# try ~ except ~ else
# 에러가 있으면 except 구문을 실행하고, 없으면
# try ~ else ~를 실행함
try:
    with open("../ch06/output/kbo2023.txt", 'r') as f:
        team = f.read()
        print("실행 테스트")
except FileNotFoundError as e:
    print(e) #[Errno 2] No such file or directory: '../ch0/output/kbo2023.txt' 파일을 찾을수없다
else:
    for i in team:
        print(i, end='')
