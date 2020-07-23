from tkinter import *


root = Tk()
root.title("SW GUI")
root.geometry("640x480")

chkvar = IntVar()   # chkvar에 int형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable = chkvar)
chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 자동 선택 해제 처리

def btncmd():
    print(chkvar.get())
btn = Button(root, text="클릭", command=btncmd)


chkbox.pack()
btn.pack()
root.mainloop()
