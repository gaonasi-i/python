# 컨트롤 도구 - 클래스 사용 생성
from tkinter import *

class App():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()  # 가운데 정렬

        #1행
        Label(frame, text="제목").grid(row=0, column=0)
        Entry(frame, bg='pink').grid(row=0, column=1)
        Button(frame, text="확인").grid(row=0, column=2)

        # 체크 박스 #2행 1열
        Checkbutton(frame, text="체크 버튼").grid(row=1, column=0)

        # 리스트 목록 상자 #2행 2열
        listbox = Listbox(frame, height=6, bg='pink', selectmode=SINGLE) #보이는줄 - 6줄
        # selectmode = MULTIPLE 다중 클릭 선택 / SINGLE 한개만 선택
        colors = ['red', 'green', 'yellow', 'pink', 'orange']
        for item in colors:
            listbox.insert(END, item)

        listbox.grid(row=1, column=1) # 2행 2열

        # 레이아웃 - radio 버튼(2개) - 프레임 위에 작성
        radio_frame = Frame(frame) #프레임 생성
        radio_selection = StringVar()
        b1 = Radiobutton(radio_frame, text='left',
                         variable=radio_selection, value='L')
        b1.pack(side=LEFT) #pack()을 써줘야 ul에 프레임이 올라감
        b2 = Radiobutton(radio_frame, text='right',
                         variable=radio_selection, value='R')
        b2.pack(side=RIGHT)
        radio_frame.grid(row=1, column=2) # 2행 3열





root = Tk()
app = App(root)


root.mainloop()