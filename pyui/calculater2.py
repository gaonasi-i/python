#계산기
from tkinter import *

root = Tk()
root.title("나의 계산기")

# top_row 프레임
top_row = Frame(root)
top_row.grid(row=0, column=0, sticky=N) #sticky=N (북쪽에 위치)
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
    Button(num_pad, text=btn_text).grid(row=r, column=c)
    c += 1
    if c > 2:     #colum이 2(3열)보다 크면 0으로 설정
        c = 0
        r += 1    #row(행) 1증가
root.mainloop()
