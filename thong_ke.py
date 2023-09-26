import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
print(in_data)

#muc 1: tong so sinh vien
def sum_sv(in_data):
    tong_sv = np.sum(in_data[:, 1])
    return tong_sv

#muc 2: tong so sinh vien dat tung loai diem
def tong_sv_type(in_data):
    Text = "Loại A,Loại B+,Loại B,Loại C+,Loại C,Loại D+,Loại D,Loại F"
    loai_diem = Text.split(",")
    tong_Ldiem = []
    for i in range(3, 11):
        tong_Ldiem.append(np.sum(in_data[:, i]))
    result = dict(zip(loai_diem, tong_Ldiem))
    return result

#muc 3.1: Phần trăm số SV đạt của môn học
def phantram(in_data):
    sv_dat = []
    for i in range(1, 9):
        n = np.array(in_data[i, :])
        sv_dat.append(np.sum(n[3:10]))
    phan_tram_sv_dat = np.sum(sv_dat) / sum_sv(in_data)
    return phan_tram_sv_dat

#muc 3:Tìm lớp có số SV đạt >=D nhiều nhất/ ít nhất
def Max_Min_pass_class(in_data):
    sv_dat = []
    option = ['Max', 'Min']
    lop2 = []
    for i in range(1, 9):
        n = np.array(in_data[i, :])
        sv_dat.append(np.sum(n[3:10]))
    lop1 = in_data[:, 0]
    a1 = sv_dat.index(max(sv_dat))
    lop2.append(lop1[a1])
    a2 = sv_dat.index(min(sv_dat))
    lop2.append(lop1[a2])
    Dict1 = dict(zip(option, lop2))
    return Dict1

#muc 4: lop co nhieu/it diem A, B, C nhat
def ABC_Max_Min(in_data):
    Text = "Loại A,Loại B+,Loại B,Loại C+,Loại C,Loại D+,Loại D,Loại F"
    option1= Text.split(",")
    option2 = ['Max', 'Min']
    lop1 = in_data[:, 0]
    lop3 = []
    for i in range(3, 11):
        my_dict = {}
        lop2 = []
        A = list(in_data[:, i])
        ind = A.index(max(A))
        lop2.append(lop1[ind])
        ind = A.index(min(A))
        lop2.append(lop1[ind])
        my_dict = dict(zip(option2, lop2))
        lop3.append(my_dict)
    my_dict1 = dict(zip(option1, lop3))
    
    return my_dict1

#muc 5: tim diem nao co sinh vien dat nhieu nhat
def Type_max_min(in_data):
    Text = "Loại A,Loại B+,Loại B,Loại C+,Loại C,Loại D+,Loại D,Loại F"
    loai_diem1 = Text.split(",")
    loai_diem2 = []
    option = ['Max', 'Min']
    tong_Ldiem = []
    for i in range(3, 11):
        tong_Ldiem.append(np.sum(in_data[:, i]))
    ind1 = tong_Ldiem.index(max(tong_Ldiem))
    loai_diem2.append(loai_diem1[ind1])
    ind2 = tong_Ldiem.index(min(tong_Ldiem))
    loai_diem2.append(loai_diem1[ind2])
    result = dict(zip(option, loai_diem2))
    return result

#mục 7: tổng số sinh viên đạt bài cuối kỳ
def sv_ck(in_data):
    print("số sinh viên đạt bài cuối kỳ: ")
    sv_cuoi_ky = in_data[:, 15]
    return np.sum(sv_cuoi_ky)

#muc 8: so sanh so sinh vien dat chuan L1, L2
def ipL1_l2(in_data):
    sv_L1 = np.sum(in_data[:, 12])
    print("so sinh vien dat chuan dau ra L1: ", sv_L1)
    sv_L2 = np.sum(in_data[:, 13])
    print("so sinh vien dat chuan dau ra L2: ", sv_L2)
    if (sv_L1 > sv_L2) :
        return "=> so sinh vien dat L1 lon hon L2"
    elif (sv_L1 < sv_L2):
        return "=> so sinh vien dat L2 lon hon L1"
    else:
        return "=> so sinh vien dat L2 bang L1"

""" print('Tong so sinh vien di thi :')
tongsv= in_data[:,1]
print(np.sum(tongsv))
diemA = in_data[:,3]
diemBc = in_data[:,4]
print('Tong sv:',tongsv)
maxa = diemA.max()
i, = np.where(diemA == maxa)
print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))
plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
plt.plot(range(len(diemBc)),diemBc,'g-',label="Diem B +")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show() """
      
