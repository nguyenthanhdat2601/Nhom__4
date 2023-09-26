import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
print(in_data)

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
print(sv_ck(in_data))
print(ipL1_l2(in_data))

#muc 1: tong so sinh vien tham gia mon h

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
      
