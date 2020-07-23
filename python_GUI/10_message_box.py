from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("SW GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "ㅁㄴㅇㄹㅁㄴㅇㄹ")
Button(root, command=info, text="알림").pack()

def warn():
    msgbox.showwarning("경고", "ㅁㄴㅇㄹㅁㄴㅇㄹ")
Button(root, command=warn, text="경고").pack()

def error():
    msgbox.showerror("에러", "ㅁㄴㅇㄹㅁㄴㅇㄹ")
Button(root, command=error, text="에러").pack()

def okcancel():
    msgbox.askokcancel("확인/ 취소", "ㅁㄴㅇㄹㅁㄴㅇㄹ")
Button(root, command=okcancel, text="확인 취소").pack()

def retrycancel():
    msgbox.askretrycancel("재시도/ 취소", "ㅁㄴㅇㄹㅁㄴㅇㄹ")
Button(root, command=retrycancel, text="재시도 취소").pack()

def yesno():
    msgbox.askyesno("예/ 아니오", "ㅁㄴㅇㄹㅁㄴㅇㄹ")
Button(root, command=yesno, text="예, 아니오").pack()

def yesnocancle():
    response = msgbox.askyesnocancel(None, "ㅁㄴㅇㄹㅁㄴㅇㄹ")
    print(response)
    if response == True:
        print("yes")
    elif response == False:
        print("No")
    else:
        print("cancle")
Button(root, command=yesnocancle, text="예, 아니오, 취소").pack()


root.mainloop()
