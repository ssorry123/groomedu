from tkinter import *
from functools import partial


root = Tk()
root.title("SW GUI")    # 창 이름 설정
root.geometry("640x480")

def btncmd_1(listBox, n):
    listBox.delete(0)       # 첫 번째 항목 삭제
    print(n)

def btncmd_2(listBox, n):
    print(n)
    print(listBox.size())   # 크기 반환
    print(listBox.get(0,2)) # 구간 반환

def btncmd_3(listBox):
    print(listBox.curselection())   # 선택한 항목들의 인덱스 반환

    

# selectmode = "single", "extended", ...
# height=0 -> 리스트가 포함하는 것을 모두 보여준다
listbox = Listbox(root,selectmode = "extended", height = 6)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "고구마")
listbox.insert(END, "감자")
listbox.pack()
# 버튼을 눌렀을때 실행하는 함수에 인자를 전달하는 방법
btn_1 = Button(root, text="클릭", command = partial(btncmd_1, listbox, 5))
btn_1.pack()
btn_2 = Button(root, text="클릭", command = lambda: btncmd_2(listbox, 123))
btn_2.pack()
btn_3 = Button(root, text="클릭", command = lambda: btncmd_3(listbox))
btn_3.pack()


root.mainloop()
