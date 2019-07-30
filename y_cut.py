# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv


# x = ['10.0', '30.0', '50.0', '70.0', '90.0', '110.0', '130.0',
# '150.0', '170.0', '190.0', '210.0', '230.0', '250.0', '270.0',
# '290.0', '310.0', '330.0', '350.0', '370.0', '390.0', '410.0',
# '430.0', '450.0', '470.0', '490.0']

# y = ['10.0', '30.0', '50.0', '70.0', '90.0', '110.0', '130.0',
# '150.0', '170.0', '190.0', '210.0', '230.0', '250.0', '270.0',
# '290.0', '310.0', '330.0', '350.0', '370.0', '390.0', '410.0',
# '430.0', '450.0', '470.0', '490.0']

# z = ['-2.0', '-6.0', '-10.0', '-14.0', '-18.0', '-22.0', '-26.0',
# '-30.0', '-34.0', '-38.0', '-42.0', '-46.0', '-50.0', '-54.0', '-58.0']

# 在这里获取x的所有取值
# x = []
# with open('Plot_coord.csv', 'r') as zb:
#     reader = csv.reader(zb)
#     colx = [row[2] for row in reader]
#     # x=[]
#     for element in colx:
#         if (element not in x):
#             x.append(element)
#     print(x)

def y_cut(time,attri,y_index,grid_line,x,y,z):
    print("y_cut得到的时间文件是：" + time)
    print(attri)
    print("↑属性编号   ↓网格线   →y_index：" + y_index)
    print(grid_line)
    df = pd.read_csv('Plot_coord.csv',header=None)#注意没有表头，都是坑
    #csv = pd.read_csv('Plot_coord.csv')
    #print(df.iloc[:, [1]] == 10.0)
    # 取第1列的所有数据
    lines = []
    res = (df.iloc[:, [1]] == float(y_index))  # 这是一个DataFrame
    for idx, row in res.iterrows():
        #print(idx,end='')
        #print(str(row[1]))
        if (str(row[1]) == 'True'):
            lines.append(idx)
            #print("line found")
            # print(df.iloc[[idx,2],0])
    print("run at line 50")

    col1 = []
    col2 = []
    colors = []
    #这里读取了具体的属性文件
    with open('cutted2csv\\%s'%time, 'r') as f:
        reader = csv.reader(f)
        col1 = [row[attri] for row in reader]
    with open('Plot_coord.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, rows in enumerate(reader):
            if (i in lines):
                #print(i)
                col2.append(col1[i])
                #print(col1[i])
                if (col1[i] not in colors):
                    colors.append(col1[i])
    print("run at line 67")
    #这里的坐标很混乱（但是能用），等一个有缘人来改一改
    #固定了y的坐标，reshape（x，z）
    Z = np.array(col2).reshape(x, z)
    #现在的x对应z  &&&&&&&  y对应x
    xx = np.arange(0, z)
    yy = np.arange(0, x)
    X, Y = np.meshgrid(xx, yy)

    g = plt.contourf(X, Y, Z, len(colors), alpha=0.8, cmap=plt.cm.jet)
    #plt.clabel(g, inline=1, fontsize=10)
    # plt.title('this is a test')
    plt.colorbar()
    if grid_line == 1:
        plt.grid(color='black')
    elif grid_line == 0:
        pass
    plt.show()

#y_cut(" 1.55000000E+03.csv",1,"10",1,25,25,15)