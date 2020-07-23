from tkinter import *


root = Tk()
root.title("SW GUI")
root.geometry("640x480")

'''
# 팩 복습( 팩은 쌓는 느낌 )
btn1 = Button(root, text="버튼 1")
btn2 = Button(root, text="버튼 2")
# btn1.pack(side = "left")
# btn2.pack(side = "left")

# 그리드
btn1.grid(row=0, column=0)
btn2.grid(row=1, column=1)
'''

# 맨 윗줄 버튼
btn_f16 = Button(root, text="F16")
btn_f17 = Button(root, text="F17")
btn_f18 = Button(root, text="F18")
btn_f19 = Button(root, text="F19")

btn_f16.grid(row=0, column=0)
btn_f17.grid(row=0, column=1)
btn_f18.grid(row=0, column=2)
btn_f19.grid(row=0, column=3)

# 두번째 줄 버튼
btn_clear = Button(root, text="clear")
btn_equal = Button(root, text="=")
btn_div = Button(root, text="/")
btn_mul = Button(root, text="*")

btn_clear.grid(row=1, column=0)
btn_equal.grid(row=1, column=1)
btn_div.grid(row=1, column=2)
btn_mul.grid(row=1, column=3)

# 세번째 줄 버튼
btn_f1 = Button(root, text="1")
btn_f2 = Button(root, text="2")
btn_f3 = Button(root, text="3")
btn_enter = Button(root, text="enter")

btn_f1.grid(row=2, column=0)
btn_f2.grid(row=2, column=1)
btn_f3.grid(row=2, column=2)
btn_enter.grid(row=2, column=3, rowspan=2)

# 네번째 줄 버튼
btn_f0 = Button(root, text="0")
btn_dot = Button(root, text=".")

btn_f0.grid(row=3, column=0, columnspan=2)
btn_dot.grid(row=3, column=2)


root.mainloop()
