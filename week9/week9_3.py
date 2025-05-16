from tkinter import *
from time import *

fnameList = ["bee.gif", "cake.gif", "camera.gif", "clover.gif", "earth.gif", "flower.gif", "strawberry.gif", "sun.gif", "watermelon.gif"]
photoList = [None] * 9
num = 0

def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file=r"/Users/youngbinsong/Desktop/" +fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    btnfname.config(text=fnameList[num])

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file=r"/Users/youngbinsong/Desktop/" +fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    btnfname.config(text=fnameList[num])

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text= "<< 이전", command=clickPrev)
btnNext = Button(window, text= "다음 >>", command=clickNext)
btnfname = Button(window, text=fnameList[num])

photo = PhotoImage(file=r"/Users/youngbinsong/Desktop/" +fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
btnfname.place(x = 325, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()