from tkinter import *
import os

dirpath = os.path.dirname(os.path.realpath(__file__)) 
imgpath = os.path.join(dirpath, 'image')


root = Tk()
root.title("SW GUI")    # 창 이름 설정
root.geometry("640x480")

# 단순히 보여주는 Label
label1 = Label(root, text = "Hello World!")
label1.pack()

photo = PhotoImage(file = os.path.join(imgpath, 'img.png'))
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text = "또 만나요")

    # global하지 않으면 갈비지 컬렉션으로 사라짐.
    global photo2   # 전역변수로 설정해야 함수 밖에 있는 것이 바뀐다
    photo2 = PhotoImage(file = os.path.join(imgpath, 'img2.png'))
    label2.config(image = photo2)
    

# label을 바꾼다
btn1 = Button(root, text="클릭", command = change)
btn1.pack()


root.mainloop()
