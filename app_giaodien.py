import numpy as np
import tkinter as tk
from tkinter import ttk

def Input1():
    sopt = int(input("Nhap so phuong trinh cua he: "))
    return sopt

def Input2():
    soan = int(input("Nhap so an cua phuong trinh: "))
    return soan

def test_input(sopt, soan):
    if sopt != soan or sopt < 0 or soan < 0:
        print("Error! Nhap lai!")
        sopt = Input1()
        soan = Input2()
        test_input(sopt, soan)
    else:
        return sopt, soan

def Input3(sopt, soan):
    A = np.zeros((sopt, soan), dtype=float)
    B = np.zeros((sopt, 1), dtype=float)
    for pt in range(0, sopt):
        print(f"Nhap he so cua phuong trinh thu {pt + 1}: ")
        for an in range(0, sopt):
            A[pt, an] = float(input(f"----He so thu {an + 1}: "))
        B[pt, 0] = float(input("----He so cuoi: "))
    print(A)
    print(B)
    return A, B

def calculate(A, B):
    try:
        if np.linalg.det(A) != 0:
            X = np.dot(np.linalg.inv(A), B)
            return X
        else:
            calculate(A, B)
    except:
        print("Error!")
        Input3(A, B)
        calculate()

def continue_button():
    sopt = int(input1_entry.get())
    soan = int(input2_entry.get())
    sopt, soan = test_input(sopt, soan)
    A, B = Input3(sopt, soan)
    X = calculate(A, B)
    result_label.config(text=f'Nghiem cua he: {X}')

def Exit_button():
    print("Cam on!")
    root.destroy()

root = tk.Tk()
root.title("Giai he phuong trinh tuyen tinh")
root.geometry('500x400')
frame = ttk.Frame(root)
frame.grid(column=0, row=0, padx=10, pady=10)

input1_label = ttk.Label(frame, text="Nhap so phuong trinh cua he:")
input1_label.grid(column=0, row=0, padx=5, pady=5)

input1_entry = ttk.Entry(frame)
input1_entry.grid(column=1, row=0, padx=5, pady=5)

input2_label = ttk.Label(frame, text="Nhap so an cua phuong trinh:")
input2_label.grid(column=0, row=1, padx=5, pady=5)

input2_entry = ttk.Entry(frame)
input2_entry.grid(column=1, row=1, padx=5, pady=5)

continue_button = ttk.Button(frame, text="Tiep tuc", command=continue_button)
continue_button.grid(column=0, row=2, padx=5, pady=5)

exit_button = ttk.Button(frame, text="Thoat", command=Exit_button)
exit_button.grid(column=1, row=2, padx=5, pady=5)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
