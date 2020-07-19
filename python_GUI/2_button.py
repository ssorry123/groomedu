from tkinter import *

root = Tk()
root.title("SW GUI")    # 창 이름 설정
root.geometry("640x480")

btn1 = Button(root, text="버튼1")
btn1.pack() # 버튼을 실제로 프로그램에 적용

# pad* 버튼의 크기를 더 차지하게 만듬
# text가 길어지면 버튼이 커진 후에 pad만큼 공간을 더 차지
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3333333333")
btn3.pack()

# 버튼 크기 조정
btn4 = Button(root, width=10, height=3, text="버튼44444444444444")
btn4.pack()

btn5 = Button(root, fg='red', bg="yellow" , text="버튼5")
btn5.pack()

photo = PhotoImage(file="./image/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었다.")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()
