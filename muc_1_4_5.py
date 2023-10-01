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
    df = pd.DataFrame.from_dict(my_dict1, orient='index')
    return df
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