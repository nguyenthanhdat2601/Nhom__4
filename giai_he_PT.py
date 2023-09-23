import numpy as np
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("giai he co n phuong trinh va n an")
win.geometry('900x700')
win.configure(bg = 'purple')

Label(win, text = 'Giai he phuong trinh n an', font = ('Arial', 13), bg = 'yellow', fg = 'black', height=2, relief='solid', borderwidth = 2, width = 40).place(x = 250, y = 0)

sopt = IntVar()
Label(win, text = 'Nhap so phuong trinh', font = ('Arial', 9), bg = 'yellow', fg = 'black', height=1, relief='solid', borderwidth = 2, width = 30).place(x = 250, y = 60)
Entry(win, textvariable = sopt, font = ('Arial', 13), bg = 'yellow', fg = 'black', relief='solid', borderwidth = 2, width = 5).place(x = 485, y = 60)

a = 'abcdefghijklmnopqrstuvwxyz'
a1 = list(a)
A = []
entries_A = []
B = []
entries_B = []
class Cal:
    def __init__(self, A, entries_A, B, entries_B):
        self.A = A
        self.entries_A = entries_A
        self.B = B
        self.entries_B = entries_B
    def create(self):
        try:
            if (sopt.get() <= 0):
                messagebox.showwarning("CHu y","So phuong trinh phai >0")
            for i in range(sopt.get()):
                self.A.append([])
                self.entries_A.append([])
                self.B.append([])
                self.entries_B.append([])
                for j in range(sopt.get()):
                    self.A[i].append(StringVar())
                    if (i > 0):
                        Label(win,background = 'purple', text = ' + '+a1[j]+f'{i}', width = 3).place(x = 80 + 80*i, y = 200 + 30*j)#grid(row = i, column = j+2)
                    else:
                        Label(win,background = 'purple', text = a1[j]+f'{i}', width = 3).place(x = 80 + 80*i, y = 200 + 30*j)#grid(row = i, column = j+2)
                    self.entries_A[i].append(Entry(win, textvariable = self.A[i][j], width=3))
                    self.entries_A[i][j].place(x =110 + 83*j, y = 200 + 30*i)#grid(row=i, column=j+4)
                self.B[i].append(StringVar())
                Label(win,background = 'purple', text = f' = ', width = 3).place( x = 140 + 83*2, y = 200 + 30*i)#grid(row = i, column = 4)
                self.entries_B[i].append(Entry(win, textvariable = self.B[i][0], width=3))
                self.entries_B[i][0].place( x = 83*4, y = 200 + 30*i)#grid(row= i, column= 5)
        except:
            messagebox.showwarning("CHu y","Kieu du lieu khong dung!")

    def get_mat_A(self):
        matrix_A = []
        for i3 in range(sopt.get()):
            matrix_A.append([])
            for j3 in range(sopt.get()):
                if (self.A[i3][j3].get() != None):
                    matrix_A[i3].append(float(self.A[i3][j3].get()))
                else: 
                    messagebox.showwarning("Thieu du lieu", f'Nhap thieu he so cua {a1[j3]}{i3}')

        return np.array(matrix_A)

    def get_mat_B(self):
        matrix_B = []
        for i3 in range(sopt.get()):
            matrix_B.append([])
            for j3 in range(1):
                if (self.B[i3][j3].get() != None):
                    matrix_B[i3].append(float(self.B[i3][j3].get()))
                else:
                    messagebox.showwarning("Thieu du lieu", f'Nhap thieu he so cua phuong trinh thu {i3}')
        return np.array(matrix_B)

    def calculate(self):
        try:
            A = Cal.get_mat_A(self)
            B = Cal.get_mat_B(self)
            if (np.linalg.det(A) != 0):
                X = np.dot(np.linalg.inv(A), B)
                for i in range(sopt.get()):
                    Label(win,background = 'purple', text = f'x{i} = ', width = 4).place( x = 50 + 83*i, y = 450)#grid(row = i, column = 4)
                    Label(win,background = 'purple', text = f'{round(X[i][0], 2)}' + ', ', width = 4).place( x = 100 + 83*i, y = 450)#grid(row = i, column = 4)
            else:
                messagebox.showwarning("Error!", "Ma tran khong kha nghich")
        except:
            messagebox.showwarning("Error!", "Nhap sai!")
def clear():
    Label(win,background = 'purple', width = 180*sopt.get(), height = 20).place( x = 240, y = 100)
cal = Cal(A, entries_A, B, entries_B)
Button(win, text = 'Create', command = cal.create, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 280, y = 510)
Button(win, text = 'Exit', command = exit, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 380, y = 510)
Button(win, text = 'Clear', command = clear, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 480, y = 510)
Button(win, text = 'Calculate', command = cal.calculate, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 580, y = 510)

win.mainloop()

