import numpy as np

def Input1():
    #so phuong trinh
    sopt = int(input("Nhap so phuong trinh cua he: "))
    return sopt
def Input2():
    #so an 
    soan = int(input("nhap so an cua phuong trinh: "))
    return soan
def test_input(sopt, soan):
    if (sopt != soan or sopt < 0 or soan < 0):
            print("Error! Nhap lai!")
            sopt = Input1()
            soan = Input2()
            test_input(sopt, soan)
    else: 
        return sopt, soan
def Input3(sopt, soan):
        A = np.zeros((sopt, soan), dtype = float)
        B = np.zeros((sopt, 1), dtype = float)
        for pt in range(0, sopt):
            print(f"Nhap he so cua phuong trinh thu {pt + 1}: ")
            for an in range(0, sopt):
                A[pt, an] = float(input(f"----he so thu {an + 1}: "))
            B[pt, 0] = float(input("----he so cuoi: "))
        print (A)
        print (B)
        return A, B
def calculate(A, B):
    try:
        if (np.linalg.det(A) != 0):
            X = np.dot(np.linalg.inv(A), B)
            return X
        else: 
            calculate(A, B)
    except:
        print("Error!")
        Input3(A, B)
        calculate()

def selection():
    opinion = input("Nhap vao lua chon: Continue or Exit? ")
    if (opinion == "Continue"):
        sopt = Input1()
        soan = Input2()
        sopt, soan = test_input(sopt, soan)
        A, B = Input3(sopt, soan)
        X = calculate(A, B)
        print('Nghiem cua he:',X)
        print("=====================")
        selection()
    elif (opinion == "Exit"): 
        print("Thank for using!")
        exit()
    else: 
        print("Ban da nhap sai lua chon, vui long nhap lai!")
        selection()
selection()

