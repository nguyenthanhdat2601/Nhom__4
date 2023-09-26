import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
t1 = in_data[1, :]
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
print(Type_max_min(in_data))