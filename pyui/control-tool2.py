# 컨트롤 도구 - 클래스 사용 생성
from tkinter import *

class App():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()  # 가운데 정렬

        Label(frame, text="제목").grid(row=0, column=0)
        Entry(frame, bg='pink').grid(row=0, column=1)
        Button(frame, text="확인").grid(row=0, column=2)

        # 체크 박스
        Checkbutton(frame, text="체크 버튼").grid(row=1, column=0)

        # 리스트 목록 상자
        listbox = Listbox(frame, height=6, bg='pink', selectmode=SINGLE) #보이는줄 - 6줄
        # selectmode = MULTIPLE 다중 클릭 선택 / SINGLE 한개만 선택
        colors = ['red', 'green', 'yellow', 'pink', 'orange']
        for item in colors:
            listbox.insert(END, item)

        listbox.grid(row=1, column=1)





root = Tk()
app = App(root)


root.mainloop()