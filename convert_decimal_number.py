def to_binary(a):
    result = []
    result.append(a % 2)
    b = int(a / 2)
    while b > 0:
        result.append(b % 2)
        b = int(b / 2)
    result.reverse()
    new_result = "".join(map(str, result))
    return new_result

def to_octal(a):
    result = []
    result.append(a % 8)
    b = int(a / 8)
    while b > 0:
        result.append(b % 8)
        b = int(b / 8)
    result.reverse()
    new_result = "".join(map(str, result))
    return new_result
def hexal_number(a):
    if a == 10:
        return 'A'
    if a == 11:
        return 'B'
    if a == 12:
        return 'C'
    if a == 13:
        return 'D'
    if a == 14:
        return 'E'
    if a == 15:
        return 'F'
def to_hexal(a):
    result = []
    if a % 16 < 10:
        result.append(a % 16)
    else:
        result.append(hexal_number(a % 16))
    b = int(a / 16)
    while b > 0:
        if b % 16 < 10:
            result.append(b % 16)
        else:
            result.append(hexal_number(b % 16))
        b = int(b / 16)
    result.reverse()
    new_result = "".join(map(str, result))
    return new_result

from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("convert decimal to other")
win.geometry('900x700')
win.configure(bg = 'purple')

#title
Label(win, text = "Convert integer decimal to other", font = ('Times new roman', 15), bg = 'white', fg = 'Black', width = 40, height = 2, relief='solid', borderwidth = 2).place(x = 246, y = 2)

#input
Label(win, text = "Input", font = ('Times new roman', 15), bg = 'orange', fg = 'Black', width = 11, height = 2, relief='solid', borderwidth = 2).place(x = 57, y = 100)
input = Text(win,font = ('Times New Roman', 15), height = 2, width = 16, relief='solid', borderwidth = 2)
input.configure(fg = 'black', bg = "white")
input.place(x = 190, y = 100)

#output
Label(win, text = "Output", font = ('Times new roman', 15), bg = 'orange', fg = 'Black', width = 11, height = 2, relief='solid', borderwidth = 2).place(x = 57, y = 170)
output = Text(win,font = ('Times New Roman', 15), height = 2, width = 16, relief='solid', borderwidth = 2)
output.configure(fg = 'black', bg = "white")
output.place(x = 190, y = 170)

#data
def button1():
    input.insert(INSERT, '1')
def button2():
    input.insert(INSERT, '2')
def button3():
    input.insert(INSERT, '3')
def button4():
    input.insert(INSERT, '4')
def button5():
    input.insert(INSERT, '5')
def button6():
    input.insert(INSERT, '6')
def button7():
    input.insert(INSERT, '7')
def button8():
    input.insert(INSERT, '8')
def button9():
    input.insert(INSERT, '9')
def button0():
    input.insert(INSERT, '0')

#result 
def Binary():
    a = input.get("1.0", "end").strip()
    output.delete("1.0", "end")
    output.insert(INSERT, to_binary(int(a)))
def Octal():
    b = input.get("1.0", "end").strip()
    output.delete("1.0", "end")
    output.insert(INSERT, to_octal(int(b)))
def Hexal():
    c = input.get("1.0", "end").strip()
    output.delete("1.0", "end")
    output.insert(INSERT, to_hexal(int(c)))

#clear
def Clear():
    input.delete("1.0", "end")
    output.delete("1.0", "end")
#keyboard
Label(win, bg = 'white', width = 50, height = 23, relief='solid', borderwidth = 2).place(x = 40, y = 250)
Button(win, text = '1', command = button1, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 80, y = 300)
Button(win, text = '2', command = button2, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 180, y = 300)
Button(win, text = '3', command = button3, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 280, y = 300)

Button(win, text = '4', command = button4, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 80, y = 370)
Button(win, text = '5', command = button5, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 180, y = 370)
Button(win, text = '6', command = button6, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 280, y = 370)

Button(win, text = '7', command = button7, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 80, y = 440)
Button(win, text = '8', command = button8, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 180, y = 440)
Button(win, text = '9', command = button9, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 280, y = 440)

Button(win, text = '0', command = button0, font = ('Times new roman', 15), fg = 'black', bg = 'yellow', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 180, y = 510)
Button(win, text = 'Clear', command = Clear, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 80, y = 510)
Button(win, text = 'Exit', command = exit, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 4, height = 2, relief='solid', borderwidth = 2).place(x = 280, y = 510)

#selection
Label(win, bg = 'white', width = 40, height = 23, relief='solid', borderwidth = 2).place(x = 490, y = 250)
Button(win, text = 'Binary', command = Binary, font = ('Times new roman', 15), fg = 'black', bg = 'orange', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 550, y = 300)
Button(win, text = 'Octal', command = Octal, font = ('Times new roman', 15), fg = 'black', bg = 'orange', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 550, y = 370)
Button(win, text = 'Hexal', command = Hexal, font = ('Times new roman', 15), fg = 'black', bg = 'orange', width = 13, height = 2, relief='solid', borderwidth = 2).place(x = 550, y = 440)
#advertised
Label(win, bg = 'white', width = 40, height = 8, relief='solid', borderwidth = 2).place(x = 490, y = 100)

win.mainloop()