from tkinter import *

root = Tk()
root.title("SW GUI")    # 창 이름 설정
root.geometry("640x480")

# 텍스트 창
txt = Text(root, width = 30, height = 5)
txt.pack()
txt.insert(END,"글자를 입력하세요")

# 엔터를 칠 수 없는 텍스트 창
e = Entry(root, width = 30)
e.pack()
e.insert(0, '한줄만 입력하시오')

def btncmd():
    # 라인 1의 0번째 컬럼부터, END까지 가져오시오
    print(txt.get("1.0", END))
    print(e.get())

def btncmd1():
    # 라인 1의 0번째 컬럼부터, END까지 가져오시오
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

btn1 = Button(root, text="삭제", command=btncmd1)
btn1.pack()

root.mainloop()
