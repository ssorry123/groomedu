from tkinter import *


root = Tk()
root.title("SW GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

# 스크롤 바 프레임에 넣고 오른쪽에 위치시키기
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(
    frame, 
    selectmode="extended",
    height=10,
    # 리스트 박스에 스크롤바 세팅하기(맵핑하기)
    yscrollcommand=scrollbar.set
)
for i in range(1,32):
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

# 스크롤 바 드래그로 움직이기
# 스크롤바를 리스트박스와 매핑하기
scrollbar.config(command=listbox.yview)

root.mainloop()
