from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.title("SW GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1,32)]
comboBox = ttk.Combobox(root, height = 5, values = values, state = "readonly")
comboBox.set("카드 결제일") # 항목에 없는, 그러나 임의의 글자를 보여주며 시작
# comboBox.current(0) # 첫번째 항목 선택된 상태로 시작
comboBox.pack()

def btncmd():
    print(comboBox.get())
btn = Button(root, text = "클릭", command = btncmd).pack()


root.mainloop()
