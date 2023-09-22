import numpy as np 
from tkinter import *
win= Tk()
win.title("giai he")
win.geometry('300x300')
def Tinhtoan():
    def __init__(self,a,b):
        self.A = a
        self.B = b
    def tinhtoan(self):
        A1=np.linalg.inv(self.A)

        x= np.dot(self.A1,self.B)
        print(x)
a=Label(win,text="A11",font="Times 10 bold")
b=Label(win,text="A12",font="Times 10 bold")
c=Label(win,text="A21",font="Times 10 bold")
d=Label(win,text="A22",font="Times 10 bold")
e=Label(win,text="B11",font="Times 10 bold")
f=Label(win,text="B12",font="Times 10 bold")
g = Label(win,text = Tinhtoan).place(x = 50 ,y = 300)


at=IntVar()
bt=IntVar()
ct=IntVar()
dt=IntVar()
et=IntVar()
ft=IntVar()
ent1= Entry(win,textvariable=at,font="Times 10 bold")
ent2= Entry(win,textvariable=bt,font="Times 10 bold")
ent3= Entry(win,textvariable=ct,font="Times 10 bold")
ent4= Entry(win,textvariable=dt,font="Times 10 bold")
ent5= Entry(win,textvariable=et,font="Times 10 bold")
ent6= Entry(win,textvariable=ft,font="Times 10 bold")
but=Button(win,text="ket qua",font="Times 10 bold",command=Tinhtoan)

a.place(x=20,y=20)
b.place(x=100,y=20)
c.place(x=20,y=100)
d.place(x=100,y=100)
e.place(x=200,y=20)
f.place(x=200,y=100)
 
ent1.place(x=15,y=40,width=50,height=25)
ent2.place(x=120,y=40,width=50,height=25)
ent3.place(x=15,y=120,width=50,height=25)
ent4.place(x=120,y=120,width=50,height=25)
ent5.place(x=190,y=40,width=50,height=25)
ent6.place(x=190,y=120,width=50,height=25)
but.place(x=100,y=200,width=50,height=25)


win.mainloop()
