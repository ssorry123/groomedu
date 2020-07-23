from tkinter import *


root = Tk()
root.title("SW GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()


burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="햄버거", value = 1, variable = burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value = 3, variable = burger_var)
def btncmd_1():
    print(burger_var.get())
btn_1 = Button(root, text="클릭", command=btncmd_1)


drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value = "콜라", variable = drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value = "사이다", variable = drink_var)
def btncmd_2():
    print(drink_var.get())
btn_2 = Button(root, text="클릭", command=btncmd_2)


btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_drink1.pack()
btn_drink2.pack()
btn_1.pack()
btn_2.pack()
root.mainloop()
