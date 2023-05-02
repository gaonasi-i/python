from tkinter import *

root = Tk()
root.title("Temp Converter")
root.geometry("250x100")
app = App(root)
root.mainloop()

class App():
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        Label(frame, text="deg.C").grid(row=0, column=0)
        Button(frame, text="변환", command=self.convert).grid(row=2, column=0)

    def convert(self):
        print("Not implemented")





def convert():
    try:
        temp_c = eval(ent_c.get())
        txt_f.delete(0.0, END)
        temp_f = temp_c * 1.8 + 32
        temp_f = "{: .1f}F".format(temp_f)
        txt_f.inert(END, temp_f)
    except NameError:
        txt_f.insert(END, '오류')
