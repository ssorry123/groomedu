from tkinter import *


root = Tk()
root.title("SW GUI")
root.geometry("640x480")

# 메뉴 프레임
frame_burgur = Frame(root, relief="solid", bd=1)
frame_burgur.pack(side = "left", fill="both", expand=True)
Button(frame_burgur, text="햄버거").pack()
Button(frame_burgur, text="치즈버거").pack()
Button(frame_burgur, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side = "right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()
