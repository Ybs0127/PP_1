from tkinter import *
from tkinter import messagebox

def shiftUpEvent(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 위쪽 화살표")

def shiftDownEvent(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 아래쪽 화살표")

def shiftLeftEvent(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 왼쪽 화살표")

def shiftRightEvent(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 오른쪽 화살표")

#def keyEvent(event) :
    #messagebox.showinfo("키보드 이벤트", "눌린 키 : " + chr(event.keycode))

window = Tk()

window.bind("<Shift-Up>", shiftUpEvent)
window.bind("<Shift-Down>", shiftDownEvent)
window.bind("<Shift-Left>", shiftLeftEvent)
window.bind("<Shift-Right>", shiftRightEvent)

#window.bind("<Key>", keyEvent)

window.mainloop()