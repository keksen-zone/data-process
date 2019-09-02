# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv


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
    # 9.2 这里试图直接通过坐标来旋转图像
    Z = np.array(col2).reshape(x, z)
    # 9.2 上面这一行绝对不能动
    #现在的x对应z  &&&&&&&  y对应x
    xx = np.arange(0, x)
    yy = np.arange(0, z)
    Y, X = np.meshgrid(yy, xx)
    # 9.2 改了上面这一行，似乎可行

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