#계산기
from tkinter import *

def click(key):
    if key == '=':
        try:
            # eval(문자열 계산) -> 문자형을 숫자형 으로 표현하여 계산하게 해줌 / 실수도 가능
            value = eval(display.get()) #입력창에 입력된 계산값
            result = str(value)[0:10] #소수점 포함 10자리까지 출력
            display.insert(END, '=' + result)
        except:
            display.insert(END, "--> 오류")
    elif key == 'C': #취소버튼을 누르면 입력값 삭제
        display.delete(0, END) #첫번째 문자부터 삭제
    else:
        display.insert(END, key)

root = Tk()
root.title("나의 계산기")

# top_row 프레임
top_row = Frame(root)
top_row.grid(row=0, column=0, columnspan=2,sticky=N) #sticky=N (북쪽에 위치) #columnspan=2 (병합)
display = Entry(top_row, width=50, bg='lavender')
display.grid(row=0, column=0)

# num_pad 숫자 버튼 프레임
num_pad = Frame(root)
num_pad.grid(row=1, column=0, sticky=W) #sticky=W (서쪽에 위치)
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text): #cmd함수에 인수(버튼 키)를 전달
        click(x)
    Button(num_pad, text=btn_text, width=5, command=cmd, bg='pink').grid(row=r, column=c)
    c += 1
    if c > 2:     #colum이 2(3열)보다 크면 0으로 설정
        c = 0
        r += 1    #row(행) 1증가

# 연산자 프레임
operator = Frame(root)
operator.grid(row=1, column=1, sticky=E)
operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C']
r = 0
c = 0
for btn_text in operator_list:
    def cmd(x=btn_text): #cmd함수에 인수(연산자 키)를 전달
        click(x)
    Button(operator, text=btn_text, width=5, command=cmd, bg='pink').grid(row=r, column=c)
    c += 1
    if c > 1:
        c = 0
        r += 1

root.mainloop()
