from tkinter import *

root = Tk()
root.title("SW GUI")                # 창 이름 설정
root.geometry("640x480")            # 가로 세로 설정
root.geometry("640x480+100+300")    # 가로세로, x좌표, y좌표 

root.resizable(False, False)    # 창 크기 x, y 변경 불가

root.mainloop()
