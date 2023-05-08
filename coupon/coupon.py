# 쿠폰 추첨기 만들기
import random
from tkinter import *

namelist = ['이진성', '노승우', '박성호', '권지혜', '김은효',
            '이경철', '성의석', '이유진', '유성길', '한주훈',
            '강정현', '김현우', '이영준', '안재훈', '김민정',
            '유세현', '윤기은', '오화룡', '조은별', '이가은']
# 5명 랜덤 추출
# 구현 1
"""
winner = []
while len(winner) < 5:
    name = random.choice(namelist)
    if name not in winner: # 중복제거
        winner.append(name)
"""
def cilck():
    selected_names = random.sample(namelist, 5)  # namelist에서 5명 무작위로 추출
    output.delete('1.0', END)  # 기존 출력 내용 삭제
    for name in selected_names:
        output.insert(END, name + ' ')


window = Tk()
window.title("쿠폰 추첨기")
window.option_add("*font", "맑은고딕 14")

# 이미지 넣기 - PhotoImage(file)
img = PhotoImage(file='bronx.png')

lbl_img = Label(window)
lbl_img.config(image=img)
lbl_img.grid(row=0, column=0, sticky=W)


# 추첨 버튼
Button(window, text="추첨", command=cilck).grid(row=1, column=0, sticky=E)

# 이름 출력
output = Text(window, width=33, height=4, bg='sky blue')
output.grid(row=2, column=0, sticky=W)


window.mainloop()