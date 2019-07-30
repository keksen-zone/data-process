import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from time import *
import cv2
import os
begin_time=time()

# ['10.0', '30.0', '50.0', '70.0', '90.0', '110.0', '130.0',
# '150.0', '170.0', '190.0', '210.0', '230.0', '250.0', '270.0',
# '290.0', '310.0', '330.0', '350.0', '370.0', '390.0', '410.0',
# '430.0', '450.0', '470.0', '490.0']

# 在这里获取x的所有取值
x = []
with open('Plot_coord.csv', 'r') as zb:
    reader = csv.reader(zb)
    colx = [row[0] for row in reader]
    # x=[]
    for element in colx:
        if (element not in x):
            x.append(element)
    print(x)
# for x_value in x:
#     df = pd.read_csv('Plot_coord.csv',header=None)#注意没有表头，都是坑
#     #csv = pd.read_csv('Plot_coord.csv')
#     #print(df.iloc[:, [0]] == float(x_value))
#     # 取第0列的所有数据
#     lines = []
#     res = (df.iloc[:, [0]] == float(x_value))  # 这是一个DataFrame
#     for idx, row in res.iterrows():
#         # print(idx)
#         # print(str(row[0]))
#         if (str(row[0]) == 'True'):
#             lines.append(idx)
#             #print("line found")
#             # print(df.iloc[[idx,2],0])
#     #print(lines)
#
#     col1 = []
#     col2 = []
#     with open('cutted2csv\\test.csv', 'r') as f:
#         reader = csv.reader(f)
#         col1 = [row[0] for row in reader]
#     with open('Plot_coord.csv', 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         for i, rows in enumerate(reader):
#             if (i in lines):
#                 #print(i)
#                 col2.append(col1[i])
#                 #print(col1[i])
#
#     #固定了x的坐标，reshape（y，z）
#     Z = np.array(col2).reshape(25, 15)
#     #现在的x对应z  &&&&&&&  y对应y
#     x = np.arange(0, 15)
#     y = np.arange(0, 25)
#     X, Y = np.meshgrid(x, y)
#
#     g = plt.contourf(X, Y, Z, 5, alpha=0.8, cmap=plt.cm.jet)
#     #plt.clabel(g, inline=1, fontsize=10)
#     plt.title('this is a test')
#     plt.colorbar()
#     plt.grid(c='w', linestyle='-.')
#     plt.savefig('pics\\%s.png' % x_value)
#     plt.show()
#
# end_time = time()
# print(end_time-begin_time)

path = 'pics\\'
#filelist = os.listdir(path)

fps = 2 #视频每秒2帧
size = (640, 480) #需要转为视频的图片的尺寸
#可以使用cv2.resize()进行修改

video = cv2.VideoWriter("pics\\VideoTest1.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

for x_value in x:
    item= path + x_value + ".png"
    img = cv2.imread(item)
    video.write(img)
    print(item)

video.release()
cv2.destroyAllWindows()